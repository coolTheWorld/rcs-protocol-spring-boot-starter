# Starter 仓库协作指南

## 仓库职责

本仓库负责 Spring Boot 3 集成、MQTT 客户端配置以及进程内内存或 Redis 状态基础设施。协议模型、校验、状态机、协议消息生成、状态快照 Codec 和 Effect Codec 属于核心协议 jar，不得在 Starter 中重复实现。

本文件是 `rcs-protocol-spec` 当前 Spec 的派生执行说明，不是独立事实来源。本文件与 Spec 冲突时必须以 Spec 为准并同步更正；Spec 更新了本文件中也存在的声明时，必须在同一工作周期更新本文件。不得在本文件中自行引入 Spec 未确认的项目决定。

相关仓库地址：

- Java 核心库：`https://github.com/coolTheWorld/rcs-protocol-java.git`
- Spring Boot Starter：`https://github.com/coolTheWorld/rcs-protocol-spring-boot-starter.git`
- Spec：`https://github.com/coolTheWorld/rcs-protocol-spec.git`

## 运行时约束

- 应用必须显式选择一个协议类型和一个角色；Fleet Control 与 Mobile Robot 不得在同一实例中同时启用。
- 状态存储必须显式选择 `memory` 或 `redis`。
- `memory` 模式直接使用进程内状态，不限定为非生产环境。
- `redis` 模式支持多实例共享；配置、连接或兼容性检查失败时必须启动失败，不得静默降级。
- 不提供 JDBC 存储，不自动迁移不兼容快照。
- Starter 不自动消费协议 Topic、反序列化业务消息或驱动核心状态机。

## 技术与文档规则

- 首版使用 JDK 21、Maven、Spring Boot 3.5.x 和 Jackson 2。
- 新增说明文档、设计文档和仓库指南使用中文正文；代码标识符、配置键和正式技术术语可以保留原文。
- Java 使用四空格缩进、全小写包名、`PascalCase` 类型和 `camelCase` 成员。
- 测试放在 `src/test/java` 并镜像生产包，测试类命名为 `*Test`。
- 不提交 IDE 状态、`target/`、凭据或生成构建输出。

## 变更流程

公共配置、模块边界或持久化语义变化前，先更新 `rcs-protocol-spec` 中的规格和适用 ADR。行为代码先写失败测试，再实现最小行为，并在提交前运行 Maven Wrapper 的完整 `verify`。提交保持聚焦，主题使用简短中文祈使句。
