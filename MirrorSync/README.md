# MirrorSync

一个在镜像服内同步生存服存档至镜像服的[MCDReforged](https://github.com/Fallen-Breath/MCDReforged)插件。

## 安装

将`MirrorSync.py`文件拖入**镜像服**的`/plugins`文件夹

## 命令格式说明

`!!mirror` 显示帮助信息

`!!mirror sync` 同步生存服存档至镜像服

`!!mirror commit` 在执行`sync`后使用，再次确认是否同步

`!!mirror abort` 在任何时候键入此指令可中断同步

## 一些常量说明

调整这些常量的数值也就是在配置 MirrorSync 插件

### SurvivalServerPath

默认值：`SurvivalServerPath = "../survival/server"`

生存服的路径，包含生存服的`server.jar`以及存档文件夹

### MirrorServerPath

默认值：`MirrorServerPath = "./server"`

镜像服的路径，包含镜像服的`server.jar`以及存档文件夹

### WorldNames

默认值：

```
WorldNames = [
    "world",
    ]
```

需要同步的世界文件夹列表，原版服务端只会有一个世界，在默认值基础上填上世界文件夹的名字即可

对于非原版服务端如水桶、水龙头服务端，会有三个世界文件夹，此时可填写：

```
WorldNames = [
    'world',
    'world_nether',
    'world_the_end',
]
```

### CountDown

默认值：`CountDown = 10`

执行`!!mirror commit`后的倒计时

### MinimumPermissionLevel

默认值：`MinimumPermissionLevel = 3`

一个整数，代表可以使用此插件命令的最低MCDR权限，详见[此处](https://github.com/Fallen-Breath/MCDReforged/blob/master/doc/readme_cn.md#%E6%9D%83%E9%99%90)

### Prefix

默认值：`Prefix = "!!mirror"`

触发插件的前缀
