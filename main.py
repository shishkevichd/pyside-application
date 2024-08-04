import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, Slot, QRect

class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello world")
        self.setFixedSize(320, 240)

        central_widget = QWidget()
        
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.label = QLabel("Hello world", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Change text", self)
        self.button.clicked.connect(self.change_text)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

    @Slot()
    def change_text(self):
        current_text = self.label.text()

        if current_text == "Hello world":
            self.label.setText("World Hello")
        else:
            self.label.setText("Hello world")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Application()
    window.show()

    sys.exit(app.exec())
