import sys
from PyQt5.QtWidgets import *

class EmptyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("티켓팅 연습 게임")
        self.setGeometry(300, 200, 1200, 700) # x축, y축, 가로, 세로

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    window.show()
    app.exec_()
"""
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
