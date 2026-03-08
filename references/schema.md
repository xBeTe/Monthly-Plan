# 数据结构模型 (Schema)及更新规则

你的脑海中需要始终维持以下 JSON 数据模型结构来存储和更新月度计划。
所有读写操作都必须严格遵循本数据字典与默认值规则，不允许随意捏造字段。

## 1. 月计划 (Monthly Plan)
- `year`: 年份。**非空**，自动读取当前年份（如 2026）
- `month`: 月份。**非空**，自动读取当前月份（如 3）
- `monthly_goal`: 月度核心目标描述。**非空**
- `tasks`: 任务列表（Array，包含多个“任务”对象）。**非空**

## 2. 任务 (Task)
- `id`: 任务ID（如 T01）。**非空**，自动生成
- `name`: 任务名称。**非空**
- `pic`: 负责人。**非空**
- `description`: 任务描述或目标产出。*可为空*
- `category`: 分类。**非空**。**只能是**：运维、项目、个人
- `priority`: 优先级。**非空**。**只能是**：高、中、低
- `severity`: 重要程度。**非空**。**只能是**：Minor、Major、Cruci、Crucial
- `status`: 状态。**非空**。**只能是**：Todo、In Progress、Done、Reviewed、Blocked
- `progress`: 进度情况（例如百分比 0-100%）。**非空**，默认值 `0%`
- `start_date_planned`: 计划开始日期（YYYY-MM-DD）。**非空**，默认值当月第一天
- `end_date_planned`: 计划截至日期（YYYY-MM-DD）。**非空**，默认值当月最后一天
- `start_date_actual`: 实际开始日期（YYYY-MM-DD）。*可为空*
- `end_date_actual`: 实际完成日期（YYYY-MM-DD）。*可为空*
- `risks`: 风险因素。*可为空*
- `remarks`: 备注说明。*可为空*
- `subtasks`: 子任务列表（Array，包含多个“子任务”对象）。*可为空*

## 3. 子任务 (Subtask)
- `id`: 子任务ID。**非空**，自动生成，以“父任务id-后缀标识”形式（如 T01-1）
- `name`: 子任务名称。**非空**
- `pic`: 负责人。**非空**
- `priority`: 优先级。**非空**。**只能是**：高、中、低
- `severity`: 重要程度。**非空**。**只能是**：Minor、Major、Cruci、Crucial
- `status`: 状态。**非空**。**只能是**：Todo、In Progress、Done、Reviewed、Blocked
- `completion_time`: 完成时间（YYYY-MM-DD HH:mm:ss）。*可为空*
- `remarks`: 备注说明。*可为空*
