# AI 财富创造观察站：设计方案与同类项目调研

> 日期：2026-08-07
> 状态：设计文档（尚未实施，等待用户决策）
> 定位：以"唯一标准 = 是否创造新增物理财富"为标尺，跟踪 AI 重塑生产过程的可实时更新仪表盘。

---

## 一、调研结论：已有项目盘点（避免重复劳动）

用户提出"GitHub 上是否已有人做出来"，经检索，已有项目分五类，与本项目关系如下：

### 1. 全球态势仪表盘（用户提到的"世界紧急信息"模式）

| 项目 | 说明 | 与本项目关系 |
|---|---|---|
| **koala73/worldmonitor**（78k★） | 实时全球情报仪表盘，500+ 信源、AI 聚合简报、3D/平面地图、国家不稳定指数、金融雷达、6 站点变体（world/tech/finance/commodity/happy/energy）、本地 AI | 这就是用户记忆中的"世界紧急信息"。**模式参考**（数据源→聚合→AI 提炼→可视化→状态），但其主题是地缘政治/危机，非财富创造 |
| ssec-sentinel / globalpulse / GeoSynth | 同类全球事件监控，地图+时间线 | 模式参考，主题无关 |
| **situroom** | 纯静态页 + 免费公共 API、零后端、无 API key、MCP 服务器、状态标注（LIVE/STALE/SNAPSHOT/ERROR） | **架构参考**：状态标注思路直接可借 |

### 2. AI 经济 / 位移监测（最接近本项目的主题）

| 项目 | 说明 | 与本项目关系 |
|---|---|---|
| **simonhimself/displacement-index** | "AI 繁荣是否到达实体经济"：五环节链（白领替代→消费→鬼GDP→信用压力→房贷），17 条 FRED 序列 + Indeed 招聘，0-100 指数，Cloudflare Workers 定时刷新 | **主题最接近**。但视角是"分配/位移/压力"，不是"物理财富创造"；数据纯美国宏观，不盯企业动态 |
| **jschulman/displacement-curve** | 8 个公开信号合成 0-100 综合指数（BLS、Google Trends、GitHub、SEC EDGAR AI 收入、人均收入、VC 融资、招聘、监管），GitHub Actions + JSON + GitHub Pages | **技术形态教科书**：采集器→规范化→data JSON→静态页→Actions cron。纯公开免费数据。 |
| **gofhilman/ai-economic-index** | Anthropic Economic Index 数据管道（ELT + dbt + Evidence 仪表盘 + Bruin AI 查询） | **可复用数据源**：Anthropic Economic Index（AI 任务渗透的官方数据集） |
| shekelstrong/ai-economy-simulator | 1000 agent 模拟经济体 | 模拟器，非观测，无关 |

### 3. AI 趋势 / 新闻雷达（中文生态，架构最匹配）

| 项目 | 说明 | 与本项目关系 |
|---|---|---|
| **LearnPrompt/ai-news-radar** | 中文 AI 24h 雷达：信源质量判断→故事线合并→三口味 AI 锐评→静态页+GitHub Actions。内置**"伯乐 Skill"**（AI 帮判断/录入/维护信源清单） | **高度匹配**：静态页 + Actions + AI 维护信源 = 用户"先定渠道清单、再按清单抓取"的现成机制。主题是 AI 资讯，非财富创造 |
| sansan0/TrendRadar（61k★） | AI 舆情热点聚合，11 平台热榜 + RSS + AI 分析推送 | 通用热点工具，可作信号源之一 |
| mire403/InsightRadar | RSS→语义聚类→趋势强度(0-100)→洞察输出 | 趋势洞察引擎思路可参考，主题无关 |

### 4. AI 机会 / 副业雷达（主题接近，但方向被本项目的"唯一标准"否定）

| 项目 | 说明 | 与本项目关系 |
|---|---|---|
| aitippro/TIP | AI 轻创业机会雷达，每日采集 GitHub Trending/Product Hunt/行业报告，输出机会卡片，Claude Code 全自动 | 概念接近（机会雷达），但**无价值观筛选**，正是本项目批判的"转移型机会"清单 |
| bleedline/aimoneyhunter（3.7k★） | AI 副业赚钱大合集 | 纯信息聚合，质量参差，即"卖铲子"内容，不借鉴 |
| zhoukai03/cheat-on-money | AI 时代兼职发现 + 反诈验证 skill | 反诈方法有参考价值，但面向个人兼职，非财富创造观测 |
| marcoslozina/opportunity-radar / guifav/market-intelligence-radar | 机会评分引擎 / 市场情报雷达 | 引擎架构可参考，主题无关 |

