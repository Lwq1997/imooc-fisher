# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 17:38
# @Author  : Lwq
# @File    : gift.py
# @Software: PyCharm
from app.view_modules.book import BookViewModule


class MyGifts:
    def __init__(self, gifts_of_mine, wishes_count_list):
        self.gifts = []

        self.__gift_of_mine = gifts_of_mine
        self.__wisher_count_list = wishes_count_list

        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gift_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wisher_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count': count,
            'book': BookViewModule(gift.book),
            'id': gift.id
        }
        return r
