# [n8n加AI搭建自动化工作流，手把手入门教程，附实用案例](https://www.cocoloop.cn/t/topic/1740)

n8n加AI搭建自动化工作流，手把手入门教程，附实用案例 ](https://www.cocoloop.cn/t/topic/1740)
[![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)
[openclaw docker教程](https://www.cocoloop.cn/tag/371-tag/371 "openclaw docker教程 - CocoLoop社区收录了122篇关于openclaw docker教程的精选内容，涵盖教程、实战经验和深度讨论。"),[docker部署openclaw](https://www.cocoloop.cn/tag/370-tag/370 "docker部署openclaw - CocoLoop社区收录了116篇关于docker部署openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[免费AI API推荐](https://www.cocoloop.cn/tag/362-tag/362 "免费AI API推荐 - CocoLoop社区收录了74篇关于免费AI API推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw接入钉钉](https://www.cocoloop.cn/tag/255-tag/255 "openclaw接入钉钉 - CocoLoop社区收录了24篇关于openclaw接入钉钉的精选内容，涵盖教程、实战经验和深度讨论。")
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/1740)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/1740)
368 浏览量  11 赞  17 用户 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/d/22d042/48.png) 2 ](https://www.cocoloop.cn/u/devrel_diana "devrel_diana")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/g/90ced4/48.png) ](https://www.cocoloop.cn/u/glen460 "glen460")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/r/a8b319/48.png) ](https://www.cocoloop.cn/u/Ryan "Ryan")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/p/ecccb3/48.png) ](https://www.cocoloop.cn/u/pz_work "pz_work")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/m/3be4f8/48.png) ](https://www.cocoloop.cn/u/my_node "my_node")
[ 3月 26 日  ](https://www.cocoloop.cn/t/topic/1740/1 "跳到第一个帖子")
1 / 18 
3月 26 日 
[ 4月 3 日 ](https://www.cocoloop.cn/t/topic/1740/18)
##  由 devrel_diana 于 3月 26 日 发布 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/d/22d042/48.png) ](https://www.cocoloop.cn/u/devrel_diana)
[ devrel_diana  ](https://www.cocoloop.cn/u/devrel_diana)
[ 3月 26 日 ](https://www.cocoloop.cn/t/topic/1740 "发布日期")
发现身边还有很多人在手动做重复性工作，想安利一下n8n这个神器。配合AI使用，真的能省掉大量时间。
##  [](https://www.cocoloop.cn/t/topic/1740#p-17709-n8n-1)n8n是什么
开源的工作流自动化平台，类似Zapier但**自部署免费** 。把它理解成"连线工具"——把各种服务用线连起来，数据自动流转。
##  [](https://www.cocoloop.cn/t/topic/1740#p-17709-h-2)和其他工具的对比  
| 对比  | n8n  | Zapier  | Make  |  
| --- | --- | --- | --- |  
| 价格  | 自部署免费  | $20/月起  | $9/月起  |  
| AI集成  | 好  | 一般  | 好  |  
| 自定义  | 非常强  | 有限  | 中等  |  
| 数据隐私  | 完全本地  | 云端  | 云端  |  
##  [](https://www.cocoloop.cn/t/topic/1740#p-17709-h-3)部署超简单

```

docker run -d --name n8n -p 5678:5678 n8nio/n8n

```

打开localhost:5678就能用。
##  [](https://www.cocoloop.cn/t/topic/1740#p-17709-h-4)实战案例：邮件分类助手
  1. Email Trigger检查新邮件
  2. AI Agent节点分析重要性和分类
  3. Switch节点分流：重要→钉钉通知，普通→待处理，垃圾→归档
  4. Webhook发送通知

用了三个月，每月省了40-50小时的重复工作。
还有什么好的自动化工作流场景推荐吗？想多搭几个~
  

1 个回复
​ 
​ 
368 浏览量  11 赞  17 用户 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/d/22d042/48.png) 2 ](https://www.cocoloop.cn/u/devrel_diana "devrel_diana")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/g/90ced4/48.png) ](https://www.cocoloop.cn/u/glen460 "glen460")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/r/a8b319/48.png) ](https://www.cocoloop.cn/u/Ryan "Ryan")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/p/ecccb3/48.png) ](https://www.cocoloop.cn/u/pz_work "pz_work")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/m/3be4f8/48.png) ](https://www.cocoloop.cn/u/my_node "my_node")
##  由 ops_tiger 于 3月 26 日 发布 
##  由 data_plumber 于 3月 26 日 发布 
##  由 homebrew_hacker 于 3月 26 日 发布 
##  由 serverless_fan 于 3月 26 日 发布 
##  由 kevin_wang88 于 3月 26 日 发布 
##  由 devrel_diana 于 3月 26 日 发布 
8 天后 
##  由 dabaicai 于 4月 3 日 发布 
##  由 yitian_jm 于 4月 3 日 发布 
##  由 laoliu_py 于 4月 3 日 发布 
##  由 opsxuer 于 4月 3 日 发布 
##  由 Ryan 于 4月 3 日 发布 
##  由 agent_builder 于 4月 3 日 发布 
##  由 glen460 于 4月 3 日 发布 
##  由 pz_work 于 4月 3 日 发布 
##  由 my_node 于 4月 3 日 发布 
##  由 rw_ai 于 4月 3 日 发布 
##  由 hd_pm 于 4月 3 日 发布 
回复
  

###  新话题和未读话题   
话题列表，带有按钮的列标题可以排序。  
|  话题   |  回复   |  浏览量   |  活动   |  
| --- | --- | --- | --- |  
|  [你们公司让装 OpenClaw 吗？聊聊办公场景下的安全顾虑](https://www.cocoloop.cn/t/topic/299) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [openclaw docker教程](https://www.cocoloop.cn/tag/371-tag/371 "openclaw docker教程 - CocoLoop社区收录了122篇关于openclaw docker教程的精选内容，涵盖教程、实战经验和深度讨论。"),[docker部署openclaw](https://www.cocoloop.cn/tag/370-tag/370 "docker部署openclaw - CocoLoop社区收录了116篇关于docker部署openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[AI办公效率](https://www.cocoloop.cn/tag/227-tag/227 "AI办公效率 - CocoLoop社区收录了60篇关于AI办公效率的精选内容，涵盖教程、实战经验和深度讨论。"),[AI安全](https://www.cocoloop.cn/tag/236-tag/236 "AI安全 - CocoLoop社区收录了54篇关于AI安全的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/299/1)  |  225  |  [3月 24 日](https://www.cocoloop.cn/t/topic/299/8)  |  
|  [用OpenClaw赚钱靠谱吗？有哪些副业方向？](https://www.cocoloop.cn/t/topic/2296) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [OpenClaw](https://www.cocoloop.cn/tag/637-tag/637 "OpenClaw - CocoLoop社区收录了132篇关于OpenClaw的精选内容，涵盖教程、实战经验和深度讨论。"),[AI副业](https://www.cocoloop.cn/tag/154-tag/154 "AI副业 - CocoLoop社区收录了9篇关于AI副业的精选内容，涵盖教程、实战经验和深度讨论。"),[OpenClaw赚钱](https://www.cocoloop.cn/tag/1181-tag/1181 "OpenClaw赚钱 - CocoLoop社区收录了3篇关于OpenClaw赚钱的精选内容，涵盖教程、实战经验和深度讨论。"),[自动化赚钱](https://www.cocoloop.cn/tag/1182-tag/1182 "自动化赚钱 - CocoLoop社区收录了2篇关于自动化赚钱的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 6 ](https://www.cocoloop.cn/t/topic/2296/1)  |  2.1k  |  [4月 1 日](https://www.cocoloop.cn/t/topic/2296/7)  |  
|  [Ollama是什么？值得折腾吗？](https://www.cocoloop.cn/t/topic/3121) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [大模型](https://www.cocoloop.cn/tag/11-tag/11 "大模型 - CocoLoop社区收录了37篇关于大模型的精选内容，涵盖教程、实战经验和深度讨论。"),[ollama](https://www.cocoloop.cn/tag/13-tag/13 "ollama - CocoLoop社区收录了31篇关于ollama的精选内容，涵盖教程、实战经验和深度讨论。"),[ollama是什么](https://www.cocoloop.cn/tag/792-tag/792 "ollama是什么 - CocoLoop社区收录了3篇关于ollama是什么的精选内容，涵盖教程、实战经验和深度讨论。"),[本地AI](https://www.cocoloop.cn/tag/1247-tag/1247 "本地AI - CocoLoop社区收录了2篇关于本地AI的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/3121/1)  |  2.4k  |  [5月 6 日](https://www.cocoloop.cn/t/topic/3121/8)  |  
|  [奥特曼被曝推动 OpenAI 为自己的核聚变项目投资，内部炸锅](https://www.cocoloop.cn/t/topic/3158) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)  |  [ 11 ](https://www.cocoloop.cn/t/topic/3158/1)  |  1.9k  |  [5月 27 日](https://www.cocoloop.cn/t/topic/3158/12)  |  
|  [讨论：AI 工具适不适合做工作流快照和备份？](https://www.cocoloop.cn/t/topic/611) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [openclaw排错](https://www.cocoloop.cn/tag/35-tag/35 "openclaw排错 - CocoLoop社区收录了158篇关于openclaw排错的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw配置](https://www.cocoloop.cn/tag/223-tag/223 "openclaw配置 - CocoLoop社区收录了151篇关于openclaw配置的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw备份恢复教程](https://www.cocoloop.cn/tag/380-tag/380 "openclaw备份恢复教程 - CocoLoop社区收录了29篇关于openclaw备份恢复教程的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw数据备份](https://www.cocoloop.cn/tag/379-tag/379 "openclaw数据备份 - CocoLoop社区收录了21篇关于openclaw数据备份的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/611/1)  |  175  |  [3月 31 日](https://www.cocoloop.cn/t/topic/611/8)  |  
|  [咪鼠AI绘图教程：文生图、图生图、画同款、去水印+实操案例](https://www.cocoloop.cn/t/topic/2065) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [ai绘图指令词大全](https://www.cocoloop.cn/tag/754-tag/754 "ai绘图指令词大全 - CocoLoop社区收录了2篇关于ai绘图指令词大全的精选内容，涵盖教程、实战经验和深度讨论。"),[咪鼠去水印方法](https://www.cocoloop.cn/tag/753-tag/753 "咪鼠去水印方法 - CocoLoop社区收录了2篇关于咪鼠去水印方法的精选内容，涵盖教程、实战经验和深度讨论。"),[ai文生图怎么用](https://www.cocoloop.cn/tag/752-tag/752 "ai文生图怎么用 - CocoLoop社区收录了2篇关于ai文生图怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[咪鼠ai绘图教程](https://www.cocoloop.cn/tag/751-tag/751 "咪鼠ai绘图教程 - CocoLoop社区收录了2篇关于咪鼠ai绘图教程的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 2 ](https://www.cocoloop.cn/t/topic/2065/1)  |  1.7k  |  [4月 3 日](https://www.cocoloop.cn/t/topic/2065/3)  |  
|  [花了十几块 Token 总结出来的经验：AI 助手到底能干什么](https://www.cocoloop.cn/t/topic/624) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [AI翻译工具推荐](https://www.cocoloop.cn/tag/364-tag/364 "AI翻译工具推荐 - CocoLoop社区收录了106篇关于AI翻译工具推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[最好用的AI翻译](https://www.cocoloop.cn/tag/365-tag/365 "最好用的AI翻译 - CocoLoop社区收录了88篇关于最好用的AI翻译的精选内容，涵盖教程、实战经验和深度讨论。"),[AI入门科普](https://www.cocoloop.cn/tag/62-tag/62 "AI入门科普 - CocoLoop社区收录了76篇关于AI入门科普的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw是什么](https://www.cocoloop.cn/tag/145-tag/145 "openclaw是什么 - CocoLoop社区收录了56篇关于openclaw是什么的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 6 ](https://www.cocoloop.cn/t/topic/624/1)  |  154  |  [3月 30 日](https://www.cocoloop.cn/t/topic/624/7)  |  
|  [你们的 AI 助手都喂的什么’饲料’？各家模型 API 成本对比](https://www.cocoloop.cn/t/topic/625) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [claude模型怎么选](https://www.cocoloop.cn/tag/374-tag/374 "claude模型怎么选 - CocoLoop社区收录了83篇关于claude模型怎么选的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw免费](https://www.cocoloop.cn/tag/160-tag/160 "openclaw免费 - CocoLoop社区收录了44篇关于openclaw免费的精选内容，涵盖教程、实战经验和深度讨论。"),[claude最新版本](https://www.cocoloop.cn/tag/375-tag/375 "claude最新版本 - CocoLoop社区收录了43篇关于claude最新版本的精选内容，涵盖教程、实战经验和深度讨论。"),[claude code](https://www.cocoloop.cn/tag/225-tag/225 "claude code - CocoLoop社区收录了34篇关于claude code的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 5 ](https://www.cocoloop.cn/t/topic/625/1)  |  153  |  [3月 31 日](https://www.cocoloop.cn/t/topic/625/6)  |  
|  [2026年了，AI生成的内容做SEO到底还有没有效？实测数据说话](https://www.cocoloop.cn/t/topic/1936) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [内容营销](https://www.cocoloop.cn/tag/486-tag/486 "内容营销 - CocoLoop社区收录了1篇关于内容营销的精选内容，涵盖教程、实战经验和深度讨论。"),[google排名](https://www.cocoloop.cn/tag/485-tag/485 "google排名 - CocoLoop社区收录了1篇关于google排名的精选内容，涵盖教程、实战经验和深度讨论。"),[ai内容](https://www.cocoloop.cn/tag/484-tag/484 "ai内容 - CocoLoop社区收录了1篇关于ai内容的精选内容，涵盖教程、实战经验和深度讨论。"),[seo](https://www.cocoloop.cn/tag/483-tag/483 "seo - CocoLoop社区收录了1篇关于seo的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 6 ](https://www.cocoloop.cn/t/topic/1936/1)  |  147  |  [3月 28 日](https://www.cocoloop.cn/t/topic/1936/7)  |  
|  [想知道hermes 在不良资产行业的应用](https://www.cocoloop.cn/t/topic/5806) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [问题讨论](https://www.cocoloop.cn/tag/9-tag/9 "问题讨论 - CocoLoop社区收录了18篇关于问题讨论的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 5 ](https://www.cocoloop.cn/t/topic/5806/1)  |  154  |  [6月 21 日](https://www.cocoloop.cn/t/topic/5806/6)  |  
###  想阅读更多？请浏览[![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)中的其他话题或[查看最新话题](https://www.cocoloop.cn/latest)。 
Invalid date  Invalid date 


