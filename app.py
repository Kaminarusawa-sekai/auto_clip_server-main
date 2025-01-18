import gradio as gr
import yaml
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

import autogen
import engine
# def greet(name, intensity):

#     return "Hello, " + str(name) + str(intensity)

# demo = gr.Interface(
#     fn=greet,
#     inputs=["file", "file"],
#     outputs=["text"],
# )

# 指定保存文件的目录
save_directory = './uploads/'  # 请确保此目录存在或在代码中创建它
project_directory="./project/"
# 如果保存目录不存在，则创建它
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
if not os.path.exists(project_directory):
    os.makedirs(project_directory)

def open_yaml(yaml_file):
    for f in yaml_file.temp_files:
        try:
            gen = autogen.AutoGen(f, project_directory)
            asyncio.run(gen.tts())
            

            project_path_list = project_directory
            assets_path = save_directory

            # project_name = os.path.basename(project_path)
            # print("project_name:", project_name)
            with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
                futures = []
                for project_path in project_path_list:
                    content = engine.read_cookbook_yaml(project_path)
                    if content:
                        movies = content["影片"]
                        
                        # count = len(video_title_array)
                        prefix = content["素材文件前缀"]
                        # video_tail = content["片尾"]
                        print("初始化prefix:", prefix)
                        m = movies[0]
                        for m in movies:
                            video_title = m["标题"]
                            print("video_title:", video_title)
                            video_content = m["内容顺序"]
                            movie_cover = m["影片封面"]
                            bgm_obj = m["BGM"]
                            subtitle_obj = m["字幕"]
                            audio_obj = m["音频"]
                            tail_obj = m["片尾"]
                            mid = m["编号"]
                            future = executor.submit(engine.NewInstance, prefix, video_title, project_path, assets_path, video_content, movie_cover, bgm_obj, audio_obj, subtitle_obj, tail_obj, mid)
                            futures.append(future)

                # Wait for all threads to complete
                for future in futures:
                    future.result()    
                    print("视频合成完成")

        except FileNotFoundError:
            print(f"File '.yaml' not found")
        except yaml.YAMLError as e:
            print(f"Error parsing: {e}")
        
    return "成功"

def list_files():
    try:
        # 获取文件夹内所有文件和目录的列表
        entries = os.scandir(save_directory)
        
        # 创建一个列表来保存文件信息
        file_list = []
        
        for entry in entries:
            if entry.is_file():
                # 获取文件信息并添加到列表中
                file_info = {
                    'name': entry.name,
                    'size': f"{entry.stat().st_size / (1024 * 1024):.2f} MB",
                    'modified': entry.stat().st_mtime  # 文件最后修改时间戳
                }
                file_list.append(file_info)
        
        # 将文件列表转换为Pandas DataFrame以便于在Gradio中显示
        import pandas as pd
        df = pd.DataFrame(file_list)
        return df
    
    except Exception as e:
        return str(e)

def save_file(file):
    # 获取文件名
    file_name = os.path.basename(file.name)
    
    # 构建完整的保存路径
    save_path = os.path.join(save_directory, file_name)
    
    # 将上传的文件复制到指定路径
    with open(file.name, 'rb') as f_src, open(save_path, 'wb') as f_dst:
        f_dst.write(f_src.read())
    
    
    return f"文件已保存: {save_path}"
    

def change_button_able_upload(fileGR):
     if fileGR!=None:
          save_file(fileGR)
          return gr.update(visible=True)
     
def change_button_able_delate(fileGR):
     if fileGR!=None:
          return gr.update(visible=False)
     

def clip(file_scipt):
    return open_yaml(file_script)
    


     
with gr.Blocks() as demo:
    file_script = gr.File(label="选择要剪辑的脚本文件，请确保素材库中有与脚本文件对应的素材")
    
    file_footage = gr.File(label="选择素材文件上传")
    button=gr.Button("开始剪辑")
    # button.visible=False

    file_footage.upload(fn=change_button_able_upload,inputs=file_footage,outputs=button)
    # file_script.delete(fn=change_button_able_delate,inputs=file_script,outputs=button)
    gr.Markdown("### 素材库")
    # 创建一个表格输出用于显示文件信息
    file_table = gr.Dataframe(headers=["名称", "大小", "最后修改"], label="文件列表")
    
    # 创建一个按钮用于刷新文件列表
    refresh_button = gr.Button("刷新文件列表")
    
    # 当点击刷新按钮时，调用list_files函数更新文件列表
    refresh_button.click(list_files, outputs=file_table)
    demo.load(list_files, outputs=file_table)

    text = gr.Textbox(lines=2, interactive=True)
    button.click(fn=clip, inputs=file_script, outputs=text)


demo.launch(share=True)
