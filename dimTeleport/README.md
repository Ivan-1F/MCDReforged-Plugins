# dimTeleport

输入`!!overworld`传送到主世界指定坐标

输入`!!nether`传送到地狱指定坐标

输入`!!end`传送到末地指定坐标

## 安装

将`dimTeleport.py`放入`/plugins`文件夹

## 可修改常量

### OVERWORLD NETHER END

默认值：

```python
OVERWORLD = "!!overworld"
NETHER = "!!nether"
END = "!!end"
```

触发传送的指令

### OVERWORLD_POS NETHER_POS END_POS

默认值：

```python
OVERWORLD_POS = "0 1 0"
NETHER_POS = "0 65 0"
END_POS = "0 100 0"
```

传送的坐标，格式为`"x y z"`