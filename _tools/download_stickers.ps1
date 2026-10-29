# 下载《重返未来：1999》全部官方表情包（数据源：灰机 wiki「官方多媒体/表情包」收录的官方图集）
# 图片 CDN 路径规则 = /uploads/<md5[0]>/<md5[0..1]>/<urlencode 文件名>
# 使用 .NET HttpClient（Schannel TLS），Python urllib 会被 CDN 以 567 拒绝
$ErrorActionPreference = "Stop"
$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8
Add-Type -AssemblyName System.Net.Http

$Base = "C:\桌面\素材\人物素材\表情包\官方表情包"
$Cdn  = "https://huiji-public.huijistatic.com/res1999/uploads"
$UA   = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

$md5 = [System.Security.Cryptography.MD5]::Create()
function Get-FileUrl([string]$name) {
    $h = -join ($md5.ComputeHash([Text.Encoding]::UTF8.GetBytes($name)) | ForEach-Object { $_.ToString("x2") })
    $enc = [Uri]::EscapeDataString($name)
    return "$Cdn/$($h.Substring(0,1))/$($h.Substring(0,2))/$enc"
}

# ---------- 系列清单 ----------
$kaoju = @(
    @{ i = 1;  n = "敲响心灵";   nums = @(101..108) },
    @{ i = 2;  n = "公测上线";   nums = @(109..124) },
    @{ i = 3;  n = "摩卢旁卡";   nums = @(125..140) },
    @{ i = 4;  n = "洞穴囚徒";   nums = @(141..154) + @(163..164) },
    @{ i = 5;  n = "一路发发发"; nums = @(155..162) },
    @{ i = 6;  n = "乌卢鲁";     nums = @(165..180) },
    @{ i = 7;  n = "朔日手记";   nums = @(181..196) },
    @{ i = 8;  n = "春节贺岁";   nums = @(100..104) + @(197..199) },
    @{ i = 9;  n = "星光灿烂";   nums = @(105..120) },
    @{ i = 10; n = "来亚什基";   nums = @(121..136) },
    @{ i = 11; n = "孤独之歌";   nums = @(137..152) },
    @{ i = 12; n = "悠长夏日";   nums = @(153..160) },
    @{ i = 13; n = "明日之城";   nums = @(161..176) },
    @{ i = 14; n = "77号往事";   nums = @(177..192) },
    @{ i = 15; n = "忧郁热带";   nums = @(100..108) + @(193..199) },
    @{ i = 16; n = "东区黎明";   nums = @(109..124) },
    @{ i = 17; n = "箱中运动会"; nums = @(125..132) },
    @{ i = 18; n = "途中留影";   nums = @(133..140) },
    @{ i = 19; n = "地球终夜";   nums = @(141..156) },
    @{ i = 20; n = "落雪前夜";   nums = @(157..164) },
    @{ i = 21; n = "喜迎春至";   nums = @(172) + @(165..171) },
    @{ i = 22; n = "唐人街影话"; nums = @() }
)
$numeric = @(
    @{ i = 23; n = "玩1999享厘普人生"; c = 16 }, @{ i = 24; n = "疯癫文明"; c = 16 },
    @{ i = 25; n = "宇宙组曲"; c = 16 },         @{ i = 26; n = "复乐园"; c = 16 },
    @{ i = 27; n = "箱中雪景"; c = 8 },          @{ i = 28; n = "箱中假面"; c = 16 },
    @{ i = 29; n = "漫漫长路"; c = 16 },         @{ i = 30; n = "箱中漫游"; c = 8 },
    @{ i = 31; n = "信仰之跃"; c = 16 },         @{ i = 32; n = "长夜鸣笛"; c = 16 },
    @{ i = 33; n = "迁流的盛宴"; c = 16 },       @{ i = 34; n = "解与答的研思"; c = 8 },
    @{ i = 35; n = "箱中栖语"; c = 8 },          @{ i = 36; n = "远征记"; c = 16 },
    @{ i = 37; n = "三仙过海"; c = 8 },          @{ i = 38; n = "不老春"; c = 16 },
    @{ i = 39; n = "箱中岁暖"; c = 8 }
)
$named = @(
    @{ i = 40; n = "绿松石蛇"; c = 16 },   @{ i = 41; n = "人们何去"; c = 8 },
    @{ i = 42; n = "箱中逗趣"; c = 8 },    @{ i = 43; n = "箱中电影节"; c = 8 },
    @{ i = 44; n = "他者悲哀"; c = 16 },   @{ i = 45; n = "次元奇旅"; c = 8 },
    @{ i = 46; n = "世纪尺度"; c = 16 },   @{ i = 47; n = "箱中缝缝补"; c = 32 },
    @{ i = 48; n = "聚合浪潮"; c = 8 },    @{ i = 49; n = "对策部"; c = 16 },
    @{ i = 50; n = "流金之海"; c = 16 },   @{ i = 51; n = "奇妙9堡"; c = 16 }
)

