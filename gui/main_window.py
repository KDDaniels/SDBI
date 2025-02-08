"""
Little user interface for a small sqlite3 database holding whatever data
Copyright (C) 2025 Kendall Daniels

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QFrame, QTableWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel, QStatusBar, QListWidget
from gui.menu_bar import MenuBar

class MainWindow(QMainWindow):


    def __init__(self, title, version):
        super().__init__()
        self.setWindowTitle(f'{title} v{version}')
        height = 600
        width = 800
        self.setGeometry(100, 100, width, height)
        self.setMinimumSize(width, height)

        self.generate_menu()
        self.generate_statusbar()
        self.generate_gui()

        self.menu.menu_action.connect(self.handle_menu)

        self.showMaximized()


    def generate_menu(self):
        self.menu = MenuBar()
        self.setMenuBar(self.menu)

    def generate_statusbar(self):
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)


    def generate_gui(self):
        self.main_window_widget = QWidget(self)
        self.main_window_widget_layout = QGridLayout(self.main_window_widget)

        self.main_window_widget_layout.addWidget(self.generate_search_widget(), 0, 0, 1, 1)

        self.main_window_widget_layout.addWidget(self.generate_input_widget(), 1, 0, 2, 1)

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
    

    def generate_input_widget(self):
        self.input_frame = QFrame(self.main_window_widget)
        
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(2)
        sp.setVerticalStretch(9)
        sp.setHeightForWidth(self.input_frame.sizePolicy().hasHeightForWidth())
        self.input_frame.setSizePolicy(sp)

        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Sunken)

        self.input_frame_layout = QVBoxLayout(self.input_frame)
        self.input_widget = QWidget(self.input_frame)
        
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(0)
        sp.setVerticalStretch(10)
        sp.setHeightForWidth(self.input_widget.sizePolicy().hasHeightForWidth())
        self.input_widget.setSizePolicy(sp);

        self.input_frame_layout.addWidget(self.input_widget);


        self.add_entries_button = QPushButton("Add", self.input_frame)
        self.input_frame_layout.addWidget(self.add_entries_button)


        self.line = QFrame(self.input_frame)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.input_frame_layout.addWidget(self.line)


        self.tables_list_label = QLabel("Tables", self.input_frame)

        self.input_frame_layout.addWidget(self.tables_list_label)


        self.tables_list_widget = QListWidget(self.input_frame)
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(0)
        sp.setVerticalStretch(0)
        sp.setHeightForWidth(self.input_frame.sizePolicy().hasHeightForWidth())

        self.tables_list_widget.setSizePolicy(sp)


        self.input_frame_layout.addWidget(self.tables_list_widget)


        return self.input_frame
    

    def generate_table_widget(self):
        self.table_widget = QTableWidget(self.main_window_widget)
        
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(8)
        sp.setVerticalStretch(0)
        sp.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sp)

        self.table_widget.setColumnCount(7);
        self.table_widget.setRowCount(20);

        self.table_widget.setFrameShape(QFrame.StyledPanel)
        self.table_widget.setFrameShadow(QFrame.Sunken)

        return self.table_widget

        


    def handle_menu(self, action):
        print("Action: " + action)
        match action:
            # File
            case "new":
                # check if unsaved, then create new db
                pass
            case "open":
                # check if unsaved, then open file dialog
                pass
            case "save":
                # save db
                pass
            case "save as":
                # save db as {filename}
                pass
            case "close":
                # close db
                pass
            case "exit":
                # check if unsaved, then exit program
                self.close()
            # end

            # Edit
            case "undo":
                # undo last action
                pass
            case "redo":
                # redo last action
                pass
            case "cut":
                # cut selected content
                pass
            case "copy":
                # copy content from clipboard
                pass
            case "paste":
                # paste content from clipboard
                pass
            case "delete":
                # delete selected content
                pass
            # end

            # Settings

            # end

            # Help
            case "help":
                # show help window
                pass
            case "about":
                # show about window
                pass
            # end


