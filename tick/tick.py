Prefix = "!!tick"
format_error = f"§c格式错误！使用§6{Prefix}§c查看帮助！"
help_msg = '''========MCDR-Tick========
§6!!tick h§r 使用/tick health
§6!!tick e§r 使用/tick entities'''

def on_info(server, info):
    content = info.content
    if info.is_player == False and ("ms" in content or "overworld" in content or "the_nether" in content or "Top" in content):
        server.say("§7" + content)

    cmd = content.split()
    if cmd[0] != Prefix:
        return
    del cmd[0]

    if len(cmd) == 0:
        server.reply(info, help_msg)
        return

    if len(cmd) != 1:
        server.reply(info, format_error)
        return

    if cmd[0] == "h" or cmd[0] == "health":
        server.execute("carpet commandTick true")
        server.execute("tick health")
        server.execute("carpet commandTick false")

    elif cmd[0] == "e" or cmd[0] == "entities":
        server.execute("carpet commandTick true")
        server.execute("tick entities")
        server.execute("carpet commandTick false")

def on_load(server,module):
    server.add_help_message(Prefix, "使用Carpet的/tick health和/tick entities指令")