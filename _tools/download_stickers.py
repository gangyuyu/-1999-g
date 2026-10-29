# -*- coding: utf-8 -*-
"""
下载《重返未来：1999》官方表情包（全部已发布系列）。
数据来源：灰机 wiki 「官方多媒体/表情包」页面收录的官方图片直链
          https://res1999.huijiwiki.com/wiki/官方多媒体/表情包
图片 CDN：huiji-public.huijistatic.com（MediaWiki 上传目录，路径 = MD5(文件名)）
"""
import hashlib
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = r"C:\桌面\素材\人物素材\表情包\官方表情包"
CDN = "https://huiji-public.huijistatic.com/res1999/uploads"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")


def file_url(name: str) -> str:
    h = hashlib.md5(name.encode("utf-8")).hexdigest()
    return f"{CDN}/{h[0]}/{h[:2]}/{urllib.parse.quote(name, safe='')}"


# ---- 各系列与文件名规则 -------------------------------------------------
# 1-22 使用「考据-表情包-NN_MMMM.png」全局顺序编号（编号不连续）
# 23-39 使用「表情包-NN-01..16.png」
# 40-51 使用「表情包-系列名-01..16.png」
KAOJU = [
    (1,  "敲响心灵",   [range(101, 109)]),
    (2,  "公测上线",   [range(109, 125)]),
    (3,  "摩卢旁卡",   [range(125, 141)]),
    (4,  "洞穴囚徒",   [range(141, 155), range(163, 165)]),
    (5,  "一路发发发", [range(155, 163)]),
    (6,  "乌卢鲁",     [range(165, 181)]),
    (7,  "朔日手记",   [range(181, 197)]),
    (8,  "春节贺岁",   [range(100, 105), range(197, 200)]),
    (9,  "星光灿烂",   [range(105, 121)]),
    (10, "来亚什基",   [range(121, 137)]),
    (11, "孤独之歌",   [range(137, 153)]),
    (12, "悠长夏日",   [range(153, 161)]),
    (13, "明日之城",   [range(161, 177)]),
    (14, "77号往事",   [range(177, 193)]),
    (15, "忧郁热带",   [range(100, 109), range(193, 200)]),
    (16, "东区黎明",   [range(109, 125)]),
    (17, "箱中运动会", [range(125, 133)]),
    (18, "途中留影",   [range(133, 141)]),
    (19, "地球终夜",   [range(141, 157)]),
    (20, "落雪前夜",   [range(157, 165)]),
    (21, "喜迎春至",   [range(172, 173), range(165, 172)]),
    (22, "唐人街影话", [range(173, 189)]),
]

# 23-39：按编号命名
NUMERIC = [
    (23, "玩1999享厘普人生", 16),
    (24, "疯癫文明", 16),
    (25, "宇宙组曲", 16),
    (26, "复乐园", 16),
    (27, "箱中雪景", 8),
    (28, "箱中假面", 16),
    (29, "漫漫长路", 16),
    (30, "箱中漫游", 8),
    (31, "信仰之跃", 16),
    (32, "长夜鸣笛", 16),
    (33, "迁流的盛宴", 16),
    (34, "解与答的研思", 8),
    (35, "箱中栖语", 8),
    (36, "远征记", 16),
    (37, "三仙过海", 8),
    (38, "不老春", 16),
    (39, "箱中岁暖", 8),
]

# 40-51：按系列名命名
NAMED = [
    (40, "绿松石蛇", 16),
    (41, "人们何去", 8),
    (42, "箱中逗趣", 8),
    (43, "箱中电影节", 8),
    (44, "他者悲哀", 16),
    (45, "次元奇旅", 8),
    (46, "世纪尺度", 16),
    (47, "箱中缝缝补", 32),
    (48, "聚合浪潮", 8),
    (49, "对策部", 16),
    (50, "流金之海", 16),
    (51, "奇妙9堡", 16),
]

# 22 号系列同时有 GIF 与 PNG 两套
GIF_NAMES = [f"考据-表情包-22_{n}.gif" for n in range(173, 189)]
PNG_NAMES = [f"考据-表情包-22_{n}-p.png" for n in range(173, 189)]


