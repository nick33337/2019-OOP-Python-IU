import sys

from PyQt5.QtWidgets import *

app = QApplication([])
dialog = Qdialog([])
dialog.show()
app.exec()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
