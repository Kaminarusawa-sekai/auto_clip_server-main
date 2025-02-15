

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






def get_product_characterisitc(competitive_report):
        
    template='''
        我会提供给你一份竞品报告，你需要将竞品报告中所有出现的产品优点告诉我，注意，你只需要告诉我优点就可以了，不需要告诉我具体的公司名
        注意，你的回答中不要出现公司或者企业名字，把所有产品优点一起告诉我就可以了
        以下是你要分析的竞品报告
        {competitive_report}
        '''
    


    input=''''
        以下是你需要分析的内容：
        {competitive_report}="你要分析的竞品报告"
    '''
    input=input.format(competitive_report=competitive_report)
    template=template.format(competitive_report=competitive_report)
    res=llm_base.get_Tongyi_response(template,input)
    return res





if __name__ == '__main__':

    
   competitive_report='''### 智能RPA助手竞品分析报告

#### 1. 产品概述
**智能RPA助手**是中科蓝吧数字科技有限公司推出的一款具备AI能力的自动化工具，旨在帮助企业简化日常运营中的繁琐工作。其核心功能包括但不限于流程自动化、数据处理、报表生成等。该产品采用先进的AI技术，能够自适应不同业务场景，并提供直观的用户界面和强大的数据分析能力。目 标用户群体主要为中大型企业的IT部门、财务部门、人力资源部门等，市场定位为高端企业级RPA解决方案。

#### 2. 竞争对手识别
在智能RPA助手所处的细分市场中，以下是主要竞争对手及其代表性产品：
- **UiPath**：全球领先的RPA平台，提供从开发到部署的一站式解决方案。
- **Automation Anywhere**：专注于企业级自动化，以其强大的机器人管理和安全特性著称。
- **Blue Prism**：最早进入市场的RPA供应商之一，以高度定制化的解决方案闻名。
- **WorkFusion**：结合了RPA与AI的智能自动化平台，适用于复杂业务流程。

#### 3. 竞品特性对比
| 特性/品牌 | 智能RPA助手 | UiPath | Automation Anywhere | Blue Prism | WorkFusion |
|-----------|--------------|--------|---------------------|------------|-------------|
| **核心功能** | 流程自动化、数据处理、报表生成 | 流程自动化、跨平台支持 | 流程自动化、机器人管理 | 流程自动化、定制化服务 | RPA + AI集成 |
| **AI能力** | 强 | 中等 | 弱 | 弱 | 强 |
| **用户体验** | 直观易用 | 复杂但功能强大 | 企业级管理友好 | 定制化要求高 | 高度集成 |
| **价格区间** | 中等偏上 | 高端 | 高端 | 高端 | 高端 |
| **市场定位** | 中大型企业 | 全球企业 | 企业级市场 | 企业级市场 | 全球企业 |

#### 4. 市场表现与用户反馈分析
根据市场调研机构的数据，各竞争产品的市场表现如下：
- **UiPath**：占据全球RPA市场份额的约30%，用户评价普遍较高，尤其在技术支持和社区活跃度方面表现突出。
- **Automation Anywhere**：市场份额约为25%，用户对其安全性及机器人管理功能赞赏有加，但在灵活性和易用性方面存在一些批评。
- **Blue Prism**：市场份额约为20%，用户对其定制化能力和客户服务满意，但认为成本过高。
- **WorkFusion**：市场份额约为15%，用户对其AI集成能力印象深刻，但价格昂贵且学习曲线陡峭。

#### 5. SWOT分析

##### UiPath
- **优势（Strengths）**：广泛的市场覆盖、强大的技术支持、活跃的开发者社区。
- **劣势（Weaknesses）**：部分高级功能需要额外付费，导致整体成本上升。
- **机会（Opportunities）**：继续扩展AI集成能力，增强与其他系统的兼容性。
- **威胁（Threats）**：新进入者可能带来技术和价格上的挑战。

##### Automation Anywhere
- **优势（Strengths）**：强大的机器人管理功能，适合大型企业使用。
- **劣势（Weaknesses）**：用户体验相对复杂，不适合小型企业。
- **机会（Opportunities）**：简化操作流程，降低入门门槛。
- **威胁（Threats）**：来自其他更灵活、更经济的竞争对手的压力。

##### Blue Prism
- **优势（Strengths）**：高度定制化的解决方案，适合特定行业需求。
- **劣势（Weaknesses）**：较高的实施成本和较长的学习周期。
- **机会（Opportunities）**：拓展中小型企业市场，提供更具性价比的产品。
- **威胁（Threats）**：市场竞争加剧，可能导致市场份额流失。

##### WorkFusion
- **优势（Strengths）**：卓越的AI集成能力，适合复杂业务流程。
- **劣势（Weaknesses）**：价格高昂，学习曲线陡峭。
- **机会（Opportunities）**：进一步优化用户体验，降低实施难度。
- **威胁（Threats）**：价格敏感型客户可能会转向更便宜的替代方案。

#### 6. 竞争策略建议

##### 短期行动方案
- **差异化定位**：强调智能RPA助手在AI能力上的优势，尤其是在自然语言处理和图像识别方面的应用，形成差异化竞争。
- **技术创新**：持续投入研发，提升产品的智能化水平，确保在技术上保持领先地位。
- **客户服务改善**：建立完善的售后服务体系，提供快速响应的技术支持，增强用户粘性。

##### 长期行动方案
- **市场拓展**：逐步扩大市场份额，特别是在金融、制造等关键行业，通过行业案例展示产品价值。
- **合作伙伴关系**：与更多第三方系统和服务提供商建立合作关系，打造开放的生态系统。
- **成本控制**：优化内部流程，降低成本结构，提高产品性价比，吸引更多潜在客户。

通过以上策略的实施，智能RPA助手可以在激烈的市场竞争中保持领先地位，并不断提升自身的市场竞争力。
# 人工智能行业细分赛道专业分析报告

## 行业概览

人工智能（AI）作为一项颠覆性的技术，正深刻地改变着全球经济和社会结构。从自动化流程到智能决策支持系统，AI的应用范围极为广泛，涵盖了 医疗、金融、制造、交通等多个领域。根据最新数据，2023年全球AI市场规模预计达到1906亿美元，并以每年超过30%的速度持续增长。

随着算法优化、计算能力提升以及大数据资源的丰富，AI技术正在向更深层次和更广泛的场景渗透。与此同时，各国政府和企业纷纷加大在AI领域的 投入，推动技术创新与应用落地，为行业发展注入强劲动力。

## 细分赛道列表及其简要说明

### 1. 计算机视觉
计算机视觉是指机器通过摄像头或其他成像设备获取并处理图像信息的能力。该领域主要应用于安防监控、自动驾驶、工业检测等场景。
- **定义**：使计算机能够“看”并理解周围环境的技术。
- **规模**：2023年全球市场规模约为480亿美元。
- **增长率**：过去五年复合年均增长率（CAGR）为35%，预计未来三年将继续保持高速增长。
- **关键参与者**：商汤科技、旷视科技、海康威视等。
- **技术驱动因素**：深度学习算法的进步、GPU/CPU性能增强、边缘计算的发展。

### 2. 自然语言处理（NLP）
自然语言处理旨在让计算机理解、生成人类语言，从而实现人机交互或文本自动处理。
- **定义**：研究计算机与人类语言之间交互的技术。
- **规模**：2023年全球市场规模约为250亿美元。
- **增长率**：过去五年CAGR为27%，未来有望加速发展。
- **关键参与者**：百度、科大讯飞、阿里云等。
- **技术驱动因素**：预训练模型如BERT、GPT系列的发展、Transformer架构的应用。

### 3. 语音识别与合成
语音识别将音频转化为文字，而语音合成为将文字转换为自然流畅的声音输出。
- **定义**：涉及声音信号处理及语言模型构建的技术。
- **规模**：2023年全球市场规模约为200亿美元。
- **增长率**：过去五年CAGR为28%，随着智能家居设备普及率提高，市场前景广阔。
- **关键参与者**：谷歌、苹果、亚马逊等国际巨头，国内有科大讯飞、思必驰等。
- **技术驱动因素**：端到端深度学习模型、多模态融合技术。

### 4. 机器人过程自动化（RPA）
RPA利用软件机器人模拟人类操作，完成重复性任务，如数据录入、文件管理等。
- **定义**：使用软件工具模仿人类工作流程的技术。
- **规模**：2023年全球市场规模约为20亿美元。
- **增长率**：过去五年CAGR为60%，是增速最快的AI子领域之一。
- **关键参与者**：UiPath、Automation Anywhere、Blue Prism等。
- **技术驱动因素**：低代码/无代码平台兴起、集成度更高的API接口。

### 5. 强化学习与智能决策
强化学习通过奖励机制引导智能体在环境中做出最优选择，广泛应用于游戏、推荐系统等领域；智能决策则侧重于基于数据的复杂问题求解。       
- **定义**：一种让机器自主学习策略以最大化长期收益的方法。
- **规模**：2023年全球市场规模约为150亿美元。
- **增长率**：过去五年CAGR为32%，应用场景不断拓展。
- **关键参与者**：DeepMind、腾讯、阿里巴巴等。
- **技术驱动因素**：AlphaGo的成功引发广泛关注，DQN、A3C等算法不断演进。

## 关键技术和创新点

1. **深度学习框架**：TensorFlow、PyTorch等开源框架降低了AI开发门槛，促进了技术交流与发展。
2. **迁移学习**：使得模型能够在不同但相关任务间共享知识，提高了泛化能力和效率。
3. **联邦学习**：允许多个参与方共同训练模型而不泄露各自的数据隐私，保障了数据安全。
4. **边缘计算**：将计算资源分布至靠近数据源的位置，减少了延迟并提升了实时响应能力。

## 主要企业及其市场地位

1. **谷歌**：凭借强大的搜索业务积累海量用户行为数据，其AI技术广泛应用于广告推荐、自动驾驶等多个领域。
2. **微软**：Azure云服务提供全面的AI开发工具和服务，Azure Machine Learning Studio备受开发者青睐。
3. **亚马逊**：AWS云平台为全球众多企业提供稳定的AI基础设施支持，Alexa智能助手引领智能家居潮流。
4. **阿里巴巴**：达摩院聚焦前沿研究，同时将AI成果应用于电商、物流等实际业务场景中。
5. **商汤科技**：专注于计算机视觉技术研发，在安防、金融等行业拥有显著市场份额。

## 未来发展趋势预测

1. **跨学科融合加深**：AI将与生物学、物理学等其他科学领域深度融合，催生更多新型应用场景。
2. **伦理法规逐步完善**：随着AI影响日益扩大，各国政府将加强对AI使用的规范管理，确保技术健康发展。
3. **个性化服务盛行**：借助精准数据分析，AI将为企业提供更加个性化的用户体验，助力商业价值最大化。
4. **量子计算助力突破**：一旦量子计算机实现商业化应用，AI计算效率将迎来质的飞跃，开启全新的智能时代。
### 中科蓝吧数字科技有限公司细分赛道推荐报告

#### 一、企业概况与现有业务评估

**企业简介：**
中科蓝吧数字科技有限公司专注于AI智能体开发，致力于为客户提供高效、智能的解决方案。公司拥有强大的研发团队和技术积累，在计算机视觉、 自然语言处理等领域已经取得了一定成果。目前，公司的主要产品包括智能客服系统、图像识别平台等。

**现有业务评估：**
1. **技术实力**：公司在AI算法和模型训练方面具备深厚的技术积淀，特别是在计算机视觉领域已形成较为成熟的产品线。
2. **市场表现**：通过多年努力，中科蓝吧在行业内树立了良好的品牌形象，客户涵盖金融、医疗等多个行业。然而，随着市场竞争加剧，现有市场份额增长面临一定压力。
3. **创新能力**：公司持续投入研发资源，保持技术创新能力，但在新兴技术如联邦学习、边缘计算等方面的应用尚处于探索阶段。
4. **运营效率**：内部管理流程较为规范，但面对快速变化的市场需求，决策速度和灵活性有待提升。

#### 二、行业细分赛道现状分析

根据当前AI行业发展态势，以下是几个值得关注的细分赛道：

1. **计算机视觉**：
   - **市场规模**：2023年全球市场规模约为480亿美元，CAGR为35%。
   - **竞争态势**：市场竞争激烈，头部玩家如商汤科技、旷视科技占据较大份额，但仍有大量中小企业活跃于特定应用场景中。
   - **技术趋势**：深度学习算法不断优化，边缘计算推动实时性增强，多模态融合成为新的发展方向。

2. **自然语言处理（NLP）**：
   - **市场规模**：2023年全球市场规模约为250亿美元，CAGR为27%。
   - **竞争态势**：国内市场上，百度、科大讯飞等企业在语音识别和语义理解方面具有明显优势，但细分场景下的创新机会依然存在。
   - **技术趋势**：预训练模型（如BERT、GPT系列）的发展极大地提升了NLP性能，跨语言迁移学习也成为研究热点。

3. **机器人过程自动化（RPA）**：
   - **市场规模**：2023年全球市场规模约为20亿美元，CAGR为60%，是增速最快的AI子领域之一。
   - **竞争态势**：国际厂商如UiPath、Automation Anywhere占据主导地位，但国内市场潜力巨大，本土企业正在迅速崛起。
   - **技术趋势**：低代码/无代码平台降低使用门槛，集成度更高的API接口促进与其他系统的无缝对接。

4. **强化学习与智能决策**：
   - **市场规模**：2023年全球市场规模约为150亿美元，CAGR为32%。
   - **竞争态势**：DeepMind、腾讯等公司在游戏、推荐系统等领域应用广泛，智能决策在金融风控、智能制造等领域的价值逐渐显现。
   - **技术趋势**：AlphaGo的成功引发广泛关注，DQN、A3C等算法不断演进，应用场景逐步扩展至更多复杂任务。

#### 三、潜在细分赛道识别与评估

基于中科蓝吧现有的技术和市场基础，结合未来发展趋势，以下三个细分赛道值得重点考虑：

1. **边缘计算与计算机视觉结合**：
   - **SWOT分析**：
     - **优势（Strengths）**：公司在计算机视觉领域已有丰富经验，边缘计算可进一步提升实时性和响应速度。
     - **劣势（Weaknesses）**：边缘计算基础设施建设成本较高，短期内可能影响利润空间。
     - **机会（Opportunities）**：智能家居、工业物联网等新兴市场对低延迟、高可靠性的需求强烈。
     - **威胁（Threats）**：竞争对手也在积极布局该领域，市场份额争夺将更加激烈。

2. **个性化推荐系统**：
   - **SWOT分析**：
     - **优势（Strengths）**：中科蓝吧在NLP和数据挖掘方面的技术积累有助于构建精准的用户画像和推荐模型。
     - **劣势（Weaknesses）**：个性化推荐涉及隐私保护问题，需确保合规性并赢得用户信任。
     - **机会（Opportunities）**：电商、内容分发等行业对个性化服务的需求持续增长，市场前景广阔。
     - **威胁（Threats）**：大型互联网平台凭借海量数据占据先发优势，新进入者面临较大挑战。

3. **RPA+AI的复合型解决方案**：
   - **SWOT分析**：
     - **优势（Strengths）**：中科蓝吧可以整合现有AI技术与RPA工具，提供更具竞争力的企业级解决方案。
     - **劣势（Weaknesses）**：RPA产品的市场认知度较低，教育市场的成本较高。
     - **机会（Opportunities）**：企业数字化转型加速，对提高工作效率和减少人力成本的需求迫切。
     - **威胁（Threats）**：国际厂商在品牌和技术上具有一定优势，需要加强本地化和差异化竞争。

#### 四、进入新赛道的战略建议

针对上述三个潜在细分赛道，提出以下具体进入策略：

1. **边缘计算与计算机视觉结合**：
   - **进入策略**：通过并购或战略合作方式获取边缘计算技术，建立联合实验室进行前瞻性研究。同时，推出面向特定行业的定制化解决方案，如智能安防、工业质检等。
   - **实施计划**：
     - 第一年：完成技术整合，启动试点项目。
     - 第二年：扩大试点范围，优化产品性能。
     - 第三年：全面推广，争取成为行业领先供应商。
   - **风险管理**：密切关注政策法规变化，确保技术方案符合安全标准；控制初期投资规模，逐步回收资金以减轻财务压力。

2. **个性化推荐系统**：
   - **进入策略**：自主研发核心算法，与电商平台、内容提供商合作开展试点应用。注重用户体验设计，打造差异化竞争优势。
   - **实施计划**：
     - 第一年：搭建技术框架，选择合作伙伴。
     - 第二年：迭代优化算法，拓展合作渠道。
     - 第三年：大规模商用，探索更多垂直领域。
   - **风险管理**：严格遵守数据隐私法规，建立健全的安全防护机制；定期评估效果，及时调整策略以应对市场反馈。

3. **RPA+AI的复合型解决方案**：
   - **进入策略**：采用自主研发为主、外部采购为辅的方式，快速推出基础版产品，逐步完善功能模块。积极参与行业协会活动，提升品牌知名度。
   - **实施计划**：
     - 第一年：完成产品研发，开展市场调研。
     - 第二年：推出试用版本，收集用户意见。
     - 第三年：正式发布，加大市场推广力度。
   - **风险管理**：加强对竞争对手动态的监测，灵活调整产品定位；注重客户服务体验，建立良好的口碑效应。

综上所述，中科蓝吧应根据自身特点和发展战略，选择合适的细分赛道切入，并制定切实可行的行动计划，以实现企业的持续增长和长远发展。 '''

   competitive_repor1t='''
   ### 全渠道智能客服平台分析报告

#### 1. 产品概述

全渠道智能客服平台是一款集成了多种沟通渠道（电话、短信、邮件、网站在线客服、APP内置客服、社交媒体私信等）的一站式智能客服平台。该平台旨在为企业提供高效、便捷且低成本的客户服务管理工具，特别适用于中小型企业和大型企业集团 中的客服部门。其核心功能包括：

- **多渠道消息集中管理和智能分发**：根据客户历史交互记录和当前问题类型自动选择最合适的客服人员或智能应答程序进行处理。
- **可视化报表工具**：方便管理者实时监控客服工作状态和绩效指标。
- **API接口对接**：支持与其他业务系统（如CRM、ERP等）集成。

技术实现路径基于云计算架构，采用容器化部署方式，运用NLP和语音识别技术，并结合深度学习算法训练智能应答模型，利用大数据分析优化智能分发策略。

#### 2. 主要竞品分析

在智能客服平台市场中，以下是几个主要竞争对手及其代表性产品：

- **Zendesk**
  - **目标客户群体**：中小企业及初创公司，尤其是电商和SaaS领域的企业。
  - **成功原因**：简单易用的界面设计、强大的多渠道支持和灵活的定价模式。

- **Freshdesk**
  - **目标客户群体**：中小型企业，特别是那些需要快速响应客户需求的企业。
  - **成功原因**：易于安装和配置，丰富的第三方应用集成，以及较低的入门成本。

- **Salesforce Service Cloud**
  - **目标客户群体**：大型企业，尤其是那些已经使用Salesforce CRM系统的公司。
  - **成功原因**：与CRM系统的无缝集成，强大的数据分析能力和高级定制选项。

- **Microsoft Dynamics 365 Customer Service**
  - **目标客户群体**：大型企业，特别是那些已经在使用微软生态系统的企业。
  - **成功原因**：与微软产品的紧密集成，AI驱动的智能服务和全面的安全性保障。

#### 3. 目标客户画像定义

根据全渠道智能客服平台的产品描述，初步勾勒出的目标客户画像如下：

- **年龄范围**：25-45岁，这部分人群通常处于职业生涯的关键阶段，对新技术有较高的接受度。
- **性别**：无明显性别偏好，但男性可能略多，因为科技和企业管理领域男性占比相对较高。
- **职业**：
  - 中小型企业的创始人或高层管理人员，他们正在经历数字化转型，希望以较低成本建立完善的客户服务系统。
  - 大型企业集团中的客服部门负责人或IT主管，负责优化内部客服资源配置，提升整体服务效率。
- **收入水平**：中等偏上，能够承担一定成本的技术投资。
- **教育背景**：本科及以上学历，具备一定的信息技术知识和管理经验。
- **生活方式**：忙碌的工作节奏，注重工作效率和时间管理，追求创新和高效的解决方案。
- **消费习惯**：倾向于选择性价比高、易于实施和维护的产品，重视长期合作和服务质量。

#### 4. 竞品与目标客户画像对比分析

通过对主要竞品的目标客户画像进行对比分析，可以发现以下差异点和相似之处：

- **相似之处**：
  - 各竞品均面向中小企业和大型企业的客服部门，强调多渠道支持和高效的客户服务管理。
  - 对于中小型企业，价格敏感性和实施便捷性是共同关注的重点；对于大型企业，则更注重与现有系统的集成和高级定制能力。

- **差异点**：
  - **Zendesk** 和 **Freshdesk** 更侧重于中小型企业，尤其是电商和SaaS领域的创业公司，强调易用性和灵活性。
  - **Salesforce Service Cloud** 和 **Microsoft Dynamics 365 Customer Service** 则专注于大型企业，尤其是那些已经在使用相应生态系统的公司，强调深度集成和高级功能。
  - **全渠道智能客服平台** 的优势在于其广泛的适用性和灵活的API接口对接，能够满足不同规模企业的多样化需求，特别是在数字化转型过程中寻求高效、低成本解决方案的企业。

#### 5. 推荐市场营销策略

根据目标客户画像分析的结果，提出以下针对性的市场营销策略建议：

- **广告渠道选择**：
  - 针对中小企业，可以选择社交媒体平台（如LinkedIn、微信公众号等）进行精准广告投放，吸引创业者和管理层的关注。
  - 针对大型企业，可以通过行业展会、专业论坛和B2B平台（如阿里巴巴、慧聪网等）展示产品优势，扩大品牌影响力。

- **促销活动设计**：
  - 推出限时免费试用或折扣优惠，降低客户的初次使用门槛，增加产品的吸引力。
  - 设立推荐奖励机制，鼓励现有用户推荐新客户，形成口碑传播效应。

- **社交媒体互动**：
  - 定期发布关于数字化转型和客户服务管理的成功案例，分享行业动态和技术趋势，增强用户的粘性和信任感。
  - 组织线上研讨会和线下沙龙，邀请专家讲解如何利用智能客服平台提升企业竞争力，促进潜在客户的转化。

通过以上策略，全渠道智能客服平台可以在竞争激烈的市场中脱颖而出，吸引更多目标客户，实现市场份额的稳步增长。

#### 审查与修订

完成初稿后，仔细检查报告的内容准确性、逻辑连贯性和语言表达质量，必要时进行修订以提高报告的质量。确保所有数据来源可靠，引用准确，并且语言表达清晰明了，便于读者理解和应用。
'''
   get_product_characterisitc(competitive_repor1t)

