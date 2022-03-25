# PerimeterMaker (Deprecated)

Create perimeters in creative/mirror servers, operate layer by layer to avoid lags.

## Attention

Requires [Carpet Mod](https://github.com/gnembon/fabric-carpet) to override fill limit.

## Install

Drag `PerimeterMaker.py` to `/plugins` folder

## Useage

 - `!!perimeter` show help messgae
 - `!!perimeter make <length> <width>` make a perimeter here
 - `!!perimeter commit` use after make, commit the operation
 - `!!perimeter abort` abort the operation at any time

## Constants can Modify

### DELAY

Defult value：`DELAY = 1`

The delay after the layer operation, change it by the performance of the server

---

在创造/镜像服中快速制造空置域，逐层操作，防止卡顿

## 注意事项

由于需要修改fill上限，所以需要[Carpet Mod](https://github.com/gnembon/fabric-carpet)的支持

## 安装

将`PerimeterMake.py`文件放入`/plugins`文件夹

## 使用

 - `!!perimeter` 显示帮助信息
 - `!!perimeter make <length> <width>` 以当前位置为中心清理一个空置域
 - `!!perimeter commit` 在使用make后使用，确认操作
 - `!!perimeter abort` 在任何时候中断操作

## 可修改常量

### DELAY

默认值：`DELAY = 1`

每修改一层后的延迟，按照服务器性能决定