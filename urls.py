#coding:utf-8

from handlers.user import LoginHandler
from handlers.user import LogoutHandler
from handlers.user import RegisterHandler
from handlers.index import MainHandler
from handlers.book import BookHandler, AddBookHandler, DeleteBookHandler
from handlers.save import SaveBookHandler
from handlers.borrow import BorrowBookHandler

urls = [
    (r'/', MainHandler),
    (r'/api/v1/users/login', LoginHandler),
    (r'/api/v1/users/logout', LogoutHandler),
    (r'/api/v1/users/register', RegisterHandler),
    (r'/api/v1/books', BookHandler),
    (r'/api/v1/books/add', AddBookHandler),
    (r'/api/v1/books/delete', DeleteBookHandler),
    (r'/api/v1/savebook', SaveBookHandler),
    (r'/api/v1/borrowbook', BorrowBookHandler),
]