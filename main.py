from api.a import a;
from api.b import b;
from api.c import c;
from api.d import d;
from api.g import g;
import sys
from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QCheckBox)
import functools 

webdriver = "/Users/hwangjaehyeong/Desktop/utils/chromedriver"
title = "경찰관 관두고 피규어 샵 차린 찐 덕후"
body = "경찰을 관두다니..."
image = "/Users/hwangjaehyeong/Downloads/asdfsdf235412desadfasdf3452.jpg"

editor_list = ['webdriver', 'title', 'body', 'image']
api_list = [a, b, c, d]

class App(QWidget):

  def __init__(self):
    super().__init__()
    self.data=['', '', '', '', '']
    self.checked=[False, False, False, False, False]
    self.initUI()

  def initUI(self):
    grid = QGridLayout()
    self.setLayout(grid)

    grid.addWidget(QLabel('크롬 driver:'), 0, 0)
    grid.addWidget(QLabel('제목:'), 1, 0)
    grid.addWidget(QLabel('설명:'), 2, 0)
    grid.addWidget(QLabel('이미지(url):'), 3, 0)
    grid.addWidget(QLabel('이미지2(url):'), 4, 0)

    editor = [QLineEdit(self),QLineEdit(self),QLineEdit(self),QLineEdit(self),QLineEdit(self)]

    for i in range(5):
      editor[i].textChanged[str].connect(functools.partial(self.onChange,i))
      grid.addWidget(editor[i], i, 1)

    self.checkBox = [QCheckBox('뽐뿌', self),QCheckBox('보배드림', self),QCheckBox('에펨코리아', self),QCheckBox('루리웹', self),QCheckBox('개그집합소', self)]

    for i in range(5):
      self.checkBox[i].stateChanged.connect(functools.partial(self.onCheckBoxClick, i))
      grid.addWidget(self.checkBox[i])

    self.submitButton = QPushButton('입력')
    self.submitButton.clicked.connect(self.onSubmitButtonClick)

    grid.addWidget(self.submitButton, 8, 1)

    self.setWindowTitle('마케팅팀 힘들다길래 만들어봤어요.')
    self.setGeometry(300, 300, 400, 200)
    self.show()

  def onChange(self, index, text):
    self.data[index] = text

  def onCheckBoxClick(self, index):
    self.checked[index] = self.checkBox[index].isChecked()

  def onSubmitButtonClick(self):
    for i in range(5):
      if self.checked[i]:
        api_list[i](self.data[0], self.data[1], self.data[2], self.data[3], self.data[4])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())