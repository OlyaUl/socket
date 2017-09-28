#! env bin/python
# codding = utf-8
import wsgiref
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape
#from cgi import parse_qs,escape


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    # return [b'Hello']
    #return [b'%s=%s' % (str(k).encode(), str(v).encode()) for k,v in enviror.items()]
    #return [('%s=%s\n' % (k,v)).encode('UTF-8') for k,v in enviror.items()]
    qs = parse_qs(environ['QUERY_STRING'])
    # a = escape(qs['a'][0])
    a = escape(qs.get('a', [''])[0])
    # return [('%s=%s\n' % (k,str(v))).encode('UTF-8') for k,v in qs.items()]
    #return [('%s=%s\n' % (k,v and escape(v[0]))).encode('UTF-8') for k,v in qs.items()]



httpserv = make_server('localhost', 8080, app)
httpserv.serve_forever()
