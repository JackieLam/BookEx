#coding:utf-8

import tornado.web

#param of a book
book_fields = ['book_name', 'author', 'genre', 'image_url', 'summary']

class BookHandler(tornado.web.RequestHandler):
	def get(self):
		search = dict()
		for key in book_fields:
			search[key] = self.get_argument(key, None)
			if search[key] != None:
				search[key] = search[key].encode("utf-8")
			else: 
				search.pop(key)
		
		coll = self.application.db['Book']
		
		shouldsearch = False
		for key in search:
			if search[key] != None:
				shouldsearch = True
		
		if shouldsearch:
			books = coll.find(search)
		else:
			books = coll.find()

		result = []
		for book in books:
			del book["_id"]
			result.append(book)

		self.write(str(result))	#不能返回python的list数据格式，需要把list转换成字符串
		#没有把unicode转换成utf-8码

class AddBookHandler(tornado.web.RequestHandler):
	def get(self, book_name=None):	#实际不需要这个API
		book = dict()
		if book_name:
			coll = self.application.db['Book']
			book = coll.find_one({"book_name": book_name})
		self.render("book_edit.html",
			page_title="Burt's Books",
			header_text="Edit book",
			book=book)

	def post(self, book_name=None):
		import time
		BookTable = self.application.db['Book']
		BorrowBookTable = self.application.db["BorrowBook"]

		# 1. Insert new book to the [Book Table]
		book = dict()
		if book_name:
			book = BookTable.find_one({"book_name": book_name}) #找到已存在的book并且修改
		for key in book_fields:
			book[key] = self.get_argument(key, None)

		if book_name:
			BookTable.save(book)
		else:
			book['date_added'] = int(time.time())
			BookTable.insert(book)

		# 2. Insert info to [BorrowBook Table]
		new_row = dict()
		new_row['book_name'] = self.get_argument('book_name')
		new_row['owner_id'] = self.get_argument('user_id')
		new_row['borrower_id'] = None
		new_row['state'] = 'available'
		BorrowBookTable.insert(new_row)

		del book['_id']
		self.write(book)

class DeleteBookHandler(tornado.web.RequestHandler):
	def delete(self):
		
		BookTable = self.application.db['Book']
		BorrowBookTable = self.application.db['BorrowBook']
		SaveBookTable = self.application.db['SaveBook']
		book_name = self.get_argument('book_name')
		user_id = self.get_argument('user_id')
		books_to_delete = BookTable.find({'book_name': book_name})

		result = []
		for book in books_to_delete:
			del book["_id"]
			result.append(book)

		# 1. Delete from the [Book Table]
		BookTable.remove({'book_name': book_name})
		# 2. Delete from the [BorrowBook Table]
		BorrowBookTable.remove({'book_name': book_name, 'user_id': user_id})
		# 3. Delete from the [SaveBook Table]
		SaveBookTable.remove({'book_name': book_name, 'owner_id': user_id})

		self.write(str(result))