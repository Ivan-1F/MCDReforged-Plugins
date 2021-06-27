from mcdreforged.api.all import *
import os

PLUGIN_METADATA = {
    'id': 'where',
	'version': '1.0.0',
	'name': 'Where',
	'description': 'A plugin to check the coordinate of a player',
	'author': 'IvanYF',
	'link': 'https://github.com/Ivan-YFw/MCDReforged-Plugins/tree/master/where',
	'dependencies': {
		'mcdreforged': '>=1.0.0',
		'minecraft_data_api': '*'
	}
}

# 在这里更改命令触发前缀
# Modify the prefix of the command here
PREFIX = '!!where'

dim_convert = {
		0: '§a主世界§r',
		-1: '§c下界§r',
		1: '§5末地§r'
	}

help_msg = '''
========== MCDR-Where v{1} ==========
一个用于查看其他玩家坐标的插件
§7{0}§r 显示此帮助信息
§7{0} §b<player>§r 查看其它玩家的坐标
'''.format(PREFIX, PLUGIN_METADATA['version'])

def on_load(server: ServerInterface, old_module):
	server.register_help_message(PREFIX, "查看其他玩家的坐标")
	server.register_command(Literal(PREFIX).runs(lambda src: src.reply(help_msg)).then(Text('player').runs(lambda src, ctx: reply_info(server, src, ctx))))

@new_thread(PLUGIN_METADATA['id'])
def reply_info(server: ServerInterface, src: CommandSource, ctx):
	api = server.get_plugin_instance('minecraft_data_api')
	dim = api.get_player_dimension(ctx['player'])
	cord = api.get_player_coordinate(ctx['player'])
	src.reply('§6{} §7@ {} [x:{}, y:{}, z:{}]'.format(ctx['player'], dim_convert[dim], int(cord.x), int(cord.y), int(cord.z)))
