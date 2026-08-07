# [聊聊复杂功能时我的vibe coding实践流程](https://www.cocoloop.cn/t/topic/6714)

聊聊复杂功能时我的vibe coding实践流程 ](https://www.cocoloop.cn/t/topic/6714)
[![spouting_whale](https://www.cocoloop.cn/images/emoji/twitter/spouting_whale.png?v=15)综合交流大区](https://www.cocoloop.cn/c/discussions/12)
[使用心得](https://www.cocoloop.cn/tag/2535-tag/2535)
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/6714)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/6714)
[ 5月 29 日  ](https://www.cocoloop.cn/t/topic/6714/1 "跳到第一个帖子")
1 / 24 
5月 29 日 
[ 6月 19 日 ](https://www.cocoloop.cn/t/topic/6714/24)
##  由 backendweione 于 5月 29 日 发布 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/b/b19c9b/48.png) ](https://www.cocoloop.cn/u/backendweione)
[ backendweione  ](https://www.cocoloop.cn/u/backendweione)
1
[ 5月 29 日 ](https://www.cocoloop.cn/t/topic/6714 "发布日期")
vibe coding玩上瘾之后，感觉就是惊喜来得快，但麻烦来得更快。
最明显的问题就是vibe几分钟，review几小时。除了玩具小项目能一把梭，很多质量要求高的复杂功能，vibe花的时间其实不比手写少多少。
为了省点token、提点效率、结果也能靠谱点，试了不少方法。最近摸出来一套感觉还行的流程，到26年5月为止我自己觉得可行，发出来大家看看。
  1. 先用网页版，找gpt-5.5pro（进阶专业版）把需求聊透，让它出个prd或者开发文档初稿。  
理由：这版本现在想东西挺深的，搜东西也强，容易帮你找到功能的最佳实践路子，文档逻辑也清楚，适合打底子。
  2. 把文档扔进cc，用mattpocock那个grill with doc skills去审这个prd。问它几十个问题，让它自动更新文档，这样prd的落地性就能有个七八成了（这里用codex也行，但mattpocock在cc里适配更好点）。
  3. 让cc和cx交叉审一遍prd，定下最终执行稿。自己看看测试覆盖全了没，要是token多可以用superpowers的writing-plan skill搞执行方案。这一步可做可不做，因为有时候计划写太长反而容易走神，效果更差。
  4. 白天忙完前期准备，晚上睡觉前，打开codex选/goal，把prd扔进去，告诉它“用agent团队并行开发所有任务”。然后早上起来就能收菜了。
  5. 目前我实测/goal的完成率大概七八成，所以还得至少两轮review，分粗筛和细筛：  
用cc开deepseek看看进度——codex补缺。deepseek再review，codex修。codex打包传给网页版gpt5.5pro review，codex再修。cc/cx交叉核验（可选），最后人工收尾或者提pr。

我个人体验，按这套走，一轮开发大概2天：第一天规划，半夜写代码，第二天review。能达到的效果差不多是以前15到30人天的开发量，结果还相对稳。
这里几个关键：多蹭gpt-pro的能力，它确实和现在主力模型有代差。善用skill细化流程保证能落地，还有“人”自己的判断力不能丢。
传统单平台或者单模型那套plan-coding-review流程，做做web玩具、改点小功能没问题，一遇到复杂重构或者要探索新功能就抓瞎。
所以大家也说说自己的最佳实践，互相参考下。
补充几点：  
一、这套操作核心是用流程+token换相对确定的结果，人还能处在专注度可用的自由状态里。不太累+不太费时+结果可控。而且要把功能拆成批次循环搞。
二、我测下来的等效价值是2天顶15-30人天有效产能。所以模块功能切分最好也按这个来。原来你30天能做多少功能，就塞到一个轮次里，别塞太多，专注度和效果会打折；也别塞太少，小功能不值得这么复杂流程。  
vibe coding现在最大毛病就是两极分化：要么完全放养，结果只能搓玩具；要么信息给不够，你都用上AI了，原来两天干完的活现在还要两天，那折腾AI图啥？
三、工具和模型组合受token成本和个人专注度限制。我属于半摸鱼开发，确实没法随时进心流，一天高度专注也就一两个小时，所以也没必要多开并发。  
这套流程跑下来，含方案梳理+代码实现+review，两天总计token数大概5到8亿。如果有专注度更强的老哥，效果肯定更好，所以我说的等效人天也是动态的。
  

4 个回复
​ 
​ 
2.3k 浏览量  24 用户 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/strmz/48/1149_2.png) ](https://www.cocoloop.cn/u/strmz "strmz")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/47e85d/48.png) ](https://www.cocoloop.cn/u/srechengrun "srechengrun")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/t/5daacb/48.png) ](https://www.cocoloop.cn/u/techzhoupro "techzhoupro")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/m/ee59a6/48.png) ](https://www.cocoloop.cn/u/makerhuangdev "makerhuangdev")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/g/eada6e/48.png) ](https://www.cocoloop.cn/u/gitdengcode "gitdengcode")
##  由 srechengrun 于 5月 29 日 发布 
##  由 gitdengcode 于 5月 29 日 发布 
##  由 syschenglab 于 5月 29 日 发布 
##  由 strmz 于 5月 29 日 发布 
##  由 cloud_walker 于 5月 29 日 发布 
##  由 archbaigo 于 5月 29 日 发布 
##  由 techzhoupro 于 5月 29 日 发布 
##  由 wanglaoshi6 于 5月 29 日 发布 
##  由 makerhuangdev 于 5月 29 日 发布 
##  由 botshitech 于 5月 29 日 发布 
##  由 tako_dev 于 5月 29 日 发布 
##  由 vimgod 于 5月 30 日 发布 
##  由 lazycat99 于 5月 31 日 发布 
##  由 mintyz 于 5月 31 日 发布 
##  由 mochaqi 于 6月 1 日 发布 
##  由 lin_zhe 于 6月 7 日 发布 
##  由 guxiaobei 于 6月 7 日 发布 
##  由 byteshizhi 于 6月 7 日 发布 
##  由 vibe_menger 于 6月 8 日 发布 
##  加载下方更多帖子 
Invalid date  Invalid date 


