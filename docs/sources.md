# 总信息来源清单（sources.md）v2

> 定位修正：**不做大杂烩，聚焦生产端**。重点 = 利用 AI 新增更多财富：
> 1. 企业生产（工厂/产线/公司披露）
> 2. 个人生产（独立开发者/自由职业/个体）
> 3. 生产工具（模型/工具链/开源）
>
> 但凡 AI 参与的生产，都算。信号流程：**先定渠道清单 → 再按清单抓取**。
> 状态：LIVE=自动可用（API/CSV/RSS），STALE=需人工核对，MANUAL=人工录入。

## 一、企业生产端（本项目的核心差异化）

> 对应观测链"生产企业/物理载体"，观测指标=物理产出增量。**最终验证 = 企业披露的成本降幅 / 产能提升 / 资本开支**。

| 来源 | 类型 | 更新频率 | 状态 | 获取方式 |
|---|---|---|---|---|
| **WEF 全球灯塔网络（Lumina）** | 生产企业实证（官方） | 年 | LIVE | 官网报告+白皮书 |
| **国家统计局（stats.gov.cn）** | 工业机器人/高技术制造产量 | 月 | LIVE | 官网/API |
| 工信部 | 工业机器人产量、电子信息制造 | 月 | LIVE | 官网/发布会 |
| SEC EDGAR Full-Text（efts.sec.gov） | 10-K/8-K 中 AI 披露全文检索 | 季/实时 | LIVE | 免费 API，无需 key |
| 巨潮资讯网 cninfo.com.cn | 中国上市公司财报（含 AI 披露） | 季 | STALE | 网页/爬取 |
| 特斯拉 / 比亚迪 / 宁德时代 / 富士康 / 海尔 IR | 生产企业财报与资本开支 | 季 | LIVE | 财报/IR |
| KPMG 全球制造业科技趋势报告 | 高管调研（财务回报率） | 年 | LIVE | 官网免费报告 |

### WEF 灯塔工厂 = 生产端主线索（重点）

- **形态**：世界经济论坛认证"规模化应用 AI/4IR 技术实现可量化效益"的工厂，2026 年已达 **224-238 家**，中国占一半以上。
- **我们为什么盯它**：每条披露都有硬数字——福特奥托桑（产能翻倍/劳动生产↑44%）、联合利华合肥（运营成本↓24%/交货↓75%）、西门子南京（交付周期 45→10 天/缺陷率↓46%）、海辰储能（制造成本↓37%/产能↑200%）。**这就是"AI 新增物理财富"的实证**。
- **Lumina 平台**：WEF 官方 AI 工业智能平台，沉淀 8 年灯塔数据 + 1000+ 转型案例，有基准数据。
- **量化亮点**（2026 白皮书）：分析型 AI/ML 渗透率 62%，GenAI 从 9%→23%，AI agent 5%；约 5% 的企业 GenAI 试点获可观 ROI；3 年 2-3 倍 ROI、5 年 4-5 倍。

### 国家统计局 = 中国产能硬指标（重点）

- **工业机器人产量（月度）**：2026 上半年 53.8 万套，同比 +28%；1-2 月同比 +31.1%。
- **高技术制造业增加值**：2026 1-2 月 +13.1%，贡献率 31.5%；工业控制计算机 +90%、3D 打印 +54%、工业机器人 +31%。
- **方法**：直接对应"物理载体层/产能"，是自动可抓的免费宏观源。

### SEC EDGAR = 企业 AI 披露实证（重点）

- **端点**：`https://efts.sec.gov/LATEST/search-index`，全文搜索 2001 至今所有申报。
- **用法**：搜 10-K 中 "artificial intelligence" + "cost" / "productivity" / "reduction"，按季度筛选 → 拿到具体公司披露。免费、无需 key，需 User-Agent。
- **对应**："生产企业闭环"的自动化来源。

## 二、个人生产端（独立生产者）

> 对应"执行层"，观测指标=单位任务成本 / 个人产出增量。

