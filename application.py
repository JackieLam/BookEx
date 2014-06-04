#coding:utf-8

from urls import urls

import tornado.web
import os
import pymongo

SETTINGS = dict(
template_path=os.path.join(os.path.dirname(__file__), "templates"),
static_path=os.path.join(os.path.dirname(__file__), "static"),
cookie_secret="Q21RWvKbSlqao0wY0wcCKW497Fav7ENRnpB3u68kXPI=",
)
application = tornado.web.Application(
                handlers = urls,
                **SETTINGS
)

conn = pymongo.Connection("localhost", 27017)
application.db = conn["bookEX"]
