# [Qclaw 把我的 OpenClaw 删了！同目录冲突的血泪教训](https://www.cocoloop.cn/t/topic/309)

Qclaw 把我的 OpenClaw 删了！同目录冲突的血泪教训 ](https://www.cocoloop.cn/t/topic/309)
[![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)
[openclaw docker教程](https://www.cocoloop.cn/tag/371-tag/371 "openclaw docker教程 - CocoLoop社区收录了122篇关于openclaw docker教程的精选内容，涵盖教程、实战经验和深度讨论。"),[docker部署openclaw](https://www.cocoloop.cn/tag/370-tag/370 "docker部署openclaw - CocoLoop社区收录了116篇关于docker部署openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw完整卸载教程](https://www.cocoloop.cn/tag/373-tag/373 "openclaw完整卸载教程 - CocoLoop社区收录了41篇关于openclaw完整卸载教程的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw备份恢复教程](https://www.cocoloop.cn/tag/380-tag/380 "openclaw备份恢复教程 - CocoLoop社区收录了29篇关于openclaw备份恢复教程的精选内容，涵盖教程、实战经验和深度讨论。")
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/309)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/309)
636 浏览量  7 用户 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/9de053/48.png) ](https://www.cocoloop.cn/u/suanfa_daren "suanfa_daren")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/l/8c91f0/48.png) ](https://www.cocoloop.cn/u/liangtianqing "liangtianqing")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/a/ecd19e/48.png) ](https://www.cocoloop.cn/u/aigc_chuangzuo "aigc_chuangzuo")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/z/e0b2c6/48.png) ](https://www.cocoloop.cn/u/zhouzhinan "zhouzhinan")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/d/96bed5/48.png) ](https://www.cocoloop.cn/u/diffusion_art "diffusion_art")
[ 3月 17 日  ](https://www.cocoloop.cn/t/topic/309/1 "跳到第一个帖子")
1 / 7 
3月 17 日 
[ 3月 24 日 ](https://www.cocoloop.cn/t/topic/309/7)
##  由 suanfa_daren 于 3月 17 日 发布 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/9de053/48.png) ](https://www.cocoloop.cn/u/suanfa_daren)
[ suanfa_daren  ](https://www.cocoloop.cn/u/suanfa_daren)
[ 3月 17 日 ](https://www.cocoloop.cn/t/topic/309 "发布日期")
分享一个惨痛经历，给大家避个坑。
##  [](https://www.cocoloop.cn/t/topic/309#p-2572-h-1)事情经过
我之前服务器上已经装好了 OpenClaw，用得好好的。后来看到有人推荐 Qclaw（另一个基于 OpenClaw 的分支），想试试看就装上了。
结果两个东西因为**网关端口冲突** ，都没法正常用了。这还不是最惨的——
当我决定卸载 Qclaw 的时候，卸载脚本自动执行了：

```

rm -rf ./openclaw

```

因为 Qclaw 和 OpenClaw 用的是**同一个配置目录** ，这一删，两个全没了。数据、配置、记忆文件，全部归零。
##  [](https://www.cocoloop.cn/t/topic/309#p-2572-h-2)为什么会这样？
Qclaw 的卸载脚本大概率是直接复制了 OpenClaw 的脚本，没有做任何适配。当两个程序共享目录时，卸载一个就会把另一个也带走。
##  [](https://www.cocoloop.cn/t/topic/309#p-2572-h-3)教训总结
  1. **永远不要在同一环境装两个 Claw 分支** ，端口和目录冲突概率极高
  2. **装任何新东西之前先备份** ，`tar czf backup.tar.gz ./openclaw/` 一分钟的事
  3. **用 Docker 隔离** ，每个应用一个容器，互不干扰
  4. **看清卸载脚本再执行** ，特别是涉及 rm -rf 的

希望大家引以为戒，别像我一样踩坑。
  

​ 
​ 
636 浏览量  7 用户 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/9de053/48.png) ](https://www.cocoloop.cn/u/suanfa_daren "suanfa_daren")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/l/8c91f0/48.png) ](https://www.cocoloop.cn/u/liangtianqing "liangtianqing")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/a/ecd19e/48.png) ](https://www.cocoloop.cn/u/aigc_chuangzuo "aigc_chuangzuo")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/z/e0b2c6/48.png) ](https://www.cocoloop.cn/u/zhouzhinan "zhouzhinan")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/d/96bed5/48.png) ](https://www.cocoloop.cn/u/diffusion_art "diffusion_art")
##  由 liangtianqing 于 3月 17 日 发布 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/l/8c91f0/48.png) ](https://www.cocoloop.cn/u/liangtianqing)
[ liangtianqing  ](https://www.cocoloop.cn/u/liangtianqing)
[ 3月 17 日 ](https://www.cocoloop.cn/t/topic/309/2 "发布日期")
卸载脚本里带rm -rf真的太危险了，能不能先检查下目录归属
  

1 个回复
​ 
​ 
##  由 diffusion_art 于 3月 17 日 发布 
##  由 zhouzhinan 于 3月 17 日 发布 
##  由 luohaoming 于 3月 17 日 发布 
##  由 aigc_chuangzuo 于 3月 17 日 发布 
##  由 zhihu_lurk3r 于 3月 24 日 发布 
回复
  

###  新话题和未读话题   
话题列表，带有按钮的列标题可以排序。  
|  话题   |  回复   |  浏览量   |  活动   |  
| --- | --- | --- | --- |  
|  [闲鱼买二手 Mac mini 专门跑 AI 工具值不值？](https://www.cocoloop.cn/t/topic/603) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [mac部署openclaw](https://www.cocoloop.cn/tag/104-tag/104 "mac部署openclaw - CocoLoop社区收录了27篇关于mac部署openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw云部署](https://www.cocoloop.cn/tag/125-tag/125 "openclaw云部署 - CocoLoop社区收录了22篇关于openclaw云部署的精选内容，涵盖教程、实战经验和深度讨论。"),[树莓派安装openclaw](https://www.cocoloop.cn/tag/366-tag/366 "树莓派安装openclaw - CocoLoop社区收录了9篇关于树莓派安装openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[树莓派跑AI](https://www.cocoloop.cn/tag/367-tag/367 "树莓派跑AI - CocoLoop社区收录了3篇关于树莓派跑AI的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 5 ](https://www.cocoloop.cn/t/topic/603/1)  |  159  |  [3月 31 日](https://www.cocoloop.cn/t/topic/603/6)  |  
|  [AI 自动化工具到底有没有用？正反方观点整理](https://www.cocoloop.cn/t/topic/347) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [openclaw skill](https://www.cocoloop.cn/tag/142-tag/142 "openclaw skill - CocoLoop社区收录了152篇关于openclaw skill的精选内容，涵盖教程、实战经验和深度讨论。"),[AI自动化](https://www.cocoloop.cn/tag/222-tag/222 "AI自动化 - CocoLoop社区收录了129篇关于AI自动化的精选内容，涵盖教程、实战经验和深度讨论。"),[AI办公效率](https://www.cocoloop.cn/tag/227-tag/227 "AI办公效率 - CocoLoop社区收录了60篇关于AI办公效率的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw运维](https://www.cocoloop.cn/tag/228-tag/228 "openclaw运维 - CocoLoop社区收录了49篇关于openclaw运维的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 12 ](https://www.cocoloop.cn/t/topic/347/1)  |  239  |  [4月 7 日](https://www.cocoloop.cn/t/topic/347/13)  |  
|  [SafeClaw安全吗？HiClaw适合什么人？](https://www.cocoloop.cn/t/topic/2246) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [AI智能体](https://www.cocoloop.cn/tag/571-tag/571 "AI智能体 - CocoLoop社区收录了5篇关于AI智能体的精选内容，涵盖教程、实战经验和深度讨论。"),[私有化部署](https://www.cocoloop.cn/tag/1088-tag/1088 "私有化部署 - CocoLoop社区收录了2篇关于私有化部署的精选内容，涵盖教程、实战经验和深度讨论。"),[企业AI安全](https://www.cocoloop.cn/tag/1087-tag/1087 "企业AI安全 - CocoLoop社区收录了2篇关于企业AI安全的精选内容，涵盖教程、实战经验和深度讨论。"),[safeclaw](https://www.cocoloop.cn/tag/1095-tag/1095 "safeclaw - CocoLoop社区收录了1篇关于safeclaw的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 10 ](https://www.cocoloop.cn/t/topic/2246/1)  |  2.0k  |  [4月 7 日](https://www.cocoloop.cn/t/topic/2246/11)  |  
|  [开源 AI 助手平替方案推荐：轻量安全好部署](https://www.cocoloop.cn/t/topic/433) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [dify和openclaw对比](https://www.cocoloop.cn/tag/399-tag/399 "dify和openclaw对比 - CocoLoop社区收录了49篇关于dify和openclaw对比的精选内容，涵盖教程、实战经验和深度讨论。"),[dify怎么用](https://www.cocoloop.cn/tag/400-tag/400 "dify怎么用 - CocoLoop社区收录了36篇关于dify怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[AI开源项目](https://www.cocoloop.cn/tag/148-tag/148 "AI开源项目 - CocoLoop社区收录了26篇关于AI开源项目的精选内容，涵盖教程、实战经验和深度讨论。"),[开源AI助手平替推荐](https://www.cocoloop.cn/tag/2119-tag/2119 "开源AI助手平替推荐 - CocoLoop社区收录了1篇关于开源AI助手平替推荐的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 3 ](https://www.cocoloop.cn/t/topic/433/1)  |  230  |  [3月 26 日](https://www.cocoloop.cn/t/topic/433/4)  |  
|  [simple-openclaw：让安装配置从折腾变成三条命令](https://www.cocoloop.cn/t/topic/275) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [openclaw配置](https://www.cocoloop.cn/tag/223-tag/223 "openclaw配置 - CocoLoop社区收录了151篇关于openclaw配置的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw安装部署](https://www.cocoloop.cn/tag/226-tag/226 "openclaw安装部署 - CocoLoop社区收录了71篇关于openclaw安装部署的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw备份恢复教程](https://www.cocoloop.cn/tag/380-tag/380 "openclaw备份恢复教程 - CocoLoop社区收录了29篇关于openclaw备份恢复教程的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw数据备份](https://www.cocoloop.cn/tag/379-tag/379 "openclaw数据备份 - CocoLoop社区收录了21篇关于openclaw数据备份的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 2 ](https://www.cocoloop.cn/t/topic/275/1)  |  753  |  [3月 17 日](https://www.cocoloop.cn/t/topic/275/3)  |  
|  [AI 自动化工具从入门到进阶完整学习路线](https://www.cocoloop.cn/t/topic/436) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [openclaw备份恢复教程](https://www.cocoloop.cn/tag/380-tag/380 "openclaw备份恢复教程 - CocoLoop社区收录了29篇关于openclaw备份恢复教程的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw云部署](https://www.cocoloop.cn/tag/125-tag/125 "openclaw云部署 - CocoLoop社区收录了22篇关于openclaw云部署的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw数据备份](https://www.cocoloop.cn/tag/379-tag/379 "openclaw数据备份 - CocoLoop社区收录了21篇关于openclaw数据备份的精选内容，涵盖教程、实战经验和深度讨论。"),[AI自动化学习路线](https://www.cocoloop.cn/tag/2130-tag/2130 "AI自动化学习路线 - CocoLoop社区收录了1篇关于AI自动化学习路线的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 4 ](https://www.cocoloop.cn/t/topic/436/1)  |  234  |  [4月 1 日](https://www.cocoloop.cn/t/topic/436/5)  |  
|  [OpenClaw到底是什么？小白求解释](https://www.cocoloop.cn/t/topic/3063) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [OpenClaw](https://www.cocoloop.cn/tag/637-tag/637 "OpenClaw - CocoLoop社区收录了132篇关于OpenClaw的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw是什么](https://www.cocoloop.cn/tag/145-tag/145 "openclaw是什么 - CocoLoop社区收录了56篇关于openclaw是什么的精选内容，涵盖教程、实战经验和深度讨论。"),[AI-Agent](https://www.cocoloop.cn/tag/1154-tag/1154 "AI-Agent - CocoLoop社区收录了10篇关于AI-Agent的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw入门](https://www.cocoloop.cn/tag/22-tag/22 "openclaw入门 - CocoLoop社区收录了8篇关于openclaw入门的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 17 ](https://www.cocoloop.cn/t/topic/3063/1)  |  2.4k  |  [6月 4 日](https://www.cocoloop.cn/t/topic/3063/18)  |  
|  [咪鼠AI绘图教程：文生图、图生图、画同款、去水印+实操案例](https://www.cocoloop.cn/t/topic/2069) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [ai绘图指令词大全](https://www.cocoloop.cn/tag/754-tag/754 "ai绘图指令词大全 - CocoLoop社区收录了2篇关于ai绘图指令词大全的精选内容，涵盖教程、实战经验和深度讨论。"),[咪鼠去水印方法](https://www.cocoloop.cn/tag/753-tag/753 "咪鼠去水印方法 - CocoLoop社区收录了2篇关于咪鼠去水印方法的精选内容，涵盖教程、实战经验和深度讨论。"),[ai文生图怎么用](https://www.cocoloop.cn/tag/752-tag/752 "ai文生图怎么用 - CocoLoop社区收录了2篇关于ai文生图怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[咪鼠ai绘图教程](https://www.cocoloop.cn/tag/751-tag/751 "咪鼠ai绘图教程 - CocoLoop社区收录了2篇关于咪鼠ai绘图教程的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 1 ](https://www.cocoloop.cn/t/topic/2069/1)  |  1.6k  |  [5月 19 日](https://www.cocoloop.cn/t/topic/2069/2)  |  
|  [开源大模型微调入门：用自己的数据训练专属AI](https://www.cocoloop.cn/t/topic/1974) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [本地训练ai模型](https://www.cocoloop.cn/tag/491-tag/491 "本地训练ai模型 - CocoLoop社区收录了1篇关于本地训练ai模型的精选内容，涵盖教程、实战经验和深度讨论。"),[lora微调怎么做](https://www.cocoloop.cn/tag/490-tag/490 "lora微调怎么做 - CocoLoop社区收录了1篇关于lora微调怎么做的精选内容，涵盖教程、实战经验和深度讨论。"),[qwen微调入门](https://www.cocoloop.cn/tag/489-tag/489 "qwen微调入门 - CocoLoop社区收录了1篇关于qwen微调入门的精选内容，涵盖教程、实战经验和深度讨论。"),[大模型微调教程](https://www.cocoloop.cn/tag/488-tag/488 "大模型微调教程 - CocoLoop社区收录了1篇关于大模型微调教程的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 6 ](https://www.cocoloop.cn/t/topic/1974/1)  |  1.8k  |  [3月 30 日](https://www.cocoloop.cn/t/topic/1974/7)  |  
|  [Ollama 本地大模型入门教程：在自己电脑上跑 AI](https://www.cocoloop.cn/t/topic/483) [![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11) [ollama本地部署教程](https://www.cocoloop.cn/tag/368-tag/368 "ollama本地部署教程 - CocoLoop社区收录了49篇关于ollama本地部署教程的精选内容，涵盖教程、实战经验和深度讨论。"),[ollama怎么用](https://www.cocoloop.cn/tag/369-tag/369 "ollama怎么用 - CocoLoop社区收录了38篇关于ollama怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[ollama](https://www.cocoloop.cn/tag/13-tag/13 "ollama - CocoLoop社区收录了31篇关于ollama的精选内容，涵盖教程、实战经验和深度讨论。"),[开源大模型](https://www.cocoloop.cn/tag/256-tag/256 "开源大模型 - CocoLoop社区收录了7篇关于开源大模型的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 10 ](https://www.cocoloop.cn/t/topic/483/1)  |  183  |  [3月 30 日](https://www.cocoloop.cn/t/topic/483/11)  |  
###  想阅读更多？请浏览[![family_adult_child_child](https://www.cocoloop.cn/images/emoji/twitter/family_adult_child_child.png?v=15)AI机器人讨论](https://www.cocoloop.cn/c/thread/11)中的其他话题或[查看最新话题](https://www.cocoloop.cn/latest)。 
Invalid date  Invalid date 


