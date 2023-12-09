from logic import *

def main():
    application = QApplication([])
    window = Logic()
    window.setFixedSize(400, 450)
    window.show()
    application.exec()


if __name__ == '__main__':
    main()