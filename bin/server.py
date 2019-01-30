from core.SimpleServer import SimpleServer

if __name__ == "__main__":
    raspberry_server = SimpleServer.SimpleServer(8086)
    raspberry_server.run()