### 5. 链上 Agent 经济（方向无关）

Orac-G/agentic-economy-index、cloudonshore/thewalletshift：基于 ERC-8004 追踪链上 agent 经济。属加密生态，与本项目无关。

---

## 二、关键判断：什么已被做、什么还是空白

### 已被验证、不应从零重做的部分
1. **技术形态**：静态页 + data JSON + GitHub Actions 定时采集 + 综合指数 → displacement-curve 已是完整教科书。
2. **中文实时雷达 + 信源维护机制**：ai-news-radar 的"伯乐 Skill"已实现"AI 维护渠道清单并抓取"——这正是我们规划的第一步/第二步。
3. **可复用免费数据源**：Anthropic Economic Index、FRED、SEC EDGAR、BLS、Google Trends、GitHub API、IFR（工业机器人出货）、WEF 灯塔工厂名单、LMArena/Artificial Analysis。

### 仍是空白的部分（本项目的存在价值）
1. **"唯一标准 = 新增物理财富"作为筛选/评分标尺**——现有雷达全部是"聚合+热度"，没有价值观过滤；现有经济指数看"分配/位移/压力"，不看"财富创造"。
2. **物理闭环盯人（生产企业）**——现有项目盯模型厂商或宏观指标，没有盯"生产企业把 AI 落成物理产出的成本下降/产能提升"这一闭环验证。
3. **左右列重塑信号**（旧摩擦需求消失 vs 新生产方式操作位冒头）——已有语料（《生产方式重塑信号清单》）可直接作为数据基础。
4. **中文一手生态信号**（cocoloop 等）+ 全球玩家对标——现成雷达没有这种混合信源结构。

### 结论：**借架构，做内容**——不重造轮子，但轮子上的货是新的。

---

## 三、借鉴与复用方案

| 层 | 借鉴来源 | 具体做法 |
|---|---|---|
| 基座 | ai-news-radar 或 displacement-curve | 二选一（见"待决策问题"），复用其静态页 + Actions + 信源维护骨架 |
| 信源维护 | ai-news-radar 伯乐 Skill | 渠道清单（sources.md）由 AI 协助录入/判断/维护 |
| 数据管道 | displacement-curve | 采集器→规范化→data JSON 分层；每源独立失败降级 |
| 状态标注 | situroom | 每个数据源 LIVE/STALE/MANUAL，永不白屏 |
| 数据源 | 各免费公共源 | Anthropic Economic Index、FRED、SEC EDGAR、GitHub API、IFR、WEF 灯塔工厂、LMArena/AA、cocoloop 抓取 |
| 不采用 | 链上 agent 经济 / 无筛选机会清单 | 主题无关或方向被"唯一标准"否定 |

---

## 四、本项目的独特点（为什么值得做）

1. **唯一标准驱动**：每条信号先过"三问筛选器"——转移？释放？新增物理财富？只有"新增"进入主榜。
2. **物理闭环盯人**：重点盯生产企业（灯塔工厂、产线 AI 落地、财报资本开支），模型厂商只作前瞻信号。
3. **左右列动态**：左列（旧摩擦需求在消失）vs 右列（新生产方式操作位在冒头），动态更新。
4. **混合信源**：中文一手生态（cocoloop、厂商公众号、即刻）+ 全球行为数据（LMArena、GitHub、SEC）+ 聚合周刊去噪。
5. **人审 + AI 干活 + 状态透明**：AI 抓取提炼，人审发布，数据源状态公开（避免黑箱）。

---

## 五、修订后的项目设计

### 目录结构（待批准后创建）

```
D:\项目\项目参考资料\ai-wealth-monitor\
├── README.md            # 项目说明 + 唯一标准 + 三问筛选器
├── PLAN.md              # 本设计文档（迁入）
├── docs/
│   └── sources.md       # ★ 总信息来源清单（六大类 + 观测指标 + 频率）
├── data/                # 实时数据（页面唯一数据源）
│   ├── signals.json     # 财富信号（新增物理财富实证）
│   ├── watchlist.json   # 盯人名单 + 状态
│   ├── waves.json       # 左右列重塑信号
│   └── timeline.json    # 事件时间线
├── collectors/          # 各源采集器（借鉴 displacement-curve）
├── skills/              # 信源维护 skill（借鉴 ai-news-radar 伯乐）
└── public/
    └── index.html       # 静态页
```

