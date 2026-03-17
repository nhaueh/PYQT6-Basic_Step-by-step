import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QLineEdit
from PyQt6 import uic
import resources_rc # Import file resources.py được tạo từ Qt Designer_r
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = Path(__file__).with_name("testqt.ui")
        uic.loadUi(str(ui_path), self)
    def control_led(self):
        print("Nút bấm từ Designer đã gọi hàm này!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
