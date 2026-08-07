# [血泪教训：AI 工具差点把我服务器删干净了](https://www.cocoloop.cn/t/topic/419)

血泪教训：AI 工具差点把我服务器删干净了 ](https://www.cocoloop.cn/t/topic/419)
[![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)
[AI自动化](https://www.cocoloop.cn/tag/222-tag/222 "AI自动化 - CocoLoop社区收录了129篇关于AI自动化的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw备份恢复教程](https://www.cocoloop.cn/tag/380-tag/380 "openclaw备份恢复教程 - CocoLoop社区收录了29篇关于openclaw备份恢复教程的精选内容，涵盖教程、实战经验和深度讨论。"),[API开发](https://www.cocoloop.cn/tag/259-tag/259 "API开发 - CocoLoop社区收录了22篇关于API开发的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw数据备份](https://www.cocoloop.cn/tag/379-tag/379 "openclaw数据备份 - CocoLoop社区收录了21篇关于openclaw数据备份的精选内容，涵盖教程、实战经验和深度讨论。")
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/419)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/419)
910 浏览量  6 用户 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/z/ee59a6/48.png) ](https://www.cocoloop.cn/u/zhaoyi_ml "zhaoyi_ml")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/c/a88e57/48.png) ](https://www.cocoloop.cn/u/chensiyu_dev "chensiyu_dev")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/b77776/48.png) ](https://www.cocoloop.cn/u/sunhaoyu "sunhaoyu")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/y/e9bcb4/48.png) ](https://www.cocoloop.cn/u/yangsiqi "yangsiqi")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/hexinyu/48/1172_2.png) ](https://www.cocoloop.cn/u/hexinyu "hexinyu")
[ 3月 19 日  ](https://www.cocoloop.cn/t/topic/419/1 "跳到第一个帖子")
1 / 6 
3月 19 日 
[ 3月 29 日 ](https://www.cocoloop.cn/t/topic/419/6)
##  由 yangsiqi 于 3月 19 日 发布 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/y/e9bcb4/48.png) ](https://www.cocoloop.cn/u/yangsiqi)
[ yangsiqi  ](https://www.cocoloop.cn/u/yangsiqi)
[ 3月 19 日 ](https://www.cocoloop.cn/t/topic/419 "发布日期")
分享一个惨痛经历，给大家提个醒。
##  [](https://www.cocoloop.cn/t/topic/419#p-3016-h-1)事情经过
我让 AI 助手帮忙清理服务器上的临时文件和日志，结果它理解错了指令，直接把数据库文件和项目目录全删了。博客、API 服务全部下线。
当时心态直接崩了。
##  [](https://www.cocoloop.cn/t/topic/419#p-3016-h-2)万幸的是
之前设置了每日自动备份，所以最多丢失 24 小时的数据。但那天刚好更新了不少内容，还是损失了几个小时的工作。
##  [](https://www.cocoloop.cn/t/topic/419#p-3016-h-3)教训总结
  1. **永远不要给 AI 工具 root 权限** ：用最小权限原则
  2. **关键操作必须人工确认** ：别开全自动模式处理重要数据
  3. **备份！备份！备份！** ：自动备份是最后的救命稻草
  4. **用沙箱环境测试** ：新的自动化脚本先在测试环境跑
  5. **设置操作白名单** ：明确 AI 能操作哪些目录，禁止访问关键路径

现在我给 AI 工具设了严格的目录权限，只能访问指定的工作目录，核心数据目录完全隔离。
大家使用 AI 工具的时候一定要注意安全！
  

​ 
​ 
910 浏览量  6 用户 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/z/ee59a6/48.png) ](https://www.cocoloop.cn/u/zhaoyi_ml "zhaoyi_ml")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/c/a88e57/48.png) ](https://www.cocoloop.cn/u/chensiyu_dev "chensiyu_dev")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/b77776/48.png) ](https://www.cocoloop.cn/u/sunhaoyu "sunhaoyu")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/y/e9bcb4/48.png) ](https://www.cocoloop.cn/u/yangsiqi "yangsiqi")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/hexinyu/48/1172_2.png) ](https://www.cocoloop.cn/u/hexinyu "hexinyu")
##  由 chensiyu_dev 于 3月 19 日 发布 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/c/a88e57/48.png) ](https://www.cocoloop.cn/u/chensiyu_dev)
[ chensiyu_dev  ](https://www.cocoloop.cn/u/chensiyu_dev)
[ 3月 19 日 ](https://www.cocoloop.cn/t/topic/419/2 "发布日期")
备份真的是最后一道防线，血的教训
  

1 个回复
​ 
​ 
##  由 hexinyu 于 3月 19 日 发布 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/hexinyu/48/1172_2.png) ](https://www.cocoloop.cn/u/hexinyu)
[ hexinyu  ](https://www.cocoloop.cn/u/hexinyu)
[ 3月 19 日 ](https://www.cocoloop.cn/t/topic/419/3 "发布日期")
我现在用 Docker 隔离，AI 只能操作容器内的文件
  

​ 
​ 
##  由 sunhaoyu 于 3月 19 日 发布 
##  由 zhaoyi_ml 于 3月 19 日 发布 
10 天后 
##  由 crabwalk 于 3月 29 日 发布 
回复
  

###  新话题和未读话题   
话题列表，带有按钮的列标题可以排序。  
|  话题   |  回复   |  浏览量   |  活动   |  
| --- | --- | --- | --- |  
|  [咪鼠M-Claw（小龙虾）操作指南：下载安装+微信远程+新媒体运营](https://www.cocoloop.cn/t/topic/2064) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [咪鼠ai新媒体运营](https://www.cocoloop.cn/tag/750-tag/750 "咪鼠ai新媒体运营 - CocoLoop社区收录了2篇关于咪鼠ai新媒体运营的精选内容，涵盖教程、实战经验和深度讨论。"),[微信远程控制电脑](https://www.cocoloop.cn/tag/749-tag/749 "微信远程控制电脑 - CocoLoop社区收录了2篇关于微信远程控制电脑的精选内容，涵盖教程、实战经验和深度讨论。"),[咪鼠小龙虾安装](https://www.cocoloop.cn/tag/748-tag/748 "咪鼠小龙虾安装 - CocoLoop社区收录了2篇关于咪鼠小龙虾安装的精选内容，涵盖教程、实战经验和深度讨论。"),[咪鼠mclaw使用教程](https://www.cocoloop.cn/tag/747-tag/747 "咪鼠mclaw使用教程 - CocoLoop社区收录了2篇关于咪鼠mclaw使用教程的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 1 ](https://www.cocoloop.cn/t/topic/2064/1)  |  2.0k  |  [5月 19 日](https://www.cocoloop.cn/t/topic/2064/2)  |  
|  [2026年到底学什么编程语言最有前途？Python还是Go？纠结死了求建议](https://www.cocoloop.cn/t/topic/1775) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [AI编程工具](https://www.cocoloop.cn/tag/193-tag/193 "AI编程工具 - CocoLoop社区收录了126篇关于AI编程工具的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw docker教程](https://www.cocoloop.cn/tag/371-tag/371 "openclaw docker教程 - CocoLoop社区收录了122篇关于openclaw docker教程的精选内容，涵盖教程、实战经验和深度讨论。"),[docker部署openclaw](https://www.cocoloop.cn/tag/370-tag/370 "docker部署openclaw - CocoLoop社区收录了116篇关于docker部署openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[AI入门科普](https://www.cocoloop.cn/tag/62-tag/62 "AI入门科普 - CocoLoop社区收录了76篇关于AI入门科普的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 4 ](https://www.cocoloop.cn/t/topic/1775/1)  |  239  |  [3月 26 日](https://www.cocoloop.cn/t/topic/1775/5)  |  
|  [V4 还没发，国内各家模型已经开始抢跑了](https://www.cocoloop.cn/t/topic/3257) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)  |  [ 6 ](https://www.cocoloop.cn/t/topic/3257/1)  |  2.4k  |  [5月 10 日](https://www.cocoloop.cn/t/topic/3257/7)  |  
|  [AI Agent的安全问题比你想的严重得多，最近做安全审计发现的真实案例](https://www.cocoloop.cn/t/topic/1765) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [openclaw排错](https://www.cocoloop.cn/tag/35-tag/35 "openclaw排错 - CocoLoop社区收录了158篇关于openclaw排错的精选内容，涵盖教程、实战经验和深度讨论。"),[AI agent](https://www.cocoloop.cn/tag/146-tag/146 "AI agent - CocoLoop社区收录了91篇关于AI agent的精选内容，涵盖教程、实战经验和深度讨论。"),[MCP和skill区别](https://www.cocoloop.cn/tag/352-tag/352 "MCP和skill区别 - CocoLoop社区收录了34篇关于MCP和skill区别的精选内容，涵盖教程、实战经验和深度讨论。"),[MCP协议是什么](https://www.cocoloop.cn/tag/351-tag/351 "MCP协议是什么 - CocoLoop社区收录了16篇关于MCP协议是什么的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 4 ](https://www.cocoloop.cn/t/topic/1765/1)  |  202  |  [3月 26 日](https://www.cocoloop.cn/t/topic/1765/5)  |  
|  [推荐一个轻量化 AI 自动化方案，开箱即用](https://www.cocoloop.cn/t/topic/324) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [AI自动化](https://www.cocoloop.cn/tag/222-tag/222 "AI自动化 - CocoLoop社区收录了129篇关于AI自动化的精选内容，涵盖教程、实战经验和深度讨论。"),[AI炒股](https://www.cocoloop.cn/tag/80-tag/80 "AI炒股 - CocoLoop社区收录了25篇关于AI炒股的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/324/1)  |  199  |  [4月 3 日](https://www.cocoloop.cn/t/topic/324/8)  |  
|  [微信什么时候能开放 Bot 接口？聊聊 IM 平台的 AI 生态](https://www.cocoloop.cn/t/topic/375) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [微信AI机器人怎么做](https://www.cocoloop.cn/tag/340-tag/340 "微信AI机器人怎么做 - CocoLoop社区收录了154篇关于微信AI机器人怎么做的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw接入微信](https://www.cocoloop.cn/tag/151-tag/151 "openclaw接入微信 - CocoLoop社区收录了136篇关于openclaw接入微信的精选内容，涵盖教程、实战经验和深度讨论。"),[AI机器人](https://www.cocoloop.cn/tag/262-tag/262 "AI机器人 - CocoLoop社区收录了12篇关于AI机器人的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 4 ](https://www.cocoloop.cn/t/topic/375/1)  |  319  |  [3月 24 日](https://www.cocoloop.cn/t/topic/375/5)  |  
|  [不花钱跑 AI 自动化：本地大模型方案实测](https://www.cocoloop.cn/t/topic/361) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [AI自动化](https://www.cocoloop.cn/tag/222-tag/222 "AI自动化 - CocoLoop社区收录了129篇关于AI自动化的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw docker教程](https://www.cocoloop.cn/tag/371-tag/371 "openclaw docker教程 - CocoLoop社区收录了122篇关于openclaw docker教程的精选内容，涵盖教程、实战经验和深度讨论。"),[docker部署openclaw](https://www.cocoloop.cn/tag/370-tag/370 "docker部署openclaw - CocoLoop社区收录了116篇关于docker部署openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[大模型](https://www.cocoloop.cn/tag/11-tag/11 "大模型 - CocoLoop社区收录了37篇关于大模型的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 4 ](https://www.cocoloop.cn/t/topic/361/1)  |  151  |  [3月 26 日](https://www.cocoloop.cn/t/topic/361/5)  |  
|  [技术社区为什么对 AI 自动化工具褒贬不一？](https://www.cocoloop.cn/t/topic/376) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [claude code怎么用](https://www.cocoloop.cn/tag/355-tag/355 "claude code怎么用 - CocoLoop社区收录了251篇关于claude code怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[claude code教程](https://www.cocoloop.cn/tag/206-tag/206 "claude code教程 - CocoLoop社区收录了245篇关于claude code教程的精选内容，涵盖教程、实战经验和深度讨论。"),[claude模型怎么选](https://www.cocoloop.cn/tag/374-tag/374 "claude模型怎么选 - CocoLoop社区收录了83篇关于claude模型怎么选的精选内容，涵盖教程、实战经验和深度讨论。"),[claude最新版本](https://www.cocoloop.cn/tag/375-tag/375 "claude最新版本 - CocoLoop社区收录了43篇关于claude最新版本的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 6 ](https://www.cocoloop.cn/t/topic/376/1)  |  788  |  [4月 3 日](https://www.cocoloop.cn/t/topic/376/7)  |  
|  [有篇文章说 2026 是人类最后一次掌控 AI，看完睡不着觉](https://www.cocoloop.cn/t/topic/3623) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)  |  [ 7 ](https://www.cocoloop.cn/t/topic/3623/1)  |  2.5k  |  [6月 3 日](https://www.cocoloop.cn/t/topic/3623/8)  |  
|  [李飞飞团队把亿级粒子 3D 世界跑在手机上了](https://www.cocoloop.cn/t/topic/3176) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)  |  [ 10 ](https://www.cocoloop.cn/t/topic/3176/1)  |  2.1k  |  [5月 31 日](https://www.cocoloop.cn/t/topic/3176/11)  |  
###  想阅读更多？请浏览[![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)中的其他话题或[查看最新话题](https://www.cocoloop.cn/latest)。 
Invalid date  Invalid date 


