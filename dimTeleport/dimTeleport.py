OVERWORLD = "!!overworld"
NETHER = "!!nether"
END = "!!end"

OVERWORLD_POS = "0 1 0"
NETHER_POS = "0 65 0"
END_POS = "0 100 0"

def on_info(server, info):
    global OVERWORLD,OVERWORLD_POS
    global END, END_POS
    content = info.content
    if content == OVERWORLD:
        server.execute(f"execute in minecraft:overworld run teleport {info.player} {OVERWORLD_POS}")
        return
    if content == NETHER:
        server.execute(f"execute in minecraft:the_nether run teleport {info.player} {NETHER_POS}")
        return
    if content == END:
        server.execute(f"execute in minecraft:the_end run teleport {info.player} {END_POS}")
        return