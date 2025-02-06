

from langchain_community.llms.tongyi import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


import dashscope
import datetime

DASHSCOPE_API_KEY="sk-a48a1d84e015410292d07021f60b9acb"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

from contentgenerate import llm_base,audio2text





def get_movie_voice_to_screenplay(topic,voice):
    template='''

        ###背景：
        我会给你提供一段短视频的语音。通过分析这段语音的内容、情感表达、语速、语调等元素，我们可以推测出该短视频的剪辑风格和表现手法。基于这种风格，我们将为一个特定的主题{topic}创作一份视频脚本，旨在保持相似的情感氛围和视觉效果。

        ###目标：
        请根据提供的短视频中的语音内容，分析并揣测该视频的剪辑表现方式，然后根据分析结果为指定的主题创作一份视频脚本。脚本应包括场景描述、对话/旁白文本、视觉元素说明以及音乐和音效建议。

        ###风格：
        采用影视编剧的专业写作风格，注重情节发展、人物塑造和视觉叙事技巧，确保内容既具有创意性又易于实现。

        ###语气：
        使用富有创造性和激励性的语气，激发想象力，同时保持专业性和实际可操作性。

        ###受众：
        这份脚本面向的是视频制作团队，包括导演、剪辑师、摄影师及配音演员等，他们需要具体且详细的指导来完成高质量的视频制作。

        ###输出：
        请以结构化的格式呈现结果，你的输出参考以下：
            编号: 森咖啡-script1
            工程: 森咖啡
            标题: 快乐氛围
            配音: zh-CN-YunxiNeural
            字体: yishu.ttf
            字号: 80
            BGM : Diffrent.mp3
            脚本: 
            - 镜头: 展示
                内容: 森咖啡为您创造愉快的氛围就像与小猫玩耍一样快乐充满每一个角落
            - 镜头: 展示
                内容: 在这个温馨的大厅中幸福的氛围伴随着香浓的咖啡让您的心情愉悦起来
            - 镜头: 展示
                内容: 舒适的卡座营造出宜人的快乐氛围让您与亲友共度美好的时光
            - 镜头: 展示
                内容: 在舒适的卡座中与亲友共享美味咖啡每一刻都充满了快乐和欢笑
            - 镜头: 展示
                内容: 当您需要一份快乐森咖啡的大门随时为您敞开让您进入快乐的世界
        ###步骤：
        为了实现上述目标，请遵循以下步骤进行研究和撰写：

        #短视频剪辑表现方式分析
        分析语音内容的情感色彩（如欢快、严肃、感人等）、语速（快、慢）、语调（高亢、低沉）等特征。
        根据这些特征推断视频可能采用的剪辑风格（如快速切换、缓慢过渡、特写镜头等），以及视觉和听觉元素的配合方式。
        #确定特定主题
        明确视频脚本需要围绕的主题或核心信息，例如环保意识提升、科技产品介绍等。
        #创作视频脚本
        场景描述：详细描述每个场景的设置，包括地点、时间、参与角色及其行为。
        对话/旁白文本：编写清晰且吸引人的对话或旁白，确保与选定的主题紧密相关。
        视觉元素说明：提供关于如何拍摄每个场景的具体指示，比如镜头的选择、视角的变化等。
        音乐和音效建议：推荐适合的背景音乐类型及关键音效，增强观众的情感共鸣。
        #整合与调整
        将所有元素整合成一个连贯的故事线，确保逻辑流畅，视觉与听觉效果相得益彰。
        根据初步反馈对脚本进行必要的修订和完善。
        #审查与优化
        完成初稿后，你需要仔细检查脚本的内容完整性、逻辑连贯性和执行可行性，必要时进行优化以提高最终作品的质量。
        ### 你需要模仿的短视频语音
        {voice}
        
        
                
    '''
    


    input=''''
        以下是你需要创作的主题：
        {topic}

    '''
    template=template.format(topic=topic,voice=voice)
    input=input.format(topic=topic)
    res=llm_base.get_Tongyi_response(template,input)
    return res



def get_movie_to_screenplay(filepath,topic):
    voice=audio2text.vocie2text_offline(filepath)
    get_movie_voice_to_screenplay(topic,voice)

if __name__ == '__main__':

    topic="袜子"
    voice='''  小李通过问卷了解家庭财务状况，生成详细的财务健康报告。系统自动调整投资策略，帮助小李实现长期稳健的财务规划。
    定期推送理财小贴士，培养良好的财务管理习惯。
    强大的AI技术推荐个性化投资组合，让理财更简单高效。
    高效客服随时响应需求，确保每一步都安心无忧。'''
    get_movie_voice_to_screenplay(topic,voice)

