#! env bin/python
# codding = utf-8
import socketserver


# class MyHandler(socketserver.BaseRequestHandler):
class MyHandler(socketserver.StreamRequestHandler):
# class MyHandler(socketserver.ThreadingMixIn, socketserver.TCPServer): - no working

    def handle(self):  # при подкл клиента
        print(self.client_address)  # ~conn, addr =  = s.accept()
        data = self.request.recv(1024)  # request - object socket
        self.request.sendall(data.upper())
        self.wfile.write(data.upper())


# for > 1 user
class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    server = Server(("localhost", 5000), MyHandler)
    server.serve_forever()



