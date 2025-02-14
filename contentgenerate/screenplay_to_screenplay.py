

from langchain_community.llms.tongyi import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


import dashscope
import datetime

DASHSCOPE_API_KEY="sk-a48a1d84e015410292d07021f60b9acb"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

from contentgenerate import llm_base

# import llm_base



def get_screenplay_to_screenplay(sreenplay):
    template='''

       你是一位产品短视频IP设计师，我会给你一份脚本，请你根据脚本里的“内容”部分为我在保留原有主题上进行改写，改写要抓住原有特征的同时大幅度改变语言，但也要使得其看起来像一系列作品里的作品。
       你要注意，你的内容只需要考虑配音内容就可以，而不用考虑画面内容，内容不用太长，每个镜头20字左右即可，总长度100字左右
       
       你的产品故事或者使用场景输出格式参考要和原脚本一致，注意，务必格式保持一致，内容请你改写

                
    '''
    


    input=''''
       
        {sreenplay}

    '''
    template=template.format()
    input=input.format(sreenplay=sreenplay)
    res=llm_base.get_Tongyi_response(template,input)
    return res



if __name__ == '__main__':


    sreenplay='''  编号: 紫气东来-script1
工程: 紫气东来
标题: 回归自然的奢华体验
配音: zh-CN-YunxiNeural
字体: yishu.ttf
字号: 80
BGM : Nature.mp3
脚本:
  - 镜头: 风展示
    内容: 从名山大川采集的纯净空气，带您回归大自然的怀抱。
  - 镜头: 风展示
    内容: 特制陶罐密封保存，确保每一口空气都新鲜如初。
  - 镜头: 风展示
    内容: 模拟高山环境，浓缩高氧空气，让您随时随地享受清新。
  - 镜头: 风展示
    内容: 限量发售，稀有且独特，为生活增添一份奢华与艺术感。
  - 镜头: 风展示
    内容: 紫气东来，不仅是产品，更是一种健康、自然的生活态度。'''
    get_screenplay_to_screenplay(sreenplay)




