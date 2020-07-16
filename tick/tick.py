def on_info(server, info):
    content = info.content
    if content == "!!tick h" or content == "!!tick health":
        server.execute("carpet commandTick true")
        server.execute("tick health")
        server.execute("carpet commandTick false")
    elif content == "!!tick e" or content == "!!tick entities":
        server.execute("carpet commandTick true")
        server.execute("tick entities")
        server.execute("carpet commandTick false")