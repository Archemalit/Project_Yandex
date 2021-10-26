import sys
import time
import sqlite3
import ctypes
import random
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QAction, QPushButton, QFontDialog, QLabel
from PyQt5.QtGui import QIcon, QColor, QPixmap, QFont
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('projectMain.ui', self)
        self.setWindowTitle('Первая форма')
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.startTest)
        self.pushButton_2.clicked.connect(self.aboutGame)
        self.pushButton_3.clicked.connect(self.exitFromGame)
        vkAction = QAction(QIcon('vk.png'), 'Vk', self)
        vkAction.setShortcut('Ctrl+Q')
        vkAction.triggered.connect(lambda: webbrowser.open('https://vk.com/yandex'))
        isntaAction = QAction(QIcon('insta.png'), 'Insta', self)
        isntaAction.setShortcut('Ctrl+W')
        isntaAction.triggered.connect(lambda: webbrowser.open('https://www.instagram.com/yandex/'))
        twitterAction = QAction(QIcon('twitter.png'), 'Twitter', self)
        twitterAction.setShortcut('Ctrl+E')
        twitterAction.triggered.connect(lambda: webbrowser.open('https://twitter.com/yandex'))
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Яндекс в соц. сетях')
        fileMenu.addAction(vkAction)
        fileMenu.addAction(isntaAction)
        fileMenu.addAction(twitterAction)

    def startTest(self):
        self.startGame = StartGame()
        self.hide()
        self.startGame.show()

    def aboutGame(self):
        self.aboutGameForm = AboutGameForm()
        self.hide()
        self.aboutGameForm.show()

    def exitFromGame(self, event):
        reply = QMessageBox(
            QMessageBox.Question,
            "Закрытие :(",
            "Ты точно хочешь выйти?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            parent=self,
        )
        reply.setDefaultButton(QMessageBox.No)
        reply.setStyleSheet("QLabel{ border-image: None }")
        reply.setStyleSheet("QMessageBox{ border-image: None }")
        reply.exec_()
        reply = reply.standardButton(reply.clickedButton())
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass


