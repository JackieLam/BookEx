#coding:utf-8

from urls import urls

import sys
import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.httpserver
import os
import torndb

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
		self.db = torndb.Connection('localhost','mysql',user='root', charset='utf8')
		# drop_sen = 'DROP TABLE IF EXISTS Book, Users, SaveBook, BorrowBook, Comment'
		# self.db.execute(drop_sen)
		book_create = 'CREATE TABLE IF NOT EXISTS Book(isbn VARCHAR(40), book_name TEXT, author TEXT, genre TEXT, summary TEXT, CONSTRAINT pk_book PRIMARY KEY(isbn))'
		self.db.execute(book_create)
		user_create = 'CREATE TABLE IF NOT EXISTS Users(user_id BIGINT, user_name TEXT, email TEXT, address TEXT, password TEXT, CONSTRAINT pk_users PRIMARY KEY(user_id))'
		self.db.execute(user_create)
		savebook_create = 'CREATE TABLE IF NOT EXISTS SaveBook(user_id BIGINT, isbn VARCHAR(40), CONSTRAINT pk_savebook PRIMARY KEY(user_id, isbn))'
		self.db.execute(savebook_create)
		borrowbook_create = 'CREATE TABLE IF NOT EXISTS BorrowBook(owner_id BIGINT, isbn VARCHAR(40), state TEXT, borrower_id BIGINT, CONSTRAINT pk_borrowbook PRIMARY KEY(owner_id, isbn))'
		self.db.execute(borrowbook_create)
		comment_cre = 'CREATE TABLE IF NOT EXISTS Comment(isbn VARCHAR(40), user_id BIGINT, content TEXT, CONSTRAINT pk_comment PRIMARY KEY(user_id, isbn))'
		self.db.execute(comment_cre)

application = Application()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PORT = sys.argv[1]
    application.listen(PORT)
    print 'Development server is running at http://127.0.0.1:%s/' % PORT
    print 'Quit the server with CONTROL-C'
    tornado.ioloop.IOLoop.instance().start()