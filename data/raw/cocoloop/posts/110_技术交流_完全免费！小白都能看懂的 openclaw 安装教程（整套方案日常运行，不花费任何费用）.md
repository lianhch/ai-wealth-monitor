# [完全免费！小白都能看懂的 openclaw 安装教程（整套方案日常运行，不花费任何费用）](https://www.cocoloop.cn/t/topic/110)

完全免费！小白都能看懂的 openclaw 安装教程（整套方案日常运行，不花费任何费用） ](https://www.cocoloop.cn/t/topic/110)
[![jellyfish](https://www.cocoloop.cn/images/emoji/twitter/jellyfish.png?v=15)技术交流](https://www.cocoloop.cn/c/general/4)
[claude code怎么用](https://www.cocoloop.cn/tag/355-tag/355 "claude code怎么用 - CocoLoop社区收录了251篇关于claude code怎么用的精选内容，涵盖教程、实战经验和深度讨论。"),[claude code教程](https://www.cocoloop.cn/tag/206-tag/206 "claude code教程 - CocoLoop社区收录了245篇关于claude code教程的精选内容，涵盖教程、实战经验和深度讨论。"),[windows部署openclaw](https://www.cocoloop.cn/tag/353-tag/353 "windows部署openclaw - CocoLoop社区收录了157篇关于windows部署openclaw的精选内容，涵盖教程、实战经验和深度讨论。"),[openclaw windows安装](https://www.cocoloop.cn/tag/101-tag/101 "openclaw windows安装 - CocoLoop社区收录了158篇关于openclaw windows安装的精选内容，涵盖教程、实战经验和深度讨论。")
您已选择 **0** 个帖子。
[ 全选 ](https://www.cocoloop.cn/t/topic/110)
[ 取消选择 ](https://www.cocoloop.cn/t/topic/110)
[ 3月 13 日  ](https://www.cocoloop.cn/t/topic/110/1 "跳到第一个帖子")
1 / 61 
3月 13 日 
[ 3月 23 日 ](https://www.cocoloop.cn/t/topic/110/61)
##  由 Arya 于 3月 13 日 发布 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/arya/48/481_2.png) ](https://www.cocoloop.cn/u/arya)
[ Arya  ](https://www.cocoloop.cn/u/arya)
1
[ 3月 13 日 ](https://www.cocoloop.cn/t/topic/110 "发布日期")
虽说是小白都会的教程，但是仍然需要我的读者熟练掌握如下技能：
  * 会开机关机 Windows
  * 会操作键盘和鼠标
  * 有汉字和少许英文的基本阅读能力
  * 知道如何打开 Windows 的命令行终端
  * 具备多模态识别能力（说人话：能看懂我的截图在说什么）
  * 看得懂我的笑话和梗图

废话不多说，直接开搞。AI时代的博客会发生巨大的不同。从下面第一步操作开始就是。
##  [](https://www.cocoloop.cn/t/topic/110#p-682-qwen-claude-code-1)第一步. 安装你的万能助手 qwen 或者claude code
这是一个本地的AI助手，可以通过比你聪明1万倍的方法操作本地的终端1秒钟写出1万行你看不懂的代码来快速调度你计算机的资源。有了它，你就再也不用担心网上那些大佬贴出来的的代码为什么在你的本地报运行之后会出现1万个报错。这些AI助手都会帮你自动解决。
> 当然，不要让它帮你清理磁盘！！小心删库跑路！！
目前主流的可以跑在终端上的助手有 qwen，claude code，codex 和 opencode，中间要两个要收费，旁边两个部分免费。
因为 qwen 每天有2000次免费的使用次数，所以我优先说如何安装 qwen。
为了让 qwen 这样的AI助手可以运行，我们首先需要安装基础的编程环境 [nodejs]，自己去 B站 上搜【如何安装 NodeJS】即可，你随便找个高赞的点进去安装就完事。注意，我们一定要安装 node22 或者 node24（不要安装别的版本！！！）：
[![image](https://www.cocoloop.cn/uploads/default/original/1X/3c4a22dab8c5b5eb541bc77d5a926b106689958b.jpeg) image690×395 102 KB ](https://www.cocoloop.cn/uploads/default/original/1X/3c4a22dab8c5b5eb541bc77d5a926b106689958b.jpeg "image")
相信你在安装的过程中一定知道了如何打开命令行终端对吧？
打开命令行，输入下面的命令安装 qwen

```

npm install -g @qwen-code/qwen-code@latest

```

安装完成后，直接按下 qwen 进入助手对话框，然后选择第一个认证方式 Qwen OAuth，按下回车
[![image](https://www.cocoloop.cn/uploads/default/original/1X/3bdb71420ab0f198aa5a8b98beee7c65492c8b46.jpeg) image690×420 72.7 KB ](https://www.cocoloop.cn/uploads/default/original/1X/3bdb71420ab0f198aa5a8b98beee7c65492c8b46.jpeg "image")
然后会跳出一个链接和一个二维码，将链接扔进浏览器中选择账号进行登录即可（我选的是 github 账号）。
[![image](https://www.cocoloop.cn/uploads/default/original/1X/a9a8e662d01279dd99d2b40d582f94af2b64a84f.png) image602×500 21.4 KB ](https://www.cocoloop.cn/uploads/default/original/1X/a9a8e662d01279dd99d2b40d582f94af2b64a84f.png "image")
登录完成后回到命令行，qwen 助手就可以使用了。
此时按下 shift + tab，输入框会从蓝色变成红色，意味着 YOLO 模式被激活（全自动执行模式，完全不需要你操心）
[![image](https://www.cocoloop.cn/uploads/default/original/1X/868b67dc59631d08472444f0b3560a59562b7377.jpeg) image690×298 64.5 KB ](https://www.cocoloop.cn/uploads/default/original/1X/868b67dc59631d08472444f0b3560a59562b7377.jpeg "image")
如果你已经成功完成了第一步，那么恭喜你，游戏已经结束了。
##  [](https://www.cocoloop.cn/t/topic/110#p-682-cmake-2)**第二步. 安装cmake
在 qwen 里面输入
【请帮我安装 cmake 并暴露到当前的环境变量中，并帮我验证】
然后按下回车。
##  [](https://www.cocoloop.cn/t/topic/110#p-682-openclaw-3)**第三步. 安装 openclaw**
在 qwen 里面输入
【阅读 <https://openclaw.ai/> 后，帮我使用 npm 全局安装 openclaw，并帮我验证】
然后按下回车。
* * *
##  [](https://www.cocoloop.cn/t/topic/110#p-682-openclaw-4)**配置 openclaw**
好，openclaw 安装完成。
后面就是配置 openclaw 了，在命令行输入

```

openclaw onboard

```

等待一会儿进入 openclaw 配置页面
[![image](https://www.cocoloop.cn/uploads/default/original/1X/f6f459dd3b4ffa20c49eb95ab578cd26155df007.jpeg) image690×420 69.1 KB ](https://www.cocoloop.cn/uploads/default/original/1X/f6f459dd3b4ffa20c49eb95ab578cd26155df007.jpeg "image")
通过上下左右方向键选择选项，按下回车确认，懂？
选择 Yes, QuickStart, Qwen（你也可以选择别的模型，qwen 单纯配置容易）
[![image](https://www.cocoloop.cn/uploads/default/original/1X/35a857a2895649a7fe6c2b4e746203603faeffe8.jpeg) image690×226 38.2 KB ](https://www.cocoloop.cn/uploads/default/original/1X/35a857a2895649a7fe6c2b4e746203603faeffe8.jpeg "image")
还是一样，进入上面链接进行认证，然后，还是和上面一样的操作，完成登录认证。
然后选 Keep current
然后选择社交媒体，国内用户选择Feishu/Lark (飞书)
[![image](https://www.cocoloop.cn/uploads/default/original/1X/c778041de5a6b3df1d3c3645c698c4501c7d3f53.jpeg) image685×500 73 KB ](https://www.cocoloop.cn/uploads/default/original/1X/c778041de5a6b3df1d3c3645c698c4501c7d3f53.jpeg "image")
后面一路选择默认的回车，直到遇到下面这个
[![image](https://www.cocoloop.cn/uploads/default/original/1X/deeb290712e6a99693f8eb0bda5a6fda114435bb.jpeg) image690×422 79.1 KB ](https://www.cocoloop.cn/uploads/default/original/1X/deeb290712e6a99693f8eb0bda5a6fda114435bb.jpeg "image")
接下来我们就需要依靠飞书的强大平台能力了。
你首先需要先下载并创建对应的飞书账号，然后创建组织，这一套都是基本流程了。不懂的朋友请自行查看飞书的基本使用方法。
完成上面的一系列操作之后，让你的客户端和浏览器的飞书各个应用都登录你当前的组织和账号，点击 [飞书开放平台]进入飞书开发者平台。点击右上角的开发者后台。选择机器人
[![image](https://www.cocoloop.cn/uploads/default/original/1X/2d599d6147aedf7fd82082d1ac998b630bd1a094.png) image690×394 23 KB ](https://www.cocoloop.cn/uploads/default/original/1X/2d599d6147aedf7fd82082d1ac998b630bd1a094.png "image")
简单配置一下介绍和头像
[![image](https://www.cocoloop.cn/uploads/default/original/1X/97b06f30c7eb6f11af8be8d1e5a7e02b27e681c2.jpeg) image690×395 49.2 KB ](https://www.cocoloop.cn/uploads/default/original/1X/97b06f30c7eb6f11af8be8d1e5a7e02b27e681c2.jpeg "image")
然后点击【权限管理】->【批量导入/导出权限】
[![image](https://www.cocoloop.cn/uploads/default/original/1X/97b06f30c7eb6f11af8be8d1e5a7e02b27e681c2.jpeg) image690×395 49.2 KB ](https://www.cocoloop.cn/uploads/default/original/1X/97b06f30c7eb6f11af8be8d1e5a7e02b27e681c2.jpeg "image")
会弹出一个导入窗口
[![image](https://www.cocoloop.cn/uploads/default/original/1X/8e16cfd4e4d7439c7dec2984a374e25ba0d2057d.png) image690×461 19.8 KB ](https://www.cocoloop.cn/uploads/default/original/1X/8e16cfd4e4d7439c7dec2984a374e25ba0d2057d.png "image")
把里面的内容全部删除，然后把下面的这一坨东西复制后粘贴进去。

```

{
  "scopes": {
    "tenant": [
      "aily:file:read",
      "aily:file:write",
      "application:application.app_message_stats.overview:readonly",
      "application:application:self_manage",
      "application:bot.menu:write",
      "base:app:copy",
      "base:app:create",
      "base:app:read",
      "base:app:update",
      "base:collaborator:create",
      "base:collaborator:delete",
      "base:collaborator:read",
      "base:dashboard:copy",
      "base:dashboard:read",
      "base:field:create",
      "base:field:delete",
      "base:field:read",
      "base:field:update",
      "base:form:read",
      "base:form:update",
      "base:record:create",
      "base:record:delete",
      "base:record:read",
      "base:record:retrieve",
      "base:record:update",
      "base:role:create",
      "base:role:delete",
      "base:role:read",
      "base:role:update",
      "base:table:create",
      "base:table:delete",
      "base:table:read",
      "base:table:update",
      "base:view:read",
      "base:view:write_only",
      "base:workflow:read",
      "base:workflow:write",
      "bitable:app",
      "bitable:app:readonly",
      "calendar:room:readonly",
      "contact:user.assign_info:read",
      "contact:user.base:readonly",
      "contact:user.department:readonly",
      "contact:user.dotted_line_leader_info.read",
      "contact:user.email:readonly",
      "contact:user.employee:readonly",
      "contact:user.employee_id:readonly",
      "contact:user.employee_number:read",
      "contact:user.gender:readonly",
      "contact:user.id:readonly",
      "contact:user.job_family:readonly",
      "contact:user.job_level:readonly",
      "contact:user.phone:readonly",
      "contact:user.subscription_ids:write",
      "contact:user.user_geo",
      "corehr:file:download",
      "docs:doc",
      "docs:doc:readonly",
      "docs:document.comment:create",
      "docs:document.comment:read",
      "docs:document.comment:update",
      "docs:document.comment:write_only",
      "docs:document.content:read",
      "docs:document.media:download",
      "docs:document.media:upload",
      "docs:document.subscription",
      "docs:document.subscription:read",
      "docs:document:copy",
      "docs:document:export",
      "docs:document:import",
      "event:ip_list",
      "im:app_feed_card:write",
      "im:biz_entity_tag_relation:read",
      "im:biz_entity_tag_relation:write",
      "im:chat",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.announcement:read",
      "im:chat.announcement:write_only",
      "im:chat.chat_pins:read",
      "im:chat.chat_pins:write_only",
      "im:chat.collab_plugins:read",
      "im:chat.collab_plugins:write_only",
      "im:chat.managers:write_only",
      "im:chat.members:bot_access",
      "im:chat.members:read",
      "im:chat.members:write_only",
      "im:chat.menu_tree:read",
      "im:chat.menu_tree:write_only",
      "im:chat.moderation:read",
      "im:chat.tabs:read",
      "im:chat.tabs:write_only",
      "im:chat.top_notice:write_only",
      "im:chat.widgets:read",
      "im:chat.widgets:write_only",
      "im:chat:create",
      "im:chat:delete",
      "im:chat:moderation:write_only",
      "im:chat:operate_as_owner",
      "im:chat:read",
      "im:chat:readonly",
      "im:chat:update",
      "im:datasync.feed_card.time_sensitive:write",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.group_msg",
      "im:message.p2p_msg:readonly",
      "im:message.pins:read",
      "im:message.pins:write_only",
      "im:message.reactions:read",
      "im:message.reactions:write_only",
      "im:message.urgent",
      "im:message.urgent.status:write",
      "im:message.urgent:phone",
      "im:message.urgent:sms",
      "im:message:readonly",
      "im:message:recall",
      "im:message:send_as_bot",
      "im:message:send_multi_depts",
      "im:message:send_multi_users",
      "im:message:send_sys_msg",
      "im:message:update",
      "im:resource",
      "im:tag:read",
      "im:tag:write",
      "im:url_preview.update",
      "im:user_agent:read",
      "vc:meeting.all_meeting:readonly",
      "vc:meeting:readonly"
    ],
    "user": [
      "aily:file:read",
      "aily:file:write",
      "base:app:copy",
      "base:app:create",
      "base:app:read",
      "base:app:update",
      "bitable:app",
      "bitable:app:readonly",
      "contact:user.assign_info:read",
      "contact:user.base:readonly",
      "contact:user.department:readonly",
      "contact:user.department_path:readonly",
      "contact:user.dotted_line_leader_info.read",
      "contact:user.email:readonly",
      "contact:user.employee:readonly",
      "contact:user.employee_id:readonly",
      "contact:user.employee_number:read",
      "contact:user.gender:readonly",
      "contact:user.id:readonly",
      "contact:user.job_family:readonly",
      "contact:user.job_level:readonly",
      "contact:user.phone:readonly",
      "contact:user.subscription_ids:write",
      "contact:user.user_geo",
      "contact:user:search",
      "docs:doc",
      "docs:doc:readonly",
      "docs:document.comment:create",
      "docs:document.comment:read",
      "docs:document.comment:update",
      "docs:document.comment:write_only",
      "docs:document.content:read",
      "docs:document.media:download",
      "docs:document.media:upload",
      "docs:document.subscription",
      "docs:document.subscription:read",
      "docs:document:copy",
      "docs:document:export",
      "docs:document:import",
      "im:chat",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.announcement:read",
      "im:chat.announcement:write_only",
      "im:chat.chat_pins:read",
      "im:chat.chat_pins:write_only",
      "im:chat.collab_plugins:read",
      "im:chat.collab_plugins:write_only",
      "im:chat.managers:write_only",
      "im:chat.members:read",
      "im:chat.members:write_only",
      "im:chat.moderation:read",
      "im:chat.tabs:read",
      "im:chat.tabs:write_only",
      "im:chat.top_notice:write_only",
      "im:chat:delete",
      "im:chat:moderation:write_only",
      "im:chat:read",
      "im:chat:readonly",
      "im:chat:update",
      "im:message",
      "im:message.pins:read",
      "im:message.pins:write_only",
      "im:message.reactions:read",
      "im:message.reactions:write_only",
      "im:message.urgent.status:write",
      "im:message:readonly",
      "im:message:recall",
      "im:message:update"
    ]
  }
}

```

然后一路点击申请或者确认。
然后点击创建版本
[![image](https://www.cocoloop.cn/uploads/default/original/1X/ffd5408fd18a145f2377ae1f085111eeb0cdcced.png) image690×395 22.3 KB ](https://www.cocoloop.cn/uploads/default/original/1X/ffd5408fd18a145f2377ae1f085111eeb0cdcced.png "image")
[![image](https://www.cocoloop.cn/uploads/default/original/1X/6bcdc79e417a25fc5646d6796a97904139b07f49.png) image690×394 24.1 KB ](https://www.cocoloop.cn/uploads/default/original/1X/6bcdc79e417a25fc5646d6796a97904139b07f49.png "image")
一路滚到最下面点击保存，然后点击申请审批，然后让组织的管理员审批一下，下面是管理员视角：
[![image](https://www.cocoloop.cn/uploads/default/original/1X/0ef94fd807c6b9de5cef48af0f36873a8fbc3a0f.png) image690×413 29.1 KB ](https://www.cocoloop.cn/uploads/default/original/1X/0ef94fd807c6b9de5cef48af0f36873a8fbc3a0f.png "image")
[![image](https://www.cocoloop.cn/uploads/default/original/1X/4a64181e29af4aa253c8aa3303081e8f0af4f2d4.png) image690×214 12.5 KB ](https://www.cocoloop.cn/uploads/default/original/1X/4a64181e29af4aa253c8aa3303081e8f0af4f2d4.png "image")
[![image](https://www.cocoloop.cn/uploads/default/original/1X/e73e0679c53fc774845971ccbb269d421fa14f85.png) image690×407 19.5 KB ](https://www.cocoloop.cn/uploads/default/original/1X/e73e0679c53fc774845971ccbb269d421fa14f85.png "image")
然后我们在飞书创建一个群聊：
[![image](https://www.cocoloop.cn/uploads/default/original/1X/94750a82d910628011c53a8e62e11f60106ef1c3.jpeg) image252×499 41.5 KB ](https://www.cocoloop.cn/uploads/default/original/1X/94750a82d910628011c53a8e62e11f60106ef1c3.jpeg "image")
点击设置：
[![image](https://www.cocoloop.cn/uploads/default/original/1X/fe914ae0480b934ebe051e945b1ba7cc92a56c2d.png) image554×397 17.8 KB ](https://www.cocoloop.cn/uploads/default/original/1X/fe914ae0480b934ebe051e945b1ba7cc92a56c2d.png "image")
点击群机器人
[![image](https://www.cocoloop.cn/uploads/default/original/1X/dea7af18e4f7cf93f02fc42076ff49da39367dc3.png) image278×499 8.83 KB ](https://www.cocoloop.cn/uploads/default/original/1X/dea7af18e4f7cf93f02fc42076ff49da39367dc3.png "image")
添加我们刚刚创建的机器人
[![image](https://www.cocoloop.cn/uploads/default/original/1X/8f17a061e31ab78de4ac42a6c75ccebd109b1f70.jpeg) image690×455 47 KB ](https://www.cocoloop.cn/uploads/default/original/1X/8f17a061e31ab78de4ac42a6c75ccebd109b1f70.jpeg "image")
ok，完成后，我们回到开发者平台，点击【凭证与基础信息】
[![image](https://www.cocoloop.cn/uploads/default/original/1X/91439efd98bf884fc8aa37b5da50024a966c4761.png) image690×395 23.2 KB ](https://www.cocoloop.cn/uploads/default/original/1X/91439efd98bf884fc8aa37b5da50024a966c4761.png "image")
右侧有一个 AppID 和 App Secret，分别复制并按照要求粘贴到 openclaw 的配置页面：
[![image](https://www.cocoloop.cn/uploads/default/original/1X/e0e317a77250c273d4c62745ba076616c64eb9d0.jpeg) image690×484 65.6 KB ](https://www.cocoloop.cn/uploads/default/original/1X/e0e317a77250c273d4c62745ba076616c64eb9d0.jpeg "image")
后续分别选择 Feishu- China 和 Open - respond in all groups (requires mention)
加油，就快完成了！
只差临门一脚，openclaw 本质是一个大模型的网关，其本身并不具备任何的Agent 的能力。所以我们还需要为它配置一些基础的技能包，让它可以执行更加复杂的操作。
所以下一个选择 yes，然后可以自由配置一些技能组，下面分享一下我自己配置的：
  * himalaya：让AI可以自由的管理你的邮箱。
  * mcporter：让AI可以自由快速MCP服务器，你只需要简单理解为可以给 AI 外挂更加强大的功能。理论上可以接管任何通过电脑接管到的虚拟世界和物理世界。
  * nano-pdf：让AI可以阅读你上传的PDF文件。
  * summarize：让AI可以总结你分享在群聊中的网页，本地文件或者是一些社交媒体。

然后一路回车即可。
这几个国外的服务可以暂时全部选择 No，需要的时候，后面再回来配置就行。
[![image](https://www.cocoloop.cn/uploads/default/original/1X/70b0198327215574f8b324eb39977a72e3625e16.jpeg) image676×500 78.2 KB ](https://www.cocoloop.cn/uploads/default/original/1X/70b0198327215574f8b324eb39977a72e3625e16.jpeg "image")
生命周期事件我选择的是如下的几个：
[![image](https://www.cocoloop.cn/uploads/default/original/1X/377def498e423b23f9d53a7f86a84200ad6d2c51.png) image690×217 25.5 KB ](https://www.cocoloop.cn/uploads/default/original/1X/377def498e423b23f9d53a7f86a84200ad6d2c51.png "image")
AI 管理模块我选择的是 [TUI]，如果你当前安装 openclaw的机器和你当前的PC机在同一个局域网内，那么你可以选择第二个。
[![image](https://www.cocoloop.cn/uploads/default/original/1X/377def498e423b23f9d53a7f86a84200ad6d2c51.png) image690×217 25.5 KB ](https://www.cocoloop.cn/uploads/default/original/1X/377def498e423b23f9d53a7f86a84200ad6d2c51.png "image")
等待初始化完成后，你就能看到如下的东西：
[![image](https://www.cocoloop.cn/uploads/default/original/1X/8ec22f8906616ae9a680423be84dd81f823940b2.jpeg) image690×328 65.8 KB ](https://www.cocoloop.cn/uploads/default/original/1X/8ec22f8906616ae9a680423be84dd81f823940b2.jpeg "image")
只差最后一步，我们就可以彻底完成配置了。现在懵懂的AI已经初醒，它想要知道一些基础的信息，我们只需要回答它就行了。下面是我的回答：

```

你是 Tiphareth，你是冷静睿智的助手，我是锦恢，你的搭档。
你是我的助手，你可以直接在飞书里 @我 或者通过邮箱 xxx 来给我发送消息。
我们所在的时区是北京时区。

```

[![image](https://www.cocoloop.cn/uploads/default/original/1X/d7b19390d83515bdb662d4d57583de77d122b372.jpeg) image690×369 61.5 KB ](https://www.cocoloop.cn/uploads/default/original/1X/d7b19390d83515bdb662d4d57583de77d122b372.jpeg "image")
现在配置完成了。
然后按两次 Ctrl C 退出对话框，重启 openclaw：

```

openclaw gateway restart

```

进入飞书开发者平台，我们还需要为 AI 创建接受和发送消息的信道，点击【事件与回调】，点击订阅方式右侧的笔按钮，选择长连接，点击保存
[![image](https://www.cocoloop.cn/uploads/default/original/1X/590de2029258b8cb9c681e3bc9f738499f8a48ad.jpeg) image690×394 44.1 KB ](https://www.cocoloop.cn/uploads/default/original/1X/590de2029258b8cb9c681e3bc9f738499f8a48ad.jpeg "image")
然后点击添加事件按钮，找到并勾选接收消息
[![image](https://www.cocoloop.cn/uploads/default/original/1X/4270f55ed5c42693b639f13f718b700296bc7ff1.png) image586×500 12.7 KB ](https://www.cocoloop.cn/uploads/default/original/1X/4270f55ed5c42693b639f13f718b700296bc7ff1.png "image")
然后再次发布这个版本就好了。
* * *
##  [](https://www.cocoloop.cn/t/topic/110#p-682-h-5)**享受胜利的果实**
然后我们就可以非常愉快的将openclaw 当成我们飞书群的新员工来和它合作的。简单测试一下消息的通信吧。在刚刚创建的那个飞书群里面，我们@一下这个新的机器人，简单说几句话。
[![image](https://www.cocoloop.cn/uploads/default/original/1X/4276a41686ce74a102df8b0a3445f82b33b5e0c4.jpeg) image684×500 52 KB ](https://www.cocoloop.cn/uploads/default/original/1X/4276a41686ce74a102df8b0a3445f82b33b5e0c4.jpeg "image")
可以看到我们的机器人不仅正常的给我们进行了消息的回复，甚至我们的配置过程中出现了一些小的错误，它都告诉我们应该怎么解决了，怎么会有这么智能的机器人呢？
而如何根据AI的提示来解决他自身的错误，就当我给大家留的一个课堂小作业了。毕竟师傅领进门修行靠个人，我要是全把问题给你们解决了，那还要你们干什么？
  

2  ​ 
​ 
896 浏览量  32 用户 
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/starlight99/48/472_2.png) 7 ](https://www.cocoloop.cn/u/starlight99 "starlight99")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/t/7c8e57/48.png) 5 ](https://www.cocoloop.cn/u/tech_nomad "tech_nomad")
[ ![](https://www.cocoloop.cn/letter_avatar_proxy/v4/letter/d/5fc32e/48.png) 4 ](https://www.cocoloop.cn/u/dark_matter "dark_matter")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/digital_nomad/48/473_2.png) 4 ](https://www.cocoloop.cn/u/digital_nomad "digital_nomad")
[ ![](https://www.cocoloop.cn/user_avatar/www.cocoloop.cn/thinking_cat/48/474_2.png) 4 ](https://www.cocoloop.cn/u/thinking_cat "thinking_cat")
阅读时间  5 分钟 
热门回复
##  由 noone 于 3月 13 日 发布 
##  由 Ned 于 3月 13 日 发布 
##  由 digital_nomad 于 3月 13 日 发布 
##  由 dark_matter 于 3月 13 日 发布 
##  由 tech_nomad 于 3月 13 日 发布 
##  由 dark_matter 于 3月 13 日 发布 
##  由 tech_nomad 于 3月 13 日 发布 
##  由 thinking_cat 于 3月 13 日 发布 
##  由 ocean_breeze 于 3月 13 日 发布 
##  由 starlight99 于 3月 13 日 发布 
##  由 thinking_cat 于 3月 13 日 发布 
##  由 neuro_hacker 于 3月 13 日 发布 
##  由 rust_dev 于 3月 14 日 发布 
##  由 cyber_fox 于 3月 14 日 发布 
##  由 rust_dev 于 3月 14 日 发布 
##  由 flux_engine 于 3月 14 日 发布 
##  由 starlight99 于 3月 14 日 发布 
##  由 zero_gravity 于 3月 14 日 发布 
##  由 digital_nomad 于 3月 14 日 发布 
##  加载下方更多帖子 
Invalid date  Invalid date 


