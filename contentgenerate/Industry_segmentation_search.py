

from langchain_community.llms.tongyi import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


import dashscope
import datetime

DASHSCOPE_API_KEY="sk-a48a1d84e015410292d07021f60b9acb"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY


from contentgenerate import llm_base






def get_industry_segmentation_search(industry):
        
    template='''

                ###背景：
                在当今快速发展的经济环境中，各行业不断细分，新兴赛道层出不穷。为了准确把握{industry}的全貌，我们需要对这一行业的各个细分领域进行详尽的梳理和分析。此任务对于了解市场动态、识别投资机会以及制定商业策略至关重要。

                ###目标：
                请根据提供的信息，找出并详细描述[具体行业名称]的所有细分赛道。确保每个细分赛道都有清晰的定义，并尽可能提供其规模、增长趋势、关键参与者及技术驱动因素等信息。

                ###风格：
                采用专业分析师的写作风格，以数据为支撑，逻辑严密，论证充分，同时保持文字的流畅性和可读性。

                ###语气：
                使用正式而客观的语气，避免个人情感色彩，确保信息传递的专业性和可靠性。

                ###受众：
                该内容面向的是行业内的专业人士，包括但不限于投资者、企业家、研究员等。他们具备一定的行业知识基础，但需要更深入的数据支持和见解来辅助决策。

                ###输出：
                请以结构化的专业分析报告形式呈现结果，包含但不限于以下部分：

                    行业概览
                    细分赛道列表及其简要说明
                    各赛道市场规模与增长率
                    关键技术和创新点
                    主要企业及其市场地位
                    未来发展趋势预测
                    
                ###步骤：
                为了实现上述目标，请遵循以下步骤进行研究和撰写：
                    确定研究范围
                    确认您将要探讨的行业的边界和核心特征，明确哪些元素属于这个行业的范畴。
                    收集资料
                    从权威渠道搜集关于[具体行业名称]的信息，包括但不限于官方统计数据、市场研究报告、学术论文、新闻报道等。
                    识别细分赛道
                    根据收集到的资料，列出行业内所有可能存在的细分赛道，注意不要遗漏任何重要的分支领域。
                    分析每个细分赛道
                    对每一个细分赛道进行深入分析，记录其定义、市场规模、增长率、主要参与者和技术驱动因素等关键信息。
                    评估技术和市场趋势
                    探讨影响各细分赛道的技术进步和市场变化，评估这些因素如何塑造未来的行业发展路径。
                    构建细分赛道矩阵
                    将获得的信息整理成一个逻辑清晰的框架，如按照服务对象、技术类型、应用场景等维度对细分赛道进行分类整理。
                    撰写专业分析报告
                    根据上述分析结果，编写一份结构化且详尽的专业分析报告，确保报告符合预设的格式要求。
                    审查与修订
                   请你完成初稿后，你要仔细检查报告的内容准确性、逻辑连贯性和语言表达质量，必要时由你进行修订以提高报告的质量，这里是我给你的提示，你尽量不要在回答出现这些语句。
        
        '''
    


    input=''''
        以下是你需要分析的内容：
        {industry}="你需要研究的行业"
    '''
    input=input.format(industry=industry)
    template=template.format(industry=industry)
    res=llm_base.get_Tongyi_response(template,input)
    return res





if __name__ == '__main__':

    industry="AI行业"
    get_industry_segmentation_search(industry)

