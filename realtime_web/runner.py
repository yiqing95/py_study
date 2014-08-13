__author__ = 'yiqing'

import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define,options
import os

import threading
import re
import simplejson as json

import queue
tweetQueue = queue.Queue(0)

define('port',default=8888,help="Run ser er on specific port ",type=int)

class MainHendler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        logging.info('request to MainHandler !')
        self.write("Great , now let's make this app speak in realtime !")

local_static_path = os.path.join(os.path.dirname(__file__),'static')


class Tweet(object):
    waiters = []
    cache = []
    cache_size = 200

    def wait_for_messages(self,callback,cursor=None):
        cls = Tweet
        if cursor:
            index = 0
            for i in range(len(cls.cache)):
                index = len(cls.cache) -i -1
                if cls.cache[index]['id'] == cursor: break
            recent = cls.cache[index+1:]
            if recent:
                callback(recent)
                return
        cls.waiters.append(callback)

    def new_tweets(self, messages):
        cls = Tweet
        for callback in cls.waiters:
            try:
                callback(messages)
            except:
                  logging.error("Error in waiter callback", exc_info=True)
        cls.waiters = []
        cls.cache.extend(messages)
        if len(cls.cache) > self.cache_size:
             cls.cache = cls.cache[-self.cache_size:]


app = tornado.web.Application([
    (r"/",MainHendler),
],static_path=local_static_path)


if __name__ == '__main__':
    http_server =tornado.httpserver.HTTPServer(app)
    tornado.options.parse_command_line()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()