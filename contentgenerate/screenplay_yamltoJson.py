

from langchain_community.llms.tongyi import Tongyi
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


DASHSCOPE_API_KEY="sk-a48a1d84e015410292d07021f60b9acb"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY




template='''
       你是一个严苛的人，注重格式，我会给你一段文字，你需要按照输出参考将文字进行规整，请注意，输入里可能有多余的内容，你需要将他剔除掉以保证其完全符合输出参考，可能有不需要的标题段，
       你需要仅保留脚本部分。对话/旁白文本等部分不算做脚本部分，只有标注了脚本的标题段才算脚本
       你需要格式的文字如下
       {theme}
       你需要输出应该是个json，json格式参考以下：
            {{
            "编号": 文本中出现的编号名，例如：森咖啡-script1,
            "工程": 文本中出现的工程名，例如：森咖啡,
            "标题": 文本中出现的标题名，例如：快乐氛围
            "配音": 文本中出现的配音名，例如：zh-CN-YunxiNeural
            "字体": 文本中出现的字体名，例如：yishu.ttf
            "字号": 文本中出现的字号名，例如：80
            "BGM: : 文本中出现的BGM名，例如Differnt.mp3
            "脚本":[
            {{"镜头": 文本中出现的镜头名，例如：猫。 "内容":文本中出现的内容名，例如：森咖啡为您创造愉快的氛围就像与小猫玩耍一样快乐充满每一个角落}}
            {{"镜头": 文本中出现的镜头名，例如：大厅。 "内容":文本中出现的内容名，例如：在这个温馨的大厅中幸福的氛围伴随着香浓的咖啡让您的心情愉悦起来}}
            {{"镜头": 文本中出现的镜头名，例如：卡座2。 "内容":文本中出现的内容名，例如舒适的卡座营造出宜人的快乐氛围让您与亲友共度美好的时光}}
            {{"镜头": 文本中出现的镜头名，例如：卡座1。 "内容":文本中出现的内容名，例如在舒适的卡座中与亲友共享美味咖啡每一刻都充满了快乐和欢笑}}
            {{"镜头": 文本中出现的镜头名，例如：门头。"内容":文本中出现的内容名，例如当您需要一份快乐森咖啡的大门随时为您敞开让您进入快乐的世界}}

            ] 
                }}
    '''


llm=Tongyi(model_name="qwen-plus",temperature=1)


prompt=PromptTemplate(
        template=template,
        input_variables=["theme"]#这个question就是用户输入的内容,这行代码不可缺少
)

chain = prompt|llm


def get_screenplay_yamltojson(theme):
    input={
        "theme":theme,
    }
    res=chain.invoke(input)#运行
    print(res)#打印结果
    return res



if __name__ == '__main__':
    theme='''
# 编号: 袜子-script1
## 工程: 袜子
## 标题: 智慧生活，从脚开始
## 配音: zh-CN-YunxiNeural
## 字体: yishu.ttf
## 字号: 80
## BGM : Technology.mp3

### 脚本:
- 镜头: 清晨起床
    内容: 小李穿上一双智能袜子，准备迎接新的一天。
- 镜头: 工作途中
    内容: 小李在拥挤的人群中行走自如，智能袜子提供舒适的支撑和保护。
- 镜头: 办公室内
    内容: 小李展示袜子上的健康监测功能，如步数统计、压力分布等。
- 镜头: 健身房锻炼
    内容: 小李穿着智能袜子进行高强度训练，袜子帮助他更好地感知运动状态并调整姿势。
- 镜头: 回家休息
    内容: 小李与家人分享一天的经历，并展示了袜子如何帮助他度过了充实的一天。

---     '''
    get_screenplay_yamltojson(theme)



