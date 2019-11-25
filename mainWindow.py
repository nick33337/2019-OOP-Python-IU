import sys
from PyQt5.QtWidgets import *


class PushButtonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.setWindowTitle("티켓팅 연습 게임")
        self.setGeometry(300, 200, 1200, 700)  # x축, y축, 가로, 세로 지정하기

    def setupUI(self):
        self.setWindowTitle("PushButtonWindow")

        start_btn = QPushButton("시작하기", self)
        start_btn.move(20, 20)
        start_btn.setGeometry(400, 600, 150, 50)
        start_btn.clicked.connect(self.refresh_Window)  # 버튼을 클릭하면 괄호 안의 창과 연결됨

    def refresh_Window(self):
        QMessageBox.about(self, "페이지를 새로고침합니다.\n정각에 타이머를 버튼을 눌러 주세요" "타이머 구현")


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
