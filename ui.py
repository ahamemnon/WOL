import sys
from PyQt5.QtWidgets import QApplication, QWidget

class WOL_window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self) -> None:
        self.setWindowTitle('WakeOnLan')
        
        self.setFixedHeight(500)
        self.setFixedWidth(350)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WOL_window()
    sys.exit(app.exec_())