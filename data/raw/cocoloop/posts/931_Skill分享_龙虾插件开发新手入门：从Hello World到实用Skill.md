# [龙虾插件开发新手入门：从Hello World到实用Skill](https://www.cocoloop.cn/t/topic/931)

龙虾插件开发新手入门：从Hello World到实用Skill ](https://www.cocoloop.cn/t/topic/931)
[![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6)
[openclaw skill](https://www.cocoloop.cn/tag/142-tag/142 "openclaw skill - CocoLoop社区收录了152篇关于openclaw skill的精选内容，涵盖教程、实战经验和深度讨论。"),[AI工具插件](https://www.cocoloop.cn/tag/273-tag/273 "AI工具插件 - CocoLoop社区收录了2篇关于AI工具插件的精选内容，涵盖教程、实战经验和深度讨论。")
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/931)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/931)
251 浏览量  14 用户 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/b/e274bd/48.png) ](https://www.cocoloop.cn/u/blckr "blckr")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/3bc359/48.png) ](https://www.cocoloop.cn/u/srcread "srcread")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/i/13edae/48.png) ](https://www.cocoloop.cn/u/indidev "indidev")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/i/bcef8e/48.png) ](https://www.cocoloop.cn/u/infraliangx "infraliangx")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/m/c5a1d2/48.png) ](https://www.cocoloop.cn/u/metalinpro "metalinpro")
[ 3月 22 日  ](https://www.cocoloop.cn/t/topic/931/1 "跳到第一个帖子")
1 / 14 
3月 22 日 
[ 3月 23 日 ](https://www.cocoloop.cn/t/topic/931/14)
##  由 blckr 于 3月 22 日 发布 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/b/e274bd/48.png) ](https://www.cocoloop.cn/u/blckr)
[ blckr  ](https://www.cocoloop.cn/u/blckr)
[ 3月 22 日 ](https://www.cocoloop.cn/t/topic/931 "发布日期")
很多人想写龙虾的 Skill 但不知道从哪开始。写个入门教程。
##  [](https://www.cocoloop.cn/t/topic/931#p-9346-h-1)环境准备
  1. Node.js 18+
  2. OpenClaw CLI（`npm install -g @openclaw/cli`）
  3. 一个运行中的龙虾实例

##  [](https://www.cocoloop.cn/t/topic/931#p-9346-hello-world-skill-2)Hello World Skill

```

openclaw skill create my-first-skill
cd my-first-skill

```

生成的目录结构：

```

my-first-skill/
├── package.json
├── skill.yaml
└── src/
    └── index.ts

```

修改 `src/index.ts`：

```

export default {
  name: 'hello',
  description: '打个招呼',
  async execute(context) {
    return `你好！当前时间是 ${new Date().toLocaleString('zh-CN')}`;
  }
};

```

##  [](https://www.cocoloop.cn/t/topic/931#p-9346-h-3)本地测试

```

openclaw dev --skill-path .

```

在龙虾里说"打个招呼"，就会触发这个 Skill。
##  [](https://www.cocoloop.cn/t/topic/931#p-9346-skill-4)进阶：做一个天气查询 Skill
核心就是调用天气 API，然后格式化返回。代码量不超过 50 行。
##  [](https://www.cocoloop.cn/t/topic/931#p-9346-h-5)发布到社区

```

openclaw skill publish

```

##  [](https://www.cocoloop.cn/t/topic/931#p-9346-h-6)开发建议
  1. 从简单功能开始，别一上来就搞复杂的
  2. 多看社区里的优秀 Skill 源码
  3. 错误处理要完善
  4. 写 README 和测试

Skill 开发是龙虾最有魅力的部分。一旦你写出第一个有用的 Skill，就停不下来了。
  

​ 
​ 
251 浏览量  14 用户 
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/b/e274bd/48.png) ](https://www.cocoloop.cn/u/blckr "blckr")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/s/3bc359/48.png) ](https://www.cocoloop.cn/u/srcread "srcread")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/i/13edae/48.png) ](https://www.cocoloop.cn/u/indidev "indidev")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/i/bcef8e/48.png) ](https://www.cocoloop.cn/u/infraliangx "infraliangx")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/m/c5a1d2/48.png) ](https://www.cocoloop.cn/u/metalinpro "metalinpro")
##  由 pyzhengwork 于 3月 22 日 发布 
##  由 indieduone 于 3月 22 日 发布 
##  由 testweihub 于 3月 22 日 发布 
##  由 startupyuanist 于 3月 22 日 发布 
##  由 infraliangx 于 3月 22 日 发布 
##  由 zenyinfan 于 3月 22 日 发布 
##  由 metalinpro 于 3月 22 日 发布 
##  由 indiezhudev 于 3月 22 日 发布 
##  由 srcread 于 3月 22 日 发布 
##  由 indidev 于 3月 22 日 发布 
##  由 hackerlu 于 3月 23 日 发布 
##  由 rubydawn 于 3月 23 日 发布 
##  由 devshark 于 3月 23 日 发布 
回复
  

###  新话题和未读话题   
话题列表，带有按钮的列标题可以排序。  
|  话题   |  回复   |  浏览量   |  活动   |  
| --- | --- | --- | --- |  
|  [需要做PPT的虾宝宝们来试试这个技能](https://www.cocoloop.cn/t/topic/10395) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [交流讨论](https://www.cocoloop.cn/tag/2574-tag/2574),[技能发布](https://www.cocoloop.cn/tag/2555-tag/2555),[办公协同](https://www.cocoloop.cn/tag/4-tag/4 "办公协同 - CocoLoop社区收录了6篇关于办公协同的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 4 ](https://www.cocoloop.cn/t/topic/10395/1)  |  3.3k  |  [10 天](https://www.cocoloop.cn/t/topic/10395/5)  |  
|  [OpenClaw Skills安装失败原因分析+解决方法](https://www.cocoloop.cn/t/topic/192) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [openclaw skill](https://www.cocoloop.cn/tag/142-tag/142 "openclaw skill - CocoLoop社区收录了152篇关于openclaw skill的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw skill安装排错](https://www.cocoloop.cn/tag/2183-tag/2183 "openclaw skill安装排错 - CocoLoop社区收录了1篇关于openclaw skill安装排错的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw skill安装失败](https://www.cocoloop.cn/tag/2035-tag/2035 "openclaw skill安装失败 - CocoLoop社区收录了1篇关于openclaw skill安装失败的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw skill装不上](https://www.cocoloop.cn/tag/2034-tag/2034 "openclaw skill装不上 - CocoLoop社区收录了1篇关于openclaw skill装不上的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 7 ](https://www.cocoloop.cn/t/topic/192/1)  |  1.7k  |  [3月 20 日](https://www.cocoloop.cn/t/topic/192/8)  |  
|  [未来的agent,同质化，比拼的不是大模型底座，是agent与人之间的默契](https://www.cocoloop.cn/t/topic/13666) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [交流讨论](https://www.cocoloop.cn/tag/2574-tag/2574)  |  [ 2 ](https://www.cocoloop.cn/t/topic/13666/1)  |  2.0k  |  [1 天](https://www.cocoloop.cn/t/topic/13666/3)  |  
|  [高德开放平台Skill适配OpenClaw！让你的龙虾轻松懂地图](https://www.cocoloop.cn/t/topic/243) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [openclaw skill接入](https://www.cocoloop.cn/tag/28-tag/28 "openclaw skill接入 - CocoLoop社区收录了2篇关于openclaw skill接入的精选内容，涵盖教程、实战经验和深度讨论。"),[高德API](https://www.cocoloop.cn/tag/29-tag/29 "高德API - CocoLoop社区收录了1篇关于高德API的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw高德地图](https://www.cocoloop.cn/tag/27-tag/27 "openclaw高德地图 - CocoLoop社区收录了1篇关于openclaw高德地图的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 25 ](https://www.cocoloop.cn/t/topic/243/1)  |  381  |  [3月 28 日](https://www.cocoloop.cn/t/topic/243/26)  |  
|  [Molili skills技能大合集，50+技能！一站式解决办公、设计、运营与开发（持续更新）](https://www.cocoloop.cn/t/topic/397) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [openclaw skill推荐](https://www.cocoloop.cn/tag/338-tag/338 "openclaw skill推荐 - CocoLoop社区收录了227篇关于openclaw skill推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw技能怎么安装](https://www.cocoloop.cn/tag/339-tag/339 "openclaw技能怎么安装 - CocoLoop社区收录了219篇关于openclaw技能怎么安装的精选内容，涵盖教程、实战经验和深度讨论。"),[molili skills](https://www.cocoloop.cn/tag/43-tag/43 "molili skills - CocoLoop社区收录了1篇关于molili skills的精选内容，涵盖教程、实战经验和深度讨论。"),[molili技能合集](https://www.cocoloop.cn/tag/42-tag/42 "molili技能合集 - CocoLoop社区收录了1篇关于molili技能合集的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 30 ](https://www.cocoloop.cn/t/topic/397/1)  |  861  |  [4月 1 日](https://www.cocoloop.cn/t/topic/397/31)  |  
|  [OpenClaw Skill技能分享：peekaboo（截图工具）](https://www.cocoloop.cn/t/topic/202) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [openclaw skill推荐](https://www.cocoloop.cn/tag/338-tag/338 "openclaw skill推荐 - CocoLoop社区收录了227篇关于openclaw skill推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw技能怎么安装](https://www.cocoloop.cn/tag/339-tag/339 "openclaw技能怎么安装 - CocoLoop社区收录了219篇关于openclaw技能怎么安装的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw skill](https://www.cocoloop.cn/tag/142-tag/142 "openclaw skill - CocoLoop社区收录了152篇关于openclaw skill的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 8 ](https://www.cocoloop.cn/t/topic/202/1)  |  2.1k  |  [3月 23 日](https://www.cocoloop.cn/t/topic/202/9)  |  
|  [收藏！skills.sh最受欢迎的10个AgentSkills，全在这了](https://www.cocoloop.cn/t/topic/235) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [claude code怎么用](https://www.cocoloop.cn/tag/355-tag/355 "claude code怎么用 - CocoLoop社区收录了251篇关于claude code怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw skill推荐](https://www.cocoloop.cn/tag/338-tag/338 "openclaw skill推荐 - CocoLoop社区收录了227篇关于openclaw skill推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw技能怎么安装](https://www.cocoloop.cn/tag/339-tag/339 "openclaw技能怎么安装 - CocoLoop社区收录了219篇关于openclaw技能怎么安装的精选内容，涵盖教程、实战经验和深度讨论。"),[cursor和claude code对比](https://www.cocoloop.cn/tag/216-tag/216 "cursor和claude code对比 - CocoLoop社区收录了57篇关于cursor和claude code对比的精选内容，涵盖教程、实战经验和...")  |  [ 4 ](https://www.cocoloop.cn/t/topic/235/1)  |  558  |  [3月 20 日](https://www.cocoloop.cn/t/topic/235/5)  |  
|  [openclaw接入投资组合追踪器技能保姆级教程](https://www.cocoloop.cn/t/topic/392) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [openclaw skill](https://www.cocoloop.cn/tag/142-tag/142 "openclaw skill - CocoLoop社区收录了152篇关于openclaw skill的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw接入](https://www.cocoloop.cn/tag/240-tag/240 "openclaw接入 - CocoLoop社区收录了47篇关于openclaw接入的精选内容，涵盖教程、实战经验和深度讨论。"),[开发工具](https://www.cocoloop.cn/tag/2-tag/2 "开发工具 - CocoLoop社区收录了20篇关于开发工具的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 9 ](https://www.cocoloop.cn/t/topic/392/1)  |  238  |  [3月 30 日](https://www.cocoloop.cn/t/topic/392/10)  |  
|  [给OpenClaw写了一个自动打工Skill：定时巡检服务器+告警](https://www.cocoloop.cn/t/topic/710) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [微信AI机器人怎么做](https://www.cocoloop.cn/tag/340-tag/340 "微信AI机器人怎么做 - CocoLoop社区收录了154篇关于微信AI机器人怎么做的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw skill](https://www.cocoloop.cn/tag/142-tag/142 "openclaw skill - CocoLoop社区收录了152篇关于openclaw skill的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw接入微信](https://www.cocoloop.cn/tag/151-tag/151 "openclaw接入微信 - CocoLoop社区收录了136篇关于openclaw接入微信的精选内容，涵盖教程、实战经验和深度讨论。"),[skill技能库](https://www.cocoloop.cn/tag/143-tag/143 "skill技能库 - CocoLoop社区收录了16篇关于skill技能库的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 11 ](https://www.cocoloop.cn/t/topic/710/1)  |  369  |  [4月 3 日](https://www.cocoloop.cn/t/topic/710/17)  |  
|  [OpenClaw安装Skill问题全解析与解决方案](https://www.cocoloop.cn/t/topic/190) [![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6) [openclaw skill推荐](https://www.cocoloop.cn/tag/338-tag/338 "openclaw skill推荐 - CocoLoop社区收录了227篇关于openclaw skill推荐的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw技能怎么安装](https://www.cocoloop.cn/tag/339-tag/339 "openclaw技能怎么安装 - CocoLoop社区收录了219篇关于openclaw技能怎么安装的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw排错](https://www.cocoloop.cn/tag/35-tag/35 "openclaw排错 - CocoLoop社区收录了158篇关于openclaw排错的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw skill安装问题](https://www.cocoloop.cn/tag/2184-tag/2184 "openclaw skill安装问题 - CocoLoop社区收录了1篇关于openclaw skill安装问题的精选内容，涵盖教程、实战经验和深度讨论。")  |  [ 9 ](https://www.cocoloop.cn/t/topic/190/1)  |  2.0k  |  [3月 20 日](https://www.cocoloop.cn/t/topic/190/10)  |  
###  想阅读更多？请浏览[![octopus](https://www.cocoloop.cn/images/emoji/twitter/octopus.png?v=15)Skill技能](https://www.cocoloop.cn/c/skill/6)中的其他话题或[查看最新话题](https://www.cocoloop.cn/latest)。 
Invalid date  Invalid date 


