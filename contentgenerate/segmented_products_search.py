

from langchain_community.llms.tongyi import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


import dashscope
import datetime

DASHSCOPE_API_KEY="sk-a48a1d84e015410292d07021f60b9acb"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

from contentgenerate import llm_base






def get_segmentation_product_search(industry,segmentation):
        
    template='''
        ###背景：
        在{industry}中，{segmentation}是一个快速增长且充满潜力的领域。随着技术进步和市场需求的变化，探索该细分赛道下的所有潜在产品方向对于企业抓住市场机会、实现创新发展至关重要。

        ###目标：
        请根据现有信息，全面分析[具体细分赛道名称]，并为该细分赛道提出一系列具有创新性和可行性的产品方向建议。每个产品方向应包含其市场定位、目标用户群体、核心功能或价值主张以及可能的技术实现路径。

        ###风格：
        采用产品经理或创新顾问的专业写作风格，注重创意与实践相结合，确保内容既富有前瞻性又具备实际操作性。

        ###语气：
        使用正式而鼓舞人心的语气，旨在激发创造力和行动力，同时保持专业性和客观性。

        ###受众：
        这份报告面向的是企业的研发团队、产品管理部门及高层决策者，他们需要深入了解细分赛道的潜力，并寻找新的产品开发方向来推动企业发展。

        ###输出：
        请以结构化的分析报告形式呈现结果，包括但不限于以下部分：

        ###细分赛道概述
        市场需求与趋势分析
        竞争态势评估
        潜在产品方向列表及其详细描述
        技术可行性分析
        ###步骤：
        为了实现上述目标，请遵循以下步骤进行研究和撰写：

        细分赛道概述
        描述具体细分赛道名称的基本特征，包括市场规模、增长率、主要参与者等。
        市场需求与趋势分析
        分析当前市场中存在的未满足需求或痛点，以及未来可能的趋势变化。
        识别消费者偏好和技术发展的动向，理解这些因素如何影响新产品的需求。
        竞争态势评估
        调查市场上现有的竞争对手及其提供的产品和服务。
        分析竞争对手的优势和不足，找出市场的空白点或改进空间。
        潜在产品方向生成
        基于前几步的研究成果，构思多个潜在的产品方向。
        对每个产品方向进行初步定义，明确其市场定位、目标用户群体、核心功能或价值主张。
        技术可行性分析
        评估每个产品方向的技术可行性，考虑所需的技术资源、开发难度、成本效益等因素。
        探讨是否有现成的技术解决方案可以利用，或者是否需要投入研发新科技。
        优先级排序与推荐
        根据市场需求、竞争态势和技术可行性等因素，对所有潜在产品方向进行优先级排序。
        提出最值得投资的几个产品方向，并简要说明理由。
        审查与修订
        请你完成初稿后，你要仔细检查报告的内容准确性、逻辑连贯性和语言表达质量，必要时由你进行修订以提高报告的质量，这里是我给你的提示，你尽量不要在回答出现这些语句。
        '''
    


    input=''''
        以下是你需要分析的内容：
        {segmentation}="你需要研究的细分领域"
    '''
    input=input.format(segmentation=segmentation)
    template=template.format(industry=industry,segmentation=segmentation)
    res=llm_base.get_Tongyi_response(template,input)
    return res





if __name__ == '__main__':

    industry="AI行业"
    segmentation="智能客服系统"
    get_segmentation_product_search(industry,segmentation)

