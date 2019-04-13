# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 14:21
# @Author  : Lwq
# @File    : book.py
# @Software: PyCharm

from flask import request, render_template, flash
from flask_login import current_user

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_modules.book import BookCollection, BookViewModule
from app.view_modules.trade import TradeInfo
from app.web.blueprint import web


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
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍详情
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModule(yushu_book.first)

    if current_user.is_authenticated:
        # 如果未登录，current_user将是一个匿名用户对象
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html', book=book,
                           has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes,
                           wishes=trade_wishes_model, gifts=trade_gifts_model)


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
