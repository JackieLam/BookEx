import tornado.web
import json

class CommentHandler(tornado.web.RequestHandler):
	def get(self):
		isbn = self.get_argument('isbn').encode('utf-8')
		select_comment = 'SELECT * FROM Comment WHERE isbn = \'' + isbn + '\''
		rows = self.application.db.query(select_comment)

		self.write(json.dumps(rows))

	def post(self):
		isbn = self.get_argument('isbn').encode('utf-8')
		user_id = self.get_argument('user_id').encode('utf-8')
		content = self.get_argument('content').encode('utf-8')

		# 1. Insert the tuple
		tup = (isbn, user_id, content)
		insert_comment = 'INSERT INTO Comment VALUES ' + str(tup)
		self.application.db.execute(insert_comment)

		# 2. Select and return
		select_comment = 'SELECT * FROM Comment WHERE isbn = \'' + isbn + '\' AND user_id = \'' + user_id + '\''
		post_result = self.application.db.query(select_comment)

		self.write(json.dumps(post_result))

	def delete(self):
		isbn = self.get_argument('isbn').encode('utf-8')
		user_id = self.get_argument('user_id').encode('utf-8')

		select_comment = 'SELECT * FROM Comment WHERE isbn = \'' + isbn + '\' AND user_id = \'' + user_id + '\''
		result = self.application.db.query(select_comment)

		delete_comment = 'DELETE FROM Comment WHERE isbn = \'' + isbn + '\' AND user_id = \'' + user_id + '\''
		self.application.db.execute(delete_comment)

		self.write(json.dumps(result))