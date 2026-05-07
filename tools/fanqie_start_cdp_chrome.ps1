param(
    [string]$Url = "https://fanqienovel.com/main/writer/7628203489469942846/publish/?enter_from=newchapter_0",
    [string]$ProfileDir = "D:\fanqie-novel\.pw-fanqie-profile",
    [int]$Port = 9222
)

$ErrorActionPreference = "Stop"

try {
    $response = Invoke-WebRequest -UseBasicParsing "http://127.0.0.1:$Port/json/version" -TimeoutSec 3
    Write-Output "CDP already available at http://127.0.0.1:$Port"
    Write-Output $response.Content
    exit 0
} catch {
    Write-Output "CDP not available, starting Chrome..."
}

$chromeCandidates = @(
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
)

$chrome = $chromeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $chrome) {
    throw "Chrome executable not found."
}

New-Item -ItemType Directory -Force -Path $ProfileDir | Out-Null

$args = @(
    "--remote-debugging-address=127.0.0.1",
    "--remote-debugging-port=$Port",
    "--user-data-dir=$ProfileDir",
    "--profile-directory=Default",
    "--no-first-run",
    "--no-default-browser-check",
    "--new-window",
    $Url
)

Start-Process -FilePath $chrome -ArgumentList $args -WindowStyle Hidden
Start-Sleep -Seconds 3

$response = Invoke-WebRequest -UseBasicParsing "http://127.0.0.1:$Port/json/version" -TimeoutSec 10
Write-Output "CDP available at http://127.0.0.1:$Port"
Write-Output $response.Content
