# -*- coding: utf-8 -*-
"""
把仓库改造成符合 AstrBot 表情包规范（/v0.3）的表情包：
  官方表情包/
    manifest.json
    memes/<分类>/<图片>
    previews/<海报>
同时把总览 HTML / CSV 移到仓库根目录并重建。
"""
import csv
import json
import os
import re
import shutil

ROOT = r"C:\桌面\素材\人物素材\表情包"
PACK = os.path.join(ROOT, "官方表情包")

# (序号, 中文系列名, 分类 key, 张数)
SERIES = [
    (1,  "敲响心灵",        "qiaoxiang-xinling",        8),
    (2,  "公测上线",        "gongce-shangxian",         16),
    (3,  "摩卢旁卡",        "molupangka",               16),
    (4,  "洞穴囚徒",        "dongxue-qiutu",            16),
    (5,  "一路发发发",      "yilu-fafafa",              8),
    (6,  "乌卢鲁",          "wululu",                   16),
    (7,  "朔日手记",        "shuori-shouji",            16),
    (8,  "春节贺岁",        "chunjie-hesui",            8),
    (9,  "星光灿烂",        "xingguang-canlan",         16),
    (10, "来亚什基",        "laiyashiji",               16),
    (11, "孤独之歌",        "gudu-zhige",               16),
    (12, "悠长夏日",        "youchang-xiari",           8),
    (13, "明日之城",        "mingri-zhicheng",          16),
    (14, "77号往事",        "77hao-wangshi",            16),
    (15, "忧郁热带",        "youyu-redai",              16),
    (16, "东区黎明",        "dongqu-liming",            16),
    (17, "箱中运动会",      "xiangzhong-yundonghui",    8),
    (18, "途中留影",        "tuzhong-liuying",          8),
    (19, "地球终夜",        "diqiu-zhongye",            16),
    (20, "落雪前夜",        "luoxue-qianye",            8),
    (21, "喜迎春至",        "xiying-chunzhi",           8),
    (22, "唐人街影话",      "tangrenjie-yinghua",       32),
    (23, "玩1999享厘普人生", "wan1999-xianglipu-rensheng", 16),
    (24, "疯癫文明",        "fengdian-wenming",         16),
    (25, "宇宙组曲",        "yuzhou-zuqu",              16),
    (26, "复乐园",          "fuleyuan",                 16),
    (27, "箱中雪景",        "xiangzhong-xuejing",       8),
    (28, "箱中假面",        "xiangzhong-jiamian",       16),
    (29, "漫漫长路",        "manman-changlu",           16),
    (30, "箱中漫游",        "xiangzhong-manyou",        8),
    (31, "信仰之跃",        "xinyang-zhiyue",           16),
    (32, "长夜鸣笛",        "changye-mingdi",           16),
    (33, "迁流的盛宴",      "qianliu-de-shengyan",      16),
    (34, "解与答的研思",    "jieyuda-de-yansi",         8),
    (35, "箱中栖语",        "xiangzhong-qiyu",          8),
    (36, "远征记",          "yuanzhengji",              16),
    (37, "三仙过海",        "sanxian-guohai",           8),
    (38, "不老春",          "bulaochun",                16),
    (39, "箱中岁暖",        "xiangzhong-suinnuan",      8),
    (40, "绿松石蛇",        "lvsongshi-she",            16),
    (41, "人们何去",        "renmen-hequ",              8),
    (42, "箱中逗趣",        "xiangzhong-douqu",         8),
    (43, "箱中电影节",      "xiangzhong-dianyingjie",   8),
    (44, "他者悲哀",        "tazhe-beiai",              16),
    (45, "次元奇旅",        "ciyuan-qilv",              8),
    (46, "世纪尺度",        "shiji-chidu",              16),
    (47, "箱中缝缝补",      "xiangzhong-fengfengbu",    32),
    (48, "聚合浪潮",        "juhe-langchao",            8),
    (49, "对策部",          "duicebu",                  16),
    (50, "流金之海",        "liujin-zhihai",            16),
    (51, "奇妙9堡",         "qimiao-9bao",              16),
]

