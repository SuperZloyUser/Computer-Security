# coding=utf8

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
import sys
from funcs import encoder


class MainForm(QMainWindow):
    pushButtonCalcKeyLength: QtWidgets.QPushButton
    pushButtonEnterText: QtWidgets.QPushButton
    pushButtonEncode: QtWidgets.QPushButton
    textEdit: QtWidgets.QTextEdit
    keyLengthLine: QtWidgets.QLineEdit
    keyLine: QtWidgets.QLineEdit
    keyIndexLine: QtWidgets.QLineEdit
    textIndexLine: QtWidgets.QLineEdit
    encodedText: QtWidgets.QTextEdit
    pushButtonCalcKey: QtWidgets.QPushButton
    mostCountedLine: QtWidgets.QLineEdit

    def __init__(self):
        super(MainForm, self).__init__()
        self.ui = uic.loadUi('form.ui', self)
        self.temp_enc = encoder()
        self.enterTextFromFile()
        self.pushButtonCalcKeyLength.clicked.connect(self.update_key_length)
        self.pushButtonEnterText.clicked.connect(self.enterTextFromFile)
        self.keyLine.textChanged.connect(self.check_key)
        self.keyLine.textChanged.connect(self.on_key_update)
        self.mostCountedLine.textChanged.connect(self.check_most_counted)
        self.pushButtonEncode.clicked.connect(self.do_text_encode)
        self.pushButtonCalcKey.clicked.connect(self.calculate_key)

    def update_key_length(self):
        self.temp_enc.text = self.temp_enc.text_translator(self.textEdit.toPlainText())
        self.temp_enc.main_func()
        self.mostCountedLine.setText(''.join('О' for _ in range(0, self.temp_enc.key_length)))
        self.keyLengthLine.setText(str(self.temp_enc.key_length))
        self.keyIndexLine.setText((lambda x: self.temp_enc.conformity_key_index[0] if (x > 7) else str(
            self.temp_enc.conformity_key_index[x]))(self.temp_enc.key_length))
        self.textIndexLine.setText(str('%.7f' % self.temp_enc.text_index))

    def calculate_key(self):
        self.temp_enc.encode_key(self.mostCountedLine.text())
        self.keyLine.setText(self.temp_enc.key)

    def on_key_update(self):
        self.temp_enc.key = self.keyLine.text()

    def enterTextFromFile(self):
        file = open('text.txt', 'r')
        text = file.read()
        file.close()
        self.textEdit.setText(text)
        self.temp_enc.text = self.temp_enc.text_translator(text)

    def check_key(self):
        key = self.keyLine.text()

        if len(key) > self.temp_enc.key_length:
            self.keyLine.setText(self.keyLine.text()[0:7])
            return
        for i in key:
            if i not in self.temp_enc.alphabet:
                key = key.replace(i, '')
        if len(key) != self.temp_enc.key_length:
            self.keyLine.setText(key)

    def check_most_counted(self):
        text = self.mostCountedLine.text()

        if len(text) > self.temp_enc.key_length:
            self.mostCountedLine.setText(self.mostCountedLine.text()[0:7])
            return
        for i in text:
            if i not in self.temp_enc.alphabet:
                text = text.replace(i, '')
        if len(text) != self.temp_enc.key_length:
            self.mostCountedLine.setText(text)

    def do_text_encode(self):
        if self.textEdit.toPlainText() != '' and \
                self.temp_enc.key_length != -1 and \
                self.temp_enc.key != '' and \
                self.temp_enc.key_length == len(self.temp_enc.key):
            self.encodedText.setText(self.temp_enc.text_encoder())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    start_window = MainForm()
    start_window.show()
    sys.exit(app.exec())
