import tornado.web
import json

class CommentHandler(tornado.web.RequestHandler):
	def get(self):
		book_name = self.get_argument('book_name').encode('utf-8')
		select_comment = 'SELECT * FROM Comment WHERE book_name = \'' + book_name + '\''
		rows = self.application.db.query(select_comment)

		self.write(json.dumps(rows))

	def post(self):
		book_name = self.get_argument('book_name').encode('utf-8')
		user_id = self.get_argument('user_id').encode('utf-8')
		content = self.get_argument('content').encode('utf-8')

		# 1. Insert the tuple
		tup = (book_name, user_id, content)
		insert_comment = 'INSERT INTO Comment VALUES ' + str(tup)
		self.application.db.execute(insert_comment)

		# 2. Select and return
		select_comment = 'SELECT * FROM Comment WHERE book_name = \'' + book_name + '\' AND user_id = \'' + user_id + '\''
		post_result = self.application.db.query(select_comment)

		self.write(json.dumps(post_result))

	def delete(self):
		book_name = self.get_argument('book_name').encode('utf-8')
		user_id = self.get_argument('user_id').encode('utf-8')

		select_comment = 'SELECT * FROM Comment WHERE book_name = \'' + book_name + '\' AND user_id = \'' + user_id + '\''
		result = self.application.db.query(select_comment)

		delete_comment = 'DELETE FROM Comment WHERE book_name = \'' + book_name + '\' AND user_id = \'' + user_id + '\''
		self.application.db.execute(delete_comment)

		self.write(json.dumps(result))