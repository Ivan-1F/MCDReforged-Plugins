# joinMOTD+++

一个 MCDReforged 插件

当玩家加入游戏时向其发送欢迎信息

![screenshot](https://github.com/wyf0762/MCDReforged-Plugins/tree/master/joinMOTD+++/screenshot.png)

## 环境要求

需要前置插件 [daycount](https://github.com/TISUnion/daycount)

需要支持 Rtext 的 MCDReforged

## 配置文件

插件第一次被加载时会生成 joinMOTD+++.json。该文件内容如下：

```python
{
	"full_server_name": "Survival Server",
	"main_server_name": "My Server",
    "current_server_name": "survival",
    "display_one_text": true,
    "display_server_list": true,
    "one_text_api": "https://v1.hitokoto.cn/?encode=text",
	"server_list":
	[
		"survival",
		"creative"
	]
}
```

### full_server_name

默认值：`"full_server_name": "Survival Server"`

完整的服务器名称

### main_server_name

默认值：`"main_server_name": "My Server"`

服务器名称缩写

### current_server_name

默认值：`"current_server_name": "survival"`

当前服务器的名称，应当与 `server_list` 中的名称一致

### one_text

`display_one_text`：是否显示一言。

`one_text_api`：一言API接口。如需更换，请确保API返回值为纯文本。

### server_list

`display_server_list`：是否显示服务器列表

`server_list`：服务器列表