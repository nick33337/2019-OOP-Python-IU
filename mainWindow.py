import sys
from PyQt5.QtWidgets import *


# 창 정의
class PushButtonWindow(QMainWindow):
    # 창 초기화
    def __init__(self):
        super().__init__()

        self.setupUI()  # 메인 창
        self.labels()  # 제목과 제작자 라벨

        self.setWindowTitle("티켓팅 연습 게임")
        self.setGeometry(300, 200, 1200, 700)  # x축, y축, 가로, 세로 지정하기

    def setupUI(self):  # 메인창
        # 시작 버튼
        start_btn = QPushButton("시작하기", self)
        start_btn.setGeometry(400, 600, 150, 50)  # move 와 resize 를 모두 포함

    def labels(self):  # 제목과 제작자 라벨
        lbl_title = QLabel('티켓팅 연습 게임')
        # lbl_people = QLabel('제작자: 성민경 | 오세현 | 정도영\n2019 객체지향프로그래밍')
        lbl_title.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px")

        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PushButtonWindow()
    window.show()
    app.exec_()


"""
예전 코드!
class MyDialog(QDialog):
    def __init__(self):
        
        QDialog.__init__(self)
        # 레이블, 버튼 컨트롤
        titleName = QLabel("티켓팅 연습 게임")
        titleName2 = QLabel("제작: 성민경 | 오세현 | 정도영")
        btnStart = QPushButton("시작하기")

        layout = QVBoxLayout()
        layout.addWidget(titleName)
        layout.addWidget(titleName2)
        layout.addWidget(btnStart)

        self.setLayout(layout)
        

app = QApplication([])
dialog = MyDialog([])
dialog.show()
app.exec_()
"""
