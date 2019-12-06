# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class WeiqiPipeline(object):
    def __init__(self):
        self.connect = sqlite3.connect('books.db')
        self.connect.execute("CREATE TABLE book_1 ("
                             "book_name TEXT,"
                             "book_sub_name TEXT,"
                             "course_index TEXT,"
                             "prepos_b TEXT,"
                             "prepos_w TEXT,"
                             "answers TEXT,"
                             "board_size TEXT,"
                             "black_first TEXT,"
                             "qtypename TEXT,"
                             "levelname TEXT,"
                             "title TEXT,"
                             "status TEXT,"
                             "signs TEXT,"
                             "sgf TEXT"
                             " ) ")

    def process_item(self, item, spider):

        book_name = item["book_name"]
        book_sub_name = item["book_sub_name"]
        course_index = item["course_index"]
        prepos_b = item["prepos_b"]
        prepos_w = item["prepos_w"]
        answers = item["answers"]
        board_size = str(item["board_size"])
        black_first = str(item["black_first"])
        qtypename = str(item["qtypename"])
        levelname = str(item["levelname"])
        title = str(item["title"])
        status = str(item["status"])
        signs = item["signs"]

        # print(item)

        sgf = self.getSgf(answers, black_first, prepos_b, prepos_w, signs, title)

        insert_sql = """
                insert into book_1(book_name,book_sub_name, course_index, prepos_b, prepos_w,answers,board_size,black_first,qtypename,levelname,title,status,sgf,signs)
                VALUES (:book_name,:book_sub_name, :course_index, :prepos_b, :prepos_w, :answers, :board_size,:black_first, :qtypename, :levelname,:title,:status,:sgf,:signs)
                """
        self.connect.execute(insert_sql,
                             {'book_name': book_name, 'book_sub_name': book_sub_name, 'course_index': course_index,
                              'prepos_b': str(prepos_b), 'prepos_w': str(prepos_w), 'answers': str(answers),
                              'board_size': board_size,
                              'black_first': black_first, 'qtypename': qtypename, 'levelname': levelname,
                              'title': title,
                              'status': status, 'sgf': sgf, 'signs': str(signs)})
        self.connect.commit()
        return item

    def getSgf(self, answers, black_first, prepos_b, prepos_w, signs, title):
        array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
        has_change = False
        for p in prepos_b:
            if array.index(p[0]) < array.__len__() / 2 < array.index(p[1]):
                has_change = True
                break
        for p in prepos_w:
            if array.index(p[0]) < array.__len__() / 2 < array.index(p[1]):
                has_change = True
                break

        sgf = "(;AB"
        for p in prepos_b:
            sgf += ("[" + (self.change(str(p)) if has_change else str(p)) + "]")
        sgf += "AW"
        for p in prepos_w:
            sgf += ("[" + (self.change(str(p)) if has_change else str(p)) + "]")
        if black_first == "1":
            sgf += "C[黑先"
        else:
            sgf += "C[白先"
        if title != "":
            sgf += ("," + str(title))
        sgf += "]"
        if signs.__len__() > 0:
            sgf += "TR"
            for sign in signs:
                sgf += ("[" + str(sign) + "]")
        if answers.__len__() > 0:
            for a in answers:
                if a["st"] == "1" or a["ty"] == "2" or a["ty"] == "3":  # 如果是待审核或者变化图的答案，则过滤掉   2019.12.6新增，失败图也不要
                    continue
                sgf += "("
                for i, v in enumerate(a["pts"]):
                    if black_first == "1":
                        if i % 2 == 0:
                            sgf += (";B[" + v["p"] + "]")
                        else:
                            sgf += (";W[" + v["p"] + "]")
                    else:
                        if i % 2 == 0:
                            sgf += (";W[" + v["p"] + "]")
                        else:
                            sgf += (";B[" + v["p"] + "]")

                    if v["c"] is not None and v["c"] != "":  # C标签非空
                        if a["pts"].__len__() == i + 1:  # 最后一步
                            if a["ty"] == "1":
                                sgf += ("C[" + v["c"] + "【正解图】]")

                            if a["ty"] == "3":
                                sgf += ("C[" + v["c"] + "【失败图】]")
                        else:
                            sgf += ("C[" + v["c"] + "]")
                    else:
                        if a["pts"].__len__() == i + 1:
                            if a["ty"] == "1":
                                sgf += "C[【正解图】]"

                            if a["ty"] == "3":
                                sgf += "C[【失败图】]"

                sgf += ")"
        sgf += ")"
        # print(sgf)
        return sgf

    def change(self, s):
        # array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
        # first_index = array.index(s[0])
        # first_index = array.__len__() - 1 - first_index
        # second_index = array.index(s[1])
        # second_index = array.__len__() - 1 - second_index
        # return str(array[second_index]) + str(array[first_index])
        return str(s[1]) + str(s[0])