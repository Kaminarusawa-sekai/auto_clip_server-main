import gradio as gr
import yaml
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

import autogen
import engine

from contentgenerate import llm_generate_content

DASHSCOPE_API_KEY="sk-a48a1d84e015410292d07021f60b9acb"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

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
        output_path=""
        try:
            gen = autogen.AutoGen(f, project_directory)
            asyncio.run(gen.tts())
            
            project_name=gen.get_project_name()
            project_path = os.path.join(project_directory,project_name)
            assets_path = save_directory

            # project_name = os.path.basename(project_path)
            # print("project_name:", project_name)
            with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
                futures = []
                # for project_path in project_path_list:
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
                        # future = engine.NewInstance(prefix, video_title, project_path, assets_path, video_content, movie_cover, bgm_obj, audio_obj, subtitle_obj, tail_obj, mid)
                        futures.append(future)

                # Wait for all threads to complete
                for future in futures:
                    output_path=future.result()    
                    print("视频合成完成")
            return output_path
            # return os.path.join(".", project_path, mid + ".mp4")
        except FileNotFoundError:
            print(f"File '.yaml' not found")
        except yaml.YAMLError as e:
            print(f"Error parsing: {e}")
        
    

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

def delete_selected_file(selected_row):
    try:
        if selected_row is None or not isinstance(selected_row, dict) or 'name' not in selected_row:
            return "请选择要删除的文件。"
        
        file_name = selected_row['name']
        file_path = os.path.join(save_directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            return f"文件 '{file_name}' 已成功删除。"
        else:
            return "文件不存在或已删除。"
    except Exception as e:
        return str(e)


def clip(file_scipt):
    
    return open_yaml(file_script)
    # return "project\森咖啡-script2\森咖啡-script2.mp4"


def process_file(file_obj):
    # file_obj['name'] 是原始文件名
    # file_obj['orig_name'] 是用户上传的文件名
    # file_obj['temp_name'] 是服务器上的临时文件路径
     # global tmpdir
    global current_temp_file
    
    try:
        # 如果存在之前的临时文件，则删除它
        if current_temp_file and os.path.exists(current_temp_file):
            os.remove(current_temp_file)
        
        # 更新当前临时文件路径为新的文件路径
        current_temp_file = file_obj['temp_name']
        
        # 处理新上传的文件
        with open(current_temp_file, 'r') as f:
            content = f.read()
            return f"File content: {content}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

    # with open(file_obj['temp_name'], 'r') as f:
    #     content = f.read()
    #     return f"File content: {content}"

     
with gr.Blocks() as demo:
    with gr.Tab("行业找细分"):
        text_enterprise_name=gr.Text(label="输入企业的名字")
        text_enterprise_industry_name=gr.Text(label="输入企业的优势描述") 
        text_industry_name=gr.Text(label="输入想了解的行业")
        button=gr.Button("开始生成细分赛道推荐报告")
        md_segmented=gr.Markdown(value="产业细分赛道推荐报告")

        button.click(fn=llm_generate_content.get_segmentation_anaysis,inputs=[text_industry_name,text_enterprise_name,text_enterprise_industry_name],outputs=md_segmented)
    with gr.Tab("细分找产品"):
        text_industry_name=gr.Text(label="输入细分所属的行业")
        text_segmented_name=gr.Text(label="输入想了解的细分")
        text_enterprise_name=gr.Text(label="输入企业的名字")
        text_enterprise_industry_name=gr.Text(label="输入企业擅长的优势描述")
        
        button=gr.Button("开始生成赛道产品推荐报告")
        md_product=gr.Markdown(value="赛道产品推荐报告")
        button.click(fn=llm_generate_content.get_product_anaysis,inputs=[text_industry_name,text_segmented_name,text_enterprise_name,text_enterprise_industry_name],outputs=md_product)
    with gr.Tab("产品找竞品"):
        text_enterprise_name=gr.Text(label="输入企业的名字")
        text_product_name=gr.Text(label="输入想了解的竞品")
        text_product_description=gr.Text(label="需要的话输入一些产品描述")
        button=gr.Button("开始生成产品竞品报告")
        md_competitive=gr.Markdown(value="产品竞品报告")
        button.click(fn=llm_generate_content.get_competitive_anaysis,inputs=[text_enterprise_name,text_product_name,text_product_description],outputs=md_competitive)
    with gr.Tab("生成剪辑脚本"):
        text_enterprise_name=gr.Text(label="输入企业的名字")
        text_competitive_anaysis=gr.Text(label="输入竞品报告")
        button=gr.Button("开始生成剪辑脚本")
        md_screenplot=gr.Markdown(value="剪辑脚本")
        button.click(fn=llm_generate_content.get_srennplay_plot,inputs=[text_enterprise_name,text_competitive_anaysis],outputs=md_screenplot)
    with gr.Tab("剪辑"):
        file_script = gr.File(label="选择要剪辑的脚本文件（.yaml），请确保素材库中有与脚本文件对应的素材")
        file_script.upload(fn=process_file,inputs=file_script,outputs=None)
        file_footage = gr.File(label="选择素材文件上传")
        html_tips1=gr.HTML(value="没思路可以去pixabay找素材")
        html_tips2=gr.HTML(value="剪辑一般时长30s左右合成时间在15min左右，请耐心等待")
        button=gr.Button("开始剪辑")
        # button.visible=False

        # file_footage.upload(fn=change_button_able_upload,inputs=file_footage,outputs=button)
        # file_script.delete(fn=change_button_able_delate,inputs=file_script,outputs=button)
        gr.Markdown("### 素材库")
        # 创建一个表格输出用于显示文件信息
        file_table = gr.Dataframe(headers=["名称", "大小", "最后修改"], label="文件列表")
        
        # 创建一个按钮用于刷新文件列表
        refresh_button = gr.Button("刷新文件列表")
        # confirm_delete = gr.Checkbox(label="我确认要删除此文件")
        # delete_button = gr.Button("删除选中的文件")
        # output_message = gr.Textbox(label="操作结果")
    
        # 当点击刷新按钮时，调用list_files函数更新文件列表
        refresh_button.click(list_files, outputs=file_table)
        demo.load(list_files, outputs=file_table)

         # 删除文件逻辑：当点击删除按钮时，检查是否选中了确认框并执行删除操作
        # delete_button.click(
        #     fn=delete_selected_file(selected_row),
        #     inputs=[file_table.select(), confirm_delete],
        #     outputs=output_message
        # )

        video = gr.PlayableVideo()
        button.click(fn=clip, inputs=file_script, outputs=video)


demo.launch(share=True)
