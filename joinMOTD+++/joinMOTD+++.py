import os
import json
import sys
import requests
from utils.rtext import *

sys.path.append('plugins/')
from daycount import getday

Prefix = "!!joinMOTD+++"

HELP_MSG = '''
========== joinMOTD+++ ==========
§6{0}§r 显示这条消息
§6{0} add §b<server>§r 添加一个服务器
§6{0} del §b<server>§r 删除一个服务器
'''.format(Prefix)

DEFULT_CONFIG = '''
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
'''

CONFIG_PATH = "config/joinMOTD+++.json"
def check_config_file():
    global CONFIG_PATH, DEFULT_CONFIG
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w+", encoding="utf-8") as f:
            f.write(DEFULT_CONFIG)

def get_config(index):
    global CONFIG_PATH
    check_config_file()
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data[index]

def get_MOTD():
    MOTD = '''§7=======§r Welcome back to §e{}§7 =======§r\n今天是§e{}§r开服的第§e{}§r天
    '''.format(get_config("full_server_name"), get_config("main_server_name"), getday())
    
    if get_config("display_one_text"):
        MOTD += "{}".format(requests.get(get_config("one_text_api")).text)

    if get_config("display_server_list"):
        MOTD += "\n§7-------§r Server List §7-------§r\n"
        for server in get_config("server_list"):
            if server == get_config("current_server_name"):
                MOTD += RText(f'[§c{server}§r] ', color=RColor.white)
            else:
                MOTD += RText(f'[§6{server}§r] ', color=RColor.white).h(f'点击加入至§6{server}§r服务器').c(RAction.run_command, f'/server {server}')

    return MOTD

def add_server(server):
    check_config_file()
    server_list = get_config("server_list")
    server_list.append(server)
    with open(CONFIG_PATH, encoding="utf-8") as f:
        data = json.load(f)
        data.update({"server_list": server_list})
        print(json.dumps(data))
        with open(CONFIG_PATH, "w", encoding="utf-8") as f1:
            f1.write(json.dumps(data))

def del_server(server):
    check_config_file()
    server_list = get_config("server_list")
    server_list.remove(server)
    with open(CONFIG_PATH, encoding="utf-8") as f:
        data = json.load(f)
        data.update({"server_list": server_list})
        print(json.dumps(data))
        with open(CONFIG_PATH, "w", encoding="utf-8") as f1:
            f1.write(json.dumps(data))
        

def on_load(server, old_module):
    global Prefix
    server.add_help_message(Prefix, "进服欢迎语及相关设置")
    check_config_file()

def on_info(server, info):
    global Prefix, HELP_MSG
    content = info.content
    cmd = content.split()
    if len(cmd) == 0 or cmd[0] != Prefix:
        return
    del cmd[0]

    if len(cmd) == 0:
        server.reply(info, get_MOTD())
        server.reply(info, HELP_MSG)

    if len(cmd) == 2 and cmd[0] == "add":
        add_server(cmd[1])
    
    if len(cmd) == 2 and cmd[0] == "del":
        del_server(cmd[1])


def on_player_joined(server, player):
    server.tell(player, get_MOTD())