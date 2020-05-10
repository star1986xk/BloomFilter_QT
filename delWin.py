# -*-coding: UTF-8 -*-
from PyQt5.QtWidgets import QDialog,QFileDialog,QMessageBox
from UI.Ui_del import Ui_Dialog
from PyQt5.QtCore import Qt, pyqtSignal


class delWin(QDialog, Ui_Dialog):
    Sig_update = pyqtSignal(list)
    def __init__(self, parent=None):
        super(delWin, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.pushButton_path.clicked.connect(self.pathBtn)
        self.pushButton_many.clicked.connect(self.manyBtn)
        self.pushButton_one.clicked.connect(self.oneBtn)

    def pathBtn(self):
        filename, _ = QFileDialog.getOpenFileName(self, '打开文件', './', '文本文件 (*.txt)')
        if filename:
            self.lineEdit_path.setText(filename)

    def manyBtn(self):
        path = self.lineEdit_path.text().strip()
        if path:
            with open(path,'r') as f:
                txt = f.read()
            txtList = txt.split('\n')
            self.Sig_update.emit(txtList)

    def oneBtn(self):
        data = self.lineEdit_data.text().strip()
        if data:
            self.Sig_update.emit([data])

    def mesgTrue(self):
        QMessageBox.about(self,'提示','成功')

    def mesgFalse(self):
        QMessageBox.about(self,'提示','失败')