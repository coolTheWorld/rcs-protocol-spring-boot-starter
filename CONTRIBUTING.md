# 贡献指南

本仓库当前处于设计阶段，尚无 Maven 工程和可执行 Starter。贡献重点是维护清晰的集成边界；没有已批准的实施任务时，不应提前加入 Spring Boot、MQTT 或 Redis 代码。

## 事实来源

开始修改前依次阅读：

- [项目开发规范](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/DEVELOPMENT.md)
- [VDA 5050 Java 实现规格](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/vda5050-java-implementation.md)
- [Starter 架构决策](https://github.com/coolTheWorld/rcs-protocol-spec/tree/main/docs/adr)
- [Starter 实施计划](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/tasks/spring-boot-starter/plan.md)
- [Starter 任务清单](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/tasks/spring-boot-starter/todo.md)
- [完成定义](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/DEFINITION-OF-DONE.md)

Spec 是项目决定的事实来源。本仓库 README 与 `AGENTS.md` 是派生说明，发现不一致时先更正 Spec，再同步受影响文档。Starter 任务集当前只是已规划、未激活；除 D01-D06 文档决策外，任何代码任务仍需维护者单独授权。

## 当前可执行检查

```powershell
git status --short
rg --files
```

仓库建立 Maven 工程后，必须提交 Maven Wrapper，并在 README 和 Spec 中补充实际可运行的构建、测试和质量门禁命令；在此之前不虚构构建结果或已发布坐标。

## 设计边界

- Starter 只负责 Spring Boot 装配、MQTT 接入和所选状态基础设施。
- 协议模型、Codec、Validator、状态机和消息生成属于核心协议 jar。
- 应用必须显式选择一个协议类型、一个角色和一个状态存储模式。
- `REDIS` 配置或连接失败时启动失败，不静默降级为 `IN_MEMORY`。
- Starter 不自动消费业务 Topic、不自动驱动状态机，也不承诺跨 Redis、MQTT 与设备的 exactly-once。
- 协议无关的 AutoConfigure 与协议适配 Starter 应保持模块边界，不把所有协议耦合进一个制品。

## 未来实现要求

实现任务获批后，行为变更必须先写失败测试。至少覆盖：条件装配、配置绑定与失败消息、单角色约束、显式存储模式、Redis fail-fast、无隐式业务消费，以及核心库依赖边界。公共配置键、Maven 坐标和持久化格式属于需要先确认的接口。

## 提交与 Pull Request

提交应小而原子，中文主题使用简短祈使句。Pull Request 应说明受影响的 Spec/ADR、边界变化、验证证据、兼容性影响和后续任务。不要把设计讨论、依赖升级与实现混在一个提交中。

## 许可证状态

项目根许可证尚未由维护者确认。在许可证和发布元数据完成前，不得把本仓库描述为已经获得某个开源许可证授权，也不得宣称存在可供生产使用的发布制品。
