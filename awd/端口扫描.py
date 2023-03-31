import socket

print("[*]正在扫描IP................")

for i in range(1, 256):
    ip = "192-168-1-" + str(i) + ".pvp1989.bugku.cn"
    try:
        socket.gethostbyname(ip)
        print(ip, "is up!")
    except socket.error:
        pass

    # 192-168-1-236.pvp1989.bugku.cn