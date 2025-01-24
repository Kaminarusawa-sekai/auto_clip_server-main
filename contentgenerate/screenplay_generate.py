

from langchain_community.llms.tongyi import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import dashscope


DASHSCOPE_API_KEY="sk-a48a1d84e015410292d07021f60b9acb"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY




template='''
       你是一位产品短视频IP设计师，我会给你一些产品特点，你首先需要思考这个产品适合于哪些客户，
       然后根据客户特征为我讲述一个产品故事或者一个产品使用场景展示，两个选择一个就可以了
       我的企业是{enterprise_name}
       我的产品特点是{characterisitic}
       你要注意，你的内容只需要考虑配音内容就可以，而不用考虑画面内容，内容不用太长，每个镜头20字左右即可，总长度100字左右
       你的产品故事或者使用场景输出参考以下：
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
    
    '''


llm=Tongyi(model_name="qwen-plus",temperature=1)


prompt=PromptTemplate(
        template=template,
        input_variables=["enterprise_name","characterisitic"]#这个question就是用户输入的内容,这行代码不可缺少
)

chain = prompt|llm


def get_screenplay_plot(enterprise_name,characterisitic):
    input={
        "enterprise_name":enterprise_name,
        "characterisitic":characterisitic,
    }
    dashscope.api_key=DASHSCOPE_API_KEY
    res=chain.invoke(input)#运行
    print(res)#打印结果
    return res



if __name__ == '__main__':
    enterprise_name="中科蓝吧数字科技有限公司"
    characterisitic='''1. **广泛的市场覆盖**：能够触及全球范围内的用户和企业。
2. **强大的技术支持**：提供高效的技术支持服务，帮助用户解决问题。
3. **活跃的开发者社区**：拥有一个活跃且充满活力的开发者社区，促进技术交流与创新。
4. **强大的机器人管理功能**：具备优秀的机器人管理和控制能力，确保自动化流程的顺畅运行。
5. **高度定制化的解决方案**：根据客户需求提供高度定制化的产品和服务，满足特定行业的特殊需求。
6. **卓越的AI集成能力**：在RPA基础上结合了先进的AI技术，适用于处理复杂的业务流程。
7. **直观易用的用户体验**：设计简洁直观的用户界面，易于上手使用。
8. **企业级管理友好**：针对大型企业的管理需求进行了优化，方便管理员操作和维护。
9. **适合复杂业务流程**：特别适合处理涉及多步骤或多条件判断的复杂任务。
10. **流程自动化、数据处理、报表生成等核心功能**：提供了全面的基础功能来简化日常工作任务。
11. **跨平台支持**：能够在多个操作系统或平台上无缝运行。
12. **安全性及机器人管理功能**：强调安全性和稳定的机器人管理机制。
13. **客户满意度高**：获得用户的积极评价，特别是在定制化能力和客户服务方面表现出色。
14. **低代码/无代码平台**：降低了使用的门槛，使得非技术人员也能轻松创建自动化流程。
15. **集成度更高的API接口**：促进了与其他系统的无缝对接，增强了系统的灵活性和扩展性。'''
    get_screenplay_plot(enterprise_name,characterisitic)



