# Agent Memory Starter

这套模板的目标不是一开始做一个很玄的“数字永生”，而是先让 agent 稳定地做三件事：

1. 记录今天发生了什么。
2. 从记录里提炼你是谁、你在做什么、你重视什么。
3. 把重要的人、项目、原则、未完成事项持续更新到可检索的 Markdown 文件里。

## 每天怎么用

1. 把当天的语音转文字、聊天记录、灵感、照片说明放进 `inbox/`。
2. 打开 Codex、Claude Code 或其他能读本地文件的 agent。
3. 对 agent 说：

```text
请读取 agent-memory-starter/AGENT_MEMORY_INSTRUCTIONS.md，
然后处理 agent-memory-starter/inbox 里的新材料，
更新 daily_logs、profiles、people、projects、principles 和 tasks。
不要编造没有依据的信息；重要结论要标注来源。
```

4. 每周检查一次 `tasks/open_tasks.md`。
5. 每月做一次 `monthly_interview.md` 里的访谈，把回答也放进 `inbox/` 再让 agent 沉淀。

## 推荐顺序

第一周只记录你自己和一个项目，不要记录太多人。

第二周开始记录重要亲人或长期关系，每次见面、通话、吃饭后用三分钟写下：

```text
时间：
地点：
和谁：
发生了什么：
对方说了什么：
我当时的感受：
这件事说明对方可能是个什么样的人：
```

第三周再开始接入更多素材，比如直播字幕、文章、课程笔记、项目文档。

## 隐私提醒

这里会沉淀非常敏感的个人数据。建议放在本地私有仓库，至少开启磁盘加密；不要随手上传到公开 GitHub。
