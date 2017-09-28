#! env bin/python
# codding = utf-8
import wsgiref
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape
#from cgi import parse_qs,escape


# def app(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     # return [b'Hello']
#     #return [b'%s=%s' % (str(k).encode(), str(v).encode()) for k,v in enviror.items()]
#     #return [('%s=%s\n' % (k,v)).encode('UTF-8') for k,v in enviror.items()]
#     qs = parse_qs(environ['QUERY_STRING'])
#     # a = escape(qs['a'][0])
#     a = escape(qs.get('a', [''])[0])
#     return [('%s=%s\n' % (k,str(v))).encode('UTF-8') for k,v in qs.items()]
#     #return [('%s=%s\n' % (k,v and escape(v[0]))).encode('UTF-8') for k,v in qs.items()]

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    try:
        size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        size = 0
    data = environ['wsgi.input'].read(size)
    data = parse_qs(data)
    return [('%s=%s\n' % (k, str(v))).encode('UTF-8') for k, v in data.items()]

'''path_info = '/path/123'
p = path_info.split('/')
if p[0] == 'path':
    id = p[1]
elif p[0] = ..
   '''

httpserv = make_server('localhost', 8080, app)
httpserv.serve_forever()


#user@ST03:~/less8/web$ curl --data 'a=1&b=2' http://localhost:8080 запускать в терминале для проверки
