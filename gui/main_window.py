from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QFrame, QTableWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QStatusBar, QListWidget, QTableWidgetItem, QDesktopWidget
from gui.components.menu_bar import MenuBar
from gui.components.input_widget import InputFrame
from gui.help_window import HelpWindow
from db.database_interface import DatabaseInterface

class MainWindow(QMainWindow):
    def __init__(self, title, version):
        super().__init__()
        self.title = f'{title} v{version}'
        self.setWindowTitle(self.title)
        height = 600
        width  = 800
        self.setGeometry(100, 100, width, height)
        self.setMinimumSize(width, height)

        self.center_window()

        self.generate_gui()

        self.menu.menu_action.connect(self.handle_menu)

        self.help_window = HelpWindow()

        # self.showMaximized()

        self.db = DatabaseInterface(self)


    def center_window(self):
        frame = self.frameGeometry()

        screen_center = QDesktopWidget().availableGeometry().center()

        frame.moveCenter(screen_center)

        self.move(frame.topLeft())

    
    def set_title(self, file_name=None):
        if file_name is not None:
            self.setWindowTitle(f'{file_name} - {self.title} [*]')
        else:
            self.setWindowTitle(f'{self.title}')


    def load_tables(self, data):

        if self.tables_list_widget.count() > 0:
            self.tables_list_widget.clear()

        for x in range(len(data)):
            for i in range(len(data[x])):
                table_name = data[x][i]
                self.tables_list_widget.addItem(table_name)

        self.tables_list_widget.itemDoubleClicked.connect(self.load_data)
        # self.tables_list_widget.setContextMenuPolicy()

        self.status_bar.showMessage(f"Loaded {table_name}", 5000)


    def right_click_menu(self, type):
        match type:
            case "table":
                print("table")
        ...


    def load_data(self, table):
        table_data = self.db.load_table(table.text())
        # load the data into the grid
        try:
            if table_data:
                self.table_widget.setColumnCount(len(table_data[0]))
                self.table_widget.setRowCount(len(table_data))

                col_text = []
                table_fields = self.db.get_fields(table.text())
                for field in table_fields:
                    col_text.append(field[1])

                self.table_widget.setHorizontalHeaderLabels(col_text)

                table_data = self.db.get_table_data(table.text())
                
                for x in range(len(table_data)):
                    for i in range(len(table_data[x])):
                        self.table_widget.setItem(x, i, QTableWidgetItem(str(table_data[x][i])))


                self.status_bar.showMessage(f"Loaded table: {table.text()}", 5000)
            else:
                raise Exception("Table has no values to load")
                
        except Exception as e:
            print(e)
            self.status_bar.showMessage(f"Error loading table: {table.text()} ({e})", 5000)


    def get_table_data(self):
        for x in range(self.table_widget.rowCount()):
            data = []
            for i in range(self.table_widget.columnCount()):
                data.append(self.table_widget.item(x, i).text())

            data = tuple(data)

            self.db.save_data(data)


    def generate_gui(self):
        self.main_window_widget = QWidget(self)
        self.main_window_widget_layout = QGridLayout(self.main_window_widget)
        
        self.menu = MenuBar()
        self.setMenuBar(self.menu)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        self.input_frame = InputFrame(self)

        # self.main_window_widget_layout.addWidget(self.generate_search_widget(), 0, 0, 1, 1)

        self.main_window_widget_layout.addWidget(self.input_frame, 1, 0, 2, 1)

        self.main_window_widget_layout.addWidget(self.generate_table_widget(), 0, 1, 3, 1)


        self.setCentralWidget(self.main_window_widget)


    def generate_search_widget(self):
        self.search_frame = QFrame(self.main_window_widget)

        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(2)
        sp.setVerticalStretch(1)
        sp.setHeightForWidth(self.search_frame.sizePolicy().hasHeightForWidth())
        self.search_frame.setSizePolicy(sp)

        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Sunken)

        self.search_layout = QHBoxLayout(self.search_frame)

        self.search_input = QLineEdit(self.search_frame)
        self.search_button = QPushButton("Search", self.search_frame)

        self.search_input.setPlaceholderText("Search...")

        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.search_button)

        return self.search_frame
    

    def generate_table_widget(self):
        self.table_widget = QTableWidget(self.main_window_widget)
        
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(8)
        sp.setVerticalStretch(0)
        sp.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sp)

        self.table_widget.setFrameShape(QFrame.StyledPanel)
        self.table_widget.setFrameShadow(QFrame.Sunken)

        return self.table_widget


    def handle_menu(self, action):
        print("Action: " + action)
        match action:
            # File
            case "new":
                # check if unsaved, then create new db
                self.get_table_data()
                ...
            case "new table":
                # open window w/ options to create a new table with
                ...
            case "open":
                # check if unsaved, then open file dialog
                self.db.open()
                ...
            case "save":
                # save db
                ...
            case "save as":
                self.db.save_as()
                # save db as {filename}
                ...
            case "close":
                # close db
                ...
            case "exit":
                # check if unsaved, then exit program
                self.close()
            # end

            # Edit
            case "undo":
                # undo last action
                ...
            case "redo":
                # redo last action
                ...
            case "cut":
                # cut selected content
                ...
            case "copy":
                # copy content from clipboard
                ...
            case "paste":
                # paste content from clipboard
                ...
            case "delete":
                # delete selected content
                ...
            # end

            # Settings

            # end

            # Help
            case "help":
                self.help_window.show()
            case "about":
                # show about window
                ...
            # end


    def handle_input(self, action):
        ...