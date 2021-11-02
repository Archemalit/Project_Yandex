import sys
import time
import sqlite3
import ctypes
import random
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,\
    QAction, QPushButton, QFontDialog, QLabel, QTableWidgetItem
from PyQt5.QtGui import QIcon
import codecs
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('projectMain.ui', self)
        self.setWindowTitle('SpeedTap')
        self.setWindowIcon(QIcon('windowIcon.png'))
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.startTest)
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton_2.clicked.connect(self.aboutGame)
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_3.clicked.connect(self.exitFromGame)
        self.pushButton_3.setFocusPolicy(Qt.NoFocus)
        # это мы создали в меню кнопки, поставили на них иконки и назначили им функции
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
        #открывается окошко начала игры
        self.startGame = StartGame()
        self.hide()
        self.startGame.show()

    def aboutGame(self):
        # открывается окошко об игре
        self.aboutGameForm = AboutGameForm()
        self.hide()
        self.aboutGameForm.show()

    def exitFromGame(self, event):
        # функция, чтобы при закрытии спрашивало о том, закрыть ли
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
        self.setWindowTitle('SpeedTap')
        self.setWindowIcon(QIcon('windowIcon.png'))
        # это мы создали в меню кнопки, поставили на них иконки и назначили им функции
        backAction = QAction(QIcon('back.png'), 'Back', self)
        backAction.setShortcut('Ctrl+Z')
        backAction.triggered.connect(self.change)
        toolbar = self.addToolBar('Exit')
        toolbar.setStyleSheet("border-image: None;")
        toolbar.addAction(backAction)
        self.connection = sqlite3.connect("projectTests.db")
        data = open('TZ.txt', encoding='utf-8').read()
        self.labelInfo.setText(data)
        self.select_data()

    def select_data(self):
        # записываем в таблицу рекордов данные
        res = self.connection.cursor().execute('''SELECT * FROM records''').fetchall()
        self.tableWidgetRecords.setColumnCount(3)
        self.tableWidgetRecords.setRowCount(0)
        self.tableWidgetRecords.setHorizontalHeaderItem(0, QTableWidgetItem('ID игрока'))
        self.tableWidgetRecords.setHorizontalHeaderItem(1, QTableWidgetItem('Имя игрока'))
        self.tableWidgetRecords.setHorizontalHeaderItem(2, QTableWidgetItem('Сред. скорость'))
        for i, row in enumerate(res):
            self.tableWidgetRecords.setRowCount(
                self.tableWidgetRecords.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidgetRecords.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def change(self):
        # меняем окно на начальное
        self.mainWindow = MainWindow()
        self.hide()
        self.mainWindow.show()


class StartGame(QMainWindow):
    def __init__(self):
        super(StartGame, self).__init__()
        uic.loadUi('projectStartGame.ui', self)
        self.setWindowTitle('SpeedTap')
        self.setWindowIcon(QIcon('windowIcon.png'))
        self.setFocusPolicy(Qt.StrongFocus)
        self.count = 0
        self.data, self.infoAboutSpeed, self.numbersTime = [], {}, []
        self.extraMarks = "'\./[]"
        self.randomText = list(map(int, range(1, 8)))
        self.labelErrors.hide()
        self.labelErrorsInput.hide()
        self.labelSpeedAverage.hide()
        self.labelSpeedAverageInput.hide()
        self.canYou = False
        self.moreTime = 0
        self.prev = 1
        self.initUI()

    def initUI(self):
        # создаем клавиатуру
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
        self.label_36 = QLabel(self)
        # это мы создали в меню кнопки, поставили на них иконки и назначили им функции
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
        self.language = 'en'
        self.pushButton.clicked.connect(self.changeLanguage)
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButtonResult.hide()
        self.pushButtonRecords.hide()
        self.label_extra.hide()
        self.lineNickName.hide()
        self.labelAboutTest.setText("Приготовтесь")
        self.buttons(self.language)

    def keyPressEvent(self, event):
        # обрабатываем нажатие клавиш
        if self.get_layout() == 'ru' and self.language == 'en':
            self.label_extra.show()
        if self.get_layout() == 'en' and self.language == 'ru':
            self.label_extra.show()
        elif self.canYou:
            self.label_extra.hide()
            if self.labelText[self.count].isupper():
                if int(event.modifiers()) == (Qt.ShiftModifier) and event.key() == ord(self.labelText[self.count]):
                    text = '''<font color="green" background="green">{}</font>'''.format(
                        self.labelText[:self.count + 1])
                    self.label.setText(text + self.labelText[self.count + 1:])
                    self.count = self.count + 1
                    self.finishGame()
                else:
                    if int(event.modifiers()) == (Qt.ShiftModifier):
                        pass
                    elif event.key() == Qt.Key_Space:
                        self.countOfErrors += 1
                    else:
                        self.countOfErrors += 1
                        text = '''<font color="red" background="red">{}</font>'''.format(self.labelText[:self.count + 1])
                        self.label.setText(self.labelText[:self.count] + text + self.labelText[self.count + 1:])
            elif event.key() == ord(self.labelText[self.count].upper()) or (
                    event.key() == 39 and ord(self.labelText[self.count])) == 8217:
                text = '''<font color="green" background-color="greed">{}</font>'''.format(
                    self.labelText[:self.count + 1])
                self.label.setText(text + self.labelText[self.count + 1:])
                self.count = self.count + 1
                self.finishGame()
            else:
                self.countOfErrors += 1
                text = '''<font color="red" background="red">{}</font>'''.format(self.labelText[self.count])
                self.label.setText(self.labelText[:self.count] + text + self.labelText[self.count + 1:])
            if self.language == 'en':
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
            else:
                if 1025 <= event.key() <= 1071 or event.key() == Qt.Key_Space or event.key() == 46 or event.key() == 44:
                    if chr(event.key()).lower() == 'й':
                        self.changeColorGreen(self.label_1)
                    elif chr(event.key()).lower() == 'ц':
                        self.changeColorGreen(self.label_2)
                    elif chr(event.key()).lower() == 'у':
                        self.changeColorGreen(self.label_3)
                    elif chr(event.key()).lower() == 'к':
                        self.changeColorGreen(self.label_4)
                    elif chr(event.key()).lower() == 'е':
                        self.changeColorGreen(self.label_5)
                    elif chr(event.key()).lower() == 'н':
                        self.changeColorGreen(self.label_6)
                    elif chr(event.key()).lower() == 'г':
                        self.changeColorGreen(self.label_7)
                    elif chr(event.key()).lower() == 'ш':
                        self.changeColorGreen(self.label_8)
                    elif chr(event.key()).lower() == 'щ':
                        self.changeColorGreen(self.label_9)
                    elif chr(event.key()).lower() == 'з':
                        self.changeColorGreen(self.label_10)
                    elif chr(event.key()).lower() == 'х':
                        self.changeColorGreen(self.label_11)
                    elif chr(event.key()).lower() == 'ъ':
                        self.changeColorGreen(self.label_12)
                    elif chr(event.key()).lower() == 'ф':
                        self.changeColorGreen(self.label_13)
                    elif chr(event.key()).lower() == 'ы':
                        self.changeColorGreen(self.label_14)
                    elif chr(event.key()).lower() == 'в':
                        self.changeColorGreen(self.label_15)
                    elif chr(event.key()).lower() == 'а':
                        self.changeColorGreen(self.label_16)
                    elif chr(event.key()).lower() == 'п':
                        self.changeColorGreen(self.label_17)
                    elif chr(event.key()).lower() == 'р':
                        self.changeColorGreen(self.label_18)
                    elif chr(event.key()).lower() == 'о':
                        self.changeColorGreen(self.label_19)
                    elif chr(event.key()).lower() == 'л':
                        self.changeColorGreen(self.label_20)
                    elif chr(event.key()).lower() == 'д':
                        self.changeColorGreen(self.label_21)
                    elif chr(event.key()).lower() == 'ж':
                        self.changeColorGreen(self.label_22)
                    elif chr(event.key()).lower() == "э":
                        self.changeColorGreen(self.label_23)
                    elif chr(event.key()).lower() == 'я':
                        self.changeColorGreen(self.label_24)
                    elif chr(event.key()).lower() == 'ч':
                        self.changeColorGreen(self.label_25)
                    elif chr(event.key()).lower() == 'с':
                        self.changeColorGreen(self.label_26)
                    elif chr(event.key()).lower() == 'м':
                        self.changeColorGreen(self.label_27)
                    elif chr(event.key()).lower() == 'и':
                        self.changeColorGreen(self.label_28)
                    elif chr(event.key()).lower() == 'т':
                        self.changeColorGreen(self.label_29)
                    elif chr(event.key()).lower() == 'ь':
                        self.changeColorGreen(self.label_30)
                    elif chr(event.key()).lower() == 'б':
                        self.changeColorGreen(self.label_31)
                    elif chr(event.key()).lower() == 'ю':
                        self.changeColorGreen(self.label_32)
                    elif chr(event.key()) == ',':
                        self.changeColorGreen(self.label_33)
                    elif chr(event.key()) == '.':
                        self.changeColorGreen(self.label_36)
                    elif event.key() == Qt.Key_Space:
                        self.changeColorGreen(self.label_34)
                        self.changeColorGreen(self.label_35)

    def changeLanguage(self):
        # функция меняющая язык при нажатии на кнопку
        if self.language == 'en':
            self.language = 'ru'
            self.startGame('ru')
        else:
            self.language = 'en'
            self.startGame('en')

    def changeColorGreen(self, object):
        # при нажатии клавиша загорается зеленым цветом
        self.data.append(object)
        if len(self.data) > 1:
            if (self.data[-2] != self.label_34 and object != self.label_35) and (
                    self.data[-2] != self.label_35 and object != self.label_34):
                self.changeColorNormal(self.data[-2])
            if len(self.data) > 2:
                if ((self.data[-2] == self.label_34 and self.data[-1] == self.label_35) or (
                        self.data[-2] == self.label_35 and self.data[-1] == self.label_34)):
                    self.changeColorNormal(self.data[-3])
                if self.data[-1] != self.label_35 and (
                        (self.data[-2] == self.label_34 and self.data[-3] == self.label_35) or (
                        self.data[-2] == self.label_35 and self.data[-3] == self.label_34)):
                    self.changeColorNormal(self.label_34)
                    self.changeColorNormal(self.label_35)
        object.setStyleSheet(
            "border-image: None;" "background-color : #00FF00;" "border-radius: 16px;" "font-size : 20px;")

    def changeColorNormal(self, object):
        # при нажатии на следующую клавишу прошлая возвращается в обычное состояние
        object.setStyleSheet("border-radius : 16px;" "border-image : None;"
                             "border: 2px solid #00CED1;" "font-size : 20px;" "color : #00CED1;")

    def get_layout(self):
        # определяется текущая раскладка
        u = ctypes.windll.LoadLibrary("user32.dll")
        pf = getattr(u, "GetKeyboardLayout")
        if hex(pf(0)) == '0x4090409':
            return 'en'
        elif hex(pf(0)) == '0x4190419':
            return 'ru'

    def checkBeforeStart(self):
        # обрабатывается раскладка и показывается уведомдение при неправильном выборе раскладки
        if self.get_layout() == 'ru' and self.language == 'en':
            self.label_extra.show()
        elif self.get_layout() == 'en' and self.language == 'ru':
            self.label_extra.show()
        else:
            self.label_extra.hide()
            self.startMainGame()

    def startMainGame(self):
        # старт игры
        time.sleep(1)
        self.lineNickName.hide()
        con = sqlite3.connect('projectTests.db')
        cur = con.cursor()
        if self.language == 'en':
            self.temp = 'SELECT text FROM testsEn WHERE id = {}'.format(random.choice(self.randomText))
        else:
            self.temp = 'SELECT text FROM testsRu WHERE id = {}'.format(random.choice(self.randomText))
        result = cur.execute(self.temp).fetchall()
        con.close()
        self.infoAboutSpeed = {}
        self.pushButton.hide()
        self.pushButtonResult.hide()
        self.pushButtonRecords.hide()
        self.mainText = result[0][0]
        self.label.setText(self.mainText)
        self.labelText = self.label.text()
        self.label.setWordWrap(True)
        self.count = 0
        self.prev = 0
        self.countOfErrors = 0
        self.canYou = True
        self.labelErrors.hide()
        self.labelErrorsInput.hide()
        self.labelSpeedAverage.hide()
        self.labelSpeedAverageInput.hide()
        self.labelAboutTest.hide()
        self.startTime = time.time()

    def startGame(self, language):
        # подготовка к старту игры
        self.language = language
        self.buttons(self.language)

    def finishGame(self):
        # конец игры
        if self.count == len(self.labelText):
            self.endTime = time.time()
            time.sleep(0.1)
            self.canYou = False
            self.pushButton.show()
            self.pushButtonResult.show()
            self.pushButtonResult.clicked.connect(self.showResult)
            self.pushButtonRecords.show()
            self.label.setText('')
            self.pushButtonRecords.clicked.connect(self.writeRecords)
            self.labelAboutTest.show()
            self.lineNickName.show()
            if self.language == 'en':
                self.changeColorNormal(self.label_32)
            elif self.language == 'ru':
                self.changeColorNormal(self.label_36)

            if self.lineNickName.text() != '':
                self.lineNickName.setText(self.nameOfPlayer)
                self.lineNickName.setReadOnly(True)
            self.errors = ['Введите ваш никнейм: ', 'Вам необходимо ввести ваш никнейм: ',
                           'Без никнейма вы не сможете продолжить!']
            self.labelAboutTest.setText('Введите ваш никнейм: ')
            self.playerSpeed = len(self.mainText) / round(self.endTime - self.startTime, 0)
            self.labelErrors.show()
            self.labelErrorsInput.show()
            self.labelErrorsInput.setText(str(self.countOfErrors))
            self.labelSpeedAverage.show()
            self.labelSpeedAverageInput.show()
            self.labelSpeedAverageInput.setText(str(round(self.playerSpeed, 2)))
        self.endTime = time.time()
        if round(self.endTime - self.startTime, 0) % 5 == 0:
            self.numbersTime.append(round(self.endTime - self.startTime, 0))
        if self.numbersTime.count(round(self.endTime - self.startTime, 0)) == 1:
            self.infoAboutSpeed[self.labelText[self.prev:self.count]] = round(self.endTime - self.startTime, 0)
            self.prev = self.count

    def showResult(self):
        # построение графика по результатам
        y = [len(i) for i in self.infoAboutSpeed.keys()]
        x = [int(i) for i in self.infoAboutSpeed.values()]
        plt.plot(x, y, 'r')
        plt.xlabel('Секунды')
        plt.ylabel('Количество символов')
        plt.title('Статистика')
        plt.show();

    def writeRecords(self):
        # запись в список рекордом, если пользователь захочет этого
        con = sqlite3.connect('projectTests.db')
        cur = con.cursor()
        self.nameOfPlayer = self.lineNickName.text()
        if self.lineNickName.text() != 'Готово!':
            while True:
                if self.lineNickName.text() == '':
                    self.labelAboutTest.setText(random.choice(self.errors))
                    break
                else:
                    self.temp = 'SELECT speed FROM records WHERE name = "{}"'.format(self.nameOfPlayer)
                    result = cur.execute(self.temp).fetchall()
                    if len(result) != 0:
                        if self.playerSpeed > result[0][0]:
                            # обновление старого рекорда у текущего пользователя
                            self.temp = 'UPDATE records SET speed = {} WHERE name = "{}"'.format(round(self.playerSpeed, 2), self.nameOfPlayer)
                            self.lineNickName.setText('Готово!')
                            self.moreTime = self.moreTime + 1
                            result = cur.execute(self.temp)
                            con.commit()
                            break
                        else:
                            self.labelAboutTest.setText('Ваш прошлый рекорд был круче!')
                            break
                    else:
                        self.temp = 'INSERT INTO records(name, speed) VALUES("{}", "{}")'.format(
                            self.lineNickName.text(),
                            round(self.playerSpeed, 2))
                        self.lineNickName.setText('Готово!')
                        self.moreTime = self.moreTime + 1
                        result = cur.execute(self.temp)
                        con.commit()
                        break

    def setInfoForButtons(self, object, x, y, letter):
        # параметры для клавиши
        object.setText(letter)
        object.setAlignment(Qt.AlignCenter)
        object.move(x, y)
        object.resize(50, 50)
        object.setStyleSheet("border-radius : 16px;" "border-image : None;"
                             "border: 2px solid #00CED1;" "font-size : 20px;" "color : #00CED1;")

    def buttons(self, language):
        self.labelAboutTest.setText('Приготовтесь!')
        if language == 'en':
            self.label_36.hide()
            # создание всех клавиш на английском языке
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
        else:
            # создание всех клавиш на русском языке
            self.setInfoForButtons(self.label_1, 200, 280, 'й')
            self.setInfoForButtons(self.label_2, 255, 280, 'ц')
            self.setInfoForButtons(self.label_3, 310, 280, 'у')
            self.setInfoForButtons(self.label_4, 365, 280, 'к')
            self.setInfoForButtons(self.label_5, 420, 280, 'е')
            self.setInfoForButtons(self.label_6, 520, 280, 'н')
            self.setInfoForButtons(self.label_7, 585, 280, 'г')
            self.setInfoForButtons(self.label_8, 640, 280, 'ш')
            self.setInfoForButtons(self.label_9, 695, 280, 'щ')
            self.setInfoForButtons(self.label_10, 750, 280, 'з')
            self.setInfoForButtons(self.label_11, 805, 280, 'х')
            self.setInfoForButtons(self.label_12, 860, 280, 'ъ')
            self.setInfoForButtons(self.label_13, 225, 340, 'ф')
            self.setInfoForButtons(self.label_14, 280, 340, 'ы')
            self.setInfoForButtons(self.label_15, 335, 340, 'в')
            self.setInfoForButtons(self.label_16, 390, 340, 'а')
            self.setInfoForButtons(self.label_17, 445, 340, 'п')
            self.setInfoForButtons(self.label_18, 555, 340, 'р')
            self.setInfoForButtons(self.label_19, 610, 340, 'о')
            self.setInfoForButtons(self.label_20, 665, 340, 'л')
            self.setInfoForButtons(self.label_21, 720, 340, 'д')
            self.setInfoForButtons(self.label_22, 775, 340, 'ж')
            self.setInfoForButtons(self.label_23, 830, 340, "э")
            self.setInfoForButtons(self.label_24, 250, 400, "я")
            self.setInfoForButtons(self.label_25, 305, 400, "ч")
            self.setInfoForButtons(self.label_26, 360, 400, "с")
            self.setInfoForButtons(self.label_27, 415, 400, "м")
            self.setInfoForButtons(self.label_28, 470, 400, "и")
            self.setInfoForButtons(self.label_29, 525, 400, "т")
            self.setInfoForButtons(self.label_30, 580, 400, "ь")
            self.setInfoForButtons(self.label_31, 635, 400, "б")
            self.setInfoForButtons(self.label_32, 690, 400, "ю")
            self.setInfoForButtons(self.label_33, 745, 400, ",")
            self.setInfoForButtons(self.label_36, 800, 400, ".")

            self.label_34.setText("пробел")
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
        # меняем окно на начальное
        self.mainWindow = MainWindow()
        self.hide()
        self.mainWindow.show()

    def showDialog(self):
        # изменение шрифта текста
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