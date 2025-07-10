from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QStatusBar, QDesktopWidget
from gui.components.menu_bar import MenuBar
from gui.components.input_widget import InputFrame
from gui.components.table_widget import TableWidget
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

        self.db = DatabaseInterface(self)

        self.generate_gui()

        self.help_window = HelpWindow()

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
        self.input_frame.update_list(data)

    def generate_gui(self):
        self.main_window_widget = QWidget(self)
        self.main_window_widget_layout = QGridLayout(self.main_window_widget)
        
        self.menu = MenuBar()
        self.setMenuBar(self.menu)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        self.input_frame = InputFrame(self)

        self.table_widget = TableWidget(self, self.db)

        self.main_window_widget_layout.addWidget(self.input_frame, 1, 0, 2, 1)

        self.main_window_widget_layout.addWidget(self.table_widget, 0, 1, 3, 1)

        self.menu.menu_action.connect(self.handle_menu)
        self.input_frame.signal.connect(self.handle_signal)
        self.table_widget.signal.connect(self.handle_signal)

        self.setCentralWidget(self.main_window_widget)

    def handle_signal(self, data):
        type, command = data.split(":")
        match type:
            case "btn":
                match command:
                    case "add_table":
                        pass
                    case "add_col":
                        pass
                    case "add_row":
                        pass

            case "status":
                self.status_bar.showMessage(command, 5000)
            
            case "load_table":
                self.table_widget.load_data(command)


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