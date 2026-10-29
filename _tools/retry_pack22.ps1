# 补下 22 号系列「唐人街影话」（GIF 16 张 + PNG 16 张）
# 说明：并发批次下 CDN 偶发把已存在文件返回 404，这里改为顺序请求 + 多次重试
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Net.Http
$Base = "C:\桌面\素材\人物素材\表情包\官方表情包\22_唐人街影话"
$Cdn  = "https://huiji-public.huijistatic.com/res1999/uploads"
$UA   = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
New-Item -ItemType Directory -Force -Path $Base | Out-Null
$md5 = [System.Security.Cryptography.MD5]::Create()
function Get-FileUrl([string]$name) {
    $h = -join ($md5.ComputeHash([Text.Encoding]::UTF8.GetBytes($name)) | ForEach-Object { $_.ToString("x2") })
    return "$Cdn/$($h.Substring(0,1))/$($h.Substring(0,2))/" + [Uri]::EscapeDataString($name)
}
$h = New-Object System.Net.Http.HttpClientHandler
$c = New-Object System.Net.Http.HttpClient($h)
$c.Timeout = [TimeSpan]::FromSeconds(60)
$c.DefaultRequestHeaders.UserAgent.ParseAdd($UA)
$c.DefaultRequestHeaders.Referrer = [Uri]"https://res1999.huijiwiki.com/"

$names = @()
foreach ($n in 173..188) { $names += "考据-表情包-22_$n.gif"; $names += "考据-表情包-22_$n-p.png" }
$ok = 0; $bad = @()
foreach ($name in $names) {
    $dest = Join-Path $Base $name
    if ((Test-Path $dest) -and ((Get-Item $dest).Length -gt 500)) { $ok++; continue }
    $got = $false
    for ($t = 0; $t -lt 6; $t++) {
        try {
            $r = $c.GetAsync((Get-FileUrl $name)).GetAwaiter().GetResult()
            if ($r.IsSuccessStatusCode) {
                $b = $r.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult()
                if ($b.Length -ge 500) { [IO.File]::WriteAllBytes($dest, $b); $ok++; $got = $true; break }
            }
        } catch { }
        Start-Sleep -Milliseconds (700 * ($t + 1))
    }
    if (-not $got) { $bad += $name }
}
"成功: $ok / $($names.Count)"
if ($bad.Count) { "失败: $($bad -join ', ')" } else { "全部完成" }