class AboutGameForm(QMainWindow):
    def __init__(self):
        super(AboutGameForm, self).__init__()
        uic.loadUi('projectAboutGame.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(408, 211, 1106, 616)
        self.setWindowTitle('Вторая форма')
        backAction = QAction(QIcon('back.png'), 'Back', self)
        backAction.setShortcut('Ctrl+Z')
        backAction.triggered.connect(self.change)
        toolbar = self.addToolBar('Exit')
        toolbar.setStyleSheet("border-image: None;")
        toolbar.addAction(backAction)

    def change(self):
        self.mainWindow = MainWindow()
        self.hide()
        self.mainWindow.show()


class StartGame(QMainWindow):
    def __init__(self):
        super(StartGame, self).__init__()
        uic.loadUi('projectStartGame.ui', self)
        self.setWindowTitle('Основной тест')
        self.count = 0
        self.data, self.infoAboutSpeed, self.numbersTime = [], {}, []
        self.extraMarks = "'\./[]"
        self.randomText = list(map(int, range(1, 3)))
        self.canYou = False
        self.prev = 1
        self.initUI()

    def initUI(self):
        self.label_1 = QLabel(self)
        self.label_2 = QLabel(self)
        self.label_3 = QLabel(self)
        self.label_4 = QLabel(self)
        self.label_5 = QLabel(self)
        self.label_6 = QLabel(self)
        self.label_7 = QLabel(self)
        self.label_8 = QLabel(self)
        self.label_9 = QLabel(self)
        self.label_10 = QLabel(self)
        self.label_11 = QLabel(self)
        self.label_12 = QLabel(self)
        self.label_13 = QLabel(self)
        self.label_14 = QLabel(self)
        self.label_15 = QLabel(self)
        self.label_16 = QLabel(self)
        self.label_17 = QLabel(self)
        self.label_18 = QLabel(self)
        self.label_19 = QLabel(self)
        self.label_20 = QLabel(self)
        self.label_21 = QLabel(self)
        self.label_22 = QLabel(self)
        self.label_23 = QLabel(self)
        self.label_24 = QLabel(self)
        self.label_25 = QLabel(self)
        self.label_26 = QLabel(self)
        self.label_27 = QLabel(self)
        self.label_28 = QLabel(self)
        self.label_29 = QLabel(self)
        self.label_30 = QLabel(self)
        self.label_31 = QLabel(self)
        self.label_32 = QLabel(self)
        self.label_33 = QLabel(self)
        self.label_34 = QLabel(self)
        self.label_35 = QLabel(self)
        backAction = QAction(QIcon('back.png'), 'Back', self)
        backAction.setShortcut('Ctrl+Z')
        backAction.triggered.connect(self.change)
        settingsAction = QAction(QIcon('settings.png'), 'Settings', self)
        settingsAction.triggered.connect(self.showDialog)
        startAction = QAction(QIcon('start.png'), 'Start', self)
        startAction.triggered.connect(self.checkBeforeStart)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(backAction)
        toolbar.addAction(settingsAction)
        toolbar.addAction(startAction)
        toolbar.setStyleSheet("border-image: None;")
        self.label_extra.hide()
        self.buttons()

    def keyPressEvent(self, event):
        if self.get_layout() == 'ru':
            self.label_extra.show()
        elif self.canYou:
            self.label_extra.hide()
            if self.labelText[self.count].isupper():
                if int(event.modifiers()) == (Qt.ShiftModifier) and event.key() == ord(self.labelText[self.count]):
                    text = '''<font color="green" background="green">{}</font>'''.format(self.labelText[:self.count + 1])
                    self.label.setText(text + self.labelText[self.count + 1:])
                    self.count = self.count + 1
                    self.finishGame()
                else:
                    text = '''<font color="red" background="red">{}</font>'''.format(self.labelText[:self.count + 1])
                    self.label.setText(self.labelText[:self.count] + text + self.labelText[self.count + 1:])
            if event.key() == ord(self.labelText[self.count].upper()) or (event.key() == 39 and ord(self.labelText[self.count])) == 8217:
                text = '''<font color="green" background-color="greed">{}</font>'''.format(self.labelText[:self.count + 1])
                self.label.setText(text + self.labelText[self.count + 1:])
                self.count = self.count + 1
                self.finishGame()
            else:
                text = '''<font color="red" background="red">{}</font>'''.format(self.labelText[self.count])
                self.label.setText(self.labelText[:self.count] + text + self.labelText[self.count + 1:])
            if 39 <= event.key() <= 110 or event.key() == Qt.Key_Space:
                if chr(event.key()).lower() == 'q':
                    self.changeColorGreen(self.label_1)
                elif chr(event.key()).lower() == 'w':
                    self.changeColorGreen(self.label_2)
                elif chr(event.key()).lower() == 'e':
                    self.changeColorGreen(self.label_3)
                elif chr(event.key()).lower() == 'r':
                    self.changeColorGreen(self.label_4)
                elif chr(event.key()).lower() == 't':
                    self.changeColorGreen(self.label_5)
                elif chr(event.key()).lower() == 'y':
                    self.changeColorGreen(self.label_6)
                elif chr(event.key()).lower() == 'u':
                    self.changeColorGreen(self.label_7)
                elif chr(event.key()).lower() == 'i':
                    self.changeColorGreen(self.label_8)
                elif chr(event.key()).lower() == 'o':
                    self.changeColorGreen(self.label_9)
                elif chr(event.key()).lower() == 'p':
                    self.changeColorGreen(self.label_10)
                elif chr(event.key()) == '[':
                    self.changeColorGreen(self.label_11)
                elif chr(event.key()) == ']':
                    self.changeColorGreen(self.label_12)
                elif chr(event.key()).lower() == 'a':
                    self.changeColorGreen(self.label_13)
                elif chr(event.key()).lower() == 's':
                    self.changeColorGreen(self.label_14)
                elif chr(event.key()).lower() == 'd':
                    self.changeColorGreen(self.label_15)
                elif chr(event.key()).lower() == 'f':
                    self.changeColorGreen(self.label_16)
                elif chr(event.key()).lower() == 'g':
                    self.changeColorGreen(self.label_17)
                elif chr(event.key()).lower() == 'h':
                    self.changeColorGreen(self.label_18)
                elif chr(event.key()).lower() == 'j':
                    self.changeColorGreen(self.label_19)
                elif chr(event.key()).lower() == 'k':
                    self.changeColorGreen(self.label_20)
                elif chr(event.key()).lower() == 'l':
                    self.changeColorGreen(self.label_21)
                elif chr(event.key()) == ';':
                    self.changeColorGreen(self.label_22)
                elif chr(event.key()) == "'":
                    self.changeColorGreen(self.label_23)
                elif chr(event.key()).lower() == 'z':
                    self.changeColorGreen(self.label_24)
                elif chr(event.key()).lower() == 'x':
                    self.changeColorGreen(self.label_25)
                elif chr(event.key()).lower() == 'c':
                    self.changeColorGreen(self.label_26)
                elif chr(event.key()).lower() == 'v':
                    self.changeColorGreen(self.label_27)
                elif chr(event.key()).lower() == 'b':
                    self.changeColorGreen(self.label_28)
                elif chr(event.key()).lower() == 'n':
                    self.changeColorGreen(self.label_29)
                elif chr(event.key()).lower() == 'm':
                    self.changeColorGreen(self.label_30)
                elif chr(event.key()) == ',':
                    self.changeColorGreen(self.label_31)
                elif chr(event.key()) == '.':
                    self.changeColorGreen(self.label_32)
                elif chr(event.key()) == '/':
                    self.changeColorGreen(self.label_33)
                elif event.key() == Qt.Key_Space:
                    self.changeColorGreen(self.label_34)
                    self.changeColorGreen(self.label_35)

    def changeColorGreen(self, object):
        self.data.append(object)
        if len(self.data) > 1:
            if (self.data[-2] != self.label_34 and object != self.label_35) and (self.data[-2] != self.label_35 and object != self.label_34):
                self.changeColorNormal(self.data[-2])
            if len(self.data) > 2:
                if ((self.data[-2] == self.label_34 and self.data[-1] == self.label_35) or (self.data[-2] == self.label_35 and self.data[-1] == self.label_34)):
                    self.changeColorNormal(self.data[-3])
                if self.data[-1] != self.label_35 and ((self.data[-2] == self.label_34 and self.data[-3] == self.label_35) or (self.data[-2] == self.label_35 and self.data[-3] == self.label_34)):
                    self.changeColorNormal(self.label_34)
                    self.changeColorNormal(self.label_35)
        object.setStyleSheet(
            "border-image: None;" "background-color : #00FF00;" "border-radius: 16px;" "font-size : 20px;")

    def changeColorNormal(self, object):
        object.setStyleSheet("border-radius : 16px;" "border-image : None;"
                             "border: 2px solid #00CED1;" "font-size : 20px;" "color : #00CED1;")

    def get_layout(self):
        u = ctypes.windll.LoadLibrary("user32.dll")
        pf = getattr(u, "GetKeyboardLayout")
        if hex(pf(0)) == '0x4090409':
            return 'en'
        elif hex(pf(0)) == '0x4190419':
            return 'ru'

    def checkBeforeStart(self):
        if self.get_layout() == 'ru':
            self.label_extra.show()
        else:
            self.label_extra.hide()
            self.startGame()

    def startGame(self):
        time.sleep(1)
        con = sqlite3.connect('projectTests.db')
        cur = con.cursor()
        temp = 'SELECT text FROM testsEn WHERE id = {}'.format(random.choice(self.randomText))
        result = cur.execute(temp).fetchall()
        con.close()
        self.buttons()
        self.label.setText(result[0][0])
        self.labelText = self.label.text()
        self.label.setWordWrap(True)
        self.count = 0
        self.prev = 1
        self.canYou = True
        self.startTime = time.time()

    def finishGame(self):
        if self.count == len(self.labelText):
            self.endTime = time.time()
            time.sleep(0.1)
            self.label.setText('Вы прошли тест!')
            self.canYou = False
            print(self.endTime - self.startTime)
            y = [len(i) for i in self.infoAboutSpeed.keys()]
            x = [int(i) for i in self.infoAboutSpeed.values()]
            plt.plot(x, y, 'r')
            plt.xlabel('Секунды')
            plt.ylabel('Количество символов')
            plt.title('Статистика')
            plt.show();

        self.endTime = time.time()
        if round(self.endTime - self.startTime, 0) % 5 == 0 or self.count + 1 == len(self.labelText) or self.count + 2 == len(self.labelText):
            self.numbersTime.append(round(self.endTime - self.startTime, 0))
        if self.numbersTime.count(round(self.endTime - self.startTime, 0)) == 1:
            self.infoAboutSpeed[self.labelText[self.prev - 1:self.count]] = round(self.endTime - self.startTime, 0)
            self.prev = self.count


    def setInfoForButtons(self, object, x, y, letter):
        object.setText(letter)
        object.setAlignment(Qt.AlignCenter)
        object.move(x, y)
        object.resize(50, 50)
        object.setStyleSheet("border-radius : 16px;" "border-image : None;"
                             "border: 2px solid #00CED1;" "font-size : 20px;" "color : #00CED1;")

    def buttons(self):
        self.label.setText('Приготовтесь!')
        self.setInfoForButtons(self.label_1, 200, 280, 'q')
        self.setInfoForButtons(self.label_2, 255, 280, 'w')
        self.setInfoForButtons(self.label_3, 310, 280, 'e')
        self.setInfoForButtons(self.label_4, 365, 280, 'r')
        self.setInfoForButtons(self.label_5, 420, 280, 't')
        self.setInfoForButtons(self.label_6, 520, 280, 'y')
        self.setInfoForButtons(self.label_7, 585, 280, 'u')
        self.setInfoForButtons(self.label_8, 640, 280, 'i')
        self.setInfoForButtons(self.label_9, 695, 280, 'o')
        self.setInfoForButtons(self.label_10, 750, 280, 'p')
        self.setInfoForButtons(self.label_11, 805, 280, '[')
        self.setInfoForButtons(self.label_12, 860, 280, ']')
        self.setInfoForButtons(self.label_13, 225, 340, 'a')
        self.setInfoForButtons(self.label_14, 280, 340, 's')
        self.setInfoForButtons(self.label_15, 335, 340, 'd')
        self.setInfoForButtons(self.label_16, 390, 340, 'f')
        self.setInfoForButtons(self.label_17, 445, 340, 'g')
        self.setInfoForButtons(self.label_18, 555, 340, 'h')
        self.setInfoForButtons(self.label_19, 610, 340, 'j')
        self.setInfoForButtons(self.label_20, 665, 340, 'k')
        self.setInfoForButtons(self.label_21, 720, 340, 'l')
        self.setInfoForButtons(self.label_22, 775, 340, ';')
        self.setInfoForButtons(self.label_23, 830, 340, "'")
        self.setInfoForButtons(self.label_24, 250, 400, "z")
        self.setInfoForButtons(self.label_25, 305, 400, "x")
        self.setInfoForButtons(self.label_26, 360, 400, "c")
        self.setInfoForButtons(self.label_27, 415, 400, "v")
        self.setInfoForButtons(self.label_28, 470, 400, "b")
        self.setInfoForButtons(self.label_29, 580, 400, "n")
        self.setInfoForButtons(self.label_30, 635, 400, "m")
        self.setInfoForButtons(self.label_31, 690, 400, ",")
        self.setInfoForButtons(self.label_32, 745, 400, ".")
        self.setInfoForButtons(self.label_33, 800, 400, "/")

        self.label_34.setText("space")
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_34.move(360, 460)
        self.label_34.resize(165, 50)
        self.label_34.setStyleSheet("border-radius : 16px;" "border-image : None;"
                                    "border: 2px solid #00CED1;" "font-size : 20px;" "color : #00CED1;")

        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_35.move(580, 460)
        self.label_35.resize(165, 50)
        self.label_35.setStyleSheet("border-radius : 16px;" "border-image : None;"
                                    "border: 2px solid #00CED1;" "font-size : 20px;" "color : #00CED1;")


    def change(self):
        self.mainWindow = MainWindow()
        self.hide()
        self.mainWindow.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)






def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())