#coding:utf-8

from urls import urls
import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.httpserver
import os
import torndb
import sae
import sae.const

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        settings = {
            "cookie_secret": "Q21RWvKbSlqao0wY0wcCKW497Fav7ENRnpB3u68kXPI=",
            "debug" : True,
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static")
        }
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = torndb.Connection(
            host="%s:%s"%(sae.const.MYSQL_HOST,str(sae.const.MYSQL_PORT)), 
            database=sae.const.MYSQL_DB, user=sae.const.MYSQL_USER, 
            password=sae.const.MYSQL_PASS, max_idle_time = 30)
        # Create the MySQL Tables
        book_create = 'CREATE TABLE IF NOT EXISTS Book(book_name VARCHAR(40), author VARCHAR(40), genre VARCHAR(40), summary TEXT, CONSTRAINT pk_book PRIMARY KEY(book_name))'
        self.db.execute(book_create)
        user_create = 'CREATE TABLE IF NOT EXISTS Users(user_id BIGINT, user_name VARCHAR(40), email TEXT, address TEXT, password TEXT, CONSTRAINT pk_users PRIMARY KEY(user_id))'
        self.db.execute(user_create)
        savebook_create = 'CREATE TABLE IF NOT EXISTS SaveBook(user_id BIGINT, book_name VARCHAR(40), CONSTRAINT pk_savebook PRIMARY KEY(user_id, book_name))'
        self.db.execute(savebook_create)
        borrowbook_create = 'CREATE TABLE IF NOT EXISTS BorrowBook(owner_id BIGINT, book_name VARCHAR(40), state VARCHAR(40), borrower_id BIGINT, CONSTRAINT pk_borrowbook PRIMARY KEY(owner_id, book_name))'
        self.db.execute(borrowbook_create)
        comment_cre = 'CREATE TABLE IF NOT EXISTS Comment(book_name VARCHAR(40), user_id BIGINT, content TEXT, CONSTRAINT pk_comment PRIMARY KEY(user_id, book_name))'
        self.db.execute(comment_cre)

application = Application()