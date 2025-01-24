

from langchain_community.llms.tongyi import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


import dashscope
import datetime

DASHSCOPE_API_KEY="sk-a48a1d84e015410292d07021f60b9acb"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

from contentgenerate import llm_base







def get_industry_segmentation_anaysis(enterprise_name,product_name,product_description):
    template='''

        背景：
        {product_name}是{enterprise_name}推出的一款产品。该产品主要功能是{product_description}。为了更好地理解市场环境和竞争对手的表现，进行详细的产品竞品分析对于优化产品策略和提升竞争力至关重要。

        目标：
        请根据[具体产品名称]的产品简介，进行全面的竞品分析。分析应涵盖主要竞争对手及其产品的特性、优势、劣势、市场定位及用户反馈等方面，并为[具体企业名称]提出针对性的竞争策略建议。

        风格：
        采用市场分析师的专业写作风格，注重数据支持和逻辑推理，确保内容既具有学术严谨性又易于理解。

        语气：
        使用正式而客观的语气，保持专业性和可靠性，避免个人情感色彩，以确保信息传递的准确性和公正性。

        受众：
        这份报告面向的是企业的产品研发团队、市场营销部门及高层决策者，他们需要深入了解市场竞争状况，并寻找改进产品和制定竞争策略的方法。

        输出：
        请以结构化的分析报告形式呈现结果，包括但不限于以下部分：

        产品概述
        竞争对手识别
        竞品特性对比
        市场表现与用户反馈分析
        SWOT分析（优势Strengths、劣势Weaknesses、机会Opportunities、威胁Threats）
        竞争策略建议
        步骤：
        为了实现上述目标，请遵循以下步骤进行研究和撰写：

        产品概述
        描述产品的基本特征。
        竞争对手识别
        确定在相同细分市场内的主要竞争对手，列出他们的品牌名称和代表性的竞争产品。
        竞品特性对比
        对每个竞争产品进行详细的特性分析，比较它们与产品之间的异同点，重点关注功能、性能、价格、用户体验等关键因素。
        市场表现与用户反馈分析
        收集并分析各竞争产品在市场上的销售数据、市场份额变化、用户评价和社交媒体反馈。
        评估用户对不同产品的满意度和不满之处，找出影响购买决策的主要因素。
        SWOT分析
        对于每个主要竞争对手，进行SWOT分析，明确其相对于产品的优势和劣势，同时识别出潜在的机会和威胁。
        竞争策略建议
        根据竞品分析的结果，为[具体企业名称]提出具体的竞争策略建议，如差异化定位、技术创新、成本控制、客户服务改善等。
        提供短期和长期的行动方案，确保企业在激烈的市场竞争中保持领先地位。
        审查与修订
        请你完成初稿后，你要仔细检查报告的内容准确性、逻辑连贯性和语言表达质量，必要时由你进行修订以提高报告的质量，这里是我给你的提示，你尽量不要在回答出现这些语句。
                
    '''
    


    input=''''
        以下是你需要分析的内容：

    '''
    template=template.format(enterprise_name=enterprise_name,product_name=product_name,product_description=product_description)
    res=llm_base.get_Tongyi_response(template,input)
    return res





if __name__ == '__main__':

    enterprise_name="中科蓝吧数字科技（苏州）有限公司"
    product_name="全渠道智能客服平台"
    product_description='''
1. **市场定位**
   - 打造一个集成了多种沟通渠道（电话、短信、邮件、网站在线客服、APP内置客服、社交媒体私信等）的一站式智能客服平台，为企业提供高效、便捷、低成本的客户服务管理工具。
2. **目标用户群体**
   - 中小型企业，尤其是那些正在经历数字化转型，希望以较低成本建立完善的客户服务系统的创业公司或成长型企业；大型企业集团中的客服部门，用于优化内部客服资源配置，提升整体服务效率。
3. **核心功能或价值主张**
   - 实现各渠道消息的集中管理和智能分发，根据客户历史交互记录和当前问题类型自动选择最合适的客服人员或智能应答程序进行处理；提供可视化报表工具，方便管理者实时监控客服工作状态和绩效指标；支持API接口对接，便于与其他业务系统（如CRM、ERP等）集成。
4. **技术实现路径**
   - 基于云计算架构搭建平台框架，采用容器化部署方式保证系统的高可用性和弹性伸缩能力；运用NLP技术对文本内容进行语义理解和分类，结合语音识别技术实现语音转文字功能，再通过深度学习算法训练智能应答模型；利用大数据分析技术挖掘用户行为数据，为智能分发策略提供依据。'''
   
    get_industry_segmentation_anaysis(enterprise_name,product_name,product_description)

