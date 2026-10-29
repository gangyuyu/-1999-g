# 《重返未来：1999》官方表情包（全系列）

采集完成：2026-10-29（Asia/Shanghai）；已整理为 AstrBot 表情包格式（v0.3）。

## 仓库结构

```text
表情包\
├─ 官方表情包\                  ← AstrBot 表情包包根目录（按来源安装填这个子目录）
│  ├─ manifest.json             清单：schema_version 1、51 个分类
│  ├─ memes\<分类>\             696 张表情图（分类 key 见下方对照表）
│  ├─ previews\                 52 张官方宣传海报（清单中声明 8 张）
│  └─ README.md                 包说明与安装方法
├─ 表情包总览.html               双击可在浏览器中按系列浏览全部图片
├─ 表情包清单.csv                696 张图片的路径 / 大小明细（Excel 可打开）
├─ 下载清单.json                 下载统计 / 逐系列数量
├─ _tools\                      采集、补下、打包、索引脚本
├─ 可直接下载的官方预览\          早期保留的两张示例图
├─ README.md                    仓库首页说明（含 AstrBot 安装步骤）
└─ README-官方表情包收集说明.md   本文件
```

## 安装到 AstrBot

表情包管理器 WebUI → **按来源安装**：

| 字段 | 值 |
|---|---|
| 仓库 | `gangyuyu/-1999-g` |
| 分支 / ref | `main` |
| 子目录 / subpath | `官方表情包` |

