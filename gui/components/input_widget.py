from PyQt5.QtWidgets import QFrame, QSizePolicy, QVBoxLayout, QWidget, QPushButton, QListWidget, QLabel
from PyQt5.QtCore import pyqtSignal


class InputFrame(QFrame):
    signal = pyqtSignal(str)
    def __init__(self, parent):
        super().__init__(parent)

        horizontal_stretch = 2
        vertical_stretch   = 9
        self.set_size_policy(self, horizontal_stretch, vertical_stretch)
        self.set_frame_style(self, QFrame.StyledPanel, QFrame.Sunken)

        self.layout = QVBoxLayout(self)

        self.generate_widgets()

    def generate_widgets(self):
        btn_horizontal_stretch = 0
        btn_vertical_stretch   = 0
        self.buttons = InputButtons(self)
        self.set_size_policy(self.buttons, btn_horizontal_stretch, btn_vertical_stretch)     

        self.line = HLine(self)
        self.set_frame_style(self.line, QFrame.HLine, QFrame.Sunken)

        self.tables_label = QLabel("Tables", self)

        tbl_horizontal_stretch = 0
        tbl_vertical_stretch   = 10
        self.tables = TableList(self)
        self.set_size_policy(self.tables, tbl_horizontal_stretch, tbl_vertical_stretch)

        self.buttons.signal.connect(self.pass_signal)
        self.tables.signal.connect(self.pass_signal)

        self.layout.addWidget(self.buttons)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.tables_label)
        self.layout.addWidget(self.tables)

    def pass_signal(self, data):
        self.signal.emit(data)
        print(data)

    def update_list(self, data):
        self.tables.load_tables(data)

    def set_size_policy(self, component, horizontal, vertical):
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(horizontal)
        sp.setVerticalStretch(vertical)
        sp.setHeightForWidth(component.sizePolicy().hasHeightForWidth())
        component.setSizePolicy(sp)

    def set_frame_style(self, component : QFrame, shape, shadow):
        component.setFrameShape(shape)
        component.setFrameShadow(shadow)


class InputButtons(QWidget):
    signal = pyqtSignal(str)
    def __init__(self, parent):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        self.generate_widgets()

    def generate_widgets(self):
        self.add_table_btn = QPushButton("Add Table", self)
        self.add_row_btn   = QPushButton("Add Row", self)
        self.add_col_btn   = QPushButton("Add Column", self)

        self.add_table_btn.clicked.connect(lambda: self.signal.emit("btn:add_table"))
        self.add_row_btn.clicked.connect(lambda: self.signal.emit("btn:add_row"))
        self.add_col_btn.clicked.connect(lambda: self.signal.emit("btn:add_col"))

        self.layout.addWidget(self.add_table_btn)
        self.layout.addWidget(self.add_row_btn)
        self.layout.addWidget(self.add_col_btn)


class HLine(QFrame):
    def __init__(self, parent):
        super().__init__(parent)


class TableList(QListWidget):
    signal = pyqtSignal(str)
    def __init__(self, parent):
        super().__init__(parent)

    def load_tables(self, data):

        if self.count() > 0:
            self.clear()

        for x in range(len(data)):
            for i in range(len(data[x])):
                table_name = data[x][i]
                self.addItem(table_name)

        self.itemDoubleClicked.connect(self.double_click)

        self.signal.emit(f"Loaded: {table_name}")

    def double_click(self, data):
        self.signal.emit(f"load_table:{data.text()}")