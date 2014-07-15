__author__ = 'yiqing'

import os,sys
from http.server import HTTPServer,CGIHTTPRequestHandler

webdir = '.'
port = 6666

os.chdir(webdir)
srvraddr = ('',port)
srvrobj = HTTPServer(srvraddr,CGIHTTPRequestHandler)
srvrobj.serve_forever()
