import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.main_view import MainView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор с визуализацией графиков функций")
        self.setGeometry(100, 100, 800, 600)

        main_view = MainView()
        self.setCentralWidget(main_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
