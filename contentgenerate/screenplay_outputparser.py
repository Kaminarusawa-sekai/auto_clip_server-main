

from langchain_community.llms.tongyi import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


DASHSCOPE_API_KEY="sk-a48a1d84e015410292d07021f60b9acb"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY




template='''
       你是一个严苛的人，注重格式，我会给你一段文字，你需要按照输出参考将文字进行规整
       你需要格式的文字如下
       {theme}
       你需要输出参考以下：
        编号: 森咖啡-script1
            工程: 森咖啡
            标题: 快乐氛围
            配音: zh-CN-YunxiNeural
            字体: yishu.ttf
            字号: 80
            脚本: 
            - 镜头: 猫
                内容: 森咖啡为您创造愉快的氛围就像与小猫玩耍一样快乐充满每一个角落
            - 镜头: 大厅
                内容: 在这个温馨的大厅中幸福的氛围伴随着香浓的咖啡让您的心情愉悦起来
            - 镜头: 卡座2
                内容: 舒适的卡座营造出宜人的快乐氛围让您与亲友共度美好的时光
            - 镜头: 卡座1
                内容: 在舒适的卡座中与亲友共享美味咖啡每一刻都充满了快乐和欢笑
            - 镜头: 门头
                内容: 当您需要一份快乐森咖啡的大门随时为您敞开让您进入快乐的世界
    '''


llm=Tongyi(model_name="qwen-plus",temperature=1)


prompt=PromptTemplate(
        template=template,
        input_variables=["theme"]#这个question就是用户输入的内容,这行代码不可缺少
)

chain = prompt|llm


def get_screenplay_plot_brainstrom(theme):
    input={
        "theme":theme,
    }
    res=chain.invoke(input)#运行
    print(res)#打印结果
    return res



if __name__ == '__main__':
    theme='''
  ### 创意短视频剧本

#### **混乱的办公室场景**
文件满天飞，员工尖叫奔跑，打印机纸张如瀑布倾泻。

**画面冻结与字幕**
“这是怎么发生的？”镜头迅速倒带，回到几分钟前的宁静。

#### **日常工作中的小问题**
打印机卡纸、电脑死机、客户电话不断，每个问题都让人头疼。

#### **引入AI解决方案**
技术顾问微笑着介绍中科蓝吧的AI助手，轻松幽默地演示其功能。

#### **逐步恢复秩序**
AI助手自动修复故障，优化性能，智能管理电话，办公室逐渐井然有序。

#### **高潮再现**
反向播放混乱场景，所有混乱逐渐消失，定格在安静整洁的办公室。

#### **结尾旁白**
技术顾问温柔而坚定地说：“有了中科蓝吧的AI解决方案，工作变得如此简单。”

---     '''
    get_screenplay_plot_brainstrom(theme)