$jobs = New-Object System.Collections.ArrayList
foreach ($p in $kaoju) {
    if ($p.i -eq 22) { continue }
    foreach ($num in $p.nums) {
        [void]$jobs.Add([pscustomobject]@{
            i = $p.i; n = $p.n; folder = ("{0:D2}_{1}" -f $p.i, $p.n);
            file = ("考据-表情包-{0:D2}_{1:D4}.png" -f $p.i, $num) })
    }
}
foreach ($num in 173..188) {
    [void]$jobs.Add([pscustomobject]@{ i = 22; n = "唐人街影话"; folder = "22_唐人街影话"; file = "考据-表情包-22_$num.gif" })
    [void]$jobs.Add([pscustomobject]@{ i = 22; n = "唐人街影话"; folder = "22_唐人街影话"; file = "考据-表情包-22_$num-p.png" })
}
foreach ($p in $numeric) {
    for ($k = 1; $k -le $p.c; $k++) {
        [void]$jobs.Add([pscustomobject]@{ i = $p.i; n = $p.n; folder = ("{0:D2}_{1}" -f $p.i, $p.n);
            file = ("表情包-{0}-{1:D2}.png" -f $p.i, $k) })
    }
}
foreach ($p in $named) {
    for ($k = 1; $k -le $p.c; $k++) {
        [void]$jobs.Add([pscustomobject]@{ i = $p.i; n = $p.n; folder = ("{0:D2}_{1}" -f $p.i, $p.n);
            file = ("表情包-{0}-{1:D2}.png" -f $p.n, $k) })
    }
}

New-Item -ItemType Directory -Force -Path $Base | Out-Null

$handler = New-Object System.Net.Http.HttpClientHandler
$client  = New-Object System.Net.Http.HttpClient($handler)
$client.Timeout = [TimeSpan]::FromSeconds(60)
$client.DefaultRequestHeaders.UserAgent.ParseAdd($UA)
$client.DefaultRequestHeaders.Referrer = [Uri]"https://res1999.huijiwiki.com/"

$total = $jobs.Count
Write-Output "计划下载: $total 张"
$ok = 0; $skip = 0; $fail = 0
$failList = New-Object System.Collections.ArrayList
$seriesStat = @{}

function Save-One($job) {
    $dir = Join-Path $Base $job.folder
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    $dest = Join-Path $dir $job.file
    if ((Test-Path $dest) -and ((Get-Item $dest).Length -gt 500)) { return "skip" }
    $url = Get-FileUrl $job.file
    for ($try = 0; $try -lt 3; $try++) {
        try {
            $resp = $client.GetAsync($url).GetAwaiter().GetResult()
            if (-not $resp.IsSuccessStatusCode) {
                if ([int]$resp.StatusCode -eq 404) { return "404" }
                Start-Sleep -Milliseconds (300 * ($try + 1)); continue
            }
            $bytes = $resp.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult()
            if ($bytes.Length -lt 500) { Start-Sleep -Milliseconds 300; continue }
            [IO.File]::WriteAllBytes($dest, $bytes)
            return "ok"
        } catch {
            Start-Sleep -Milliseconds (400 * ($try + 1))
        }
    }
    return "fail"
}