| 来源 | 类型 | 更新频率 | 状态 | 获取方式 |
|---|---|---|---|---|
| Upwork Research（In-Demand Skills / Future Workforce Index） | 自由职业市场真实数据 | 年 | LIVE | 官网免费报告 |
| Upwatcher（Upwork 实时抓取） | AI 自由职业岗位量/费率 | 日 | LIVE | 网页/爬取 |
| Indie Hackers 产品库 | 独立开发者 MRR（公开页面+Algolia API） | 日 | STALE | 公开 API/爬取 |
| TrustMRR API | 已验证初创 MRR（Stripe 直连） | 近实时 | LIVE | API（免费档） |
| cocoloop（100 篇已抓语料） | 中文个人实操 | 存量 | MANUAL | 本地 `data/raw/cocoloop/` |

### Upwork = 个人生产端最硬的数据（重点）

- **Future Workforce Index 2026**：做 AI 的自由职业者比不做的高 34% 时薪；复杂 AI 工作收入 +45%/年；AI 增补型专业服务量 +72%、收入 +22%；而低复杂度 AI 执行类单均收入 -13%（量 +90%）。
- **In-Demand Skills 2026**：AI 相关技能需求 +109%/年；AI 视频 +329%、AI 集成 +178%。
- **价值**：这就是"个人生产端"的可量化证据——哪些 AI 参与的个人生产在增值（AI orchestrator），哪些在贬值（commodity）。

### Indie Hackers / TrustMRR = 独立开发者收入（重点）

- Indie Hackers：4,500+ 产品，34% 公开 MRR（中位数 ~$7xx/月）；分类里 **AI/automation 是最快增长品类**。
- TrustMRR：840+ 家、82 国，Stripe/LemonSqueezy 直连验证，免费档 API。
- **用法**：追踪 AI 独立产品的 MRR 变化 → "个人用 AI 做出原本做不出的东西"的直接证据。

## 三、生产工具端（工具/模型/成本）

> 对应"认知层"，观测指标=agent 自主完成率 / 单位推理成本。**工具成本下降 = 生产端放量前提**。

### 生产工具可及性阶梯（谁能生产实物）

| 层 | 工具 | 证据 |
|---|---|---|
| 个人层 | AI + 3D 打印 | Hi3D：AI 自动化 3D 打印最难步骤，个人无需 CAD 开实物生意；桌面 3D 打印机数百美元 vs 工业 CNC 数十万美元 |
| 二次开发层 | 开源机器人（Unitree SDK2 Go2/H1/B2/G1 + ROS2） | 个人可改代码二次开发，但暂无"个人用机器人做出可售实物"实证 → 待验证 |
| 大企业层 | 机器人 / 机床 / 自动化产线 | WEF 灯塔 224+ 家、国家统计局工业机器人产量 |

**个人生产三件套（调研修正）**：个人生产实物不是单一"3D 打印"，而是 **AI（设计/营销）+ 3D 打印（原型/样品）+ 供应链代工（小批量量产）**。多数工厂 MOQ 1 万件，代工方如 Breeze 深圳从 1000 件起（breezehw.com）；例证 MemoTalk.ai（约 5 人团队 4 个月做出实体 AI 记忆硬件）。

**个人起源监测线**：`AI × 3D 打印 → 实物样品 → 供应链小批量 → 物理财富`（对应 new_pending → new_verified）。

| 来源 | 类型 | 更新频率 | 状态 | 获取方式 |
|---|---|---|---|---|
| GitHub API（trending/star） | 开源工具采用 | 日 | LIVE | 免费 API（已在用） |
| RoninForge AI Price Index | 模型 API 定价历史（dated） | 周 | LIVE | CC BY 4.0 JSON |
| tokenprice.fyi | 332 模型/88 供应商价格+历史 | 日 | LIVE | 网页/JSON |
| LLMRates.ai | 全供应商定价数据集 | 日 | LIVE | CC BY 4.0 JSON/CSV |
| MyTokenTracker | AI Cost Index（价格篮子指数） | 日 | LIVE | 免费 API |
| Anthropic Economic Index | AI 任务渗透/占用率官方数据 | 月 | LIVE | HuggingFace CC-BY CSV |
| LMArena | 模型行为排名 | 日 | LIVE | API |

### Anthropic Economic Index = 任务渗透官方数据（重点）

