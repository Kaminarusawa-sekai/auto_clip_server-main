import yaml
import uuid
import json
import re
import os
import random

# from app import save_directory
save_directory="uploads"
# 假设这是您不规范的 YAML 文本
json_text = """
```json
{
    "编号": "袜子-script1",
    "工程": "袜子",
    "标题": "智慧生活，从脚开始",
    "配音": "zh-CN-YunxiNeural",
    "字体": "yishu.ttf",
    "字号": 80,
    "脚": [
        {
            "镜头": "清晨起床",
            "内容": "小李穿上一双智能袜子，准备迎接新的一天。"
        },
        {
            "镜头": "工作途中",
            "内容": "小李在拥挤的人群中行走自如，智能袜子提供舒适的支撑和保护。"
        },
        {
            "镜头": "办公室内",
            "内容": "小李展示袜子上的健康监测功能，如步数统计、压力分布等。"
        },
        {
            "镜头": "健身房锻炼",
            "内容": "小李穿着智能袜子进行高强度训练，袜子帮助他更好地感知运动状态并调整姿势。"
        },
        {
            "镜头": "回家休息",
            "内容": "小李与家人分享一天的经历，并展示了袜子如何帮助他度过了充实的一天。"
        }
    ]
}
```
"""

def find_file_without_extension(dir_path, filename_without_ext):
    # 遍历指定目录下的所有文件和文件夹
    for entry in os.scandir(dir_path):
        # 如果是文件，并且去掉扩展名后的文件名等于给定的文件名，则返回True
        if entry.is_file() and os.path.splitext(entry.name)[0] == filename_without_ext:
            return True
    # 如果遍历结束都没有找到匹配的文件，则返回False
    return False

def search_len_and_content(json_text):
    # 使用正则表达式匹配"镜头"和"内容"
    pattern = r'"镜头"\s*:\s*"([^"]+)"\s*,\s*"内容"\s*:\s*"([^"]+)"'
    matches = re.findall(pattern, json_text)

    # 组装结果
    result = [{"镜头":lens ,"内容":content} for lens, content in matches]
    return result
    
def pick_random_mp4(file_path):
    # 列出所有在指定目录下的文件和文件夹
    all_files = os.listdir(file_path)
    # 使用列表推导式筛选出所有以.mp4结尾的文件
    mp4_files = [file for file in all_files if file.endswith('.mp4')]
    
    if not mp4_files:
        print("没有找到任何MP4文件。")
        return None
    
    while True:
        # 随机选择一个mp4文件
        selected_file = os.path.splitext(random.choice(mp4_files))[0]
        if selected_file !="片尾":
            break
    return selected_file

def repaire_yaml(json_text,filepath):
    tempid=uuid.uuid1()
    json_text=json_text.replace("\n","")
    startbraces=json_text.find("{")
    endbraces=json_text.rfind("}")
    json_text=json_text[startbraces:endbraces+1]
    # json_text=json_text[9:-4]
    # 加载 YAML 文本到 Python 数据结构中
    content = json.loads(json_text)
    if '编号' not in content:
        content['编号']=tempid
    if '工程' not in content:
        content['工程']=tempid
    if '配音' not in content:
        content['配音']="zh-CN-YunxiNeural"
    if '字体' not in content:
        content['字体']="yishu.ttf"
    if '字号' not in content:
        content['字号']="80"
    if 'BGM' not in content:
        content["BGM"]="Nature.mp3"
    if '脚本' not in content:
        if '镜头' in json_text:
            try:
                result=search_len_and_content(json_text)
                content["脚本"]=result
            except Exception as e:
                return False
        else:
            return False
        for c in content['脚本']:
            if '镜头' not in c or '内容' not in c:
                try:
                    result=search_len_and_content(json_text)
                    content["脚本"]=result
                except Exception as e:
                    return False

    
    for c in content["脚本"]:
        if not find_file_without_extension(save_directory,c["镜头"]):
            c["镜头"]=pick_random_mp4(save_directory)
        
    


    
    with open(filepath, 'w', encoding='utf-8') as f:
        # 将调整后的数据结构导出为 YAML 格式的字符串
        formatted_yaml = yaml.dump(content, stream=f,default_flow_style=False, allow_unicode=True,sort_keys=False)

        print(formatted_yaml)

filepath="1.yaml"
repaire_yaml(json_text,filepath)