# -*- coding: utf-8 -*-
"""生成表情包总览 HTML（纯本地，无网络依赖）"""
import os
import re

ROOT = r"C:\桌面\素材\人物素材\表情包\官方表情包"
OUT = os.path.join(ROOT, "_表情包总览.html")

dirs = sorted([d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)) and d != "_官方海报"])
poster_dir = os.path.join(ROOT, "_官方海报")
posters = sorted(os.listdir(poster_dir)) if os.path.isdir(poster_dir) else []

total = 0
sections = []
for d in dirs:
    p = os.path.join(ROOT, d)
    imgs = sorted([f for f in os.listdir(p) if f.lower().endswith((".png", ".gif", ".jpg"))])
    total += len(imgs)
    cards = "\n".join(
        f'<figure><img loading="lazy" src="{d}/{f}" alt="{f}"><figcaption>{os.path.splitext(f)[0]}</figcaption></figure>'
        for f in imgs
    )
    sections.append(f'<section id="{d}"><h2>{d} <small>{len(imgs)} 张</small></h2><div class="grid">{cards}</div></section>')

poster_cards = "\n".join(
    f'<figure><img loading="lazy" src="_官方海报/{f}" alt="{f}"><figcaption>{os.path.splitext(f)[0]}</figcaption></figure>'
    for f in posters
)
poster_section = f'<section id="posters"><h2>官方宣传海报 <small>{len(posters)} 张</small></h2><div class="grid poster">{poster_cards}</div></section>'

nav = " · ".join(f'<a href="#{d}">{d}</a>' for d in dirs)

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
  img {{ width:100%; max-width:120px; background:#faf8f4; border:1px solid #eee; border-radius:8px; image-rendering:auto; }}
  .grid.poster img {{ max-width:210px; border-radius:6px; }}
</style>
</head>
<body>
<h1>《重返未来：1999》官方表情包总览</h1>
<div class="meta">共 {len(dirs)} 个官方系列、{total} 张表情图 + {len(posters)} 张官方海报 ·
图片来源：灰机 wiki 收录的官方发布图集 <a href="https://res1999.huijiwiki.com/wiki/官方多媒体/表情包">官方多媒体/表情包</a></div>
<nav>{nav} · <a href="#posters">官方宣传海报</a></nav>
{''.join(sections)}
{poster_section}
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("生成:", OUT, len(html), "字符; 系列", len(dirs), "表情图", total, "海报", len(posters))
