# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 13:12
# @Author  : Lwq
# @File    : helper.py
# @Software: PyCharm


def is_isbn_or_key(word):
    '''
    判断传来的word是isbn还是关键字
        isbn13:由13个数字组成
        isbn10:由10个数字组成，中间带有-

    :param word:
    :return:
    '''
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit:
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'

    return isbn_or_key
