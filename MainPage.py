#!/usr/bin/python
#coding=utf-8
import tornado.httpserver  
import tornado.ioloop  
from tornado.ioloop import PeriodicCallback
import tornado.web  
import tornado.options  
import os.path  
import time
import json
import sys

import DBHelper

from tornado.options import define, options  

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

    def get_current_user(self):
        return self.get_secure_cookie("username")

class LoginHandler(BaseHandler):  
    def get(self):  
        self.render('login1.html')  
    def post(self):  
        user_name = self.get_argument("username");
        password = self.get_argument("password");
        if cmp(user_name, "dabaojian")  == 0 and cmp(password, "123456") == 0:
            self.set_secure_cookie("username", self.get_argument("username"), expires_days=None)
            self.redirect("/")  
        else:
            self.redirect('/login', status='error')

class WelcomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("main.html", user=self.current_user)

class NoticeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("notice.html", user=self.current_user)

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("username")
        self.redirect("/")

class AddAgentHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("AddAgent.html")

class QueryAgentHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("QueryAgent.html")

if __name__ == "__main__":

    port = sys.argv[1]

    define("port", default=port, help="run on the given port", type=int)

    tornado.options.parse_command_line()
    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "login_url": "/login"
    }
    application = tornado.web.Application([
        (r'/', WelcomeHandler),
        (r'/login', LoginHandler),
        (r'/logout', LogoutHandler),
        (r'/addAgent', AddAgentHandler),
        (r'/queryAgent', QueryAgentHandler),
        (r'/notice', NoticeHandler)
    ],debug= True,**settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
