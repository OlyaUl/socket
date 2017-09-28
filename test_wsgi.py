#! env bin/python
# codding = utf-8
import wsgiref
from wsgiref.simple_server import make_server
from cgi import parse_qs,escape


def app(enviror, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    # return [b'Hello']
    #return [b'%s=%s' % (str(k).encode(), str(v).encode()) for k,v in enviror.items()]
    return [('%s=%s\n' % (k,v)).encode('UTF-8') for k,v in enviror.items()]


httpserv = make_server('localhost', 8080, app)
httpserv.serve_forever()
