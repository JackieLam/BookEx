# -*- coding: utf8 -*-

import tornado.web
import torndb
import json

#param of a book
book_fields = ['isbn', 'book_name', 'author', 'image_url','genre', 'image_url', 'summary']

class BookHandler(tornado.web.RequestHandler):
	def get(self):
		# 1. Get the search params
		search = dict()
		for key in book_fields:
			search[key] = self.get_argument(key, None)
			if search[key] != None:
				search[key] = search[key].encode('utf8')
			else: 
				search.pop(key)

		# book_name = self.get_argument('book_name').encode('utf8')
		# print "utf8参数中文长什么样子" + book_name
		print "SEARCH DICT ------------- " + str(search)

		# 2. Search through the table
		condition = ""
		first = True
		for key in search.keys():
			if not first:
				condition += ' AND b.%s LIKE \'%s\'' % (key, search[key])
			else:
				first = False
				condition += 'b.%s LIKE \'%s\'' % (key, search[key])

		if condition != "":
			q_sentence = "SELECT * FROM Book b WHERE " + condition
		else:
			q_sentence = "SELECT * FROM Book b"
		print "############" + q_sentence

		result = []
		for book in self.application.db.query(q_sentence):
			result.append(book)
		
		print "Return -- " + str(result)

		self.write(json.dumps(result))

class AddBookHandler(tornado.web.RequestHandler):
	# 暂时没有考虑book_name重复的情况应该怎么通知用户/修改数据库
	def post(self, book_name=None):
		isbn = self.get_argument('isbn', None).encode('utf8')
		book_name = self.get_argument('book_name', None).encode('utf8')
		author = self.get_argument('author', None).encode('utf8')
		image_url = self.get_argument('image_url', None).encode('utf8')
		genre = self.get_argument('genre', None).encode('utf8')
		summary = self.get_argument('summary', None).encode('utf8')
		user_id = self.get_argument('user_id', None).encode('utf8')

		print "我操为什么是unicode啊 - ", book_name
		# 1. Insert into the Book Table
		tup = (isbn, book_name, author, image_url, genre, summary)
		print "我操为什么乱码啊 - ", tup
		sql_sent = 'INSERT INTO Book VALUES' + str(tup)

		self.application.db.execute(sql_sent)

		# 2. Insert into the BorrowBook Table
		tup2 = (user_id, isbn, 'available', 0)
		sql_sent2 = 'INSERT INTO BorrowBook VALUES' + str(tup2)

		self.application.db.execute(sql_sent2)
		self.write(json.dumps(tup))

class DeleteBookHandler(tornado.web.RequestHandler):
	def delete(self):
		isbn = self.get_argument('isbn').encode('utf8')
		book_name = self.get_argument('book_name').encode('utf8')
		user_id = self.get_argument('user_id').encode('utf8')

		# [WARNING] - Should first check out whether the book is owned by the owner
		# 0. Find out the book in the Book Table first
		sql_sent0 = 'SELECT * FROM Book WHERE isbn = \'' + isbn + '\''
		book = self.application.db.query(sql_sent0)
		
		# 1. Delete from the [Book Table]
		sql_sent1 = 'DELETE FROM Book WHERE isbn = \'' + isbn + '\''
		self.application.db.execute(sql_sent1)
		# 2. Delete from the [BorrowBook Table]
		sql_sent2 = 'DELETE FROM BorrowBook WHERE isbn = \'' + isbn + '\' AND owner_id = \'' + user_id + '\''
		self.application.db.execute(sql_sent2)
		# 3. Delete from the [SaveBook Table]
		sql_sent3 = 'DELETE FROM SaveBook WHERE isbn = \'' + isbn + '\' AND user_id = \'' + user_id + '\''
		self.application.db.execute(sql_sent3)

		self.write(json.dumps(book))