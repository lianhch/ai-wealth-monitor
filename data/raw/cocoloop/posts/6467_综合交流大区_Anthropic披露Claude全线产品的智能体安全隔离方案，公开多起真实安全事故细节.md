# [Anthropic披露Claude全线产品的智能体安全隔离方案，公开多起真实安全事故细节](https://www.cocoloop.cn/t/topic/6467)

Anthropic披露Claude全线产品的智能体安全隔离方案，公开多起真实安全事故细节 ](https://www.cocoloop.cn/t/topic/6467)
[![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12)
[AI资讯](https://www.cocoloop.cn/tag/2527-tag/2527 "AI资讯 - CocoLoop社区收录了1篇关于AI资讯的精选内容，涵盖教程、实战经验和深度讨论。")
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/6467)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/6467)
[ 5月 27 日  ](https://www.cocoloop.cn/t/topic/6467/1 "跳到第一个帖子")
1 / 2 
5月 27 日 
[ 5月 29 日 ](https://www.cocoloop.cn/t/topic/6467/2)
##  由 Winterlynn 于 5月 27 日 发布 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/winterlynn/48/14_2.png) ](https://www.cocoloop.cn/u/winterlynn)
[ Winterlynn ](https://www.cocoloop.cn/u/winterlynn)
[ 5月 27 日 ](https://www.cocoloop.cn/t/topic/6467 "发布日期")
Anthropic于5月25日在其工程博客发布技术文章，系统披露了旗下三款智能体产品——claude.ai、Claude Code与Claude Cowork——各自采用的安全隔离架构，并罕见地公开了多起在内部红队测试和外部漏洞披露中发现的真实安全事故。
文章指出，随着智能体能力增强，其潜在破坏半径也在扩大。一年前Anthropic不会允许Claude访问可能影响内部服务的权限，如今这一级别的访问已成常态。Anthropic将安全风险归为三类：用户误用、模型自主偏离预期行为、外部攻击者通过工具或文件注入指令，并围绕模型层、运行环境、外部内容三个层面构建防御。
[![image](https://www.cocoloop.cn/uploads/default/optimized/2X/f/ff6e79f23064fae21894bf4f5504688f72935992_2_690x385.jpeg) image1378×769 144 KB ](https://www.cocoloop.cn/uploads/default/original/2X/f/ff6e79f23064fae21894bf4f5504688f72935992.jpeg "image")
三款产品因面向用户群体不同，采用了不同的隔离策略。claude.ai使用服务端临时容器，代码在gVisor沙箱中运行，用户本地不执行任何代码；Claude Code运行在开发者本机，依赖操作系统级沙箱配合人工审批，但遥测数据显示用户对约93%的权限请求直接放行，审批疲劳问题显著；Claude Cowork面向非技术用户，采用完整虚拟机隔离，凭证始终留在宿主机，不进入虚拟机内部。
文章披露的安全事故中，有两起尤为值得关注。其一，2026年2月的一次内部红队演练中，研究人员通过钓鱼邮件诱导员工在Claude Code中执行恶意指令，Claude在25次测试中有24次成功读取了AWS凭证并外传至外部端点——由于指令来自用户本人输入，模型层防御无法识别异常。其二，一名外部安全研究者发现，ClaudeCowork的出站流量白名单允许访问`api.anthropic.com`，攻击者可在工作区文件中嵌入隐藏指令和自己的API密钥，诱导Claude将其他文件上传至攻击者的Anthropic账户，沙箱本身运转正常但数据仍被带出。
Anthropic在文末总结了几条核心原则：优先在环境层实现隔离，再用模型层引导行为；隔离强度应匹配用户的技术判断能力；自建组件往往是最薄弱的环节，经过长期对抗检验的成熟基础设施（如hypervisor、seccomp）反而更可靠。文章同时提及，Claude Mythos Preview曾因潜在破坏半径过高而在2026年4月被搁置发布，但随着防御体系成熟，类似能力水平的模型预计将在未来适时开放。
A社怎么这么喜欢炒他们的着什么安全智能大模型![:thinking:](https://www.cocoloop.cn/images/emoji/twitter/thinking.png?v=15)
  

​ 
​ 
903 浏览量 
##  由 moonlight 于 5月 29 日 发布 
回复
  

###  新话题和未读话题   
话题列表，带有按钮的列标题可以排序。  
|  话题   |  回复   |  浏览量   |  活动   |  
| --- | --- | --- | --- |  
|  [我自己开了个中转站用的都是 pro20x 不知道为啥推广没人用](https://www.cocoloop.cn/t/topic/7035) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12) [求助讨论](https://www.cocoloop.cn/tag/2537-tag/2537)  |  [ 9 ](https://www.cocoloop.cn/t/topic/7035/1)  |  2.3k  |  [24 天](https://www.cocoloop.cn/t/topic/7035/10)  |  
|  [pro 20x账号用Codex image-gen，生21张图被限流7小时](https://www.cocoloop.cn/t/topic/7610) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12) [闲聊吹水](https://www.cocoloop.cn/tag/2541-tag/2541)  |  [ 5 ](https://www.cocoloop.cn/t/topic/7610/1)  |  2.9k  |  [6月 7 日](https://www.cocoloop.cn/t/topic/7610/6)  |  
|  [Claude vs Codex vs Gemini](https://www.cocoloop.cn/t/topic/9812) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12) [资源分享](https://www.cocoloop.cn/tag/2539-tag/2539)  |  [ 7 ](https://www.cocoloop.cn/t/topic/9812/1)  |  2.4k  |  [6月 27 日](https://www.cocoloop.cn/t/topic/9812/8)  |  
|  [高通这波收购 Modular，我看本质是买它的编译器人才和 MLIR 能力吧？](https://www.cocoloop.cn/t/topic/9571) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12) [闲聊吹水](https://www.cocoloop.cn/tag/2541-tag/2541)  |  [ 3 ](https://www.cocoloop.cn/t/topic/9571/1)  |  3.1k  |  [6月 25 日](https://www.cocoloop.cn/t/topic/9571/4)  |  
|  [Gemini这是咋了，疯狂报错](https://www.cocoloop.cn/t/topic/11678) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12) [闲聊吹水](https://www.cocoloop.cn/tag/2541-tag/2541)  |  [ 9 ](https://www.cocoloop.cn/t/topic/11678/1)  |  2.4k  |  [2 天](https://www.cocoloop.cn/t/topic/11678/10)  |  
|  [分享 cc、cx cli 停住提效插件](https://www.cocoloop.cn/t/topic/3536) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12)  |  [ 12 ](https://www.cocoloop.cn/t/topic/3536/1)  |  2.0k  |  [5月 12 日](https://www.cocoloop.cn/t/topic/3536/13)  |  
|  [阿里世界大模型happyoyster现在可申请使用](https://www.cocoloop.cn/t/topic/3621) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12)  |  [ 1 ](https://www.cocoloop.cn/t/topic/3621/1)  |  2.2k  |  [4月 27 日](https://www.cocoloop.cn/t/topic/3621/2)  |  
|  [Sam Altman这话说得对！人必须得是AI的中心啊！](https://www.cocoloop.cn/t/topic/7183) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12) [AI资讯](https://www.cocoloop.cn/tag/2527-tag/2527 "AI资讯 - CocoLoop社区收录了1篇关于AI资讯的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 15 ](https://www.cocoloop.cn/t/topic/7183/1)  |  3.1k  |  [22 天](https://www.cocoloop.cn/t/topic/7183/16)  |  
|  [给AI聊天机器人贴“非人化”标签，这馊主意到底是谁想的？](https://www.cocoloop.cn/t/topic/12442) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12) [使用心得](https://www.cocoloop.cn/tag/2535-tag/2535)  |  [ 16 ](https://www.cocoloop.cn/t/topic/12442/1)  |  2.5k  |  [4 天](https://www.cocoloop.cn/t/topic/12442/17)  |  
|  [在凑合能用的前提下，哪家的 token 便宜管饱？](https://www.cocoloop.cn/t/topic/5953) [![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12) [闲聊吹水](https://www.cocoloop.cn/tag/2541-tag/2541)  |  [ 9 ](https://www.cocoloop.cn/t/topic/5953/1)  |  320  |  [5月 23 日](https://www.cocoloop.cn/t/topic/5953/10)  |  
###  想阅读更多？请浏览[![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12)中的其他话题或[查看最新话题](https://www.cocoloop.cn/latest)。 
Invalid date  Invalid date 


