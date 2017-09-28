#! env bin/python
# codding = utf-8
import wsgiref
from wsgiref.simple_server import make_server


def app(enviror, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello']


httpserv = make_server('localhost', 8080, app)
httpserv.serve_forever()
