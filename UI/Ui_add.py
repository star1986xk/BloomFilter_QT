# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_add.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 266)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(0, 200))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_path = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_path.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_path.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_path.setObjectName("pushButton_path")
        self.horizontalLayout_2.addWidget(self.pushButton_path)
        self.lineEdit_path = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout_2.addWidget(self.lineEdit_path)
        self.pushButton_many = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_many.setObjectName("pushButton_many")
        self.horizontalLayout_2.addWidget(self.pushButton_many)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_data = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_data.setObjectName("lineEdit_data")
        self.horizontalLayout_3.addWidget(self.lineEdit_data)
        self.pushButton_one = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_one.setObjectName("pushButton_one")
        self.horizontalLayout_3.addWidget(self.pushButton_one)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_old_number = QtWidgets.QLabel(self.widget_5)
        self.label_old_number.setObjectName("label_old_number")
        self.horizontalLayout_4.addWidget(self.label_old_number)
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_old_count = QtWidgets.QLabel(self.widget_5)
        self.label_old_count.setObjectName("label_old_count")
        self.horizontalLayout_4.addWidget(self.label_old_count)
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_old_ratio = QtWidgets.QLabel(self.widget_5)
        self.label_old_ratio.setObjectName("label_old_ratio")
        self.horizontalLayout_4.addWidget(self.label_old_ratio)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_new_number = QtWidgets.QLabel(self.widget_2)
        self.label_new_number.setObjectName("label_new_number")
        self.horizontalLayout.addWidget(self.label_new_number)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_new_count = QtWidgets.QLabel(self.widget_2)
        self.label_new_count.setObjectName("label_new_count")
        self.horizontalLayout.addWidget(self.label_new_count)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_new_ratio = QtWidgets.QLabel(self.widget_2)
        self.label_new_ratio.setObjectName("label_new_ratio")
        self.horizontalLayout.addWidget(self.label_new_ratio)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "插入"))
        self.pushButton_path.setText(_translate("Dialog", "路径"))
        self.pushButton_many.setText(_translate("Dialog", "插入多条"))
        self.label.setText(_translate("Dialog", "数据"))
        self.pushButton_one.setText(_translate("Dialog", "插入一条"))
        self.label_2.setText(_translate("Dialog", "原布隆溢出条数"))
        self.label_old_number.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "原布隆溢出次数"))
        self.label_old_count.setText(_translate("Dialog", "0"))
        self.label_4.setText(_translate("Dialog", "溢出率"))
        self.label_old_ratio.setText(_translate("Dialog", "0"))
        self.label_6.setText(_translate("Dialog", "新布隆溢出条数"))
        self.label_new_number.setText(_translate("Dialog", "0"))
        self.label_7.setText(_translate("Dialog", "新布隆溢出次数"))
        self.label_new_count.setText(_translate("Dialog", "0"))
        self.label_5.setText(_translate("Dialog", "溢出率"))
        self.label_new_ratio.setText(_translate("Dialog", "0"))
