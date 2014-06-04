#coding:utf-8

import tornado.web
import tornado.ioloop
import os
import sys

import pymongo

from model.entity import Entity

class BaseHandler(tornado.web.RequestHandler):
	def getCurrentUser(self):
		return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
	def get(self):
		if self.current_user:
			user_id = tornado.escape.xhtml_escape(self.current_user)
			self.write(user_id)
		else:
			self.write("none")
		self.write("\n")

class LoginHandler(BaseHandler):
	def post(self):
		userLoginFields = ['user_id', 'password']
		userDict = self.application.db.user
		userInfo = dict()
		for key in userLoginFields:
			userInfo[key] = self.get_argument(key, None)
		if userInfo["user_id"]:
			searchResult = userDict.find_one({"user_id": userInfo["user_id"]})
			if searchResult:
				if userInfo["password"] == searchResult["password"]:
					del searchResult["_id"]
					self.write(searchResult)
					self.set_secure_cookie("user", userInfo["user_id"])
				else:
					self.write("wrong password")
			else:
				self.write("user not found")
		else:
			self.write("user_id cannot be empty")
		self.write("\n")

class LogoutHandler(BaseHandler):
	def get(self):
		self.set_secure_cookie("user", "")
		self.write("logout succeed\n")

class RegisterHandler(tornado.web.RequestHandler):
	def post(self, user_id=None):
		userRegisteFields = ['user_id', 'password', 'user_name', 'email', 'cellphone', 'address']
		userDict = self.application.db.user
		userInfo = dict()
		for key in userRegisteFields:
			userInfo[key] = self.get_argument(key, None)

		if userInfo["user_id"]:
			searchResult = userDict.find_one({"user_id": userInfo["user_id"]})
			if searchResult:
				self.write("This ID has been registered")
			else:	
				userDict.insert(userInfo)
				del userInfo["_id"]
				self.write(userInfo)
		else:
			self.write("user_id cannot be empty")
		self.write("\n")