YEAR = {}
for idx, _, _, _ in SERIES:
    YEAR[idx] = 2023 if idx <= 6 else 2024 if idx <= 20 else 2025 if idx <= 36 else 2026
DESC = {
    1: "公测上线初期推出的首个官方表情系列",
    8: "春节贺岁主题",
    14: "2.1 版本「77号往事」纪念",
    21: "春节贺岁主题",
    22: "2.5 版本「唐人街影话」纪念（含 16 组 GIF 动图及对应 PNG）",
    23: "与「暹罗厘普」联动系列",
    47: "两弹合并，共 32 张",
    51: "最新系列",
}


def move_series():
    memes = os.path.join(PACK, "memes")
    os.makedirs(memes, exist_ok=True)
    moved = 0
    for idx, cn, key, cnt in SERIES:
        src = os.path.join(PACK, f"{idx:02d}_{cn}")
        dst = os.path.join(memes, key)
        os.makedirs(dst, exist_ok=True)
        if os.path.isdir(src):
            for f in sorted(os.listdir(src)):
                s = os.path.join(src, f)
                if os.path.isfile(s):
                    shutil.move(s, os.path.join(dst, f))
                    moved += 1
            try:
                os.rmdir(src)
            except OSError:
                pass
        got = len([f for f in os.listdir(dst) if os.path.isfile(os.path.join(dst, f))])
        if got != cnt:
            print(f"  ! 数量不符 {idx} {cn}: 期望 {cnt} 实际 {got}")
    print(f"移动表情图: {moved} 张")


def move_assets():
    # 海报 -> previews
    src = os.path.join(PACK, "_官方海报")
    dst = os.path.join(PACK, "previews")
    if os.path.isdir(src):
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.move(src, dst)
        print(f"海报 -> previews: {len(os.listdir(dst))} 张")
    # 总览 / 清单 -> 仓库根
    pairs = [("_表情包总览.html", "表情包总览.html"), ("_下载清单.json", "下载清单.json")]
    for a, b in pairs:
        s = os.path.join(PACK, a)
        if os.path.exists(s):
            shutil.move(s, os.path.join(ROOT, b))
            print(f"{a} -> {b}")


