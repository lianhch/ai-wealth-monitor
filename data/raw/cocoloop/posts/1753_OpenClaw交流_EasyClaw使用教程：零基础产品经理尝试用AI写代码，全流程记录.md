# [EasyClaw使用教程：零基础产品经理尝试用AI写代码，全流程记录](https://www.cocoloop.cn/t/topic/1753)

EasyClaw使用教程：零基础产品经理尝试用AI写代码，全流程记录 ](https://www.cocoloop.cn/t/topic/1753)
[![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2)
[EasyClaw怎么用](https://www.cocoloop.cn/tag/1371-tag/1371 "EasyClaw怎么用 - CocoLoop社区收录了6篇关于EasyClaw怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[EasyClaw教程](https://www.cocoloop.cn/tag/1370-tag/1370 "EasyClaw教程 - CocoLoop社区收录了6篇关于EasyClaw教程的精选内容，涵盖教程、实战经验和深度讨论。"),[EasyClaw使用教程](https://www.cocoloop.cn/tag/1373-tag/1373 "EasyClaw使用教程 - CocoLoop社区收录了1篇关于EasyClaw使用教程的精选内容，涵盖教程、实战经验和深度讨论。")
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/1753)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/1753)
208 浏览量  6 用户 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/liuxing_pm/48/1115_2.png) 2 ](https://www.cocoloop.cn/u/liuxing_pm "liuxing_pm")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/t/90db22/48.png) ](https://www.cocoloop.cn/u/tangzichen "tangzichen")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/d/3d9bf3/48.png) ](https://www.cocoloop.cn/u/docker_master_hu "docker_master_hu")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/luffy_coder/48/1110_2.png) ](https://www.cocoloop.cn/u/luffy_coder "luffy_coder")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/wangyiming_dev/48/1249_2.png) ](https://www.cocoloop.cn/u/wangyiming_dev "wangyiming_dev")
[ 3月 26 日  ](https://www.cocoloop.cn/t/topic/1753/1 "跳到第一个帖子")
1 / 7 
3月 25 日 
[ 3月 26 日 ](https://www.cocoloop.cn/t/topic/1753/7)
##  由 liuxing_pm 于 3月 26 日 发布 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/liuxing_pm/48/1115_2.png) ](https://www.cocoloop.cn/u/liuxing_pm)
[ liuxing_pm  ](https://www.cocoloop.cn/u/liuxing_pm)
[ 3月 26 日 ](https://www.cocoloop.cn/t/topic/1753 "发布日期")
拿到EasyClaw的邀请码后试用了一周，作为一个完全不会写代码的产品经理，来分享一下使用体验和教程。
##  [](https://www.cocoloop.cn/t/topic/1753#p-17796-h-1)我的目标
用EasyClaw做一个内部使用的"需求管理小工具"，功能很简单：
  * 需求列表（增删改查）
  * 按优先级分类
  * 简单的统计图表

##  [](https://www.cocoloop.cn/t/topic/1753#p-17796-h-2)使用过程
###  [](https://www.cocoloop.cn/t/topic/1753#p-17796-step-1-easyclaw-3)Step 1: 打开EasyClaw桌面版
界面很简洁，中间是一个大的对话框，左侧是项目管理面板。第一印象比VS Code友好多了。
###  [](https://www.cocoloop.cn/t/topic/1753#p-17796-step-2-4)Step 2: 用自然语言描述需求
我输入了：
> “帮我做一个需求管理工具。需要一个需求列表，可以添加需求、编辑、删除。每个需求有标题、描述、优先级（高中低）、状态（待开发/开发中/已完成）。要有一个统计页面，显示各状态的需求数量柱状图。”
###  [](https://www.cocoloop.cn/t/topic/1753#p-17796-step-3-easyclaw-5)Step 3: EasyClaw自动生成
大概等了30秒，EasyClaw生成了一个完整的项目，左侧面板出现了一堆文件。点击"预览"按钮，直接在内置的浏览器里看到了效果。
说实话效果比我预期的好：
  * 基本的增删改查功能都有
  * 优先级有颜色标记
  * 统计图表也生成了

###  [](https://www.cocoloop.cn/t/topic/1753#p-17796-step-4-6)Step 4: 修改和调整
生成的界面不太好看（默认是灰色调的），我又输入：
> “把界面改成蓝色主题，卡片式布局，按钮圆角一点”
EasyClaw自动修改了样式，结果还不错。
###  [](https://www.cocoloop.cn/t/topic/1753#p-17796-h-7)遇到的问题
  1. 刷新后数据会丢失（因为是纯前端没有后端数据库）
  2. 想加一个"导出Excel"功能，EasyClaw理解错了生成了PDF导出
  3. 复杂的交互逻辑（比如拖拽排序）生成的代码有bug

##  [](https://www.cocoloop.cn/t/topic/1753#p-17796-h-8)总结
对于做简单原型和内部小工具来说，EasyClaw真的很好用。一个不会写代码的产品经理半天就能做出一个能用的小工具，这在以前是不敢想的。
但局限性也很明显：涉及到数据库、复杂交互、跟第三方服务对接这些，就需要专业开发者介入了。
想请教社区里的老鸟：EasyClaw生成的项目，怎么部署到公司内网让其他人也能用？
  

​ 
​ 
208 浏览量  6 用户 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/liuxing_pm/48/1115_2.png) 2 ](https://www.cocoloop.cn/u/liuxing_pm "liuxing_pm")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/t/90db22/48.png) ](https://www.cocoloop.cn/u/tangzichen "tangzichen")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/d/3d9bf3/48.png) ](https://www.cocoloop.cn/u/docker_master_hu "docker_master_hu")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/luffy_coder/48/1110_2.png) ](https://www.cocoloop.cn/u/luffy_coder "luffy_coder")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/wangyiming_dev/48/1249_2.png) ](https://www.cocoloop.cn/u/wangyiming_dev "wangyiming_dev")
##  由 docker_master_hu 于 3月 26 日 发布 
##  由 qianduoduo_ai 于 3月 26 日 发布 
##  由 tangzichen 于 3月 26 日 发布 
##  由 liuxing_pm 于 3月 26 日 发布 
##  由 wangyiming_dev 于 3月 26 日 发布 
##  由 luffy_coder 于 3月 26 日 发布 
回复
  

###  新话题和未读话题   
话题列表，带有按钮的列标题可以排序。  
|  话题   |  回复   |  浏览量   |  活动   |  
| --- | --- | --- | --- |  
|  [OpenClaw算国内平替吗？跟Dify、FastGPT这些比怎么样](https://www.cocoloop.cn/t/topic/1186) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [dify和openclaw对比](https://www.cocoloop.cn/tag/399-tag/399 "dify和openclaw对比 - CocoLoop社区收录了49篇关于dify和openclaw对比的精选内容，涵盖教程、实战经验和深度讨论。"),[dify怎么用](https://www.cocoloop.cn/tag/400-tag/400 "dify怎么用 - CocoLoop社区收录了36篇关于dify怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[AI agent平台对比](https://www.cocoloop.cn/tag/166-tag/166 "AI agent平台对比 - CocoLoop社区收录了6篇关于AI agent平台对比的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw和dify区别](https://www.cocoloop.cn/tag/165-tag/165 "openclaw和dify区别 - CocoLoop社区收录了6篇关于openclaw和dify区别的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 8 ](https://www.cocoloop.cn/t/topic/1186/1)  |  371  |  [3月 29 日](https://www.cocoloop.cn/t/topic/1186/9)  |  
|  [用 OpenClaw 自动生成 Git Commit Message](https://www.cocoloop.cn/t/topic/903) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [AI入门科普](https://www.cocoloop.cn/tag/62-tag/62 "AI入门科普 - CocoLoop社区收录了76篇关于AI入门科普的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 16 ](https://www.cocoloop.cn/t/topic/903/1)  |  223  |  [4月 1 日](https://www.cocoloop.cn/t/topic/903/17)  |  
|  [OpenClaw 自学手册（六）：精通篇 - 高级架构与生产部署](https://www.cocoloop.cn/t/topic/767) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw自学手册](https://www.cocoloop.cn/tag/129-tag/129 "openclaw自学手册 - CocoLoop社区收录了6篇关于openclaw自学手册的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw高级架构](https://www.cocoloop.cn/tag/111-tag/111 "openclaw高级架构 - CocoLoop社区收录了2篇关于openclaw高级架构的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw精通教程](https://www.cocoloop.cn/tag/137-tag/137 "openclaw精通教程 - CocoLoop社区收录了1篇关于openclaw精通教程的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 5 ](https://www.cocoloop.cn/t/topic/767/1)  |  1.0k  |  [3月 20 日](https://www.cocoloop.cn/t/topic/767/6)  |  
|  [2026年AI趋势预测：幻觉监管、GPU现实撞墙与广告版AI](https://www.cocoloop.cn/t/topic/1232) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [deepseek本地部署教程](https://www.cocoloop.cn/tag/360-tag/360 "deepseek本地部署教程 - CocoLoop社区收录了38篇关于deepseek本地部署教程的精选内容，涵盖教程、实战经验和深度讨论。"),[AI趋势](https://www.cocoloop.cn/tag/199-tag/199 "AI趋势 - CocoLoop社区收录了30篇关于AI趋势的精选内容，涵盖教程、实战经验和深度讨论。"),[免费跑deepseek](https://www.cocoloop.cn/tag/361-tag/361 "免费跑deepseek - CocoLoop社区收录了16篇关于免费跑deepseek的精选内容，涵盖教程、实战经验和深度讨论。"),[AI产业](https://www.cocoloop.cn/tag/200-tag/200 "AI产业 - CocoLoop社区收录了1篇关于AI产业的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 4 ](https://www.cocoloop.cn/t/topic/1232/1)  |  161  |  [3月 25 日](https://www.cocoloop.cn/t/topic/1232/5)  |  
|  [2026自媒体生存指南：AI工具提效组合拳](https://www.cocoloop.cn/t/topic/1279) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [AI自动化](https://www.cocoloop.cn/tag/222-tag/222 "AI自动化 - CocoLoop社区收录了129篇关于AI自动化的精选内容，涵盖教程、实战经验和深度讨论。"),[AI入门科普](https://www.cocoloop.cn/tag/62-tag/62 "AI入门科普 - CocoLoop社区收录了76篇关于AI入门科普的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw教程](https://www.cocoloop.cn/tag/21-tag/21 "openclaw教程 - CocoLoop社区收录了72篇关于openclaw教程的精选内容，涵盖教程、实战经验和深度讨论。"),[AI趋势](https://www.cocoloop.cn/tag/199-tag/199 "AI趋势 - CocoLoop社区收录了30篇关于AI趋势的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 6 ](https://www.cocoloop.cn/t/topic/1279/1)  |  302  |  [3月 25 日](https://www.cocoloop.cn/t/topic/1279/7)  |  
|  [在甲骨文免费 ARM 实例上跑 OpenClaw 的完整教程](https://www.cocoloop.cn/t/topic/885) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw docker教程](https://www.cocoloop.cn/tag/371-tag/371 "openclaw docker教程 - CocoLoop社区收录了122篇关于openclaw docker教程的精选内容，涵盖教程、实战经验和深度讨论。"),[docker部署openclaw](https://www.cocoloop.cn/tag/370-tag/370 "docker部署openclaw - CocoLoop社区收录了116篇关于docker部署openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw怎么免费用](https://www.cocoloop.cn/tag/357-tag/357 "openclaw怎么免费用 - CocoLoop社区收录了84篇关于openclaw怎么免费用的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw怎么安装](https://www.cocoloop.cn/tag/392-tag/392 "openclaw怎么安装 - CocoLoop社区收录了18篇关于openclaw怎么安装的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 22 ](https://www.cocoloop.cn/t/topic/885/1)  |  407  |  [3月 24 日](https://www.cocoloop.cn/t/topic/885/23)  |  
|  [OpenClaw做报表和数据分析效果怎么样？想用它替代部分Excel手工操作](https://www.cocoloop.cn/t/topic/2175) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw数据处理](https://www.cocoloop.cn/tag/1006-tag/1006 "openclaw数据处理 - CocoLoop社区收录了2篇关于openclaw数据处理的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw财务应用](https://www.cocoloop.cn/tag/1007-tag/1007 "openclaw财务应用 - CocoLoop社区收录了1篇关于openclaw财务应用的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw做报表](https://www.cocoloop.cn/tag/1005-tag/1005 "openclaw做报表 - CocoLoop社区收录了1篇关于openclaw做报表的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/2175/1)  |  2.2k  |  [4月 2 日](https://www.cocoloop.cn/t/topic/2175/8)  |  
|  [原版openclaw和那些国产版本选哪个好](https://www.cocoloop.cn/t/topic/667) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [molili教程](https://www.cocoloop.cn/tag/47-tag/47 "molili教程 - CocoLoop社区收录了79篇关于molili教程的精选内容，涵盖教程、实战经验和深度讨论。"),[AI平台对比](https://www.cocoloop.cn/tag/233-tag/233 "AI平台对比 - CocoLoop社区收录了57篇关于AI平台对比的精选内容，涵盖教程、实战经验和深度讨论。"),[qclaw](https://www.cocoloop.cn/tag/167-tag/167 "qclaw - CocoLoop社区收录了22篇关于qclaw的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 16 ](https://www.cocoloop.cn/t/topic/667/1)  |  244  |  [3月 30 日](https://www.cocoloop.cn/t/topic/667/17)  |  
|  [公司要求用OpenClaw替代部分外包团队，这合理吗？](https://www.cocoloop.cn/t/topic/706) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [openclaw排错](https://www.cocoloop.cn/tag/35-tag/35 "openclaw排错 - CocoLoop社区收录了158篇关于openclaw排错的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw配置](https://www.cocoloop.cn/tag/223-tag/223 "openclaw配置 - CocoLoop社区收录了151篇关于openclaw配置的精选内容，涵盖教程、实战经验和深度讨论。"),[AI翻译工具推荐](https://www.cocoloop.cn/tag/364-tag/364 "AI翻译工具推荐 - CocoLoop社区收录了106篇关于AI翻译工具推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw替代外包团队](https://www.cocoloop.cn/tag/2143-tag/2143 "openclaw替代外包团队 - CocoLoop社区收录了1篇关于openclaw替代外包团队的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 15 ](https://www.cocoloop.cn/t/topic/706/1)  |  503  |  [4月 3 日](https://www.cocoloop.cn/t/topic/706/20)  |  
|  [KimiClaw是什么？月之暗面出的AI Agent到底怎么样](https://www.cocoloop.cn/t/topic/1592) [![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2) [AI平台对比](https://www.cocoloop.cn/tag/233-tag/233 "AI平台对比 - CocoLoop社区收录了57篇关于AI平台对比的精选内容，涵盖教程、实战经验和深度讨论。"),[大模型](https://www.cocoloop.cn/tag/11-tag/11 "大模型 - CocoLoop社区收录了37篇关于大模型的精选内容，涵盖教程、实战经验和深度讨论。"),[kimiclaw](https://www.cocoloop.cn/tag/162-tag/162 "kimiclaw - CocoLoop社区收录了35篇关于kimiclaw的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 5 ](https://www.cocoloop.cn/t/topic/1592/1)  |  457  |  [3月 25 日](https://www.cocoloop.cn/t/topic/1592/6)  |  
###  想阅读更多？请浏览[![lobster](https://www.cocoloop.cn/images/emoji/twitter/lobster.png?v=15)OpenClaw交流](https://www.cocoloop.cn/c/openclaw/2)中的其他话题或[查看最新话题](https://www.cocoloop.cn/latest)。 
Invalid date  Invalid date 


