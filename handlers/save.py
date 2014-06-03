import tornado.web

class SaveBookHandler(tornado.web.RequestHandler):
	def get(self):
		user_id = self.get_argument('user_id')
		SaveBookTable = self.application.db['SaveBook']
		BookTable = self.application.db['Book']
		records = SaveBookTable.find({'user_id': user_id})

		result = []
		for record in records: 
			book = BookTable.find_one({'book_name': record['book_name']})
			if book:
				del book['_id']
				result.append(book)

		self.write(str(result))

	def post(self):
		user_id = self.get_argument('user_id')
		book_name = self.get_argument('book_name')
		SaveBookTable = self.application.db['SaveBook']
		BookTable = self.application.db['Book']
		# 1. If no save record, save the book. 
		if not SaveBookTable.find_one({'user_id': user_id, 'book_name': book_name}):
			SaveBookTable.insert({'user_id': user_id, 'book_name': book_name})
			# 2. Return the book information
			book = BookTable.find_one({'book_name': book_name})
			del book['_id']
			self.write(book)
		else:
			self.write({'error': 'Already existed'})

	def delete(self):
		user_id = self.get_argument('user_id')
		book_name = self.get_argument('book_name')
		SaveBookTable = self.application.db['SaveBook']
		BookTable = self.application.db['Book']

		# 1. If there's save record, delete the book. 
		if SaveBookTable.find_one({'user_id': user_id, 'book_name': book_name}):
			SaveBookTable.remove({'user_id': user_id, 'book_name': book_name})
			# 2. Return the book information
			book = BookTable.find_one({'book_name': book_name})
			del book['_id']
			self.write(book)
		else:
			self.write({'error': 'Have not saved the book before'})