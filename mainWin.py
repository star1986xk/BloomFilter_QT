# -*-coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QFrame, QTableWidgetItem,QHeaderView
from UI.Ui_main import Ui_Form
from addWin import addWin
from delWin import delWin
from queryWin import queryWin
import sys
import hashlib
import collections

class MainWindow(QFrame, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        headerView = self.tableWidget_1.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)

        self.pushButton_addWin.clicked.connect(self.addBtn)
        self.pushButton_delWin.clicked.connect(self.delBtn)
        self.pushButton_queryWin.clicked.connect(self.queryBtn)

        # 以下均为全局变量

        # 数组每位按8位测试，即每位存储上限为255
        self.counter_size = 8
        # 数组长度为5000
        self.length = 5000
        # 初始化数组

        # overflow_time是总的溢出次数
        # overflow_number是发生了溢出的数据的条数
        # opr是溢出的占总数据条数的百分比
        # 插入时如果发生溢出，仍可正常插入，但是相应的counter不会再增加，若是插入文件则显示上面三个参数，若是插入一条数据则提示发生溢出即可
        # 执行query时在和不在集合中的数据分别存储到两个文件夹中，在读文件展示的时候同时读出数量，计算各自占总数据数量的百分比
        # 删除时如果检测出不是集合中的元素，则不执行删除操作

        # ivi-cbf
        self.b = [0] * self.length
        self.temp1 = 0
        self.overflow1_time = 0
        self.overflow1_number = 0
        self.opr1 = 0
        self.D_l = [3, 5, 7]
        # 表示D_l三个数字
        self.l = 3

        # vi-cbf
        self.a = [0] * self.length
        self.temp2 = 0
        self.overflow2_time = 0
        self.overflow2_number = 0
        self.opr2 = 0
        self.D_L = [4, 5, 6, 7]
        # 表示D_L四个数字
        self.L = 4

        self.datas1 = []

        self.loadA()
        self.loadB()

    def addBtn(self):
        self.addWin = addWin()
        self.addWin.Sig_update.connect(self.addData)
        self.addWin.show()

    def delBtn(self):
        self.delWin = delWin()
        self.delWin.Sig_update.connect(self.delData)
        self.delWin.show()

    def queryBtn(self):
        self.queryWin = queryWin()
        self.queryWin.Sig_update.connect(self.queryData)
        self.queryWin.show()

    def addData(self, datas):
        if datas:
            self.datas1 += datas
            self.load0()
            self.insert1_many(datas)
            self.insert2_many(datas)
            self.loadA()
            self.loadB()
            self.addWin.label_old_number.setText(str(self.overflow2_number))
            self.addWin.label_new_number.setText(str(self.overflow1_number))
            self.addWin.label_old_count.setText(str(self.overflow2_time))
            self.addWin.label_new_count.setText(str(self.overflow1_time))
            self.addWin.label_old_ratio.setText(str(self.opr2))
            self.addWin.label_new_ratio.setText(str(self.opr1))
            if len(datas) == 1:
                if self.overflow1_number:
                    self.addWin.mesgFalse()
                else:
                    self.addWin.mesgTrue()

    def queryData(self,datas):
        f1,f2 = self.query2_txt(datas)
        f3,f4 = self.query1_txt(datas)
        self.queryWin.tableWidget.setRowCount(0)
        for n, d in enumerate(f1):
            self.queryWin.tableWidget.setRowCount(n + 1)
            self.queryWin.tableWidget.setItem(n, 0, QTableWidgetItem(str(d)))
        self.queryWin.tableWidget_2.setRowCount(0)
        for n, d in enumerate(f2):
            self.queryWin.tableWidget_2.setRowCount(n + 1)
            self.queryWin.tableWidget_2.setItem(n, 0, QTableWidgetItem(str(d)))
        self.queryWin.label_true.setText(str(len(f1)))
        self.queryWin.label_false.setText(str(len(f2)))
        self.queryWin.label_true_bi.setText(str(len(f1)/len(datas)*100)+'%')
        self.queryWin.label_false_bi.setText(str(len(f2)/len(datas)*100)+'%')

        self.queryWin.tableWidget_3.setRowCount(0)
        for n, d in enumerate(f3):
            self.queryWin.tableWidget_3.setRowCount(n + 1)
            self.queryWin.tableWidget_3.setItem(n, 0, QTableWidgetItem(str(d)))
        self.queryWin.tableWidget_4.setRowCount(0)
        for n, d in enumerate(f4):
            self.queryWin.tableWidget_4.setRowCount(n + 1)
            self.queryWin.tableWidget_4.setItem(n, 0, QTableWidgetItem(str(d)))
        self.queryWin.label_true_2.setText(str(len(f3)))
        self.queryWin.label_false_2.setText(str(len(f4)))
        self.queryWin.label_true_bi_2.setText(str(len(f3)/len(datas)*100)+'%')
        self.queryWin.label_false_bi_2.setText(str(len(f4)/len(datas)*100)+'%')

    def delData(self,datas):
        f1,f2 = self.delete2_txt(datas)
        f3,f4 = self.delete1_txt(datas)
        self.delWin.tableWidget.setRowCount(0)
        for n, d in enumerate(f1):
            self.delWin.tableWidget.setRowCount(n + 1)
            self.delWin.tableWidget.setItem(n, 0, QTableWidgetItem(str(d)))
        self.delWin.tableWidget_2.setRowCount(0)
        for n, d in enumerate(f2):
            self.delWin.tableWidget_2.setRowCount(n + 1)
            self.delWin.tableWidget_2.setItem(n, 0, QTableWidgetItem(str(d)))
        self.delWin.label_true_count.setText(str(len(f1)))
        self.delWin.label_false_count.setText(str(len(f2)))
        self.delWin.tableWidget_3.setRowCount(0)
        for n, d in enumerate(f3):
            self.delWin.tableWidget_3.setRowCount(n + 1)
            self.delWin.tableWidget_3.setItem(n, 0, QTableWidgetItem(str(d)))
        self.delWin.tableWidget_4.setRowCount(0)
        for n, d in enumerate(f4):
            self.delWin.tableWidget_4.setRowCount(n + 1)
            self.delWin.tableWidget_4.setItem(n, 0, QTableWidgetItem(str(d)))
        self.delWin.label_true_count_2.setText(str(len(f3)))
        self.delWin.label_false_count_2.setText(str(len(f4)))
        obj = collections.Counter(self.datas1)
        for d in datas:
            obj[d] -=1
        self.datas1 = list(obj.elements())
        self.load0()
        self.loadA()
        self.loadB()
        if len(datas) ==1:
            if f1:
                self.delWin.mesgTrue()
            else:
                self.delWin.mesgFalse()

    def load0(self):
        obj = collections.Counter(self.datas1)
        self.tableWidget_1.setRowCount(0)
        for n, (k,v) in enumerate(obj.items()):
            self.tableWidget_1.setRowCount(n + 1)
            self.tableWidget_1.setItem(n, 0, QTableWidgetItem(str(k)))
            self.tableWidget_1.setItem(n, 1, QTableWidgetItem(str(v)))
        self.label_1_count.setText(str(len(self.datas1)))
        self.label_1_bit.setText(str(sys.getsizeof(self.datas1)))

    def loadA(self):
        self.tableWidget_2.setRowCount(0)
        for n, d in enumerate(self.a):
            self.tableWidget_2.setRowCount(n + 1)
            self.tableWidget_2.setItem(n, 0, QTableWidgetItem(str(d)))
        self.label_2_count.setText(str(len(self.a)))
        self.label_2_bit.setText(str(sys.getsizeof(self.a)))

    def loadB(self):
        self.tableWidget_3.setRowCount(0)
        for n, d in enumerate(self.b):
            self.tableWidget_3.setRowCount(n + 1)
            self.tableWidget_3.setItem(n, 0, QTableWidgetItem(str(d)))
        self.label_3_count.setText(str(len(self.b)))
        self.label_3_bit.setText(str(sys.getsizeof(self.b)))


    def count_line(self,datas):
        t = 0
        for line in datas:
            t = t + 1
        return t

    def md5(self,str):
        m = hashlib.md5()
        b = str.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        return str_md5

    # 以下为IVI-CBF
    def query1(self,c, m, l):
        if c == 0:
            return 0
        elif c >= l and c <= (2 * l + 1):
            if (c % 2) == 1 and m != c:
                return 0
            elif c == 2 * l and m != l:
                return 0
        elif c >= (2 * l + 2) and c <= (3 * l - 1):
            if m < l or m > (c - l):
                return 0
        elif c >= 3 * l and c <= (4 * l - 1):
            if (c % 2) == 1:
                if m < l or m > (c - 2 * l):
                    return 0
            elif (c % 2) == 0:
                if m < (c - 2 * l - 1) or m > (2 * l + 1):
                    return 0
        elif c >= (4 * l + 4) and c <= (5 * l - 1):
            if (c % 2) == 0:
                if m < l or m > (c - 3 * l):
                    return 0
        else:
            return 1

    def query1_txt(self,datas):
        # 在集合中的数据
        f1 = []
        # 不在集合中的数据
        f2 = []
        for line in datas:
            temp = 1
            t_1 = line + 'aa'
            md5_t1 = self.md5(t_1)
            t1 = int(md5_t1, 16) % self.length
            p_1 = line + 'aaa'
            md5_p1 = self.md5(p_1)
            p1 = int(md5_p1, 16) % self.l
            if self.query1(self.b[t1], self.D_l[p1], self.l) == 0:
                temp = 0

            t_2 = line + 'bb'
            md5_t2 = self.md5(t_2)
            t2 = int(md5_t2, 16) % self.length
            p_2 = line + 'bbb'
            md5_p2 = self.md5(p_2)
            p2 = int(md5_p2, 16) % self.l
            if self.query1(self.b[t2], self.D_l[p2], self.l) == 0:
                temp = 0

            t_3 = line + 'cc'
            md5_t3 = self.md5(t_3)
            t3 = int(md5_t3, 16) % self.length
            p_3 = line + 'ccc'
            md5_p3 = self.md5(p_3)
            p3 = int(md5_p3, 16) % self.l
            if self.query1(self.b[t3], self.D_l[p3], self.l) == 0:
                temp = 0

            if temp == 1:
                f1.append(line)
            else:
                f2.append(line)
        return f1,f2

    # 返回值为0表示不属于，为1表示属于
    def query1_one(self,str):
        temp = 1

        t_1 = str + 'aa'
        md5_t1 = self.md5(t_1)
        t1 = int(md5_t1, 16) % self.length
        p_1 = str + 'aaa'
        md5_p1 = self.md5(p_1)
        p1 = int(md5_p1, 16) % self.l
        if self.query1(self.b[t1], self.D_l[p1], self.l) == 0:
            temp = 0

        t_2 = str + 'bb'
        md5_t2 = self.md5(t_2)
        t2 = int(md5_t2, 16) % self.length
        p_2 = str + 'bbb'
        md5_p2 = self.md5(p_2)
        p2 = int(md5_p2, 16) % self.l
        if self.query1(self.b[t2], self.D_l[p2], self.l) == 0:
            temp = 0

        t_3 = str + 'cc'
        md5_t3 = self.md5(t_3)
        t3 = int(md5_t3, 16) % self.length
        p_3 = str + 'ccc'
        md5_p3 =self.md5(p_3)
        p3 = int(md5_p3, 16) % self.l
        if self.query1(self.b[t3], self.D_l[p3], self.l) == 0:
            temp = 0

        return temp

    def insert1(self,line, str1, str2):
        t = line + str1
        md5_t = self.md5(t)
        t = int(md5_t, 16) % self.length
        p = line + str2
        md5_p = self.md5(p)
        p = int(md5_p, 16) % self.l
        if self.b[t] <= pow(2, self.counter_size) - 1 - self.D_l[p]:
            self.b[t] = self.b[t] + self.D_l[p]
        else:
            self.b[t] = pow(2, self.counter_size) - 1
            self.overflow1_time += 1
            self.temp1 = 1

    def insert1_many(self,datas):
        self.opr1 = 0
        self.overflow1_time = 0
        self.overflow1_number = 0
        for line in datas:
            self.temp1 = 0
            self.insert1(line, 'aa', 'aaa')
            self.insert1(line, 'bb', 'bbb')
            self.insert1(line, 'cc', 'ccc')
            if self.temp1 == 1:
                self.overflow1_number += 1
        data_line = len(datas)
        self.opr1 = self.overflow1_number / data_line


    # 返回0表示插入时发生溢出
    def insert1_one(self,str):
        self.temp1 = 0
        self.insert1(str, 'aa', 'aaa')
        self.insert1(str, 'bb', 'bbb')
        self.insert1(str, 'cc', 'ccc')
        if self.temp1 == 1:
            return 0
        else:
            return 1

    def delete1(self,line, str1, str2):
        t = line + str1
        md5_t = self.md5(t)
        t = int(md5_t, 16) % self.length
        p = line + str2
        md5_p = self.md5(p)
        p = int(md5_p, 16) % self.l
        self.b[t] = self.b[t] - self.D_l[p]

    def delete1_txt(self,datas):
        # 删除操作中不在集合中的数据
        f1 = []
        f2 = []
        for line in datas:
            if self.query1_one(line) == 1:
                self.delete1(line, 'aa', 'aaa')
                self.delete1(line, 'bb', 'bbb')
                self.delete1(line, 'cc', 'ccc')
                f1.append(line)
            else:
                f2.append(line)
        return f1,f2

    # 返回1表示成功，0表示想要删除的文件不在集合中，因此删除失败
    def delete1_one(self,str):
        if self.query1_one(str) == 1:
            self.delete1(str, 'aa', 'aaa')
            self.delete1(str, 'bb', 'bbb')
            self.delete1(str, 'cc', 'ccc')
            return 1
        else:
            return 0

    def query2(self,c, m, L):
        t = c - m
        if t <= -1:
            return 0
        elif t >= 1 and t <= L - 1:
            return 0
        else:
            return 1

    def query2_txt(self,datas):
        # 在集合中的数据
        f1 = []
        # 不在集合中的数据
        f2 = []
        for line in datas:
            temp = 1

            t_1 = line + 'aa'
            md5_t1 = self.md5(t_1)
            t1 = int(md5_t1, 16) % self.length
            p_1 = line + 'aaa'
            md5_p1 = self.md5(p_1)
            p1 = int(md5_p1, 16) % self.L
            if self.query2(self.a[t1], self.D_L[p1], self.L) == 0:
                temp = 0

            t_2 = line + 'bb'
            md5_t2 = self.md5(t_2)
            t2 = int(md5_t2, 16) % self.length
            p_2 = line + 'bbb'
            md5_p2 = self.md5(p_2)
            p2 = int(md5_p2, 16) % self.L
            if self.query2(self.a[t2], self.D_L[p2], self.L) == 0:
                temp = 0

            t_3 = line + 'cc'
            md5_t3 = self.md5(t_3)
            t3 = int(md5_t3, 16) % self.length
            p_3 = line + 'ccc'
            md5_p3 = self.md5(p_3)
            p3 = int(md5_p3, 16) % self.L
            if self.query2(self.a[t3], self.D_L[p3], self.L) == 0:
                temp = 0

            if temp == 1:
                f1.append(line)
            else:
                f2.append(line)
        return f1,f2

    def query2_one(self,str):
        temp = 1

        t_1 = str + 'aa'
        md5_t1 = self.md5(t_1)
        t1 = int(md5_t1, 16) % self.length
        p_1 = str + 'aaa'
        md5_p1 = self.md5(p_1)
        p1 = int(md5_p1, 16) % self.L
        if self.query2(self.a[t1], self.D_L[p1], self.L) == 0:
            temp = 0

        t_2 = str + 'bb'
        md5_t2 = self.md5(t_2)
        t2 = int(md5_t2, 16) % self.length
        p_2 = str + 'bbb'
        md5_p2 = self.md5(p_2)
        p2 = int(md5_p2, 16) % self.L
        if self.query2(self.a[t2], self.D_L[p2], self.L) == 0:
            temp = 0

        t_3 = str + 'cc'
        md5_t3 = self.md5(t_3)
        t3 = int(md5_t3, 16) % self.length
        p_3 = str + 'ccc'
        md5_p3 = self.md5(p_3)
        p3 = int(md5_p3, 16) % self.L
        if self.query2(self.a[t3], self.D_L[p3], self.L) == 0:
            temp = 0

        return temp

    def insert2(self,line, str1, str2):
        t = line + str1
        md5_t = self.md5(t)
        t = int(md5_t, 16) % self.length
        p = line + str2
        md5_p = self.md5(p)
        p = int(md5_p, 16) % self.L
        if self.a[t] <= pow(2, self.counter_size) - 1 - self.D_L[p]:
            self.a[t] = self.a[t] + self.D_L[p]
        else:
            self.a[t] = pow(2, self.counter_size) - 1
            self.overflow2_time += 1
            self.temp2 = 1

    def insert2_many(self,datas):
        self.opr2 = 0
        self.overflow2_time = 0
        self.overflow2_number = 0

        for line in datas:
            self.temp2 = 0
            self.insert2(line, 'aa', 'aaa')
            self.insert2(line, 'bb', 'bbb')
            self.insert2(line, 'cc', 'ccc')
            if self.temp2 == 1:
                self.overflow2_number += 1
        data_line = len(datas)
        self.opr2 = self.overflow2_number / data_line


    def insert2_one(self,str):
        self.temp2 = 0
        self.insert2(str, 'aa', 'aaa')
        self.insert2(str, 'bb', 'bbb')
        self.insert2(str, 'cc', 'ccc')
        if self.temp2 == 1:
            return 0
        else:
            return 1

    def delete2(self,line, str1, str2):
        t = line + str1
        md5_t = self.md5(t)
        t = int(md5_t, 16) % self.length
        p = line + str2
        md5_p = self.md5(p)
        p = int(md5_p, 16) % self.L
        self.a[t] = self.a[t] - self.D_L[p]

    def delete2_txt(self,datas):
        # 删除操作中不在集合中的数据
        f1 = []
        f2 = []
        for line in datas:
            if self.query2_one(line) == 1:
                self.delete2(line, 'aa', 'aaa')
                self.delete2(line, 'bb', 'bbb')
                self.delete2(line, 'cc', 'ccc')
                f1.append(line)
            else:
                f2.append(line)
        return f1,f2

    # 返回1表示成功，0表示想要删除的文件不在集合中，因此不能删除
    def delete2_one(self,str):
        if self.query2_one(str) == 1:
            self.delete2(str, 'aa', 'aaa')
            self.delete2(str, 'bb', 'bbb')
            self.delete2(str, 'cc', 'ccc')
            return 1
        else:
            return 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
