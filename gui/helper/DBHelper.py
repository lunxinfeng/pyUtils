from PyQt5.QtSql import *
from PyQt5.QtCore import Qt
import threading


class DBHelper:
    _instance_lock = threading.Lock()

    def __init__(self):
        self.__create_data_base_sqlite()
        self.model = QSqlTableModel()

    def __new__(cls, *args, **kwargs):
        if not hasattr(DBHelper, "_instance"):
            with DBHelper._instance_lock:
                if not hasattr(DBHelper, "_instance"):
                    DBHelper._instance = object.__new__(cls)
        return DBHelper._instance

    def __create_data_base_sqlite(self):
        print("create_data_base_sqlite")
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        # db.setHostName("host_lxf")
        # db.setDatabaseName("db_lxf.db")
        # db.setUserName("lxf")
        # db.setPassword("lxf123")

        self.db.setDatabaseName("db_lxf.sqlite")
        self.db.open()

    def init_data(self):
        print("init_data")
        self.check_open()
        query = QSqlQuery()
        query.exec_("create table info(ID INT PRIMARY KEY, name VARCHAR(20), sex VARCHAR(5), age INT)")
        query.exec_("INSERT INTO info VALUES(1, '伦新锋', '男', 66)")
        query.exec_("INSERT INTO info VALUES(2, '余锐', '男', 88)")

    def query_data(self):
        print("query_data")
        self.check_open()
        self.model.setTable("info")
        # 允许修改字段
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Sex")
        self.model.setHeaderData(3, Qt.Horizontal, "Age")
        self.model.select()
        return self.model

    def add_data(self):
        print("add_data")
        self.check_open()
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)

    def del_data(self, index):
        print("del_data")
        self.check_open()
        if self.model:
            self.model.removeRow(index)

    def check_open(self):
        if self.db.isOpen():
            print("isOpen true")
        else:
            print("isOpen false")
            self.db.open()
