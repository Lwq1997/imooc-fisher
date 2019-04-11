# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 11:41
# @Author  : Lwq
# @File    : book.py
# @Software: PyCharm


class BookViewModule:
    def __init__(self, book):
        self.title = book['title']
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.publisher = book['publisher']
        self.image = book['image']
        self.pages = book['pages']
        self.isbn = book['isbn']
        self.summary = book['summary']

    def intro(self):
        intros = filter(lambda x: True if x else False, [self.publisher, self.author, self.price])
        return '/'.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModule(book) for book in yushu_book.books]
        self.keyword = keyword


class _BookViewModule:

    @classmethod
    def package_singler(cls, data, keyword):
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['book'] = cls.__cut_book_data(data)
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['book'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'author': '、'.join(data['author']),
            'price': data['price'],
            'publisher': data['publisher'],
            'image': data['image'],
            'pages': data['pages'] or '',
            'summary': data['summary'] or ''
        }
        return book
