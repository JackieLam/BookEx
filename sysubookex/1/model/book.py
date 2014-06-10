#coding:utf-8

class Book(object):
	def __init__(self, book_id, poster_id, name, author, image_url, summary):
		self.id = book_id
		self.poster_id = poster_id
		self.name = name
		self.author = author
		self.image_url = image_url
		self.summary = summary

def getName(name):
    return Book(name)