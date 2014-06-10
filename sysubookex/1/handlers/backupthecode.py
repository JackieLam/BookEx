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