# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 14:21
# @Author  : Lwq
# @File    : book.py
# @Software: PyCharm
import json

from flask import jsonify, request, Response, render_template, flash

from app.forms.book import SearchForm
from app.view_modules.book import BookCollection, BookViewModule
from app.web.blueprint import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search')
def search():
    """
        q:关键字或者是ISBN
        page:分页信息
        ?q=..&page=..
    """
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入搜索关键字')
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModule(yushu_book.first)
    return render_template('book_detail.html', book=book)


@web.route('/test/local')
def testlocal():
    from test.nolocal import n
    print(n.v)
    n.v = 2
    print('==========================')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('==========================')
    from flask import current_app
    print(id(current_app))
    return ''


@web.route('/test/temp')
def testtemp():
    r = {
        'name': 'lwq',
        'age': 18
    }
    # 消息闪现
    flash('hello lwq ')
    flash('这是消息闪现')
    return render_template('test.html', data=r)
