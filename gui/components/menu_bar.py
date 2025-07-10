from PyQt5.QtWidgets import QMenuBar, QMenu, QAction
from PyQt5.QtCore import pyqtSignal

class MenuBar(QMenuBar):
    menu_action = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.generate_buttons()

    def generate_buttons(self):
        self.generate_file_menu()
        self.generate_edit_menu()
        self.generate_settings_menu()
        self.generate_help_menu()

    """
    Generates the compoennts of the file menu
    """
    def generate_file_menu(self):
        self.file_menu = self.addMenu("File")

        new_action = QAction("New File", self)
        new_action.triggered.connect(lambda: self.menu_action.emit("new"))

        new_table_action = QAction("New Table", self)
        new_table_action.triggered.connect(lambda: self.menu_action.emit("new table"))

        open_action = QAction("Open", self)
        open_action.triggered.connect(lambda: self.menu_action.emit("open"))

        save_action = QAction("Save", self)
        save_action.triggered.connect(lambda: self.menu_action.emit("save"))

        save_as_action = QAction("Save As...", self)
        save_as_action.triggered.connect(lambda: self.menu_action.emit("save as"))

        close_action = QAction("Close", self)
        close_action.triggered.connect(lambda: self.menu_action.emit("close"))

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(lambda: self.menu_action.emit("exit"))

        self.file_menu.addAction(new_action)
        self.file_menu.addAction(new_table_action)
        self.file_menu.addAction(open_action)

        self.file_menu.addSeparator()

        self.file_menu.addAction(save_action)
        self.file_menu.addAction(save_as_action)

        self.file_menu.addSeparator()

        self.file_menu.addAction(close_action)

        self.file_menu.addSeparator()

        self.file_menu.addAction(exit_action)

    """
    Generates the components of the edit menu
    """
    def generate_edit_menu(self):
        self.edit_menu = self.addMenu("Edit")
        
        undo_action = QAction("Undo", self)
        undo_action.triggered.connect(lambda: self.menu_action.emit("undo"))

        redo_action = QAction("Redo", self)
        redo_action.triggered.connect(lambda: self.menu_action.emit("redo"))

        cut_action = QAction("Cut", self)
        cut_action.triggered.connect(lambda: self.menu_action.emit("cut"))

        copy_action = QAction("Copy", self)
        copy_action.triggered.connect(lambda: self.menu_action.emit("copy"))

        paste_action = QAction("Paste", self)
        paste_action.triggered.connect(lambda: self.menu_action.emit("paste"))

        del_action = QAction("Delete", self)
        del_action.triggered.connect(lambda: self.menu_action.emit("delete"))

        self.edit_menu.addAction(undo_action)
        self.edit_menu.addAction(redo_action)

        self.edit_menu.addSeparator()

        self.edit_menu.addAction(cut_action)
        self.edit_menu.addAction(copy_action)
        self.edit_menu.addAction(paste_action)
        self.edit_menu.addAction(del_action)

    """
    Generates the components of the settings menu
    """
    def generate_settings_menu(self):
        self.settings_menu = self.addMenu("Settings")

    """
    Generates the components of the help menu
    """
    def generate_help_menu(self):
        self.help_menu = self.addMenu("Help")

        help_action = QAction("EComDB Help", self)
        help_action.triggered.connect(lambda: self.menu_action.emit("help"))

        about_action = QAction("About", self)
        about_action.triggered.connect(lambda: self.menu_action.emit("about"))

        self.help_menu.addAction(help_action)

        self.help_menu.addSeparator()

        self.help_menu.addAction(about_action)