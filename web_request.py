#! env bin/python
# codding = utf-8
import socket


request = b'GET / HTTP/1.1\nHost: stackoverflow.com\n\n'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('stackoverflow.com', 80))
    s.send(request)


