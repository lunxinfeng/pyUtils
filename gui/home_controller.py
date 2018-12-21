from PyQt5.QtWidgets import *
from gui.home import Ui_MainWindow
from gui.helper.DBHelper import DBHelper
import pandas as pd


class Home_Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Home_Window, self).__init__(parent)
        self.setupUi(self)

        self.db_helper = DBHelper()
        self.initEvent()

    def initEvent(self):
        self.btnCreateDB.clicked.connect(self.db_helper.init_data)
        self.btnQueryData.clicked.connect(self.query_data)
        self.btnAddData.clicked.connect(self.db_helper.add_data)
        self.btnDelData.clicked.connect(self.del_data)
        self.btnReadExcel.clicked.connect(self.read_excel)

    def query_data(self):
        model = self.db_helper.query_data()
        self.tableView.setModel(model)

    def del_data(self):
        self.db_helper.del_data(self.tableView.currentIndex().row())

    def read_excel(self):
        # file_url = QFileDialog.getOpenFileUrl(self, "读取Excel", "", "Excel files(*.xlsx , *.xls)")
        # print(file_url[0])
        # All Files (*);;Text Files (*.txt)
        # , options=QFileDialog.DontUseNativeDialog
        file_name, file_type = QFileDialog.getOpenFileName(self, "读取Excel", "", "Excel files(*.xlsx , *.xls)")
        print(file_name)
        df = pd.read_excel(file_name)
        print("全部数据：\n")
        print(df)
        print("-----------")
        print("行数 * 列数：\n")
        print(df.shape)
        print("-----------")
        print("标题：\n")
        print(df.columns.values.tolist())
        print("-----------")
        print("数据数量：\n")  # 一行为一条,标题不算
        print(len(df))
        print("-----------")
        print("前两行：\n")
        print(df.head(2))
        print("-----------")
        print("后两行：\n")
        print(df.tail(2))
        print("-----------")
        print("自定义标题，后两行：\n")
        df.columns = ["title_1", "title_2", "title_3", "title_4"]
        print(df.tail(2))
        print("-----------")
        # 过滤
        print("获取某列：\n")
        # print(df["title_1"])
        print(df.title_1)
        print(df.pop("title_2"))
        print(df)
        print(df.title_1 < 3)
        print(df[df.title_1 < 3])
        print(df[(df.title_1 < 3) & (df.title_2 < 20)])  # 不能使用and、or，必须用 &、| 和圆括号。
        print(df[(df.title_1 < 3) | (df.title_2 > 40)])
        print(df[df.title_4.str.startswith("2")])  # 如果你的数据中字符串，你也可以使用字符串方法来进行过滤  .str.[string method]
        print(df[df.title_4.str.endswith("a")])
        # print(df[df.title_4.str.__contains__("2")])  # 如果你的数据中字符串，你也可以使用字符串方法来进行过滤  .str.[string method]
        print("-----------")
        # 索引
        print(df.iloc[3])  # 返回第四行数据，只能是数字，索引从0开始
        df = df.set_index(["title_4"])
        print(df.loc["3a"])  # 返回列title_4的值为3a的那一行数据
        print(df.ix["2a"])
        print(df)
        df = df.reset_index(["title_4"])  # 将索引恢复成数据形式
        print(df)
        df.sort_index(ascending=False, inplace=True)  # ascending：True为升序，False为降序  inplace：是否替换原数据，默认False
        print(df)
        print("-----------")
        # 操作
        print("操作")
        result_2 = df.drop(labels=["title_1"], axis=1, inplace=False)
        print(result_2)
        result_2 = df.drop(labels=df.columns[[0, 1]], axis=1, inplace=False)
        print(result_2)
        result_2 = df.drop(labels=[0, 1], axis=0, inplace=False)
        print(result_2)
        # 当想让方程作用在一维的向量上时，可以使用apply来完成
        df["title_5"] = df.title_4.apply(self.apply_data)  # 作用于某一列，Series数据
        result_2 = df.apply(self.apply_data_2)  # 作用于DataFrame 数据
        print(df)
        print(result_2)
        # 如果想让方程作用于DataFrame中的每一个元素，可以使用applymap()
        df = df.applymap(self.applymap_data)
        print(df)
        # map()只能是将函数作用于一个Series的每一个元素
        result_2 = df.title_1.map(self.apply_data)
        print(result_2)
        # 总的来说就是apply()是一种让函数作用于列或者行操作，applymap()是一种让函数作用于DataFrame每一个元素的操作，而map是一种让函数作用于Series每一个元素的操作
        print("-----------")
        df["title_6"] = ["1", "0", "1", "0", "1"]
        print(df)
        # print(df.pivot("title_6", "title_5")[["title_1", "title_2"]].fillna(""))
        # print(df.groupby(df.title_6).max())  # 获取每个分组里面最大的数据
        # print(df.groupby(df.title_6).max()["title_1"])
        # df = df.groupby([df.title_6, df.title_5]).max()
        # print(df)
        # print(df.groupby(df.title_6).min())
        # print(df.groupby(df.title_6).mean())
        # print(df.unstack(0).fillna("empty"))
        # print(df.unstack(1))
        print(df.pivot(index="title_6", columns="title_5", values=["title_1", "title_2"]).fillna(""))
        print("-----------")
        # df.to_excel("data_new.xlsx")
        print("-----------")
        # rain_jpn = pd.read_csv('jpn_rain.csv')
        # rain_jpn.columns = ['year', 'jpn_rainfall']
        #
        # uk_jpn_rain = df.merge(rain_jpn, on='year')
        # uk_jpn_rain.head(5)
        print("-----------")
        # print(df.plot(x="title_1", y=["title_2", "title_5"]))
        print("-----------")
        pd.options.display.float_format = '{:,.3f}'.format  # Limit output to 3 decimal places.
        df.describe()

    def apply_data(self, data):
        result = data[:1]
        return result + "b"

    def apply_data_2(self, data):
        return data[1]

    def applymap_data(self, data):
        return str(data) + "c"

    def open(self):
        self.show()
