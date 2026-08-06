# rcs-protocol-spring-boot-starter

`rcs-protocol` 的 Spring Boot 3 集成仓库，负责 MQTT 连接配置以及进程内内存或 Redis 状态基础设施。协议模型、校验、订单状态机和其他协议业务保留在对应的核心协议 jar 中。

## 当前状态

本仓库处于设计阶段，尚未发布 Maven 制品。未来将采用 Maven 多模块结构；使用方只需引入 Starter，由 Starter 传递依赖协议无关的 AutoConfigure 模块。

运行时必须显式选择状态存储模式：

- `memory`：直接使用进程内内存，不限制为非生产环境。
- `redis`：使用 Redis 支持多实例共享；连接或配置失败时启动失败，不静默降级到内存。

应用还必须显式选择协议类型和单一运行角色。Fleet Control 与 Mobile Robot 可以复用代码，但不能在同一个应用实例中同时启用。Starter 不自动订阅业务 Topic、不自动反序列化协议消息，也不自动驱动核心状态机。

详细设计见 [`rcs-protocol-spec`](https://github.com/coolTheWorld/rcs-protocol-spec)。
