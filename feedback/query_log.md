# Feedback Query Log

## 2026-05-06

| Time | Source | Result | Notes |
| --- | --- | --- | --- |
| 2026-05-06 | Local files | initialized | Feedback query system created |
| 2026-05-06 | Fanqie browser analytics | not queried | No verified read-only analytics page configured |
| 2026-05-06 | Feedback imports | empty | No import files yet |

## 2026-05-06_204243 Fanqie read-only query failed
- Result: failed
- Error: `Error: BrowserType.connect_over_cdp: connect ECONNREFUSED 127.0.0.1:9222
Call log:
  - <ws preparing> retrieving websocket url from http://127.0.0.1:9222
`

## 2026-05-07 Fanqie read-only query failed
- Result: failed
- Error: `Python runtime unavailable: python not found; py launcher reports no installed Python`
- Action: continued with local repository files and empty feedback imports

## 2026-05-07_185627 Fanqie read-only query skipped
- Result: skipped
- Reason: current page was not verified as Fanqie analytics/comments page
- URL: `https://fanqienovel.com/main/writer/7628203489469942846/publish/7635508309587411480?enter_from=newchapter_0`
- Title: `作家专区-番茄小说网-番茄小说旗下原创文学平台`

## 2026-05-08 Fanqie read-only query failed
- Result: failed
- Error: `python was not found on PATH; PowerShell could not resolve python tools\fanqie_readonly_metrics.py`
- CDP: reachable at `http://127.0.0.1:9222/json/version`
- Action: continued with local repository files and empty feedback imports

## 2026-05-09 Fanqie read-only query failed
- Result: failed
- Error: CDP remained unreachable after `tools\fanqie_start_cdp_chrome.ps1`; `python` was not found on PATH and `py` reported no installed Python
- CDP: unreachable at `http://127.0.0.1:9222/json/version`
- Action: continued with local repository files and empty feedback imports

## 2026-05-10 Fanqie read-only query failed
- Result: failed
- Error: CDP remained unreachable after `tools\fanqie_start_cdp_chrome.ps1`; `python` was not found on PATH and `py` reported no installed Python
- CDP: unreachable at `http://127.0.0.1:9222/json/version`
- Feedback imports: no usable imports detected beyond `.gitkeep`
- Action: continued with local repository files and empty feedback imports

## 2026-05-14 Fanqie read-only query failed
- Result: failed
- Error: `python` was not found on PATH; `py` launcher reported no installed Python runtime
- CDP: reachable at `http://127.0.0.1:9222/json/version`
- Feedback imports: no usable imports detected beyond `.gitkeep`
- Action: continued with local repository files and empty feedback imports

## 2026-05-14_215119 Fanqie read-only query failed
- Result: failed
- Error: `Error: Page.title: Execution context was destroyed, most likely because of a navigation`

## 2026-05-14_215153 Fanqie read-only query skipped
- Result: skipped
- Reason: current page was not verified as Fanqie analytics/comments page
- URL: `https://fanqienovel.com/main/writer/7628203489469942846/publish/7637501471965069848?enter_from=newchapter_0`
- Title: `作家专区-番茄小说网-番茄小说旗下原创文学平台`
