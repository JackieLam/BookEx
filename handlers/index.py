#coding:utf-8

import tornado.web
from handlers.book import BookHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
		user = self.get_secure_cookie("user")
		self.render('index.html',user=user)

class FoundHandler(tornado.web.RequestHandler):
    def get(self):
		user = self.get_secure_cookie("user")
		self.render('SearchResult.html',user=user)

class NotFoundHandler(tornado.web.RequestHandler):
    def get(self):
		user = self.get_secure_cookie("user")
		self.render('SearchNoResult.html', user=user)

class AddBookShowHandler(tornado.web.RequestHandler):
    def get(self):
		user = self.get_secure_cookie("user")
		self.render('addNewBook.html', user=user)

class HomepageHandler(tornado.web.RequestHandler):
    def get(self):
		user = self.get_secure_cookie("user")
		self.render('homePage.html',user=user)
		
class BookShowHandler(tornado.web.RequestHandler):
    def get(self):
		user = self.get_secure_cookie("user")
		self.render('bookShow.html',user=user)