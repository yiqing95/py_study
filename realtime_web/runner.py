__author__ = 'yiqing'

import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define,options
import os

define('port',default=8888,help="Run ser er on specific port ",type=int)

class MainHendler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        logging.info('request to MainHandler !')
        self.write("Great , now let's make this app speak in realtime !")

local_static_path = os.path.join(os.path.dirname(__file__),'static')


app = tornado.web.Application([
    (r"/",MainHendler),
],static_path=local_static_path)


if __name__ == '__main__':
    http_server =tornado.httpserver.HTTPServer(app)
    tornado.options.parse_command_line()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()