from random import sample
from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'pick',
    'version': '1.0.0',
    'name': 'Pick',
    'description': 'A plugin to pick players randomly from the server',
    'author': 'Ivan1F',
    'link': 'https://github.com',
    'dependencies': {
        'mcdreforged': '>=2.0.0',
        'minecraft_data_api': '>=1.1.0'
    }
}


@new_thread(PLUGIN_METADATA['id'])
def pick(source: CommandSource, count: int):
    api = source.get_server().get_plugin_instance('minecraft_data_api')
    amount, limit, players = api.get_server_player_list()
    picked = sample(players, count)
    formatted = ', '.join(picked)
    source.get_server().say('§6' + formatted)


def register_commands(server: PluginServerInterface):
    server.register_command(
        Literal('!!pick').then(Integer('count').runs(lambda src, ctx: pick(src, ctx['count'])))
    )


def on_load(server: ServerInterface, old):
    register_commands(server)

