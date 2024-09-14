# 技术支持数据集分析

![Support](https://github.com/SolitaryEgo/Analysis-of-Technical-Support-Dataset/blob/main/dataset-cover.jpg)

## 数据说明


字段 | 说明 |
|----|---- |
Status  | 支持管道中的工单状态（未解决：等待处理的新工单，正在进行：由代理处理，已解决：提供解决方案，已关闭：客户确认已关闭工单）。 |
Ticket ID | 唯一的票证标识号。 |
Source | 发出请求的渠道（聊天、电话、电子邮件）。 |
Priority | 工单的紧急程度 （低、中、高）。 |
Support Level | 票证难度级别（第 1 层、第 2 层）。 |
Product group | 与客户请求相关的产品组。|
Topic | 客户询价的主题。|
Agent Group | 代理所属的组（第 1 级支持、第 2 级支持）。|
Agent Name | 当前处理工单的服务人员的名称。|
Created time | 指示何时收到票证的时间戳。|
Expected SLA to first response | 提供初始响应的截止日期。|
First response time | 给出初始响应时的时间戳。|
SLA For first response | 首次响应合规性状态（在 SLA 范围内、违反 SLA）。|
Expected SLA to resolve | 解决工单的截止日期。|
Resolution time | 解决工单时的时间戳。|
SLA For Resolution | 解决方法合规性状态（在 SLA 内、违反 SLA）。|
Close time | 票证关闭时的时间戳。|
Agent interactions | 每个工单的座席交互总数。|
Survey results | 客户满意度得分为 1 到 5 分。|
Country | 创建工单的客户的原籍国。|
Latitude | 客户所在国家/地区的纬度坐标。|
Longitude | 客户所在国家/地区的经度坐标。|


>数据来源：[kaggle](https://www.kaggle.com/datasets/suvroo/technical-support-dataset/data)
