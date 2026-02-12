import os
import sys
import requests
from ui import Ui_Dialog
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from PyQt6.QtGui import QPixmap

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
WINDOW_TITLE = "MAP"
MAP_FILE = "map.png"

num = 0.2
x_cord = 39.736096
y_cord = 52.043386


class MapWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_map()

    def InitUi(self):
        pass

    def load_map(self):
        server_address = "https://static-maps.yandex.ru/v1?"
        api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        ll_spn = f"ll={x_cord},{y_cord}&spn={num},{num}"
        map_request = f"{server_address}{ll_spn}&apikey={api_key}"
        response = requests.get(map_request)

        if not response.ok:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        with open(MAP_FILE, "wb") as file:
            file.write(response.content)

        pixmap = QPixmap(MAP_FILE)
        self.label.setPixmap(pixmap)

    def search(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    exit_code = app.exec()
    if os.path.exists(MAP_FILE):
        os.remove(MAP_FILE)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
