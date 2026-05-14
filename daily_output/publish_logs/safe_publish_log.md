# Log

## 2026-05-06_205415 safe publish failed before completion
- Result: `failed`
- Error: `TimeoutError: Locator.inner_text: Timeout 10000ms exceeded.
Call log:
  - waiting for locator("[contenteditable='true']").filter(has_text="请输入正文").first.first
`
- Traceback:
```text
Traceback (most recent call last):
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 218, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 153, in main
    editor_text = editor.inner_text(timeout=10000)
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\sync_api\_generated.py", line 17087, in inner_text
    self._sync(self._impl_obj.inner_text(timeout=timeout))
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_sync_base.py", line 115, in _sync
    return task.result()
           ~~~~~~~~~~~^^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_locator.py", line 476, in inner_text
    return await self._frame.inner_text(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
    )
    ^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_frame.py", line 712, in inner_text
    return await self._channel.send(
           ^^^^^^^^^^^^^^^^^^^^^^^^^
        "innerText", self._timeout, locals_to_params(locals())
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_connection.py", line 69, in send
    return await self._connection.wrap_api_call(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
    )
    ^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_connection.py", line 559, in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
playwright._impl._errors.TimeoutError: Locator.inner_text: Timeout 10000ms exceeded.
Call log:
  - waiting for locator("[contenteditable='true']").filter(has_text="请输入正文").first.first
```

## 2026-05-06_205500 safe publish failed before completion
- Result: `failed`
- Error: `RuntimeError: Publish button not found`
- Traceback:
```text
Traceback (most recent call last):
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 217, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 169, in main
    raise RuntimeError("Publish button not found")
RuntimeError: Publish button not found
```

## 2026-05-06_205658 chapter 030 safe publish
- Mode: `submit`
- Title: `第030章 观察席`
- SHA256: `55a50fd73608152fc6fa08bfdb10395422b36cc45af244c934646796e80bc27f`
- Verified page: `True`
- JSON: `D:\fanqie-novel\daily_output\publish_logs\2026-05-06_205658_chapter_030_safe_publish.json`
- Screenshot: `D:\fanqie-novel\daily_output\publish_logs\2026-05-06_205658_chapter_030_precheck.png`
- Submitted: `True`

## 2026-05-07_185826 safe publish failed before completion
- Result: `failed`
- Error: `TimeoutError: Page.screenshot: Timeout 30000ms exceeded.
Call log:
  - taking page screenshot
  - waiting for fonts to load...
  - fonts loaded
`
- Traceback:
```text
Traceback (most recent call last):
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 279, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 250, in main
    page.screenshot(path=str(submitted_screenshot), full_page=True)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\sync_api\_generated.py", line 9819, in screenshot
    self._sync(
    ~~~~~~~~~~^
        self._impl_obj.screenshot(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<13 lines>...
        )
        ^
    )
    ^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_sync_base.py", line 115, in _sync
    return task.result()
           ~~~~~~~~~~~^^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_page.py", line 814, in screenshot
    encoded_binary = await self._channel.send(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
        "screenshot", self._timeout_settings.timeout, params
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_connection.py", line 69, in send
    return await self._connection.wrap_api_call(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
    )
    ^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_connection.py", line 559, in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
playwright._impl._errors.TimeoutError: Page.screenshot: Timeout 30000ms exceeded.
Call log:
  - taking page screenshot
  - waiting for fonts to load...
  - fonts loaded
```

## 2026-05-07_190013 chapter 031 safe publish
- Mode: `submit`
- Title: `第031章 下层敲门`
- SHA256: `6ae3eb580a03f3de15482188506315bd0d6065b9c7159257cf4c95f991287337`
- Verified page: `True`
- JSON: `D:\fanqie-novel\daily_output\publish_logs\2026-05-07_190013_chapter_031_safe_publish.json`
- Screenshot: `D:\fanqie-novel\daily_output\publish_logs\2026-05-07_190013_chapter_031_precheck.png`
- Submitted: `True`

## 2026-05-07_191239 chapter 031 safe publish
- Mode: `submit`
- Title: `第031章 下层敲门`
- SHA256: `6ae3eb580a03f3de15482188506315bd0d6065b9c7159257cf4c95f991287337`
- Verified page: `True`
- JSON: `D:\fanqie-novel\daily_output\publish_logs\2026-05-07_191239_chapter_031_safe_publish.json`
- Screenshot: `D:\fanqie-novel\daily_output\publish_logs\2026-05-07_191239_chapter_031_precheck.png`
- Submitted: `True`

## 2026-05-07_191718 safe publish failed before completion
- Result: `failed`
- Error: `RuntimeError: Final publish confirmation button not found`
- Traceback:
```text
Traceback (most recent call last):
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 300, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 269, in main
    raise RuntimeError("Final publish confirmation button not found")
RuntimeError: Final publish confirmation button not found
```

## 2026-05-07_191914 chapter 030 safe publish
- Mode: `submit`
- Title: `第030章 观察席`
- SHA256: `55a50fd73608152fc6fa08bfdb10395422b36cc45af244c934646796e80bc27f`
- Verified page: `True`
- JSON: `D:\fanqie-novel\daily_output\publish_logs\2026-05-07_191914_chapter_030_safe_publish.json`
- Screenshot: `D:\fanqie-novel\daily_output\publish_logs\2026-05-07_191914_chapter_030_precheck.png`
- Submitted: `True`

