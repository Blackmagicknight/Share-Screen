from source import ScreenShareClient
import threading

sender = ScreenShareClient("server ip", 9999, 15) #254 & 13
t = threading.Thread(target=sender.start_stream)

t.start()
while input("") != "Q":
    continue
sender.stop_stream()