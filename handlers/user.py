#coding:utf-8

import tornado.web
import tornado.ioloop
import os
import sys
import json

from model.entity import *

class BaseHandler(tornado.web.RequestHandler):
	def getCurrentUser(self):
		return self.get_secure_cookie("user")

class UserInfoHandler(BaseHandler):
	def post(self):
		user_id = self.get_argument("user_id", None)
		sql_sbquery = 'SELECT * FROM Users WHERE user_id = \'' + user_id + '\''
		#result = []
		user_info = self.application.db.query(sql_sbquery)
		#result.append(user_info)
		self.write(json.dumps(user_info))

class MainHandler(BaseHandler):
	def get(self):
		if self.current_user:
			user_id = tornado.escape.xhtml_escape(self.current_user)
			self.write(user_id)
		else:
			self.write("none")
		self.write("\n")

class LoginHandler(BaseHandler):
	def get(self):
		information = ""
		self.render("login.html",
					information = information)

	def post(self):
		userLoginFields = ['user_id', 'password']
		#userDict = self.application.db.userup
		userInfo = dict()
		user_id = self.get_argument("user_id", None)
		password = self.get_argument("password", None)
		sql_sbquery = 'SELECT * FROM Users WHERE user_id = \'' + user_id + '\''
		user_row = self.application.db.query(sql_sbquery)
		#for key in userLoginFields:
		#	userInfo[key] = self.get_argument(key, None)
		information = ""
		if user_id:
			#searchResult = userDict.find_one({"user_id": userInfo["user_id"]})
			if user_row:
				sql_sbquery2 = 'SELECT * FROM Users WHERE user_id = \'' + user_id + '\' AND password = \'' + password + '\''
				user_row2 = self.application.db.query(sql_sbquery2)
				if user_row2:
				#if userInfo["password"] == searchResult["password"]:
					self.set_secure_cookie("user", user_id)
					self.redirect("/")
					return
				else:
					information = "密码错误"
			else:
				information = "帐号不存在"
		else:
			information = "帐号不能为空"
		self.render("login.html",
					information = information)

class LogoutHandler(BaseHandler):
	def get(self):
		self.set_secure_cookie("user", "")
		self.write("logout succeed\n")
		self.redirect("/")

class RegisterHandler(tornado.web.RequestHandler):
	def get(self):
		information = ""
		self.render("register.html",
					information = information)

	def post(self, user_id=None):
		#userRegisteFields = ['user_id', 'password', 'confirm_password', 'email', 'address']
		user_id = self.get_argument("user_id", None).encode('utf-8')
		user_name = user_id
		password = self.get_argument('password', None).encode('utf-8')
		confirm_password = self.get_argument('confirm_password', None).encode('utf-8')
		email = self.get_argument('email', None).encode('utf-8')
		address = self.get_argument('address', None).encode('utf-8')

		#userDict = self.application.db.user
		userInfo = dict()
		#for key in userRegisteFields:
		#	userInfo[key] = self.get_argument(key, None)
		information = ""
		if password == confirm_password:
			if user_id:
				#searchResult = userDict.find_one({"user_id": userInfo["user_id"]})
				sql_sbquery = 'SELECT * FROM Users WHERE user_id = \'' + user_id + '\''
				user_row = self.application.db.query(sql_sbquery)
				if user_row:
					information = "该帐号已被注册"
				else:
					#userDict.insert(userInfo)
					tup = (user_id, user_name, email, address, password)
					sql_sent = 'INSERT INTO Users VALUES' + str(tup)
					self.application.db.execute(sql_sent)
					self.redirect("/api/v1/users/login")
					return
			else:
				information = "帐号不得为空"
		else:
			information = "两次密码输入不一致"
		self.render("register.html",
					information = information)

class UserInfoHandler(tornado.web.RequestHandler):
	def get(self):
		user_id = self.get_argument('user_id')