- **位置**：HuggingFace `Anthropic/EconomicIndex`，CC-BY，含 O*NET 任务映射、augmentation vs automation、按国家/职业/技能。
- **2026 版**：编码仍是最大用途（Claude.ai 35%）；"人无法独立完成的任务"比例上升 = automation 深化。**49% 职业至少 1/4 任务由 Claude 执行**。
- **用法**：追踪"AI 自主完成率"这一核心观测指标的官方月度序列。

### 价格指数 = 单位成本（重点）

- Opus 系列 $15/$75 → $5/$25（-67%）；o3 Pro 较 o1 Pro -87%；DeepSeek 已到 $0.14/$1M。
- **用法**：自动抓 tokenprice.fyi / LLMRates / RoninForge 的 JSON → "单位推理成本"序列，直接对应"执行层单位任务成本↓"。

### 生产工具观测渠道（AI × 具体生产工具，data/tools.json 驱动）

> 双指标 = 人力↓ / 产量↑。工具先在商品页/采购清单冒头，再流转到市场。详见 `docs/superpowers/specs/2026-08-07-生产工具观测-design.md`。

| 渠道 | 作用 | 状态 |
|---|---|---|
| 中国政府采购网 + 央企采购平台 | 苗头指标（最早）：采购公告出现 AI 化生产装备 = 官方确认 | MANUAL |
| 美国联邦采购 GSA Advantage / FedMall | 苗头指标：联邦采购目录 | MANUAL |
| 上市公司/中标公告（巨潮） | 苗头指标：AI 生产装备采购金额与供应商 | MANUAL |
| Kickstarter / Indiegogo | 新工具冒头（pre-market） | MANUAL |
| 垂直厂商直销（Bambu Lab / Unitree 等） | 新一代 AI 生产工具功能参数 | MANUAL |
| 1688 / 阿里国际站 / Made-in-China | B2B 商品页（存量工具） | MANUAL |
| Amazon / 京东工业品 | 零售普及 + 真实评价验证 | MANUAL |

**采购清单 = 苗头指标**：好东西先流向政府和富人阶层，采购清单比普通商品页早一个周期。procurement 渠道工具验证后才升级 signals。

## 四、观测链与源对应总表

| 观测链层 | 观测内容 | 自动源 | 人工源 |
|---|---|---|---|
| 认知层（模型/agent） | 能力跃迁、任务渗透 | Anthropic Economic Index、LMArena | 厂商公告 |
| 执行层（工具/成本） | 单位任务成本 | 价格指数、GitHub | — |
| 物理载体层 | 产能、出货 | 国家统计局、WEF | 机器人厂商 |
| 生产企业（闭环★） | 成本↓/产能↑/资本开支 | SEC EDGAR、WEF 灯塔 | 盯人财报 |
| 个人生产（闭环★） | 个人产出/MRR | Upwork、TrustMRR、Indie Hackers | cocoloop |
| 经济验证 | 宏观联动 | FRED | 报告 |

## 混合信源结构原则（v2 修订）

- **WEF 灯塔 + 统计局 + SEC**：企业生产实证的"官方三角"，定最终验证。
- **Upwork + Indie Hackers + cocoloop**：个人生产的一手数据，定渗透速度与实操细节。
- **价格指数 + Anthropic Index + GitHub**：工具成本与采用度，定放量前提。
- **不做大杂烩**：以上每条都必须直接回答"AI 是否创造新增物理财富"；判断不了的源不进清单。

---

## 每期更新工作流（聚焦生产端）

1. **自动层（AI）**：抓价格指数 / 统计局 / GitHub / Anthropic Index / SEC EDGAR → 生成候选信号。
2. **盯人层（AI+人）**：WEF 灯塔新增名单 → 逐厂提炼"成本/产能/周期"三个数字。
3. **个人层（AI+人）**：Upwork / Indie Hackers / cocoloop → 筛出"用 AI 做出原本做不出实物"的个体。
4. **四层判定**：转移/释放/新增·待验证/新增·已证实 → 只有 `new_verified` 进主榜，每条必带 physical 字段（见《物理财富验证制》spec）。
5. **写入** `data/signals.json`，更新状态与时间戳。

> 新渠道如何加入？先验证能否回答"新增物理财富"→ 能则录入 → 标状态 → 纳入抓取。
