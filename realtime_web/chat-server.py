__author__ = 'yiqing'

import os , logging
import tornado.httpserver
import tornado.ioloop
import tornado.web

import uuid
import simplejson as json
from tornado.options import define,options

define('port',default=8888,help="Run server on a specific port",type=int)

def notification(_type,_data):
    return {
        'type':_type,
        'data':_data
    }

class Chat(object):
    listeners = []
    users = []

    def add_listener(self,callback,user_id = None):
        data = {}
        data['user_id'] = user_id
        data['callback'] = callback
        self.listeners.append(data)

    def add_user(self,user_id,user_name):
        user_data = dict(user_id=user_id,user_name=user_name)

        self.users.append(user_data)

        note = notification('login',user_data)
        self.send_notification(note)

    def send_notification(self,message,user_id=None):
        tmp_listeners = self.listeners
        self.listeners = []

        for data in tmp_listeners:
            if user_id != None:
                if user_id != data['user_id']:
                    self.listeners.append(data)
                    continue
            callback = data['callback']
            try:
                callback(message)
            except:
                logging.error('Error in listeners callback',exc_info=True)

class BaseHandler(tornado.web.RequestHandler):
    @property
    def chat(self):
        return self.application.chat

class MainHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('templates/chat-main.html')

class LoginHandler(BaseHandler):
    def post(self):
        user_id = str(uuid.uuid4())
        user_name = self.get_argument('username')

        self.chat.add_user(user_id,user_name)

        self.finish(dict(user_id=user_id,user_name=user_name,users = self.chat.users))


class UpdateHandler(BaseHandler):

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        user_id = self.get_argument('user_id')

        # self.chat.add_listener(self.async_callback(self.handle_updates),user_id=user_id)
        self.chat.add_listener(self.handle_updates,user_id=user_id)

    def handle_updates(self,update):
        if not self.request.connection.stream.closed():
            self.finish(update)

class SendHandler(BaseHandler):
    def post(self, *args, **kwargs):
        to_user_id =self.get_argument('to_user_id')
        from_user_id = self.get_argument('from_user_id')

        data = dict(
            from_user_id = from_user_id,
            to_user_id = to_user_id,
            text = self.get_argument('text')
        )

        msg = notification('message',data)
        self.chat.send_notification(msg,user_id=to_user_id)

        msg['type'] = 'sent'
        self.finish(msg)

class TypingHandler(BaseHandler):
    def post(self, *args, **kwargs):
        to_user_id = self.get_argument('to_user_id')
        from_user_id =self.get_argument('from_user_id')

        data = dict(from_user_id = from_user_id ,to_user_id = to_user_id)
        msg = notification('typing',data)
        self.chat.send_notification(msg,user_id=to_user_id)

        msg['type'] = 'recv'
        self.finish(msg)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",MainHandler),
            (r"/login/?",LoginHandler),
            (r"/updates",UpdateHandler),
            (r"/send/?",SendHandler),
            (r"/typing/?",TypingHandler),

        ]
        path = os.path.join(os.path.dirname(__file__),'static')
        settings = dict(static_path = path)

        tornado.web.Application.__init__(self,handlers,**settings)
        self.chat = Chat()

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(Application())
    tornado.options.parse_command_line()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()