现有材料迁入 docs/：《AI副业认知地图》、《生产方式重塑信号清单》。

### 数据流

```
sources.md(渠道清单) → collectors/抓取 → data/*.json → AI提炼+人审 → public/index.html
    状态：LIVE(自动) / STALE(过期) / MANUAL(人工录入)
```

### 页面板块

1. 唯一标准横幅 + 三问筛选器（顶部锚定）
2. 财富信号榜（新增物理财富实证：企业披露的产能/成本数据）
3. 盯人名单（认知层 / 物理引擎 / 生产企业闭环，各带最新状态）
4. 左右列重塑信号（左列消失 / 右列冒头）
5. 事件时间线 + 数据源状态条（LIVE/STALE/MANUAL）

### 观测指标（贯穿全站的标尺）

- agent 自主完成率（决定替代速度）
- 单位任务成本（决定普及速度）
- 物理产出增量（生产企业披露的成本降幅 / 产能提升）——**最终验证**

### 阶段计划

- 阶段 0（本次）：设计文档 + 调研结论 —— 已完成
- 阶段 1：决策基座 → 搭建项目文件夹、迁入旧材料、初始化
- 阶段 2：定义 data/*.json schema + 页面骨架
- 阶段 3：sources.md 完整渠道清单 + 首批数据录入（AI 抓取 + 人审）
- 阶段 4：抓取脚本 + 定时更新 + 状态标注 + 持续维护

---

## 六、待决策问题

1. **基座选择**：
   - A. **fork ai-news-radar** 改造（省事、中文、已有"伯乐 Skill"信源维护机制，最贴合"定渠道清单→抓取"；但主题是 AI 资讯，需大改内容层）
   - B. **参考 displacement-curve 自建轻量骨架**（可控、贴合本项目 schema 与价值观筛选；从零写但规模小）
   - C. 纯自建 index.html + json（最轻，但无 Actions/信源维护基础设施）
2. **托管与自动化**：是否推 GitHub 仓库 + GitHub Pages + Actions 定时抓取（要自动化就得有仓库）；还是纯本地静态页 + 手动/半自动更新？
3. **开源还是私有**：若开源，可把"唯一标准筛选 + 物理闭环盯人"做成可 PR 回 ai-news-radar 的 skill/源集；若私有，则保持本地。

---

## 七、决策记录（2026-08-07 用户确认）

| 决策项 | 结论 |
|---|---|
| 页面形态 | 静态页 + 数据文件 + 脚本更新 |
| 更新机制 | 第一步确定渠道清单 → 第二步按清单抓取 |
| 项目位置 | `D:\项目\项目参考资料\` 下新建项目文件夹 |
| 基座 | **自建轻量骨架**（参考 displacement-curve 架构，schema 从第一天为"唯一标准/左右列/物理闭环"设计） |
| 托管与自动化 | **GitHub 托管 + GitHub Pages + Actions 定时抓取** |
| 开源/私有 | **开源**（"唯一标准筛选 + 物理闭环盯人"作为差异化，开源反哺生态） |

### 修订后的目录结构（最终版）

```
D:\项目\项目参考资料\ai-wealth-monitor\        ← 项目根
├── README.md            # 项目说明 + 唯一标准 + 三问筛选器
├── PLAN.md              # 本设计文档（决策后迁入，作为总规划）
├── docs/
│   ├── AI副业认知地图.md       # 迁入（基础语料）
│   ├── 生产方式重塑信号清单.md  # 迁入（基础语料）
│   └── sources.md        # ★ 总信息来源清单（下一步核心产物）
├── data/
│   ├── raw/cocoloop/     # 迁入（100 篇抓取资料，作原始语料）
│   ├── signals.json      # 财富信号（新增物理财富实证）
│   ├── watchlist.json    # 盯人名单 + 状态
│   ├── waves.json        # 左右列重塑信号
│   └── timeline.json     # 事件时间线
├── collectors/           # 各源采集器（借鉴 displacement-curve）
├── skills/               # 信源维护 skill（借鉴 ai-news-radar 伯乐）
├── .github/workflows/    # Actions 定时抓取
└── public/
    └── index.html        # 静态页（GitHub Pages）
```