## 2026-05-08_003034 safe publish failed before completion
- Result: `failed`
- Error: `Error: BrowserType.connect_over_cdp: connect ECONNREFUSED 127.0.0.1:9223
Call log:
  - <ws preparing> retrieving websocket url from http://127.0.0.1:9223
`
- Traceback:
```text
Traceback (most recent call last):
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 360, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 211, in main
    browser, page = get_page(p, args.new_page, args.page_url_contains)
                    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 170, in get_page
    return get_last_page(playwright)
  File "D:\fanqie-novel\tools\fanqie_common.py", line 70, in get_last_page
    browser = playwright.chromium.connect_over_cdp(CDP_URL)
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\sync_api\_generated.py", line 14969, in connect_over_cdp
    self._sync(
    ~~~~~~~~~~^
        self._impl_obj.connect_over_cdp(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<5 lines>...
        )
        ^
    )
    ^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_sync_base.py", line 115, in _sync
    return task.result()
           ~~~~~~~~~~~^^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_browser_type.py", line 206, in connect_over_cdp
    response = await self._channel.send_return_as_dict(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        "connectOverCDP", TimeoutSettings.launch_timeout, params
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_connection.py", line 83, in send_return_as_dict
    return await self._connection.wrap_api_call(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
    )
    ^
  File "C:\Users\26030\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\playwright\_impl\_connection.py", line 559, in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
playwright._impl._errors.Error: BrowserType.connect_over_cdp: connect ECONNREFUSED 127.0.0.1:9223
Call log:
  - <ws preparing> retrieving websocket url from http://127.0.0.1:9223
```

## 2026-05-08_003059 chapter 031 safe publish
- Mode: `dry-run`
- Title: `第031章 下层敲门`
- Chapter title field: `下层敲门`
- SHA256: `6ae3eb580a03f3de15482188506315bd0d6065b9c7159257cf4c95f991287337`
- Verified page: `True`
- JSON: `D:\fanqie-novel\daily_output\publish_logs\2026-05-08_003059_chapter_031_safe_publish.json`
- Screenshot: `D:\fanqie-novel\daily_output\publish_logs\2026-05-08_003059_chapter_031_precheck.png`
- Submitted: `False`

## 2026-05-08_003323 chapter 031 safe publish
- Mode: `dry-run`
- Title: `第031章 下层敲门`
- Chapter title field: `下层敲门`
- SHA256: `6ae3eb580a03f3de15482188506315bd0d6065b9c7159257cf4c95f991287337`
- Verified page: `True`
- JSON: `D:\fanqie-novel\daily_output\publish_logs\2026-05-08_003323_chapter_031_safe_publish.json`
- Screenshot: `D:\fanqie-novel\daily_output\publish_logs\2026-05-08_003323_chapter_031_precheck.png`
- Submitted: `False`

## 2026-05-08_095950 safe publish failed before completion
- Result: `failed`
- Error: `RuntimeError: Final publish confirmation button not found`
- Traceback:
```text
Traceback (most recent call last):
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 366, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 333, in main
    raise RuntimeError("Final publish confirmation button not found")
RuntimeError: Final publish confirmation button not found
```

## 2026-05-08_100110 chapter 032 safe publish
- Mode: `submit`
- Title: `第032章 房号900`
- Chapter title field: `房号900`
- SHA256: `b807a4ccdda76fa4ee6e4dbd655ee3b181a6d54f00d0399b449ec15c2d558103`
- Verified page: `True`
- JSON: `D:\fanqie-novel\daily_output\publish_logs\2026-05-08_100110_chapter_032_safe_publish.json`
- Screenshot: `D:\fanqie-novel\daily_output\publish_logs\2026-05-08_100110_chapter_032_precheck.png`
- Submitted: `True`

## 2026-05-08_100458 safe publish failed before completion
- Result: `failed`
- Error: `RuntimeError: Continue submit requested but no visible submit modal was found`
- Traceback:
```text
Traceback (most recent call last):
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 451, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 332, in main
    raise RuntimeError("Continue submit requested but no visible submit modal was found")
RuntimeError: Continue submit requested but no visible submit modal was found
```

## 2026-05-08_100531 chapter 032 continue submit
- Mode: `continue-submit`
- Title: `第032章 房号900`
- SHA256: `b807a4ccdda76fa4ee6e4dbd655ee3b181a6d54f00d0399b449ec15c2d558103`
- Verified page: `True`
- JSON: `D:\fanqie-novel\daily_output\publish_logs\2026-05-08_100531_chapter_032_safe_publish.json`
- Submitted: `True`

## 2026-05-09_073520 safe publish failed before completion
- Result: `failed`
- Error: `RuntimeError: Body editor not found`
- Traceback:
```text
Traceback (most recent call last):
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 463, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 378, in main
    editor = find_body_editor(page)
  File "D:\fanqie-novel\tools\fanqie_safe_publish.py", line 100, in find_body_editor
    raise RuntimeError("Body editor not found")
RuntimeError: Body editor not found
```

### 2026-05-09_073520 diagnosis

- CDP was reachable and Python was available.
- Precheck screenshot showed the Fanqie author site login form, not the chapter editor.
- The safe publisher did not find the body editor because the Fanqie session was logged out.
- Follow-up audit JSON: `daily_output/publish_logs/2026-05-09_073520_chapter_033_login_required.json`

## 2026-05-14_215119 chapter 035 safe publish
- Mode: `dry-run`
- Title: `第035章 空白观察席`
- Chapter title field: `空白观察席`
- SHA256: `28cafdf4cd5883377fea6478c3b75500d26c96bdc3702295fc5cee62fbfde7f7`
- Verified page: `True`
- JSON: `D:\fanqie-novel\daily_output\publish_logs\2026-05-14_215119_chapter_035_safe_publish.json`
- Screenshot: `D:\fanqie-novel\daily_output\publish_logs\2026-05-14_215119_chapter_035_precheck.png`
- Submitted: `False`
