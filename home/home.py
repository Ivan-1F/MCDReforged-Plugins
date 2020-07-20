import json

Prefix = "!!home"
help_msg = \
'''==========MCDR-Home==========
§6{0} help §r显示这条消息
§6{0} sethome §r将当前位置设置为家
§6{0} §r传送回家'''.format(Prefix)
format_error_msg = f"§c格式错误！请输入§6{Prefix} help§c查看帮助！"
data_path = "./plugins/home/data.json"

def get_data(target):
    global data_path
    data = json.load(open(data_path))
    if data.get(target):
        return data[target]
    return None

def add_data(target, dim, x, y, z):
    global data_path
    data = json.load(open(data_path))
    data.update({target: {"dim": dim, "x": x, "y": y, "z": z}})
    print(data)
    open(data_path, 'w').write(json.dumps(data))

def on_info(server, info):
    global Prefix
    content = info.content
    cmd = content.split()

    if len(cmd) == 0 or cmd[0] != Prefix:
        return

    del cmd[0]

    if len(cmd) == 0:
        if get_data(info.player) == None:
            server.reply(info, f"§c请先使用§6{Prefix} sethome§c设置家！")
            return
        data = get_data(info.player)
        dimension_name = {0: 'minecraft:overworld', -1: 'minecraft:the_nether', 1: 'minecraft:the_end'}
        server.reply(info, "§a正在传送......")
        dim = data["dim"]
        x = data["x"]
        y = data["y"]
        z = data["z"]
        cmd = f"execute in {dimension_name[dim]} run teleport {info.player} {x} {y} {z}"
        server.execute(cmd)
        return
    
    if cmd[0] == "help":
        if len(cmd) != 1:
            server.reply(info, format_error_msg)
            return
        server.reply(info, help_msg)
        return

    if cmd[0] == "sethome":
        if len(cmd) != 1:
            server.reply(info, format_error_msg)
            return

        PlayerInfoAPI = server.get_plugin_instance('PlayerInfoAPI')
        result = PlayerInfoAPI.getPlayerInfo(server, info.player)
        dim = result["Dimension"]
        pos_x = int(result["Pos"][0])
        pos_y = int(result["Pos"][1])
        pos_z = int(result["Pos"][2])

        dimension_display = {0: '§2主世界', -1: '§4地狱', 1: '§5末地'}
        position_show = '[x:{}, y:{}, z:{}]'.format(pos_x, pos_y, pos_z)
        server.reply(info, '设定家至 {} §r{}'.format(dimension_display[dim], position_show))
        add_data(info.player, dim, pos_x, pos_y, pos_z)
        return
