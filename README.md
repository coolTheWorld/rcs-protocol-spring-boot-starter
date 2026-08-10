# rcs-protocol-spring-boot-starter

`rcs-protocol` 的 Spring Boot 3 集成仓库，负责 MQTT 连接配置以及进程内内存或 Redis 状态基础设施。协议模型、校验、订单状态机和其他协议业务保留在对应的核心协议 jar 中。

## 当前状态

本仓库处于设计阶段，尚未发布 Maven 制品。未来将采用 Maven 多模块结构；使用方只需引入 Starter，由 Starter 传递依赖协议无关的 AutoConfigure 模块。

当前仓库没有 `pom.xml`、Maven Wrapper、自动配置实现或可运行示例，因此不存在可执行的构建和接入步骤。开始实现前必须先在 Spec 仓库批准相应计划和任务；本 README 不代表已经承诺发布日期。

## 快速了解

1. 阅读 [VDA 5050 Java 实现规格](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/vda5050-java-implementation.md)中的基础设施边界。
2. 阅读 [Starter 相关 ADR](https://github.com/coolTheWorld/rcs-protocol-spec/tree/main/docs/adr)，重点关注显式存储模式、Spring Boot/Jackson 基线和应用层装配。
3. 阅读 [Starter 实施计划](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/tasks/spring-boot-starter/plan.md)；该计划当前未激活，D01-D06 和维护者授权完成前不开始代码任务。
4. 通过 `git status --short` 与 `rg --files` 检查当前设计仓库；在 Maven 工程建立前不要使用虚构的构建命令。

## 当前命令

```powershell
git status --short
rg --files
```

以上命令只检查仓库状态与文件清单。本仓库建立 Maven 工程后，必须在这里补充实际可运行的构建、测试和完整质量门禁命令。

## 计划架构

未来仓库将分离协议无关 AutoConfigure 和协议适配 Starter。AutoConfigure 负责公共配置、生命周期、MQTT 与状态基础设施装配；具体协议 Starter 依赖对应核心 jar，并只做类型安全的边界连接。协议业务仍由核心库拥有。

运行时必须显式选择状态存储模式：

- `IN_MEMORY`：直接使用进程内内存，不限制为非生产环境。
- `REDIS`：使用 Redis 支持多实例共享；连接或配置失败时启动失败，不静默降级到内存。

应用还必须显式选择协议类型和单一运行角色。Fleet Control 与 Mobile Robot 可以复用代码，但不能在同一个应用实例中同时启用。Starter 不自动订阅业务 Topic、不自动反序列化协议消息，也不自动驱动核心状态机。

## 文档与贡献

- [项目开发规范](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/DEVELOPMENT.md)
- [项目完成定义](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/DEFINITION-OF-DONE.md)
- [发布门禁](https://github.com/coolTheWorld/rcs-protocol-spec/blob/main/RELEASE.md)
- [Starter 计划、任务与进度](https://github.com/coolTheWorld/rcs-protocol-spec/tree/main/tasks/spring-boot-starter)
- [本仓库贡献指南](./CONTRIBUTING.md)

## 许可证状态

项目根许可证尚未由维护者确认。当前设计文档不得被解释为已经获得某个开源许可证授权，也不得被解释为已经发布可用 Starter。
