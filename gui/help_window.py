from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SDBI Help")

        self.generate_image()


    def generate_image(self):
        self.help_image = QLabel();

        self.im = QPixmap("./gui/resources/help_diagram.png")
        self.help_image.setPixmap(self.im)

        self.help_image_layout = QGridLayout(self)
        self.help_image_layout.addWidget(self.help_image, 1, 1)
        self.setLayout(self.help_image_layout)

        self.resize(self.im.width(), self.im.height())
