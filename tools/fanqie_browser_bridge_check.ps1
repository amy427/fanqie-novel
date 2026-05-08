param(
    [switch]$StartCdp,
    [switch]$OpenExtensionStore,
    [int]$Port = 9222,
    [string]$FanqieUrl = "https://fanqienovel.com/main/writer/7628203489469942846/publish/?enter_from=newchapter_0",
    [string]$CodexExtensionId = "hehggadaopoacecdllhajmbjkdcmajg"
)

$ErrorActionPreference = "Stop"

function Write-Check {
    param(
        [string]$Name,
        [string]$Status,
        [string]$Detail = ""
    )

    if ($Detail) {
        Write-Output ("[{0}] {1}: {2}" -f $Status, $Name, $Detail)
    } else {
        Write-Output ("[{0}] {1}" -f $Status, $Name)
    }
}

function Get-CdpVersion {
    param([int]$CheckPort)

    try {
        return Invoke-RestMethod -Uri "http://127.0.0.1:$CheckPort/json/version" -TimeoutSec 3
    } catch {
        return $null
    }
}

function Find-Chrome {
    $candidates = @(
        "C:\Program Files\Google\Chrome\Application\chrome.exe",
        "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    )

    return $candidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
}

function Find-CodexExtension {
    param([string]$ExtensionId)

    $locations = New-Object System.Collections.Generic.List[string]
    $userData = Join-Path $env:LOCALAPPDATA "Google\Chrome\User Data"
    if (Test-Path -LiteralPath $userData) {
        $profiles = Get-ChildItem -LiteralPath $userData -Directory -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -eq "Default" -or $_.Name -like "Profile *" }
        foreach ($profile in $profiles) {
            $extensionPath = Join-Path $profile.FullName "Extensions\$ExtensionId"
            if (Test-Path -LiteralPath $extensionPath) {
                $locations.Add($extensionPath)
            }
        }
    }

    $repoRoot = Split-Path -Parent $PSScriptRoot
    $projectCandidates = @(
        (Join-Path $repoRoot ".pw-fanqie-profile\Extensions\$ExtensionId"),
        (Join-Path $repoRoot ".pw-fanqie-profile\Default\Extensions\$ExtensionId")
    )
    foreach ($path in $projectCandidates) {
        if (Test-Path -LiteralPath $path) {
            $locations.Add($path)
        }
    }

    return $locations
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$chrome = Find-Chrome
$python = Get-Command python -ErrorAction SilentlyContinue

Write-Output "Fanqie browser bridge check"
Write-Output ("Repo: {0}" -f $repoRoot)
Write-Output ("CDP: http://127.0.0.1:{0}" -f $Port)

if ($python) {
    Write-Check "python" "OK" $python.Source
} else {
    Write-Check "python" "FAIL" "not found on PATH"
}

if ($chrome) {
    Write-Check "Chrome" "OK" $chrome
} else {
    Write-Check "Chrome" "FAIL" "chrome.exe not found in standard install paths"
}

$cdp = Get-CdpVersion -CheckPort $Port
if (-not $cdp -and $StartCdp) {
    $starter = Join-Path $PSScriptRoot "fanqie_start_cdp_chrome.ps1"
    if (-not (Test-Path -LiteralPath $starter)) {
        throw "CDP starter script not found: $starter"
    }
    Write-Check "CDP startup" "RUN" "starting Chrome through fanqie_start_cdp_chrome.ps1"
    & powershell -ExecutionPolicy Bypass -File $starter -Url $FanqieUrl -Port $Port
    Start-Sleep -Seconds 2
    $cdp = Get-CdpVersion -CheckPort $Port
}

if ($cdp) {
    Write-Check "CDP" "OK" ("{0} / {1}" -f $cdp.Browser, $cdp.webSocketDebuggerUrl)
    try {
        $tabs = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/json/list" -TimeoutSec 3
        $fanqieTabs = @($tabs | Where-Object { $_.url -like "*fanqienovel.com*" })
        Write-Check "Fanqie CDP tabs" "INFO" ("{0} of {1} tabs" -f $fanqieTabs.Count, @($tabs).Count)
        foreach ($tab in $fanqieTabs | Select-Object -First 5) {
            Write-Output ("  - {0}" -f $tab.title)
            Write-Output ("    {0}" -f $tab.url)
        }
    } catch {
        Write-Check "CDP tab list" "WARN" $_.Exception.Message
    }
} else {
    Write-Check "CDP" "FAIL" "not reachable; rerun with -StartCdp or start Chrome with remote debugging"
}

$extensionLocations = @(Find-CodexExtension -ExtensionId $CodexExtensionId)
if ($extensionLocations.Count -gt 0) {
    Write-Check "Codex Chrome extension" "OK" ("found {0} install location(s)" -f $extensionLocations.Count)
    foreach ($location in $extensionLocations) {
        Write-Output ("  - {0}" -f $location)
    }
} else {
    Write-Check "Codex Chrome extension" "WARN" ("not found locally for extension id {0}" -f $CodexExtensionId)
}

if ($OpenExtensionStore) {
    if (-not $chrome) {
        throw "Cannot open Chrome Web Store because Chrome was not found."
    }
    $storeUrl = "https://chromewebstore.google.com/detail/codex/$CodexExtensionId"
    Start-Process -FilePath $chrome -ArgumentList @("--new-window", $storeUrl)
    Write-Check "Chrome Web Store" "OPENED" $storeUrl
}
