# [从零搭建一个AI客服系统全流程](https://www.cocoloop.cn/t/topic/1453)

从零搭建一个AI客服系统全流程 ](https://www.cocoloop.cn/t/topic/1453)
[![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2)
[openclaw教程](https://www.cocoloop.cn/tag/21-tag/21 "openclaw教程 - CocoLoop社区收录了72篇关于openclaw教程的精选内容，涵盖教程、实战经验和深度讨论。"),[dify和openclaw对比](https://www.cocoloop.cn/tag/399-tag/399 "dify和openclaw对比 - CocoLoop社区收录了49篇关于dify和openclaw对比的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw接入](https://www.cocoloop.cn/tag/240-tag/240 "openclaw接入 - CocoLoop社区收录了47篇关于openclaw接入的精选内容，涵盖教程、实战经验和深度讨论。"),[RAG知识库怎么搭](https://www.cocoloop.cn/tag/405-tag/405 "RAG知识库怎么搭 - CocoLoop社区收录了18篇关于RAG知识库怎么搭的精选内容，涵盖教程、实战经验和深度讨论。")
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/1453)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/1453)
592 浏览量  9 用户 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/guopeiyao/48/1153_2.png) ](https://www.cocoloop.cn/u/guopeiyao "guopeiyao")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/pyliangcode/48/1161_2.png) ](https://www.cocoloop.cn/u/pyliangcode "pyliangcode")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/free_hufan/48/1164_2.png) ](https://www.cocoloop.cn/u/free_hufan "free_hufan")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/algomahub/48/1159_2.png) ](https://www.cocoloop.cn/u/algomahub "algomahub")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/reactfengnet/48/1176_2.png) ](https://www.cocoloop.cn/u/reactfengnet "reactfengnet")
[ 3月 24 日  ](https://www.cocoloop.cn/t/topic/1453/1 "跳到第一个帖子")
1 / 9 
3月 24 日 
[ 3月 30 日 ](https://www.cocoloop.cn/t/topic/1453/9)
##  由 algomahub 于 3月 24 日 发布 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/algomahub/48/1159_2.png) ](https://www.cocoloop.cn/u/algomahub)
[ algomahub  ](https://www.cocoloop.cn/u/algomahub)
[ 3月 24 日 ](https://www.cocoloop.cn/t/topic/1453 "发布日期")
上个月帮一个做电商的朋友搭了一套AI客服系统，从零开始到正式上线大概花了两周时间。现在这套系统已经跑了一个月了，效果还不错，客服成本直接砍了60%。今天把整个流程分享出来，给有类似需求的朋友一个参考。
##  [](https://www.cocoloop.cn/t/topic/1453#p-14792-dify-rag-1)为什么选Dify + RAG知识库
市面上做AI客服的方案挺多的，我对比了几个之后选了Dify作为主力平台，主要原因有三个。
第一是Dify的工作流编排能力很强，客服场景需要的多轮对话、条件分支、人工转接这些逻辑都能可视化配置，不用写太多代码。第二是它内置了RAG知识库功能，可以直接把FAQ文档、产品手册、售后政策这些扔进去，AI就能基于这些知识来回答问题。第三是开源免费，私有部署的话数据安全有保障。
当然Dify也不是完美的，后面会说到踩的一些坑。
##  [](https://www.cocoloop.cn/t/topic/1453#p-14792-faq-2)第一步：整理FAQ和知识文档
这一步看起来简单，其实是整个项目最花时间的部分，大概占了总工时的40%。
我做了这几件事：
首先是把朋友公司过去半年的客服聊天记录导出来，用AI做了一轮分析，提取出最高频的100个问题。这些问题按类别分成了几大类：订单查询类、退换货类、产品咨询类、物流查询类、售后服务类。
然后是整理标准答案。这个不能偷懒，每个问题都要有准确的、符合公司政策的标准回答。我把公司的产品手册、退换货政策、常见问题解答这些文档全部整理了一遍，去掉了过时的信息，补充了缺失的内容。
最后是构造一些变体问题。同一个问题用户可能有很多种问法，比如"怎么退货"、“我想退”、“退货流程是什么”、“东西不满意能退吗”，这些都要覆盖到。AI虽然有泛化能力，但给它更多的变体示例，回答准确率会明显提升。
整理完大概有200多个FAQ条目，加上产品手册和政策文档，总共大概5万字的知识库内容。
##  [](https://www.cocoloop.cn/t/topic/1453#p-14792-rag-3)第二步：构建RAG知识库
Dify里创建知识库还是挺方便的。把整理好的文档上传上去，选择合适的分段策略就行。
这里有几个经验：
文档分段大小建议在300-500 token左右，太长的话检索精度会下降，太短的话上下文不完整。FAQ类的文档最好一个问答对作为一个分段，这样检索最精准。
Embedding模型我用的是bge-large-zh-v1.5，中文场景下效果不错。如果预算够的话OpenAI的text-embedding-3-large效果更好一些。
知识库建好之后一定要做测试检索，随便问几个问题看看召回的文档片段是不是相关的。我在这一步发现了好几个分段不合理的问题，调整之后检索准确率从70%提升到了90%以上。
##  [](https://www.cocoloop.cn/t/topic/1453#p-14792-dify-4)第三步：配置Dify工作流
这是核心部分。我设计的工作流大概是这样的：
用户输入 → 意图识别（AI判断问题类型）→ 知识库检索 → AI生成回答 → 置信度判断 → 高置信度直接回复 / 低置信度转人工
几个关键节点的配置：
意图识别节点用的是一个分类Prompt，把用户问题分成"产品咨询"、“订单查询”、“售后问题”、“闲聊”、"其他"五类。不同类别走不同的处理分支。
订单查询类的问题需要调用电商平台的API查询实际订单状态，这个我通过Dify的HTTP节点对接了店铺后台的API。
置信度判断这个环节很重要。我让AI在生成回答的同时给出一个1-10的置信度评分，低于6分的自动转人工客服。这样既保证了回答质量，又不会把用户晾在那里。
##  [](https://www.cocoloop.cn/t/topic/1453#p-14792-im-5)第四步：接入IM渠道
朋友的客服主要在微信和网页两个渠道。
网页端比较简单，Dify本身就提供了一个可嵌入的聊天窗口组件，复制一段代码到网站里就行。样式可以自定义，和网站整体风格保持一致。
微信端稍微麻烦一些，需要通过企业微信的API做对接。我用了一个开源的微信机器人框架做中间层，消息进来先转发到Dify的API，拿到回复再发回给用户。这部分大概花了两天时间调试。
##  [](https://www.cocoloop.cn/t/topic/1453#p-14792-h-6)第五步：测试优化
上线之前做了大量测试，这个阶段非常关键。
我准备了200个测试问题，覆盖了各种正常和边界场景。测试结果第一轮只有75%的准确率，不太理想。
分析了错误案例之后发现主要问题有三个：一是知识库里有些信息过时了导致回答错误；二是一些复杂问题AI理解偏了；三是一些问题知识库里没有覆盖到。
针对性优化之后准确率提升到了92%，对于一个V1版本来说已经够用了。
##  [](https://www.cocoloop.cn/t/topic/1453#p-14792-h-7)关键指标和效果
上线一个月后的数据：
  * **首次解决率** ：78%。也就是说近八成的问题AI一次就回答对了，用户不需要追问
  * **客户满意度** ：4.2/5分。比之前纯人工客服的4.0分还略高，主要是因为AI响应速度快，7x24小时在线
  * **人工转接率** ：22%。这些转人工的主要是复杂售后、投诉、特殊情况
  * **平均响应时间** ：从之前的3-5分钟降到了5秒以内

##  [](https://www.cocoloop.cn/t/topic/1453#p-14792-h-8)成本对比
之前朋友请了3个客服，每人月薪4000-5000，加上社保之类的，一个月人力成本大概1.8万。
现在AI客服处理了约80%的咨询量，只需要保留1个人工客服处理复杂问题。AI这边的成本主要是服务器费用（约500元/月）加上大模型API调用费（约300元/月），总共约800元/月。
算下来每月节省约1.2万，一年省14万左右。搭建的一次性投入大概1万（我的人工费 + 服务器初始配置），3-4周就回本了。
##  [](https://www.cocoloop.cn/t/topic/1453#p-14792-ai-9)给想搭AI客服的朋友几个建议
第一，知识库质量决定一切。AI再聪明，如果知识库里的信息不准确不完整，回答也好不了。在知识库建设上多花时间绝对值得。
第二，人工兜底必须要有。现阶段AI客服不可能100%替代人工，一定要设计好转人工的机制。宁可多转一些，也别让AI瞎回答损害客户体验。
第三，持续迭代很重要。上线之后要定期review AI的回答记录，发现新的高频问题及时补充到知识库，发现回答不准确的及时修正。
有做过AI客服的朋友吗？你们用的什么方案？遇到过什么问题？欢迎评论区聊聊，特别想听听大家在实际业务中的经验和教训。
  

​ 
​ 
592 浏览量  9 用户 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/guopeiyao/48/1153_2.png) ](https://www.cocoloop.cn/u/guopeiyao "guopeiyao")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/pyliangcode/48/1161_2.png) ](https://www.cocoloop.cn/u/pyliangcode "pyliangcode")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/free_hufan/48/1164_2.png) ](https://www.cocoloop.cn/u/free_hufan "free_hufan")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/algomahub/48/1159_2.png) ](https://www.cocoloop.cn/u/algomahub "algomahub")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/reactfengnet/48/1176_2.png) ](https://www.cocoloop.cn/u/reactfengnet "reactfengnet")
##  由 indieduone 于 3月 24 日 发布 
##  由 reactfengnet 于 3月 24 日 发布 
##  由 guopeiyao 于 3月 24 日 发布 
##  由 free_hufan 于 3月 24 日 发布 
##  由 openjiangnet 于 3月 24 日 发布 
##  由 pyliangcode 于 3月 24 日 发布 
##  由 niuniu_ml 于 3月 25 日 发布 
##  由 haoren_k 于 3月 30 日 发布 
回复
  

###  新话题和未读话题   
话题列表，带有按钮的列标题可以排序。  
|  话题   |  回复   |  浏览量   |  活动   |  
| --- | --- | --- | --- |  
|  [零成本用Dify赚钱？三个真实案例分享](https://www.cocoloop.cn/t/topic/1225) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw本地部署教程](https://www.cocoloop.cn/tag/345-tag/345 "openclaw本地部署教程 - CocoLoop社区收录了77篇关于openclaw本地部署教程的精选内容，涵盖教程、实战经验和深度讨论。"),[免费AI API推荐](https://www.cocoloop.cn/tag/362-tag/362 "免费AI API推荐 - CocoLoop社区收录了74篇关于免费AI API推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[dify和openclaw对比](https://www.cocoloop.cn/tag/399-tag/399 "dify和openclaw对比 - CocoLoop社区收录了49篇关于dify和openclaw对比的精选内容，涵盖教程、实战经验和深度讨论。"),[dify怎么用](https://www.cocoloop.cn/tag/400-tag/400 "dify怎么用 - CocoLoop社区收录了36篇关于dify怎么用的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 9 ](https://www.cocoloop.cn/t/topic/1225/1)  |  531  |  [4月 3 日](https://www.cocoloop.cn/t/topic/1225/10)  |  
|  [OpenClaw的商业价值评估：泡沫还是万亿赛道的入场券](https://www.cocoloop.cn/t/topic/489) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw商业分析](https://www.cocoloop.cn/tag/238-tag/238 "openclaw商业分析 - CocoLoop社区收录了5篇关于openclaw商业分析的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw深度讨论](https://www.cocoloop.cn/tag/237-tag/237 "openclaw深度讨论 - CocoLoop社区收录了5篇关于openclaw深度讨论的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 16 ](https://www.cocoloop.cn/t/topic/489/1)  |  265  |  [3月 31 日](https://www.cocoloop.cn/t/topic/489/17)  |  
|  [AI自动化赚钱：5个经过验证的方法](https://www.cocoloop.cn/t/topic/1227) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw skill推荐](https://www.cocoloop.cn/tag/338-tag/338 "openclaw skill推荐 - CocoLoop社区收录了227篇关于openclaw skill推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw技能怎么安装](https://www.cocoloop.cn/tag/339-tag/339 "openclaw技能怎么安装 - CocoLoop社区收录了219篇关于openclaw技能怎么安装的精选内容，涵盖教程、实战经验和深度讨论。"),[AI副业](https://www.cocoloop.cn/tag/154-tag/154 "AI副业 - CocoLoop社区收录了9篇关于AI副业的精选内容，涵盖教程、实战经验和深度讨论。"),[AI赚钱](https://www.cocoloop.cn/tag/153-tag/153 "AI赚钱 - CocoLoop社区收录了7篇关于AI赚钱的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 8 ](https://www.cocoloop.cn/t/topic/1227/1)  |  488  |  [4月 3 日](https://www.cocoloop.cn/t/topic/1227/9)  |  
|  [我用OpenClaw帮班主任自动批改了200份作业](https://www.cocoloop.cn/t/topic/730) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw排错](https://www.cocoloop.cn/tag/35-tag/35 "openclaw排错 - CocoLoop社区收录了158篇关于openclaw排错的精选内容，涵盖教程、实战经验和深度讨论。"),[AI翻译工具推荐](https://www.cocoloop.cn/tag/364-tag/364 "AI翻译工具推荐 - CocoLoop社区收录了106篇关于AI翻译工具推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[最好用的AI翻译](https://www.cocoloop.cn/tag/365-tag/365 "最好用的AI翻译 - CocoLoop社区收录了88篇关于最好用的AI翻译的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw架构](https://www.cocoloop.cn/tag/230-tag/230 "openclaw架构 - CocoLoop社区收录了70篇关于openclaw架构的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 13 ](https://www.cocoloop.cn/t/topic/730/1)  |  242  |  [3月 29 日](https://www.cocoloop.cn/t/topic/730/16)  |  
|  [OpenClaw到底是哪家公司做的？什么时候发布的？背景信息汇总](https://www.cocoloop.cn/t/topic/2036) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [OpenClaw](https://www.cocoloop.cn/tag/637-tag/637 "OpenClaw - CocoLoop社区收录了132篇关于OpenClaw的精选内容，涵盖教程、实战经验和深度讨论。"),[AI龙虾](https://www.cocoloop.cn/tag/561-tag/561 "AI龙虾 - CocoLoop社区收录了4篇关于AI龙虾的精选内容，涵盖教程、实战经验和深度讨论。"),[OpenClaw公司](https://www.cocoloop.cn/tag/678-tag/678 "OpenClaw公司 - CocoLoop社区收录了2篇关于OpenClaw公司的精选内容，涵盖教程、实战经验和深度讨论。"),[OpenClaw背景](https://www.cocoloop.cn/tag/679-tag/679 "OpenClaw背景 - CocoLoop社区收录了1篇关于OpenClaw背景的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 5 ](https://www.cocoloop.cn/t/topic/2036/1)  |  4.0k  |  [3月 30 日](https://www.cocoloop.cn/t/topic/2036/6)  |  
|  [Ollama本地部署大模型完全指南：一行命令搞定](https://www.cocoloop.cn/t/topic/1247) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [windows部署openclaw](https://www.cocoloop.cn/tag/353-tag/353 "windows部署openclaw - CocoLoop社区收录了157篇关于windows部署openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw windows安装](https://www.cocoloop.cn/tag/101-tag/101 "openclaw windows安装 - CocoLoop社区收录了158篇关于openclaw windows安装的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw本地部署教程](https://www.cocoloop.cn/tag/345-tag/345 "openclaw本地部署教程 - CocoLoop社区收录了77篇关于openclaw本地部署教程的精选内容，涵盖教程、实战经验和深度讨论。"),[deepseek本地部署教程](https://www.cocoloop.cn/tag/360-tag/360 "deepseek本地部署教程 - CocoLoop社区收录了38篇关于deepseek本地部署教程的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/1247/1)  |  189  |  [3月 25 日](https://www.cocoloop.cn/t/topic/1247/8)  |  
|  [OpenClaw到底是什么软件？官网在哪？想入坑AI编程工具先搞懂这个基础概念](https://www.cocoloop.cn/t/topic/1802) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw是什么](https://www.cocoloop.cn/tag/145-tag/145 "openclaw是什么 - CocoLoop社区收录了56篇关于openclaw是什么的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw官网](https://www.cocoloop.cn/tag/178-tag/178 "openclaw官网 - CocoLoop社区收录了5篇关于openclaw官网的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 6 ](https://www.cocoloop.cn/t/topic/1802/1)  |  222  |  [3月 26 日](https://www.cocoloop.cn/t/topic/1802/7)  |  
|  [给龙虾配置 Prometheus 监控和告警](https://www.cocoloop.cn/t/topic/893) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw配置](https://www.cocoloop.cn/tag/223-tag/223 "openclaw配置 - CocoLoop社区收录了151篇关于openclaw配置的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw运维](https://www.cocoloop.cn/tag/228-tag/228 "openclaw运维 - CocoLoop社区收录了49篇关于openclaw运维的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 17 ](https://www.cocoloop.cn/t/topic/893/1)  |  353  |  [4月 3 日](https://www.cocoloop.cn/t/topic/893/18)  |  
|  [Kimi产品线太多了，网页端、写作助手、KimiClaw到底用哪个](https://www.cocoloop.cn/t/topic/1212) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [kimiclaw](https://www.cocoloop.cn/tag/162-tag/162 "kimiclaw - CocoLoop社区收录了35篇关于kimiclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[AI创作](https://www.cocoloop.cn/tag/249-tag/249 "AI创作 - CocoLoop社区收录了22篇关于AI创作的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 8 ](https://www.cocoloop.cn/t/topic/1212/1)  |  402  |  [4月 3 日](https://www.cocoloop.cn/t/topic/1212/9)  |  
|  [OpenClaw免费模型推荐：不花钱也能用的API有哪些？](https://www.cocoloop.cn/t/topic/2055) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [OpenClaw](https://www.cocoloop.cn/tag/637-tag/637 "OpenClaw - CocoLoop社区收录了132篇关于OpenClaw的精选内容，涵盖教程、实战经验和深度讨论。"),[模型推荐](https://www.cocoloop.cn/tag/731-tag/731 "模型推荐 - CocoLoop社区收录了3篇关于模型推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[免费API](https://www.cocoloop.cn/tag/730-tag/730 "免费API - CocoLoop社区收录了1篇关于免费API的精选内容，涵盖教程、实战经验和深度讨论。"),[免费模型](https://www.cocoloop.cn/tag/729-tag/729 "免费模型 - CocoLoop社区收录了1篇关于免费模型的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 8 ](https://www.cocoloop.cn/t/topic/2055/1)  |  4.1k  |  [4月 3 日](https://www.cocoloop.cn/t/topic/2055/9)  |  
###  想阅读更多？请浏览[![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2)中的其他话题或[查看最新话题](https://www.cocoloop.cn/latest)。 
Invalid date  Invalid date 


