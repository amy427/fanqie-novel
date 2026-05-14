param(
    [switch]$PersistUserPath
)

$ErrorActionPreference = "Stop"

$candidateDirs = @(
    "C:\Users\26030\AppData\Local\Python\bin",
    "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Scripts",
    "C:\Users\26030\AppData\Local\Programs\Python\Python314",
    "C:\Users\26030\AppData\Local\Programs\Python\Python314\Scripts",
    "C:\Users\26030\AppData\Local\Programs\Python\Python311",
    "C:\Users\26030\AppData\Local\Programs\Python\Python311\Scripts"
) | Where-Object { Test-Path $_ }

if ($candidateDirs.Count -eq 0) {
    throw "No local Python installation directories were found."
}

$currentParts = $env:Path -split ";" | Where-Object { $_ -and $_.Trim() -ne "" }
$merged = New-Object System.Collections.Generic.List[string]
foreach ($p in $candidateDirs + $currentParts) {
    if (-not ($merged | Where-Object { $_.TrimEnd("\") -ieq $p.TrimEnd("\") })) {
        [void]$merged.Add($p)
    }
}
$env:Path = ($merged -join ";")

if ($PersistUserPath) {
    $userParts = [Environment]::GetEnvironmentVariable("Path", "User") -split ";" | Where-Object { $_ -and $_.Trim() -ne "" }
    $userMerged = New-Object System.Collections.Generic.List[string]
    foreach ($p in $candidateDirs + $userParts) {
        if (-not ($userMerged | Where-Object { $_.TrimEnd("\") -ieq $p.TrimEnd("\") })) {
            [void]$userMerged.Add($p)
        }
    }
    [Environment]::SetEnvironmentVariable("Path", ($userMerged -join ";"), "User")
}

$python = Get-Command python -ErrorAction Stop
$version = & python --version
$probe = & python -c "import sys, playwright; print(sys.executable); print('playwright-ok')"

Write-Output "Python command: $($python.Source)"
Write-Output "Python version: $version"
Write-Output $probe