def build_manifest():
    posters = sorted(os.listdir(os.path.join(PACK, "previews")))
    pj = [p for p in posters if p.lower().endswith((".jpg", ".jpeg", ".png"))]

    def poster_of(cn):
        for p in pj:
            if p == f"表情包-{cn}.jpg":
                return f"previews/{p}"
        return None

    icon = poster_of("奇妙9堡") or (f"previews/{pj[0]}" if pj else None)
    preview_pick = ["奇妙9堡", "绿松石蛇", "不老春", "世纪尺度", "箱中缝缝补", "落雪前夜", "敲响心灵", "三仙过海"]
    previews = [p for p in (poster_of(x) for x in preview_pick) if p]

    categories = {}
    for idx, cn, key, cnt in SERIES:
        extra = DESC.get(idx, "")
        desc = f"第 {idx:02d} 系列「{cn}」（{YEAR[idx]} 年，{cnt} 张）"
        if extra:
            desc += f"：{extra}"
        desc += "。用于日常聊天中的表情回应。"
        categories[key] = {"description": desc}

    manifest = {
        "schema_version": 1,
        "id": "reverse-1999-official-stickers",
        "name": "重返未来：1999 官方表情包",
        "version": "1.0.0",
        "description": ("《重返未来：1999》官方发布的全套表情包，共 51 个系列、696 张表情图，"
                        "覆盖 2023 年公测至今的各个版本与节日庆典。图片取自官方发布图集："
                        "表情图 120×120 PNG（「唐人街影话」另含 400×400 GIF 动图）。"),
        "author": "gangyuyu（整理）",
        "homepage": "https://github.com/gangyuyu/-1999-g",
        "license": "版权归《重返未来：1999》官方（Bluepoch / 深蓝互动）所有，仅限个人学习与交流，禁止商用",
        "tags": ["重返未来1999", "游戏", "官方", "表情包", "二次元"],
        "icon": icon,
        "previews": previews,
        "source": {"type": "github", "repo": "gangyuyu/-1999-g", "ref": "main", "subpath": "官方表情包"},
        "categories": categories,
    }
    if icon is None:
        del manifest["icon"]
    with open(os.path.join(PACK, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"manifest.json: {len(categories)} 个分类, {len(previews)} 张 previews")
    return manifest


def validate(manifest):
    errors = []
    # 必填
    for k in ("schema_version", "id", "name", "version", "categories"):
        if k not in manifest:
            errors.append(f"缺少必填字段 {k}")
    if manifest.get("schema_version") != 1:
        errors.append("schema_version 必须为 1")
    if not re.match(r"^[a-z0-9][a-z0-9._-]{1,63}$", manifest.get("id", "")):
        errors.append("id 不符合 ^[a-z0-9][a-z0-9._-]{1,63}$")
    if not (1 <= len(manifest.get("name", "")) <= 128):
        errors.append("name 长度超限")
    if not (1 <= len(manifest.get("version", "")) <= 64):
        errors.append("version 长度超限")
    for k in ("description", "author", "license"):
        if k in manifest and not (1 <= len(manifest[k]) <= (2000 if k == "description" else 128 if k == "author" else 256)):
            errors.append(f"{k} 长度超限")
    if "tags" in manifest:
        if len(manifest["tags"]) > 32 or len(set(manifest["tags"])) != len(manifest["tags"]):
            errors.append("tags 不合规")
        for t in manifest["tags"]:
            if not (1 <= len(t) <= 64):
                errors.append("tag 长度超限")
    # 分类
    cats = manifest.get("categories", {})
    if not cats:
        errors.append("categories 不能为空")
    for k, v in cats.items():
        if not re.match(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$", k):
            errors.append(f"分类 key 不合法: {k}")
        if set(v.keys()) - {"description"}:
            errors.append(f"分类 {k} 含多余字段")
        d = v.get("description", "")
        if not (1 <= len(d) <= 2000):
            errors.append(f"分类 {k} description 长度不合规")
    # 资源存在性
    memes = os.path.join(PACK, "memes")
    for k in cats:
        p = os.path.join(memes, k)
        if not os.path.isdir(p):
            errors.append(f"memes/{k} 目录不存在")
        elif not [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]:
            errors.append(f"memes/{k} 为空")
    for sub in sorted(os.listdir(memes)):
        if os.path.isdir(os.path.join(memes, sub)) and sub not in cats:
            errors.append(f"memes/{sub} 未在 categories 中声明")
    # 图片结构检查：memes/<category>/<image> 且无嵌套
    for k in cats:
        p = os.path.join(memes, k)
        if os.path.isdir(p):
            for f in os.listdir(p):
                fp = os.path.join(p, f)
                if os.path.isdir(fp):
                    errors.append(f"memes/{k}/{f} 不应是目录")
                elif not f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                    errors.append(f"memes/{k}/{f} 格式不在规范内")
    for rel in ([manifest.get("icon")] if manifest.get("icon") else []) + manifest.get("previews", []):
        if not rel:
            continue
        if rel.startswith("/") or ".." in rel or "\\" in rel:
            errors.append(f"路径不合规: {rel}")
        elif not os.path.exists(os.path.join(PACK, rel.replace("/", os.sep))):
            errors.append(f"引用的文件不存在: {rel}")
    if len(manifest.get("previews", [])) > 32:
        errors.append("previews 超过 32 个")
    return errors


def rebuild_index():
    """重建总览 HTML 与 CSV（路径改为 官方表情包/memes/<key>/...）"""
    memes = os.path.join(PACK, "memes")
    previews_dir = os.path.join(PACK, "previews")
    sections, nav, total = [], [], 0
    for idx, cn, key, cnt in SERIES:
        p = os.path.join(memes, key)
        imgs = sorted(f for f in os.listdir(p) if f.lower().endswith((".png", ".gif", ".jpg")))
        total += len(imgs)
        cards = "\n".join(
            f'<figure><img loading="lazy" src="官方表情包/memes/{key}/{f}" alt="{f}"><figcaption>{os.path.splitext(f)[0]}</figcaption></figure>'
            for f in imgs)
        sections.append(f'<section id="{key}"><h2>{idx:02d} {cn} <small>{len(imgs)} 张</small></h2><div class="grid">{cards}</div></section>')
        nav.append(f'<a href="#{key}">{idx:02d} {cn}</a>')

    posters = sorted(f for f in os.listdir(previews_dir) if f.lower().endswith((".jpg", ".png")))
    poster_cards = "\n".join(
        f'<figure><img loading="lazy" src="官方表情包/previews/{f}" alt="{f}"><figcaption>{os.path.splitext(f)[0]}</figcaption></figure>'
        for f in posters)
    poster_section = f'<section id="posters"><h2>官方宣传海报 <small>{len(posters)} 张</small></h2><div class="grid poster">{poster_cards}</div></section>'

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>《重返未来：1999》官方表情包总览</title>
<style>
  body {{ font-family: "Microsoft YaHei", system-ui, sans-serif; background:#f5f3ef; color:#2b2b2b; margin:0; padding:24px 32px 64px; }}
  h1 {{ font-size:22px; margin:0 0 6px; }}
  .meta {{ color:#777; font-size:13px; margin-bottom:16px; }}
  nav {{ font-size:12px; line-height:1.9; background:#fff; border:1px solid #e3ded6; padding:10px 14px; border-radius:8px; margin-bottom:24px; }}
  nav a {{ color:#5a6b7d; text-decoration:none; margin-right:2px; }}
  nav a:hover {{ color:#b3261e; }}
  section {{ margin-bottom:28px; background:#fff; border:1px solid #e3ded6; border-radius:10px; padding:14px 16px; }}
  h2 {{ font-size:16px; margin:0 0 12px; border-left:4px solid #c8a86b; padding-left:10px; }}
  h2 small {{ color:#999; font-weight:normal; font-size:12px; margin-left:6px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(112px,1fr)); gap:12px; }}
  .grid.poster {{ grid-template-columns:repeat(auto-fill, minmax(210px,1fr)); }}
  figure {{ margin:0; text-align:center; }}
  figcaption {{ font-size:10px; color:#999; margin-top:4px; word-break:break-all; }}
  img {{ width:100%; max-width:120px; background:#faf8f4; border:1px solid #eee; border-radius:8px; }}
  .grid.poster img {{ max-width:210px; border-radius:6px; }}
</style>
</head>
<body>
<h1>《重返未来：1999》官方表情包总览</h1>
<div class="meta">共 {len(SERIES)} 个官方系列、{total} 张表情图 + {len(posters)} 张官方海报 ·
包根目录：<code>官方表情包/</code>（AstrBot 表情包格式）·
来源：<a href="https://res1999.huijiwiki.com/wiki/官方多媒体/表情包">官方多媒体/表情包</a></div>
<nav>{' · '.join(nav)} · <a href="#posters">官方宣传海报</a></nav>
{''.join(sections)}
{poster_section}
</body>
</html>
"""
    with open(os.path.join(ROOT, "表情包总览.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"表情包总览.html: {len(html)} 字符")

    rows = []
    for idx, cn, key, cnt in SERIES:
        p = os.path.join(memes, key)
        for f in sorted(os.listdir(p)):
            fp = os.path.join(p, f)
            rows.append({
                "Series": f"{idx:02d}_{cn}", "Category": key, "FileName": f,
                "SizeKB": round(os.path.getsize(fp) / 1024, 1),
                "RelPath": f"官方表情包/memes/{key}/{f}",
            })
    with open(os.path.join(ROOT, "表情包清单.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Series", "Category", "FileName", "SizeKB", "RelPath"])
        w.writeheader()
        w.writerows(rows)
    print(f"表情包清单.csv: {len(rows)} 行")


def main():
    print("1) 移动表情图到 memes/<分类>/")
    move_series()
    print("2) 移动海报与文档")
    move_assets()
    print("3) 生成 manifest.json")
    m = build_manifest()
    print("4) 校验")
    errs = validate(m)
    if errs:
        print("校验失败:")
        for e in errs[:40]:
            print("  -", e)
    else:
        print("校验通过 ✓")
    print("5) 重建总览 HTML / CSV")
    rebuild_index()

    # 最终统计
    files = 0
    for base, _, fs in os.walk(PACK):
        files += len(fs)
    print(f"包内文件数: {files}")


if __name__ == "__main__":
    main()
