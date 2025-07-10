from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy, QFrame
from PyQt5.QtCore import pyqtSignal

class TableWidget(QTableWidget):
    signal = pyqtSignal(str)
    def __init__(self, parent, db):
        super().__init__(parent)
        self.db = db

        horizontal_stretch = 8
        vertical_stretch   = 0
        self.set_size_policy(self, horizontal_stretch, vertical_stretch)
        self.set_frame_style(self, QFrame.StyledPanel, QFrame.Sunken)

    def load_data(self, table):
        table_data = self.db.load_table(table)
        try:
            if table_data:
                self.setColumnCount(len(table_data[0]))
                self.setRowCount(len(table_data))

                col_text = []
                table_fields = self.db.get_fields(table)
                for field in table_fields:
                    col_text.append(field[1])

                self.setHorizontalHeaderLabels(col_text)

                table_data = self.db.get_table_data(table)
                
                for x in range(len(table_data)):
                    for i in range(len(table_data[x])):
                        self.setItem(x, i, QTableWidgetItem(str(table_data[x][i])))


                self.signal.emit(f"status:Loaded table [{table}]")
                print("loaded")
            else:
                raise Exception("Table has no values to load")
            
        except Exception as e:
            print(f"[ERROR] {e}")
            self.signal.emit(f"status:Error loading table [{table}] ({e})")
        
    def set_size_policy(self, component, horizontal, vertical):
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(horizontal)
        sp.setVerticalStretch(vertical)
        sp.setHeightForWidth(component.sizePolicy().hasHeightForWidth())
        component.setSizePolicy(sp)

    def set_frame_style(self, component : QFrame, shape, shadow):
        component.setFrameShape(shape)
        component.setFrameShadow(shadow)