包必须满足 [AstrBot 表情包规范](https://github.com/anka-afk/astrbot-meme-pack-index)：
包根目录同时存在 `manifest.json` 与 `memes/<分类>/`，分类 key 仅允许 `[A-Za-z0-9._-]`，
因此中文系列名放在 `description` 中，目录名改用拼音。

## 统计

| 项目 | 数量 |
|---|---|
| 官方表情系列（= 分类） | **51** 个（最早的「敲响心灵」→ 最新的「奇妙9堡」） |
| 表情图片 | **696** 张（其中 16 张 GIF 动图，其余 PNG/透明底） |
| 官方宣传海报 | **52** 张（含「箱中缝缝补」两弹各 1 张） |
| 表情包内文件 | **750** 个（696 图 + 52 海报 + manifest + README） |
| 体积 | 约 58 MB |
| 校验 | 图片无 0 字节/无损坏；manifest 已通过官方 JSON Schema 校验 |

按年份：2023 年 6 个系列、2024 年 14 个、2025 年 16 个、2026 年 15 个（含「次元奇旅」）。
常规系列 8 或 16 张；「唐人街影话」为 16 组 GIF + 16 张对应 PNG（共 32 个文件）；
「箱中缝缝补」两弹合计 32 张。

### 图片规格

- 表情图：**120×120 px**，PNG（GIF 动图为 400×400），与微信表情商店展示尺寸一致。
- 宣传海报：约 1024×1300～1760 px 的长图，含系列名、全部表情缩略图与二维码。

## 分类 key 对照表

| # | 分类 key | 系列 | 张数 | 年份 |
|---|---|---|---|---|
| 01 | `qiaoxiang-xinling` | 敲响心灵 | 8 | 2023 |
| 02 | `gongce-shangxian` | 公测上线 | 16 | 2023 |
| 03 | `molupangka` | 摩卢旁卡 | 16 | 2023 |
| 04 | `dongxue-qiutu` | 洞穴囚徒 | 16 | 2023 |
| 05 | `yilu-fafafa` | 一路发发发 | 8 | 2023 |
| 06 | `wululu` | 乌卢鲁 | 16 | 2023 |
| 07 | `shuori-shouji` | 朔日手记 | 16 | 2024 |
| 08 | `chunjie-hesui` | 春节贺岁 | 8 | 2024 |
| 09 | `xingguang-canlan` | 星光灿烂 | 16 | 2024 |
| 10 | `laiyashiji` | 来亚什基 | 16 | 2024 |
| 11 | `gudu-zhige` | 孤独之歌 | 16 | 2024 |
| 12 | `youchang-xiari` | 悠长夏日 | 8 | 2024 |
| 13 | `mingri-zhicheng` | 明日之城 | 16 | 2024 |
| 14 | `77hao-wangshi` | 77号往事 | 16 | 2024 |
| 15 | `youyu-redai` | 忧郁热带 | 16 | 2024 |
| 16 | `dongqu-liming` | 东区黎明 | 16 | 2024 |
| 17 | `xiangzhong-yundonghui` | 箱中运动会 | 8 | 2024 |
| 18 | `tuzhong-liuying` | 途中留影 | 8 | 2024 |
| 19 | `diqiu-zhongye` | 地球终夜 | 16 | 2024 |
| 20 | `luoxue-qianye` | 落雪前夜 | 8 | 2024 |
| 21 | `xiying-chunzhi` | 喜迎春至 | 8 | 2025 |
| 22 | `tangrenjie-yinghua` | 唐人街影话 | 32 | 2025 |
| 23 | `wan1999-xianglipu-rensheng` | 玩1999享厘普人生 | 16 | 2025 |
| 24 | `fengdian-wenming` | 疯癫文明 | 16 | 2025 |
| 25 | `yuzhou-zuqu` | 宇宙组曲 | 16 | 2025 |
| 26 | `fuleyuan` | 复乐园 | 16 | 2025 |
| 27 | `xiangzhong-xuejing` | 箱中雪景 | 8 | 2025 |
| 28 | `xiangzhong-jiamian` | 箱中假面 | 16 | 2025 |
| 29 | `manman-changlu` | 漫漫长路 | 16 | 2025 |
| 30 | `xiangzhong-manyou` | 箱中漫游 | 8 | 2025 |
| 31 | `xinyang-zhiyue` | 信仰之跃 | 16 | 2025 |
| 32 | `changye-mingdi` | 长夜鸣笛 | 16 | 2025 |
| 33 | `qianliu-de-shengyan` | 迁流的盛宴 | 16 | 2025 |
| 34 | `jieyuda-de-yansi` | 解与答的研思 | 8 | 2025 |
| 35 | `xiangzhong-qiyu` | 箱中栖语 | 8 | 2025 |
| 36 | `yuanzhengji` | 远征记 | 16 | 2025 |
| 37 | `sanxian-guohai` | 三仙过海 | 8 | 2026 |
| 38 | `bulaochun` | 不老春 | 16 | 2026 |
| 39 | `xiangzhong-suinnuan` | 箱中岁暖 | 8 | 2026 |
| 40 | `lvsongshi-she` | 绿松石蛇 | 16 | 2026 |
| 41 | `renmen-hequ` | 人们何去 | 8 | 2026 |
| 42 | `xiangzhong-douqu` | 箱中逗趣 | 8 | 2026 |
| 43 | `xiangzhong-dianyingjie` | 箱中电影节 | 8 | 2026 |
| 44 | `tazhe-beiai` | 他者悲哀 | 16 | 2026 |
| 45 | `ciyuan-qilv` | 次元奇旅 | 8 | 2026 |
| 46 | `shiji-chidu` | 世纪尺度 | 16 | 2026 |
| 47 | `xiangzhong-fengfengbu` | 箱中缝缝补 | 32 | 2026 |
| 48 | `juhe-langchao` | 聚合浪潮 | 8 | 2026 |
| 49 | `duicebu` | 对策部 | 16 | 2026 |
| 50 | `liujin-zhihai` | 流金之海 | 16 | 2026 |
| 51 | `qimiao-9bao` | 奇妙9堡 | 16 | 2026 |

## 来源与方法

1. 官方发布记录汇总：灰机 wiki [官方多媒体/表情包](https://res1999.huijiwiki.com/wiki/官方多媒体/表情包)
   —— 该页按版本/节日逐系列收录官方发布的全部表情图，是目前唯一可一次性核对的公开档案。
2. 图片直链：`huiji-public.huijistatic.com/res1999/uploads/...`（MediaWiki 上传目录，
   路径 = MD5(文件名)，脚本按此规则还原直链）。
3. 官方渠道原始发布：微博 [@芬斯伯克1999](https://weibo.com/7759764101)、Bilibili
   [@重返未来1999](https://space.bilibili.com/1197454103/dynamic)、微信表情商店（每系列海报二维码）。

> 微信表情商店没有公开的整套导出接口，无法从网页直接批量拉取原始贴图；本次下载的
> 120×120 图集与商店内贴图同尺寸，可直接用于日常排版/二创素材整理。

## 已知说明

- 「唐人街影话」在维基中同时列出 GIF 与 PNG 两套，已全部下载（GIF 可直接当动图用），
  在 `memes/tangrenjie-yinghua/` 下。
- 海报「表情包-箱中缝缝补2.jpg」为第二弹海报，其余每系列 1 张。
- 早期系列（1–22）图片沿用维基的统一命名 `考据-表情包-NN_MMMM`，其中 MMMM 是全局流水号，
  因此编号不连续、也非按图内顺序排列，属正常现象。
- 包格式要求分类 key 为 ASCII，因此目录名用系列拼音；中文名写在 `manifest.json` 的分类
  `description` 里，也见上表。
- 官方再上新系列时：先用下载脚本取图，再把新系列加入 `_tools\make_astrbot_pack.py` 的
  `SERIES` 列表并重跑，即可并入 `memes/` 并更新清单。

## 工具脚本

| 脚本 | 用途 |
|---|---|
| `_tools\download_stickers.ps1` | 按系列清单批量下载（.NET HttpClient，断点续传） |
| `_tools\retry_pack22.ps1` | 22 号系列补下（CDN 并发偶发 404 时重试） |
| `_tools\make_astrbot_pack.py` | 把系列目录整理成 `memes/<分类>/` 并生成/校验 manifest、重建总览与 CSV |
| `_tools\make_index.py` | 旧版总览生成脚本（已被 `make_astrbot_pack.py` 取代） |
| `_tools\download_stickers.py` | 早期 Python 版下载器（CDN 拒绝 Python TLS 指纹，已弃用，仅留档） |

重跑命令（Windows PowerShell）：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ".\_tools\download_stickers.ps1"
python .\_tools\make_astrbot_pack.py
```

## 版权

图片版权归《重返未来：1999》官方（Bluepoch / 深蓝互动）所有，本目录仅作个人素材整理与
考据留存，请勿商用或二次公开发布。
