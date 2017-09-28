#! env bin/python
# codding = utf-8
from urllib.request import urlopen, urlretrieve#

'''r = urlopen('http://stackoverflow.com')
print(r.read())
r.close()'''


r = urlopen('http://stackoverflow.com', data=b"p", timeout=10)  # data чтоб отповить пост, для put delete
# использовать class Request, если нет data метод будет get
print(r.read())
r.close()