$sw = [Diagnostics.Stopwatch]::StartNew()
$batchSize = 24
for ($s = 0; $s -lt $total; $s += $batchSize) {
    $end = [Math]::Min($s + $batchSize - 1, $total - 1)
    $batch = $jobs[$s..$end]
    $rs = @{}
    $tasks = @{}
    foreach ($job in $batch) {
        $dir = Join-Path $Base $job.folder
        if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
        $dest = Join-Path $dir $job.file
        if ((Test-Path $dest) -and ((Get-Item $dest).Length -gt 500)) { $rs[$job.file] = "skip"; continue }
        $url = Get-FileUrl $job.file
        $tasks[$job.file] = $client.GetAsync($url)
    }
    # 等待本批
    if ($tasks.Count -gt 0) {
        [Threading.Tasks.Task]::WaitAll([Threading.Tasks.Task[]]$tasks.Values)
        foreach ($k in $tasks.Keys) {
            $job = $batch | Where-Object { $_.file -eq $k } | Select-Object -First 1
            $resp = $tasks[$k].Result
            if ($resp.IsSuccessStatusCode) {
                $bytes = $resp.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult()
                if ($bytes.Length -ge 500) {
                    [IO.File]::WriteAllBytes((Join-Path (Join-Path $Base $job.folder) $job.file), $bytes)
                    $rs[$k] = "ok"
                } else { $rs[$k] = "fail" }
            } elseif ([int]$resp.StatusCode -eq 404) { $rs[$k] = "404" } else { $rs[$k] = "fail" }
        }
    }
    foreach ($job in $batch) {
        $st = $rs[$job.file]
        $key = $job.folder
        if (-not $seriesStat.ContainsKey($key)) { $seriesStat[$key] = @{ ok = 0; fail = 0 } }
        switch ($st) {
            "ok"   { $ok++;   $seriesStat[$key].ok++ }
            "skip" { $skip++; $seriesStat[$key].ok++ }
            default { $fail++; $seriesStat[$key].fail++; [void]$failList.Add("$($job.folder)/$($job.file) [$st]") }
        }
    }
    if ((($s / $batchSize) % 5) -eq 0 -or $end -eq ($total - 1)) {
        Write-Output ("进度 {0}/{1}  成功 {2} 跳过 {3} 失败 {4}  用时 {5:N0}s" -f ($end + 1), $total, $ok, $skip, $fail, $sw.Elapsed.TotalSeconds)
    }
}

Write-Output "==================== 完成 ===================="
Write-Output "成功: $ok  已存在跳过: $skip  失败: $fail  总计划: $total"
if ($failList.Count -gt 0) { Write-Output "失败清单:"; $failList | ForEach-Object { Write-Output "  $_" } }
$seriesStat.GetEnumerator() | Sort-Object Name | ForEach-Object { Write-Output ("  {0}: ok={1} fail={2}" -f $_.Key, $_.Value.ok, $_.Value.fail) }

# ---------- 官方海报 ----------
$posterDir = Join-Path $Base "_官方海报"
New-Item -ItemType Directory -Force -Path $posterDir | Out-Null
$posterNames = @()
foreach ($p in ($kaoju + $numeric + $named)) { if ($p.n -ne "唐人街影话") { $posterNames += "表情包-$($p.n).jpg" } }
$posterNames += "表情包-唐人街影话.jpg"
$posterNames += "表情包-箱中缝缝补2.jpg"
$pTasks = @{}
foreach ($pn in $posterNames) {
    $dest = Join-Path $posterDir $pn
    if ((Test-Path $dest) -and ((Get-Item $dest).Length -gt 500)) { continue }
    $pTasks[$pn] = $client.GetAsync((Get-FileUrl $pn))
}
if ($pTasks.Count -gt 0) {
    [Threading.Tasks.Task]::WaitAll([Threading.Tasks.Task[]]$pTasks.Values)
    $pok = 0
    foreach ($k in $pTasks.Keys) {
        $resp = $pTasks[$k].Result
        if ($resp.IsSuccessStatusCode) {
            $bytes = $resp.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult()
            [IO.File]::WriteAllBytes((Join-Path $posterDir $k), $bytes); $pok++
        }
    }
    Write-Output "海报下载: $pok 张"
}

# ---------- 清单 ----------
$manifest = [ordered]@{
    source      = "https://res1999.huijiwiki.com/wiki/官方多媒体/表情包"
    downloadedAt = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    totalPlanned = $total
    totalOk      = $ok + $skip
    totalFail    = $fail
    series       = $seriesStat
    failed       = $failList
}
$manifest | ConvertTo-Json -Depth 5 | Out-File -FilePath (Join-Path $Base "_下载清单.json") -Encoding utf8

$all = Get-ChildItem -Recurse -File $Base -Exclude "_下载清单.json"
Write-Output ("实际文件数: {0}  体积: {1:N2} MB" -f $all.Count, (($all | Measure-Object Length -Sum).Sum / 1MB))
