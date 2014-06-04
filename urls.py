#coding:utf-8

from handlers.user import LoginHandler
from handlers.user import LogoutHandler
from handlers.user import MainHandler
from handlers.user import RegisterHandler


urls = [
    (r'/api/v1/users/login', LoginHandler),
    (r'/api/v1/users/logout', LogoutHandler),
    (r'/api/v1/users/register', RegisterHandler),
    (r'/api/v1', MainHandler)
]