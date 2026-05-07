# Quality Gates

Current version date: 2026-05-08

## Automatic Rewrite Triggers

Rewrite once, and only once, if any of these are true:

1. Body is under 4000 or over 5000 non-whitespace characters.
2. First 300 characters do not contain immediate conflict.
3. No clear rule-based payoff.
4. No clear ending hook.
5. 江彻 passively waits for more than half the chapter.
6. A free cheat or no-cost power gain appears.
7. Exposition replaces action for too much of the chapter.
8. Chapter contradicts the previous ending or required hook.
9. Formal prose, backup prose, or Fanqie publish text contains blank lines.

Do not rewrite infinitely.

## Pass Conditions

Final chapter may be archived only when all are true:

1. 4000 to 5000 non-whitespace body characters.
2. No blank lines in formal prose, backup prose, and publish text.
3. Opens with conflict.
4. Has middle pressure escalation.
5. 江彻 makes active tactical choices.
6. Has a clear rule-based payoff.
7. Has a clear cost.
8. Has a strong chapter ending hook.
9. No major unauthorized setting expansion.
10. No no-cost cheat.
11. QA report says publish is recommended.

## Required QA Report Sections

`daily_output/第XXX章_质检报告.md` must include:

1. 字数统计
2. 是否承接上一章
3. 是否承接设定文件
4. 是否包含开头冲突
5. 是否包含中段压迫
6. 是否包含主角主动决策
7. 是否包含明确爽点
8. 是否包含明确代价
9. 是否包含章末钩子
10. 是否新增重大世界观设定
11. 是否出现无代价外挂
12. 是否存在设定冲突
13. 风格贴合度评分，满分10分
14. 是否建议发布
15. 是否触发自动重写
16. 是否已正式归档到 chapters
17. 是否已生成摘要到 chapter_summaries
18. 正文是否存在空白行
19. 番茄发布版是否存在空白行

## Required Dry-Run Log Sections

`daily_output/第XXX章_干跑日志.md` must include:

1. 实际读取到的设定文件列表
2. 实际读取到的章节摘要列表
3. 实际读取到的最近三章全文文件列表
4. 判断出的当前最新正式章节编号
5. 本次生成的目标章节编号
6. 缺失文件列表
7. 输出文件列表
8. 正式正文是否写入 chapters
9. 正式摘要是否写入 chapter_summaries
10. 是否联网
11. 是否打开浏览器
12. 是否访问番茄后台
13. 是否发布
14. 是否上传
15. 是否修改旧章节
16. 执行模式

## Publish Checklist Sections

`daily_output/第XXX章_发布检查清单.md` must include:

1. 今日目标章节编号
2. 正文字数
3. 是否有明显错别字
4. 是否有敏感词风险
5. 是否承接上一章
6. 是否有章末钩子
7. 正文和番茄发布版是否无空白行
8. 是否建议发布
9. 正式正文路径
10. 正式摘要路径
11. Fanqie 自动发布状态
12. Fanqie 发布日志路径
