import tornado.web

class SaveBookHandler(tornado.web.RequestHandler):
	def get(self):
		user_id = self.get_argument('user_id').encode('utf-8')

		q_sentence = 'SELECT book_name FROM SaveBook WHERE user_id = \'' + user_id + '\''
		book_names = self.application.db.query(q_sentence)

		result = []
		for book_name in book_names:
			q_book = 'SELECT * FROM Book WHERE book_name = \'' + book_name['book_name'] + '\''
			book = self.application.db.query(q_book)
			result.append(book)

		self.write(str(result))

	def post(self):
		user_id = self.get_argument('user_id').encode('utf-8')
		book_name = self.get_argument('book_name').encode('utf-8')

		tup = (user_id, book_name)
		sql_sbquery = 'SELECT * FROM SaveBook WHERE book_name = \'' + book_name + '\' AND user_id = \'' + user_id + '\''
		savebook_row = self.application.db.query(sql_sbquery)
		if not savebook_row: 
			# 1. Insert into the SaveBook Table
			sql_savebook = 'INSERT INTO SaveBook VALUES ' + str(tup)
			self.application.db.execute(sql_savebook)
			# 2. Query the book information and return
			sql_bookquery = 'SELECT * FROM Book WHERE book_name = \'' + book_name + '\''
			book = self.application.db.query(sql_bookquery)
			self.write(str(book))
		else: 
			self.write({"error": "Already collected"})

	def delete(self):
		user_id = self.get_argument('user_id').encode('utf-8')
		book_name = self.get_argument('book_name').encode('utf-8')

		sql_sbquery = 'SELECT * FROM SaveBook WHERE book_name = \'' + book_name + '\' AND user_id = \'' + user_id + '\''
		savebook_row = self.application.db.query(sql_sbquery)
		if savebook_row: 
			# 1. Delete the row in SaveBook Table
			sql_savebook = 'DELETE FROM SaveBook WHERE user_id = \'' + user_id + '\' AND book_name = \'' + book_name + '\''
			self.application.db.execute(sql_savebook)
			# 2. Query the book information and return
			sql_bookquery = 'SELECT * FROM Book WHERE book_name = \'' + book_name + '\''
			book = self.application.db.query(sql_bookquery)
			self.write(str(book))
		else: 
			self.write({"error": "Not collected"})
