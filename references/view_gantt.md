# 生成甘特图指令 (View Gantt)

按以下步骤生成包含任务进度与法定假期标注的甘特图。

## 步骤 1：读取计划数据
- 读取当月 JSON 计划文件（`monthly_plan_YYYY-MM.json`），提取所有带有 `start_date_planned` / `end_date_planned`（以及可选的 `start_date_actual` / `end_date_actual`）的任务和子任务。

## 步骤 2：查询当月法定假期
- 读取 `user_profile.json` 获取用户的 `country` 和 `region`。
  - 若 `user_profile.json` 不存在或 `country` 为空，遵循**核心规则5**，先向用户询问国家和地区并保存后再继续。
- 通过**联网搜索**该国家/地区官方渠道公布的当年法定节假日，提取**当月**所有假期的名称与日期范围（格式：`YYYY-MM-DD` 至 `YYYY-MM-DD`）。

## 步骤 3：构建 Mermaid Gantt 内容
将任务和假期数据组合成一段 Mermaid Gantt 图语法，遵循以下结构规则：

```
gantt
    title YYYY年MM月 月度计划甘特图
    dateFormat  YYYY-MM-DD
    excludes    weekends

    section 🎉 法定假期
    <假期名称>  :crit, done, <id>, <start_date>, <end_date>

    section 运维任务
    <任务名称> [<进度%>]  :<status_tag>, <id>, <start_date_planned>, <end_date_planned>

    section 项目任务
    <任务名称> [<进度%>]  :<status_tag>, <id>, <start_date_planned>, <end_date_planned>

    section 个人任务
    <任务名称> [<进度%>]  :<status_tag>, <id>, <start_date_planned>, <end_date_planned>
```

**字段转换规则：**
- **假期区块**：统一使用 `crit, done` 标签，放在名为 `🎉 法定假期` 的 section 最前面，确保视觉上醒目区分。若当月无法定假期，可省略该 section。
- **任务状态标签映射**：
  - `Done` / `Reviewed` → `done`
  - `In Progress` → `active`
  - `Todo` → *(无标签，使用默认灰色)*
  - `Blocked` → `crit`（红色警示）
- **任务名称**：在任务名后附上当前进度，例如：`需求文档撰写 [60%]`。
- **子任务**：作为父任务的缩进展示（在同一 section 中列于父任务之后，名称前加 `-` 符号）。
- **ID**：使用任务的 `id` 字段（如 T01、T01-1）作为 Mermaid 中的任务标识符。

## 步骤 4：输出 Mermaid 代码并等待确认
- 将拼接好的 Mermaid 文本以 Markdown 代码块的形式输出给用户。
- 在下方附上当月假期说明文字，例如：
  > 📅 **本月法定假期（已在甘特图中标红）：**
  > - 国庆节：10月1日 - 10月7日
- 询问用户：“是否确认渲染甘特图图片？”并等待确认。

## 步骤 5：渲染成图片（需用户确认）
- 获得用户确认后，调用本地工具，将拼接好的 Mermaid 文本写入临时文件 `gantt_temp.mmd`。
- 使用 Mermaid CLI 渲染成 png。
- 将生成的甘特图图片以 Markdown 语法返回：`![当月进度甘特图](gantt.png)`。
