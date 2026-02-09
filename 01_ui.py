"""
Код интерфейса, сгенерированный из 01.ui (PyQt6).
"""

from PyQt6.QtWidgets import (
    QDialog,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QRadioButton,
    QPushButton,
    QLabel,
    QLineEdit,
    QCheckBox,
    QSpacerItem,
    QSizePolicy,
)
from PyQt6.QtCore import Qt


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dialog")
        self.resize(624, 594)
        self._setup_ui()

    def _setup_ui(self):
        # Центральный виджет диалога
        central = QWidget(self)
        central.setGeometry(0, 0, 624, 594)

        # Блок с темами и типами карт (справа внизу)
        vertical_layout_widget_3 = QWidget(central)
        vertical_layout_widget_3.setGeometry(460, 460, 161, 131)

        vertical_layout_3 = QVBoxLayout(vertical_layout_widget_3)
        vertical_layout_3.setContentsMargins(0, 0, 0, 0)

        # Горизонтальный layout: darkTheme / lightTheme
        horizontal_layout = QHBoxLayout()
        self.radioButton_3 = QRadioButton("darkTheme")
        self.radioButton_2 = QRadioButton("lightTheme")
        horizontal_layout.addWidget(self.radioButton_3)
        horizontal_layout.addWidget(self.radioButton_2)
        vertical_layout_3.addLayout(horizontal_layout)

        # Вертикальный спейсер
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        vertical_layout_3.addItem(vertical_spacer)

        # Типы карт
        vertical_layout_2 = QVBoxLayout()
        self.radioButton = QRadioButton("baseMap")
        self.radioButton_6 = QRadioButton("carMap")
        self.radioButton_4 = QRadioButton("publicCarMap")
        self.radioButton_5 = QRadioButton("administrativMap")
        vertical_layout_2.addWidget(self.radioButton)
        vertical_layout_2.addWidget(self.radioButton_6)
        vertical_layout_2.addWidget(self.radioButton_4)
        vertical_layout_2.addWidget(self.radioButton_5)
        vertical_layout_3.addLayout(vertical_layout_2)

        # Блок поиска и кнопок (слева внизу)
        grid_layout_widget = QWidget(central)
        grid_layout_widget.setGeometry(10, 460, 441, 81)

        grid_layout = QGridLayout(grid_layout_widget)
        grid_layout.setContentsMargins(0, 0, 0, 0)

        self.addressInput = QLineEdit()
        self.pushButton_2 = QPushButton("seacrhBtn")
        self.checkBox = QCheckBox("indexChoose")
        self.showAdress = QLabel("showAdressLable")
        self.pushButton_3 = QPushButton("resetBtn")

        grid_layout.addWidget(self.addressInput, 0, 0)
        grid_layout.addWidget(self.pushButton_2, 0, 1)
        grid_layout.addWidget(self.checkBox, 1, 0)
        grid_layout.addWidget(self.showAdress, 2, 0)
        grid_layout.addWidget(self.pushButton_3, 2, 1)

        # Метка для изображения карты
        self.label = QLabel("mapImage", central)
        self.label.setGeometry(10, 0, 600, 450)


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())