def build_jobs():
    """返回 [(系列序号, 系列名, 文件名), ...]"""
    jobs = []
    for idx, name, ranges in KAOJU:
        for r in ranges:
            for n in r:
                fn = f"考据-表情包-{idx:02d}_{n:04d}.png"
                if idx == 22:
                    continue  # 22 单独处理
                jobs.append((idx, name, fn))
    for fn in GIF_NAMES:
        jobs.append((22, "唐人街影话", fn))
    for fn in PNG_NAMES:
        jobs.append((22, "唐人街影话", fn))
    for idx, name, cnt in NUMERIC:
        for n in range(1, cnt + 1):
            jobs.append((idx, name, f"表情包-{idx}-{n:02d}.png"))
    for idx, name, cnt in NAMED:
        for n in range(1, cnt + 1):
            jobs.append((idx, name, f"表情包-{name}-{n:02d}.png"))
    return jobs


def download(url, dest, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://res1999.huijiwiki.com/"})
            with urllib.request.urlopen(req, timeout=45) as r:
                data = r.read()
            if not data:
                raise ValueError("empty body")
            tmp = dest + ".part"
            with open(tmp, "wb") as f:
                f.write(data)
            os.replace(tmp, dest)
            return True, len(data)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return False, "404"
            if attempt == retries - 1:
                return False, f"HTTP {e.code}"
        except Exception as e:
            if attempt == retries - 1:
                return False, repr(e)
        time.sleep(0.6 * (attempt + 1))
    return False, "unknown"


def main():
    jobs = build_jobs()
    print(f"计划下载 {len(jobs)} 张", flush=True)
    os.makedirs(BASE, exist_ok=True)
    results = []
    lock_ok = 0

    def work(job):
        idx, name, fn = job
        folder = os.path.join(BASE, f"{idx:02d}_{name}")
        dest = os.path.join(folder, fn)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            return (idx, name, fn, "skip", os.path.getsize(dest))
        os.makedirs(folder, exist_ok=True)
        ok, info = download(file_url(fn), dest)
        return (idx, name, fn, "ok" if ok else "fail", info)

    with ThreadPoolExecutor(max_workers=10) as pool:
        futs = [pool.submit(work, j) for j in jobs]
        for i, f in enumerate(as_completed(futs), 1):
            results.append(f.result())
            if i % 50 == 0 or i == len(jobs):
                print(f"进度 {i}/{len(jobs)}", flush=True)

    ok = [r for r in results if r[3] in ("ok", "skip")]
    fail = [r for r in results if r[3] == "fail"]
    print(f"\n成功/已存在: {len(ok)}  失败: {len(fail)}")
    for r in fail[:40]:
        print("  FAIL", r[0], r[1], r[2], r[4])

    # 汇总
    summary = {}
    for idx, name, fn, st, info in results:
        d = summary.setdefault(f"{idx:02d}_{name}", {"series": name, "index": idx, "ok": 0, "fail": 0, "bytes": 0})
        if st in ("ok", "skip"):
            d["ok"] += 1
            d["bytes"] += info if isinstance(info, int) else 0
        else:
            d["fail"] += 1

    # 海报
    poster_dir = os.path.join(BASE, "_官方海报")
    os.makedirs(poster_dir, exist_ok=True)
    poster_names = [f"表情包-{n}.jpg" for _, n, _ in [(i, n, c) for i, n, c in KAOJU] +
                    [(i, n, c) for i, n, c in NUMERIC] + [(i, n, c) for i, n, c in NAMED]]
    poster_names.append("表情包-箱中缝缝补2.jpg")
    poster_fail = []
    def pw(fn):
        dest = os.path.join(poster_dir, fn)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            return (fn, "skip")
        ok_, info = download(file_url(fn), dest)
        return (fn, "ok" if ok_ else "fail")
    with ThreadPoolExecutor(max_workers=8) as pool:
        for fn, st in pool.map(pw, poster_names):
            if st == "fail":
                poster_fail.append(fn)
    print(f"海报: {len(poster_names) - len(poster_fail)}/{len(poster_names)}，缺失 {poster_fail}")

    with open(os.path.join(BASE, "_manifest.json"), "w", encoding="utf-8") as f:
        json.dump({"source": "https://res1999.huijiwiki.com/wiki/官方多媒体/表情包",
                   "total_planned": len(jobs),
                   "total_ok": len(ok), "total_fail": len(fail),
                   "series": [summary[k] for k in sorted(summary)],
                   "poster_missing": poster_fail}, f, ensure_ascii=False, indent=2)

    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
