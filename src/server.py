from source import StreamingServer
import threading

receiver = StreamingServer("your ip", 9999)
t = threading.Thread(target=receiver.start_server)

t.start()
while input("") != "Q":
    continue
receiver.stop_server()
