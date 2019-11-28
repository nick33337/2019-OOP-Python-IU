import sys
from PyQt5.QtWidgets import *

# ★중요★ pyqt 는 레이아웃을 지정해 주고 각 요소를 집어넣어야 화면에 뜸

# 창 정의
class MainWindow(QWidget):
    # 창 초기화
    def __init__(self):
        super().__init__()

        self.leftVerticalBox()  # 왼쪽 세로 구역: 제목/제작자 라벨, 졸업식 이미지/게임 도움말
        self.middleVerticalBox()  # 가운데 세로 구역: 공연 정보 라벨, 시작 버튼
        self.rightVerticalBox()  # 오른쪽 세로 구역: 달력, 공연 시간, 난이도

        # 전체 세로 박스 정렬
        hGroupLayout

        self.setWindowTitle("티켓팅 연습 게임")
        self.setGeometry(300, 200, 1200, 700)  # x축, y축, 가로, 세로 지정하기

    def horizontalBox(self):  # 세로 박스 전체를 가로로 정렬하는 레이아웃

    def leftVerticalBox(self):  # 왼쪽 세로 구역: 제목/제작자 라벨, 졸업식 이미지/게임 도움말
        # 제목, 제작자, 도움말 라벨
        label = QLabel()
        lblTitle = label.setText("<b>2019 객체지향프로그래밍\n티켓팅 연습 게임</b>")
        lblPeople = label.setText("제작자: 성민경 | 오세현 | 정도영")
        lblHelp = label.setText("<b>도움말</b>\n티켓팅 연습 게임입니다.\n시작하기 버튼을 누르면 ")

        # 레이아웃
        vLayout = QVBoxLayout
        vLayout.addwidget(lblTitle)
        vLayout.addwidget(lblPeople)
        vLayout.addWidget(lblHelp)

    def middleVerticalBox(self):  # 가운데 세로 구역: 공연 정보 라벨, 시작 버튼
        # 공연 정보 라벨
        label = QLabel()
        lblInfo = label.setText("<b>공연 정보</b>\n일시: 2020년 1월 3일\n장소: 세종과학예술영재학교 강당\nVIP석 12만원\n일반석 9만원")

        # 시작 버튼
        start_btn = QPushButton("시작하기", self)
        start_btn.resize(150, 50)  # resize(): (x축, y축) 크기

        # 레이아웃
        vLayout = QVBoxLayout
        vLayout.addwidget(lblInfo)
        vLayout.addwidget(start_btn)

    def rightVerticalBox(self):  # 오른쪽 세로 구역: 달력, 공연 시간, 난이도
        # 달력

        # 공연 시간

        # 난이도

        # 레이아웃
        vLayout = QVBoxLayout
        vLayout.addWidget()
        vLayout.addWidget()
        vLayout.addWidget()

if __name__ = "__main__":  # 실행 코드(?)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()