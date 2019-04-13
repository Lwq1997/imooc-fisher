from flask import render_template

from app.models.gift import Gift
from app.view_modules.book import BookViewModule
from app.web.blueprint import web

__author__ = '七月'


@web.route('/')
def index():
    recent_gift = Gift.recent()
    books = [BookViewModule(gift.book) for gift in recent_gift]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
