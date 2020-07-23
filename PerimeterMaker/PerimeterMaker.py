import time

# Edit this to change the delay
DELAY = 1

Prefix = "!!perimeter"
help_msg = '''========== Perimeter Maker ==========
§6{0}§r 显示这条信息
§6{0} make §b<length> <width>§r 以当前位置为中心清理一个空置域
§6{0} commit§r 在使用make后使用，确认操作
§6{0} abort§r 在任何时候中断操作'''.format(Prefix)
CHUNK = 16

ABORT = False
WORKING = False
NEED_COMMIT = False

p1 = None
p2 = None
p3 = None
p4 = None

def on_info(server, info):
    global help_msg, Prefix, DELAY
    global CHUNK, ABORT, WORKING, NEED_COMMIT
    global p1, p2, p3, p4
    content = info.content
    cmd = content.split()
    if len(cmd) == 0 or cmd[0] != Prefix:
        return
    del cmd[0]
    # !!perimeter help
    if len(cmd) == 1 and cmd[0] == "help":
        server.reply(info, help_msg)
        return
    # !!perimeter abort
    if len(cmd) == 1 and cmd[0] == "abort":
        if not WORKING and not NEED_COMMIT:
            server.reply(info, "§c没有需要中断的操作")
            return
        ABORT = True
        NEED_COMMIT = False
        server.reply(info, "§c终止操作！")
        return
    # !!perimeter abort <length> <width>
    if len(cmd) == 3 and cmd[0] == "make":
        if WORKING:
            server.reply(info, "§c当前正在清理，请等待清理结束！")
        try:
            p1 = -int(cmd[1])/2 * CHUNK
            p2 = int(cmd[1])/2 * CHUNK
            p3 = -int(cmd[2])/2 * CHUNK
            p4 = int(cmd[2])/2 * CHUNK
        except:
            server.reply(info, "§c你输入的不是数字！")
        
        NEED_COMMIT = True
        server.reply(info, "§a请输入§6{} commit§a确认操作！".format(Prefix))

    if len(cmd) == 1 and cmd[0] == "commit":

        if not NEED_COMMIT:
            server.reply(info, "§c没有需要确认的操作")
            return

        server.say("§a开始操作！请在§c原地§a耐心等待，§c不要移动")
        NEED_COMMIT = False

        server.execute("carpet fillLimit 1000000")
        
        WORKING = True
        for i in range(0, 254):
            if ABORT:
                ABORT = False
                WORKING = False
                break
            y = 255 - i
            command = "execute at {} run fill ~{} {} ~{} ~{} {} ~{} air".format(info.player, p1, y, p3, p2, y, p4)
            server.say("正在替换第{}层".format(y))
            time.sleep(DELAY)
            server.execute(command)
        WORKING = False