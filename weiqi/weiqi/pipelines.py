# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import json


class WeiqiPipeline(object):
    def __init__(self):
        self.connect = sqlite3.connect('books.db')
        # self.connect.execute("CREATE TABLE book ("
        #                      "book_name TEXT,"
        #                      "book_sub_name TEXT,"
        #                      "course_index TEXT,"
        #                      "prepos_b TEXT,"
        #                      "prepos_w TEXT,"
        #                      "answers TEXT,"
        #                      "board_size TEXT,"
        #                      "black_first TEXT,"
        #                      "qtypename TEXT,"
        #                      "levelname TEXT"
        #                      " ) ")

    def process_item(self, item, spider):
        # print("result：" + str(item))

        book_name = item["book_name"]
        book_sub_name = item["book_sub_name"]
        course_index = item["course_index"]
        prepos_b = str(item["prepos_b"])
        prepos_w = str(item["prepos_w"])
        answers = str(item["answers"])
        board_size = str(item["board_size"])
        black_first = str(item["black_first"])
        qtypename = str(item["qtypename"])
        levelname = str(item["levelname"])

        insert_sql = """
                insert into book(book_name,book_sub_name, course_index, prepos_b, prepos_w,answers,board_size,black_first,qtypename,levelname)
                VALUES (:book_name,:book_sub_name, :course_index, :prepos_b, :prepos_w, :answers, :board_size,:black_first, :qtypename, :levelname)
                """
        self.connect.execute(insert_sql,
                             {'book_name': book_name, 'book_sub_name': book_sub_name, 'course_index': course_index,
                              'prepos_b': prepos_b, 'prepos_w': prepos_w, 'answers': answers, 'board_size': board_size,
                              'black_first': black_first, 'qtypename': qtypename, 'levelname': levelname})
        self.connect.commit()
        return item
