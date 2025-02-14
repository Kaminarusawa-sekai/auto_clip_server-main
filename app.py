import gradio as gr
import yaml
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
import edge_tts

import autogen
import engine

from contentgenerate import llm_generate_content
from DataBase import database


from DataBase import database

import uuid

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

def auto_clip(text_enterprise_name,text_product_name,text_product_description,text_number):
    market_plan=llm_generate_content.get_market_plan(text_enterprise_name,text_product_name,text_product_description)
    hot_points_=database.get_hotpots()
    hot_points=[]
    for h in hot_points_:
        hot_points.append(h[1])
    hot_starts_=database.get_hotstarts()
    hot_starts=[]
    for h in hot_starts_:
        hot_starts.append(h[1])
    video_desciriptions={}
    videos=database.get_video_names()
    descriptions=database.get_video_descriptions()
    for v in videos:
        for d in descriptions:
            if v[0]==d[0]:
                video_desciriptions[v[1]]=d[1]
    voices_= asyncio.run(edge_tts.list_voices())
    voices=[]
    for v in voices_:
        if v["ShortName"].startswith("zh-CN"):
            voices.append(v["ShortName"]+":"+v["Gender"]+","+v["VoiceTag"]["ContentCategories"]+","+v["VoiceTag"]["VoicePersonalities"])
    
    all_BGM_files = os.listdir(save_directory)
    # 使用列表推导式筛选出所有以.mp4结尾的文件
    bGMS = [file for file in all_BGM_files if file.endswith('.mp3')]

    all_font_files = os.listdir(".")
    # 使用列表推导式筛选出所有以.mp4结尾的文件
    fonts = [file for file in all_font_files if file.endswith('.ttf')]

    v=None

    for i in range(text_number):
        uid=uuid.uuid1()
        yaml_file_redbbok="temp/redbook"+str(uid)+".yaml"
        yaml_file_douyin="temp/douyin"+str(uid)+".yaml"
        llm_generate_content.get_auto_screenplay(text_enterprise_name,text_product_name,text_product_description,market_plan,hot_points,hot_starts,video_desciriptions,voices,bGMS,fonts,yaml_file_redbbok,yaml_file_douyin)
        v=open_yaml(yaml_file_redbbok)
        v=open_yaml(yaml_file_douyin)
    
    return v


    





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

def process_upload(video_file, description):
    id=uuid.uuid1()
    save_file(video_file)
    database.insert_id_name_data(id,video_file)
    database.insert_id_description_data(id,description)

    return "上传成功"


database.create_db_and_tables()
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
    with gr.Tab("竞品报告生成剪辑脚本"):
        text_enterprise_name=gr.Text(label="输入企业的名字")
        text_costumer_anaysis=gr.Text(label="输入竞品报告")
        button=gr.Button("开始生成剪辑脚本")
        md_screenplot=gr.Markdown(value="剪辑脚本")
        button.click(fn=llm_generate_content.get_srennplay_plot,inputs=[text_enterprise_name,text_costumer_anaysis],outputs=md_screenplot)
    with gr.Tab("产品找客户画像"):
        text_product_name=gr.Text(label="输入产品的名字")
        text_product_description=gr.Text(label="输入产品的描述")
        button=gr.Button("开始生成产品客户画像")
        md_competitive=gr.Markdown(value="客户画像报告")
        button.click(fn=llm_generate_content.get_custom_profiling_anaysis,inputs=[text_product_name,text_product_description],outputs=md_competitive)
    with gr.Tab("客户画像生成剪辑脚本"):
        text_enterprise_name=gr.Text(label="输入企业的名字")
        text_costumer_anaysis=gr.Text(label="输入客户画像")
        button=gr.Button("开始生成剪辑脚本")
        md_screenplot=gr.Markdown(value="剪辑脚本")
        button.click(fn=llm_generate_content.get_srennplay_plot,inputs=[text_enterprise_name,text_costumer_anaysis],outputs=md_screenplot)
   
    with gr.Tab("从热门视频生成剪辑脚本"):
        text_enterprise_name=gr.Text(label="输入你想要的主题")
        file_footage = gr.File(label="选择热门短视频文件上传")
        button=gr.Button("开始生成剪辑脚本")
        md_screenplot=gr.Markdown(value="剪辑脚本")
        button.click(fn=llm_generate_content.get_movie_to_screenplay,inputs=[text_enterprise_name,file_footage],outputs=md_screenplot)
    with gr.Tab("从剪辑脚本生成剪辑脚本"):
        text_sceenplay_name=gr.Text(label="输入你想要改写的脚本")
        button=gr.Button("开始生成剪辑脚本")
        md_screenplot=gr.Markdown(value="剪辑脚本")
        button.click(fn=llm_generate_content.get_screenplay_to_screenplay,inputs=[text_sceenplay_name],outputs=md_screenplot)

    with gr.Tab("智能剪辑"):
        text_enterprise_name=gr.Text(label="输入企业的名字")
        text_product_name=gr.Text(label="输入产品的名字")
        text_product_description=gr.Text(label="输入产品的描述")
        text_number=gr.Text(label="输入想要视频条数")
        button=gr.Button("开始智能剪辑")
        video = gr.PlayableVideo()
        button.click(fn=auto_clip, inputs=[text_enterprise_name,text_product_name,text_product_description,text_number], outputs=video)
        
    with gr.Tab("剪辑"):
        file_script = gr.File(label="选择要剪辑的脚本文件（.yaml），请确保素材库中有与脚本文件对应的素材")
        file_script.upload(fn=process_file,inputs=file_script,outputs=None)

        file_footage = gr.File(label="选择素材文件上传")
        text_video_description=gr.Text(label="输入视频的描述")
        submit_button = gr.Button("上传素材")

        output_text = gr.Textbox(label="Output", interactive=False)

        submit_button.click(process_upload, inputs=[file_footage, text_video_description], outputs=output_text)

        button_hot=gr.Button("更新热点")
        # button_click=
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
