import tornado.web

class BorrowBookHandler(tornado.web.RequestHandler):
	def get(self):
		owner_id = self.get_argument('owner_id').encode('utf-8')
		book_name = self.get_argument('book_name', None)

		if book_name != None: 
			book_name = book_name.encode('utf-8')
			sql_search = 'SELECT * FROM BorrowBook WHERE owner_id = \'' + owner_id + '\' AND book_name = \'' + book_name + '\''
			row_borrowbooks = self.application.db.query(sql_search)

			sql_searchbook = 'SELECT * FROM Book WHERE book_name = \'' + book_name + '\''
			books = self.application.db.query(sql_searchbook)
			books[0]['state'] = row_borrowbooks[0]['state']
			self.write(str(books[0]))
		else:
			sql_search = 'SELECT * FROM BorrowBook WHERE owner_id = \'' + owner_id + '\''
			row_borrowbooks = self.application.db.query(sql_search)

			result = []
			for row in row_borrowbooks:
				sql_searchbook = 'SELECT * FROM Book WHERE book_name = \'' + row['book_name'] + '\''
				books = self.application.db.query(sql_searchbook)
				if len(books) > 0: 
					books[0]['state'] = row['state']
					result.append(str(books[0]))

			self.write(str(result))


	def post(self):
		owner_id = self.get_argument('owner_id').encode('utf-8')
		book_name = self.get_argument('book_name').encode('utf-8')
		borrower_id = self.get_argument('borrower_id', None).encode('utf-8')

		# 1. update the state of the BorrowBook Table
		sql_changestate = 'UPDATE BorrowBook SET state = \'borrowed\' WHERE owner_id = \'' + owner_id + '\' AND book_name = \'' + book_name + '\''
		self.application.db.execute(sql_changestate)
		if borrower_id != None: 
			# 2. Update the borrower_id of the Table if there's param
			sql_changeborrowerid = 'UPDATE BorrowBook SET borrower_id = \'' + borrower_id + '\' WHERE owner_id = \'' + owner_id + '\' AND book_name = \'' + book_name + '\''
			self.application.db.execute(sql_changeborrowerid)

		# 3. Feedback the result in the Borrow Table
		sql_search = 'SELECT * FROM BorrowBook WHERE owner_id = \'' + owner_id + '\' AND book_name = \'' + book_name + '\''
		book = self.application.db.query(sql_search)

		self.write(str(book))