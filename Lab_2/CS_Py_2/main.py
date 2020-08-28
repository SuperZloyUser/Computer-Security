# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import funcs


class Ui_form(object):

    def setupUi(self, form):

        form.setObjectName("form")
        form.resize(916, 801)

        self.centralwidget = QtWidgets.QWidget(form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_11.addWidget(self.pushButton_3, 17, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 0, 1, 1, 5)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_p = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_p.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_p.setFont(font)
        self.lineEdit_p.setAutoFillBackground(False)
        self.lineEdit_p.setText("")
        self.lineEdit_p.setReadOnly(True)
        self.lineEdit_p.setPlaceholderText("")
        self.lineEdit_p.setObjectName("lineEdit_p")
        self.gridLayout_5.addWidget(self.lineEdit_p, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_5, 1, 1, 1, 4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_s = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_s.setFont(font)
        self.lineEdit_s.setReadOnly(True)
        self.lineEdit_s.setObjectName("lineEdit_s")
        self.gridLayout_3.addWidget(self.lineEdit_s, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_3, 6, 1, 1, 4)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)
        self.lineEdit_pq_A = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pq_A.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pq_A.setFont(font)
        self.lineEdit_pq_A.setAutoFillBackground(False)
        self.lineEdit_pq_A.setText("")
        self.lineEdit_pq_A.setReadOnly(True)
        self.lineEdit_pq_A.setPlaceholderText("")
        self.lineEdit_pq_A.setObjectName("lineEdit_pq_A")
        self.gridLayout_8.addWidget(self.lineEdit_pq_A, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_8, 12, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_11.addWidget(self.pushButton, 1, 5, 3, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_11.addWidget(self.pushButton_2, 4, 5, 3, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_11.addWidget(self.line, 8, 1, 2, 5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.lineEdit_d = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_d.setFont(font)
        self.lineEdit_d.setText("")
        self.lineEdit_d.setReadOnly(True)
        self.lineEdit_d.setPlaceholderText("")
        self.lineEdit_d.setObjectName("lineEdit_d")
        self.gridLayout_4.addWidget(self.lineEdit_d, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_4, 5, 1, 1, 4)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 10, 4, 1, 2)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setObjectName("label_15")
        self.gridLayout_10.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit_pq_B = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pq_B.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pq_B.setFont(font)
        self.lineEdit_pq_B.setAutoFillBackground(False)
        self.lineEdit_pq_B.setText("")
        self.lineEdit_pq_B.setReadOnly(True)
        self.lineEdit_pq_B.setPlaceholderText("")
        self.lineEdit_pq_B.setObjectName("lineEdit_pq_B")
        self.gridLayout_10.addWidget(self.lineEdit_pq_B, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 13, 4, 1, 2)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 0, 0, 1, 1)
        self.lineEdit_e_B = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_e_B.setFont(font)
        self.lineEdit_e_B.setReadOnly(True)
        self.lineEdit_e_B.setObjectName("lineEdit_e_B")
        self.gridLayout_9.addWidget(self.lineEdit_e_B, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 11, 4, 2, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_e = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_e.setFont(font)
        self.lineEdit_e.setReadOnly(True)
        self.lineEdit_e.setObjectName("lineEdit_e")
        self.gridLayout_2.addWidget(self.lineEdit_e, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_2, 7, 1, 1, 4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_11.addWidget(self.line_3, 9, 3, 10, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_q = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_q.setFont(font)
        self.lineEdit_q.setAutoFillBackground(False)
        self.lineEdit_q.setText("")
        self.lineEdit_q.setReadOnly(True)
        self.lineEdit_q.setPlaceholderText("")
        self.lineEdit_q.setObjectName("lineEdit_q")
        self.gridLayout_6.addWidget(self.lineEdit_q, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_6, 2, 1, 1, 4)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_11.addWidget(self.label_14, 13, 1, 1, 2)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_s_A = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_s_A.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_s_A.setFont(font)
        self.lineEdit_s_A.setAutoFillBackground(False)
        self.lineEdit_s_A.setText("")
        self.lineEdit_s_A.setReadOnly(True)
        self.lineEdit_s_A.setPlaceholderText("")
        self.lineEdit_s_A.setObjectName("lineEdit_s_A")
        self.gridLayout_7.addWidget(self.lineEdit_s_A, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 11, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 7, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_11.addWidget(self.label_11, 10, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_11.addWidget(self.label_16, 14, 4, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_pq = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pq.setFont(font)
        self.lineEdit_pq.setAutoFillBackground(False)
        self.lineEdit_pq.setText("")
        self.lineEdit_pq.setReadOnly(True)
        self.lineEdit_pq.setPlaceholderText("")
        self.lineEdit_pq.setObjectName("lineEdit_pq")
        self.gridLayout.addWidget(self.lineEdit_pq, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout, 3, 1, 2, 4)
        self.textForRSA = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textForRSA.setFont(font)
        self.textForRSA.setObjectName("textForRSA")
        self.gridLayout_11.addWidget(self.textForRSA, 14, 1, 2, 2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_11.addWidget(self.textEdit, 18, 1, 1, 2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_11.addWidget(self.textEdit_2, 15, 4, 4, 2)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_11.addWidget(self.label_17, 16, 1, 2, 1)
        form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(form)
        self.statusbar.setObjectName("statusbar")
        form.setStatusBar(self.statusbar)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

        self.pushButton.clicked.connect(lambda: funcs.pqse_gen(self))

    __open_number_s = 0
    __secret_number_e = 0

    @property
    def open_number_s(self):
        return self.__open_number_s

    @open_number_s.setter
    def open_number_s(self, value):
        self.__open_number_s = value

    @property
    def open_number_e(self):
        return self.__open_number_e

    @open_number_e.setter
    def open_number_e(self, value):
        self.__open_number_e = value

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "MainWindow"))
        self.pushButton_3.setText(_translate("form", "Зашифровать и отправить пользотелю Б"))
        self.label.setText(_translate("form", "ЛР_№2. Алгоритм RSA. Вариант 7; N = 28"))
        self.label_2.setText(_translate("form", "1)P:"))
        self.label_5.setText(_translate("form", "3)s(public):"))
        self.label_10.setText(_translate("form", "P*Q(public):"))
        self.pushButton.setText(_translate("form", "Сгенерировать P и Q\n"
                                                   "Вычислить s и e"))
        self.pushButton_2.setText(_translate("form", "Сохранить e(private) и\n"
                                                     "отправить (d, P*Q)(public)"))
        self.label_9.setText(_translate("form", "2)d = (P-1)*(Q-1):"))
        self.label_12.setText(_translate("form", "Владелец(Пользователь Б)"))
        self.label_15.setText(_translate("form", "P*Q(public):"))
        self.label_13.setText(_translate("form", "e (private):"))
        self.label_4.setText(_translate("form", "4)e (private):"))
        self.label_3.setText(_translate("form", "1)Q:"))
        self.label_14.setText(_translate("form", "Текст для шифрования и передачи:"))
        self.label_6.setText(_translate("form", "s(public):"))
        self.label_7.setText(_translate("form", "(вывод для наглядности)"))
        self.label_11.setText(_translate("form", "Получатель(Пользователь А)"))
        self.label_16.setText(_translate("form", "Расшифрованный текст:"))
        self.label_8.setText(_translate("form", "2)P*Q:"))
        self.label_17.setText(_translate("form", "Шифротекст:"))


class MyWidget(QMainWindow, Ui_form):
    def __init__(self):
        super(MyWidget, self).__init__()

        self.setupUi(self)
        self.setWindowTitle('FirstWindow')

        self.pushButton_2.clicked.connect(self.show_window_2)
        self.pushButton_3.clicked.connect(self.show_window_3)

    def show_window_2(self):
        if MyWidget.check_const_flag(self):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Сначала необходимо сгенерировать P и Q!")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            funcs.prepare_encryption(self)

    def show_window_3(self):
        if MyWidget.check_const_flag_2(self) or self.textForRSA.toPlainText() == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            if MyWidget.check_const_flag(self):
                msg.setText("Сначала необходимо сгенерировать P и Q!")
            else:
                msg.setText("Сначала необходимо отправить данные!")
            if self.textForRSA.toPlainText() == "":
                msg.setText("Сначала необходимо ввести текст!")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            funcs.encryption_decryption(self)

    def check_const_flag(self):
        if self.const_flag == 0:
            return 1
        else:
            return 0

    def check_const_flag_2(self):
        if self.const_flag_2 == 0:
            return 1
        else:
            return 0

    __const_flag = 0
    __const_flag_2 = 0

    @property
    def const_flag(self):
        return self.__const_flag

    @const_flag.setter
    def const_flag(self, value):
        self.__const_flag = value

    @property
    def const_flag_2(self):
        return self.__const_flag_2

    @const_flag_2.setter
    def const_flag_2(self, value):
        self.__const_flag_2 = value


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
