#! env bin/python
# codding = utf-8
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 5000))
    s.listen(1)  # max count client
    conn, addr = s.accept()  # wait connect client
    with conn:
        print('connected', addr)
        while True:
            data = conn.recv(1024)  # max count bytes
            if not data:
                break
            conn.sendall(data)
