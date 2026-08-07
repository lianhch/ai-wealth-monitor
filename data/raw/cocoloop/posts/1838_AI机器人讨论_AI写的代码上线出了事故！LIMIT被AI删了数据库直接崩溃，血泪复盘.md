# [AI写的代码上线出了事故！LIMIT被AI删了数据库直接崩溃，血泪复盘](https://www.cocoloop.cn/t/topic/1838)

AI写的代码上线出了事故！LIMIT被AI删了数据库直接崩溃，血泪复盘 ](https://www.cocoloop.cn/t/topic/1838)
[![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)
[openclaw排错](https://www.cocoloop.cn/tag/35-tag/35 "openclaw排错 - CocoLoop社区收录了158篇关于openclaw排错的精选内容，涵盖教程、实战经验和深度讨论。"),[AI编程工具](https://www.cocoloop.cn/tag/193-tag/193 "AI编程工具 - CocoLoop社区收录了126篇关于AI编程工具的精选内容，涵盖教程、实战经验和深度讨论。"),[AI趋势](https://www.cocoloop.cn/tag/199-tag/199 "AI趋势 - CocoLoop社区收录了30篇关于AI趋势的精选内容，涵盖教程、实战经验和深度讨论。")
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/1838)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/1838)
373 浏览量  7 赞 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/6f9a4e/48.png) 2 ](https://www.cocoloop.cn/u/sre_fu_x "sre_fu_x")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/e9c0ed/48.png) ](https://www.cocoloop.cn/u/sec_hunter_lin "sec_hunter_lin")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/prod_is_down/48/1246_2.png) ](https://www.cocoloop.cn/u/prod_is_down "prod_is_down")
[ 3月 26 日  ](https://www.cocoloop.cn/t/topic/1838/1 "跳到第一个帖子")
1 / 4 
3月 26 日 
[ 3月 26 日 ](https://www.cocoloop.cn/t/topic/1838/4)
##  由 sre_fu_x 于 3月 26 日 发布 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/6f9a4e/48.png) ](https://www.cocoloop.cn/u/sre_fu_x)
[ sre_fu_x  ](https://www.cocoloop.cn/u/sre_fu_x)
[ 3月 26 日 ](https://www.cocoloop.cn/t/topic/1838 "发布日期")
上个月出了一次线上事故，直接原因是AI生成的代码有问题。完整复盘。
**经过** ：产品需求"导出增加按时间筛选"。我用Claude Code生成代码，Review通过，上线。第三天数据库CPU飙到98%。
**根因** ：AI加了时间筛选条件，但**把原有的`LIMIT 10000` 保护删了**。运营选了大时间范围导出，查询返回80万条记录，数据库打挂。
**为什么没发现** ：
  * 测试数据库才100条，测不出性能问题
  * Code Review关注了新增代码，没注意到被删除的代码
  * AI删LIMIT时没有主动告知

**5条教训：**
  1. **AI删除代码比新增代码更危险** ——Review重点看diff红色部分
  2. **AI不理解"为什么这行代码在这里"** ——关键保护代码必须加注释说明原因
  3. **测试环境和生产的数据量差距是隐患** ——关键路径必须用接近生产规模的数据压测
  4. **不要因为AI代码"看起来对"就放松Review** ——AI代码Review标准应该更严格
  5. **加防护兜底** ——查询层加了超时5秒+行数上限1万

**AI是工具，出事故的责任在用工具的人。用AI提速是好事，但速度不能以安全为代价。**
你有AI代码导致线上问题的经历吗？
  

​ 
​ 
373 浏览量  7 赞 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/6f9a4e/48.png) 2 ](https://www.cocoloop.cn/u/sre_fu_x "sre_fu_x")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/e9c0ed/48.png) ](https://www.cocoloop.cn/u/sec_hunter_lin "sec_hunter_lin")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/prod_is_down/48/1246_2.png) ](https://www.cocoloop.cn/u/prod_is_down "prod_is_down")
##  由 prod_is_down 于 3月 26 日 发布 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/prod_is_down/48/1246_2.png) ](https://www.cocoloop.cn/u/prod_is_down)
[ prod_is_down  ](https://www.cocoloop.cn/u/prod_is_down)
[ 3月 26 日 ](https://www.cocoloop.cn/t/topic/1838/2 "发布日期")
太真实了……我们也出过类似的事。
AI把一个`WHERE user_id = ?`的条件改成了`WHERE user_id IN (?)`，本意是支持批量查询。但没有限制IN的数量，有人传了5000个ID进来，查询直接超时。
**共同的教训：AI会为了完成你的需求而移除它认为"不需要"的限制。**
我现在的做法：所有涉及数据库查询的AI代码改动，必须回答3个问题：
  1. 最大可能返回多少行？
  2. 最大可能的查询耗时？
  3. 有没有防护机制（LIMIT、超时、分页）？

答不上来的不允许合并。
  

2  ​ 
​ 
##  由 sec_hunter_lin 于 3月 26 日 发布 
##  由 sre_fu_x 于 3月 26 日 发布 
回复
  

###  新话题和未读话题   
话题列表，带有按钮的列标题可以排序。  
|  话题   |  回复   |  浏览量   |  活动   |  
| --- | --- | --- | --- |  
|  [OpenClaw科研场景怎么用？求实际应用案例](https://www.cocoloop.cn/t/topic/3125) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [OpenClaw](https://www.cocoloop.cn/tag/637-tag/637 "OpenClaw - CocoLoop社区收录了132篇关于OpenClaw的精选内容，涵盖教程、实战经验和深度讨论。"),[OpenClaw科研](https://www.cocoloop.cn/tag/1241-tag/1241 "OpenClaw科研 - CocoLoop社区收录了4篇关于OpenClaw科研的精选内容，涵盖教程、实战经验和深度讨论。"),[学术工具](https://www.cocoloop.cn/tag/1243-tag/1243 "学术工具 - CocoLoop社区收录了3篇关于学术工具的精选内容，涵盖教程、实战经验和深度讨论。"),[AI科研应用](https://www.cocoloop.cn/tag/1242-tag/1242 "AI科研应用 - CocoLoop社区收录了3篇关于AI科研应用的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/3125/1)  |  2.1k  |  [5月 5 日](https://www.cocoloop.cn/t/topic/3125/8)  |  
|  [准备面试智谱 AI，有过来人分享经验吗？](https://www.cocoloop.cn/t/topic/2136) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [AI岗位面试准备](https://www.cocoloop.cn/tag/403-tag/403 "AI岗位面试准备 - CocoLoop社区收录了12篇关于AI岗位面试准备的精选内容，涵盖教程、实战经验和深度讨论。"),[智谱AI招聘哪些岗位适合应届生](https://www.cocoloop.cn/tag/918-tag/918 "智谱AI招聘哪些岗位适合应届生 - CocoLoop社区收录了1篇关于智谱AI招聘哪些岗位适合应届生的精选内容，涵盖教程、实战经验和深度讨论。"),[智谱AI面试常见问题有哪些](https://www.cocoloop.cn/tag/917-tag/917 "智谱AI面试常见问题有哪些 - CocoLoop社区收录了1篇关于智谱AI面试常见问题有哪些的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/2136/1)  |  2.2k  |  [3月 31 日](https://www.cocoloop.cn/t/topic/2136/8)  |  
|  [Copaw 本地部署接微信，多智能体真能跑通吗](https://www.cocoloop.cn/t/topic/2686) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [copaw本地部署](https://www.cocoloop.cn/tag/817-tag/817 "copaw本地部署 - CocoLoop社区收录了2篇关于copaw本地部署的精选内容，涵盖教程、实战经验和深度讨论。"),[copaw多智能体教程](https://www.cocoloop.cn/tag/1557-tag/1557 "copaw多智能体教程 - CocoLoop社区收录了1篇关于copaw多智能体教程的精选内容，涵盖教程、实战经验和深度讨论。"),[copaw接入微信](https://www.cocoloop.cn/tag/1556-tag/1556 "copaw接入微信 - CocoLoop社区收录了1篇关于copaw接入微信的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 23 ](https://www.cocoloop.cn/t/topic/2686/1)  |  2.1k  |  [5月 7 日](https://www.cocoloop.cn/t/topic/2686/24)  |  
|  [Ollama本地知识库怎么搭？RAG实战](https://www.cocoloop.cn/t/topic/3107) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [ollama](https://www.cocoloop.cn/tag/13-tag/13 "ollama - CocoLoop社区收录了31篇关于ollama的精选内容，涵盖教程、实战经验和深度讨论。"),[dify](https://www.cocoloop.cn/tag/203-tag/203 "dify - CocoLoop社区收录了7篇关于dify的精选内容，涵盖教程、实战经验和深度讨论。"),[rag](https://www.cocoloop.cn/tag/1215-tag/1215 "rag - CocoLoop社区收录了3篇关于rag的精选内容，涵盖教程、实战经验和深度讨论。"),[Ollama知识库](https://www.cocoloop.cn/tag/1268-tag/1268 "Ollama知识库 - CocoLoop社区收录了2篇关于Ollama知识库的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 8 ](https://www.cocoloop.cn/t/topic/3107/1)  |  2.4k  |  [5月 25 日](https://www.cocoloop.cn/t/topic/3107/9)  |  
|  [OpenClaw能用来分析股票吗？有人实测过吗？](https://www.cocoloop.cn/t/topic/3059) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [OpenClaw](https://www.cocoloop.cn/tag/637-tag/637 "OpenClaw - CocoLoop社区收录了132篇关于OpenClaw的精选内容，涵盖教程、实战经验和深度讨论。"),[AI炒股](https://www.cocoloop.cn/tag/80-tag/80 "AI炒股 - CocoLoop社区收录了25篇关于AI炒股的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw股票分析](https://www.cocoloop.cn/tag/86-tag/86 "openclaw股票分析 - CocoLoop社区收录了4篇关于openclaw股票分析的精选内容，涵盖教程、实战经验和深度讨论。"),[数据分析](https://www.cocoloop.cn/tag/1180-tag/1180 "数据分析 - CocoLoop社区收录了2篇关于数据分析的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 17 ](https://www.cocoloop.cn/t/topic/3059/1)  |  2.5k  |  [5月 30 日](https://www.cocoloop.cn/t/topic/3059/18)  |  
|  [MiClaw 用了一周，说说真实感受](https://www.cocoloop.cn/t/topic/2087) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [miclaw测评](https://www.cocoloop.cn/tag/807-tag/807 "miclaw测评 - CocoLoop社区收录了2篇关于miclaw测评的精选内容，涵盖教程、实战经验和深度讨论。"),[miclaw能做什么](https://www.cocoloop.cn/tag/810-tag/810 "miclaw能做什么 - CocoLoop社区收录了1篇关于miclaw能做什么的精选内容，涵盖教程、实战经验和深度讨论。"),[MiClaw手机使用技巧](https://www.cocoloop.cn/tag/809-tag/809 "MiClaw手机使用技巧 - CocoLoop社区收录了1篇关于MiClaw手机使用技巧的精选内容，涵盖教程、实战经验和深度讨论。"),[miclaw功能详细解析](https://www.cocoloop.cn/tag/808-tag/808 "miclaw功能详细解析 - CocoLoop社区收录了1篇关于miclaw功能详细解析的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/2087/1)  |  2.0k  |  [3月 30 日](https://www.cocoloop.cn/t/topic/2087/8)  |  
|  [有篇文章说 2026 是人类最后一次掌控 AI，看完睡不着觉](https://www.cocoloop.cn/t/topic/3623) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)  |  [ 7 ](https://www.cocoloop.cn/t/topic/3623/1)  |  2.5k  |  [6月 3 日](https://www.cocoloop.cn/t/topic/3623/8)  |  
|  [AI自动发小红书、抖音，Molili和AutoClaw哪个封号率低一点？](https://www.cocoloop.cn/t/topic/2210) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [molili教程](https://www.cocoloop.cn/tag/47-tag/47 "molili教程 - CocoLoop社区收录了79篇关于molili教程的精选内容，涵盖教程、实战经验和深度讨论。"),[autoclaw](https://www.cocoloop.cn/tag/1075-tag/1075 "autoclaw - CocoLoop社区收录了8篇关于autoclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[AI自动发帖](https://www.cocoloop.cn/tag/1082-tag/1082 "AI自动发帖 - CocoLoop社区收录了3篇关于AI自动发帖的精选内容，涵盖教程、实战经验和深度讨论。"),[小红书运营](https://www.cocoloop.cn/tag/1083-tag/1083 "小红书运营 - CocoLoop社区收录了2篇关于小红书运营的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 12 ](https://www.cocoloop.cn/t/topic/2210/1)  |  2.5k  |  [4月 3 日](https://www.cocoloop.cn/t/topic/2210/13)  |  
|  [咪鼠AI写作+长文写作教程：模板、配图、大纲、导出全流程](https://www.cocoloop.cn/t/topic/2075) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [ai自动写文章工具](https://www.cocoloop.cn/tag/777-tag/777 "ai自动写文章工具 - CocoLoop社区收录了1篇关于ai自动写文章工具的精选内容，涵盖教程、实战经验和深度讨论。"),[咪鼠写作模板](https://www.cocoloop.cn/tag/776-tag/776 "咪鼠写作模板 - CocoLoop社区收录了1篇关于咪鼠写作模板的精选内容，涵盖教程、实战经验和深度讨论。"),[ai长文写作怎么用](https://www.cocoloop.cn/tag/775-tag/775 "ai长文写作怎么用 - CocoLoop社区收录了1篇关于ai长文写作怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[咪鼠ai写作教程](https://www.cocoloop.cn/tag/774-tag/774 "咪鼠ai写作教程 - CocoLoop社区收录了1篇关于咪鼠ai写作教程的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 2 ](https://www.cocoloop.cn/t/topic/2075/1)  |  2.1k  |  [4月 3 日](https://www.cocoloop.cn/t/topic/2075/3)  |  
|  [2026年靠AI做副业到底能赚多少钱？有没有真实案例而不是割韭菜？](https://www.cocoloop.cn/t/topic/1737) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [claude code怎么用](https://www.cocoloop.cn/tag/355-tag/355 "claude code怎么用 - CocoLoop社区收录了251篇关于claude code怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[claude code教程](https://www.cocoloop.cn/tag/206-tag/206 "claude code教程 - CocoLoop社区收录了245篇关于claude code教程的精选内容，涵盖教程、实战经验和深度讨论。"),[cursor和claude code对比](https://www.cocoloop.cn/tag/216-tag/216 "cursor和claude code对比 - CocoLoop社区收录了57篇关于cursor和claude code对比的精选内容，涵盖教程、实战经验和..."),[cursor怎么用](https://www.cocoloop.cn/tag/354-tag/354 "cursor怎么用 - CocoLoop社区收录了40篇关于cursor怎么用的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 8 ](https://www.cocoloop.cn/t/topic/1737/1)  |  423  |  [4月 3 日](https://www.cocoloop.cn/t/topic/1737/9)  |  
###  想阅读更多？请浏览[![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)中的其他话题或[查看最新话题](https://www.cocoloop.cn/latest)。 
Invalid date  Invalid date 


