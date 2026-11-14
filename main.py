import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

def main():
    visual_box()

def visual_box():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Calculator - DayDreamingg-g")
    window.resize(600, 800)

    label = QLabel("Test", parent=window)
    label.move(100,40)

    window.show()
    sys.exit(app.exec())