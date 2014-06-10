import tornado.web
import json

class BorrowBookHandler(tornado.web.RequestHandler):
	def get(self):
		owner_id = self.get_argument('owner_id', None)
		isbn = self.get_argument('isbn', None)

		if isbn != None and owner_id != None: 
			isbn = isbn.encode('utf-8')
			owner_id = owner_id.encode('utf-8')
			sql_search = 'SELECT * FROM BorrowBook WHERE owner_id = \'' + owner_id + '\' AND isbn = \'' + isbn + '\''
			row_borrowbooks = self.application.db.query(sql_search)

			sql_searchbook = 'SELECT * FROM Book WHERE isbn = \'' + isbn + '\''
			books = self.application.db.query(sql_searchbook)
			books[0]['state'] = row_borrowbooks[0]['state']

			self.write(json.dumps(books[0]))
		elif owner_id != None:
			owner_id = owner_id.encode('utf-8')
			sql_search = 'SELECT * FROM BorrowBook WHERE owner_id = \'' + owner_id + '\''
			row_borrowbooks = self.application.db.query(sql_search)

			result = []
			for row in row_borrowbooks:
				sql_searchbook = 'SELECT * FROM Book WHERE isbn = \'' + row['isbn'] + '\''
				books = self.application.db.query(sql_searchbook)
				if len(books) > 0: 
					books[0]['state'] = row['state']
					result.append(books[0])

			self.write(json.dumps(result))
		else:
			isbn = isbn.encode('utf-8')
			sql_search = 'SELECT * FROM BorrowBook WHERE isbn = \'' + isbn + '\''
			row_borrowbooks = self.application.db.query(sql_search)

			result = []
			for row in row_borrowbooks:
				sql_searchbook = 'SELECT * FROM Users WHERE user_id = \'' + str(row['owner_id']) + '\''
				userlist = self.application.db.query(sql_searchbook)
				for us in userlist:
					result.append(us)

			self.write(json.dumps(result))

	def post(self):
		owner_id = self.get_argument('owner_id').encode('utf-8')
		isbn = self.get_argument('isbn').encode('utf-8')
		borrower_id = self.get_argument('borrower_id', None).encode('utf-8')

		# 1. update the state of the BorrowBook Table
		sql_changestate = 'UPDATE BorrowBook SET state = \'borrowed\' WHERE owner_id = \'' + owner_id + '\' AND isbn = \'' + isbn + '\''
		self.application.db.execute(sql_changestate)
		if borrower_id != None: 
			# 2. Update the borrower_id of the Table if there's param
			sql_changeborrowerid = 'UPDATE BorrowBook SET borrower_id = \'' + borrower_id + '\' WHERE owner_id = \'' + owner_id + '\' AND isbn = \'' + isbn + '\''
			self.application.db.execute(sql_changeborrowerid)

		# 3. Feedback the result in the Borrow Table
		sql_search = 'SELECT * FROM BorrowBook WHERE owner_id = \'' + owner_id + '\' AND isbn = \'' + isbn + '\''
		book = self.application.db.query(sql_search)

		self.write(json.dumps(book))