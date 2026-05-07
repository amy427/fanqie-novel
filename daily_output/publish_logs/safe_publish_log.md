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
