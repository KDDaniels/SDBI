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

from PyQt5.QtWidgets import QMainWindow
from gui.menu_bar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self, title, version):
        super().__init__()
        self.setWindowTitle(f'{title} v{version}')

        self.generate_menu()
        self.generate_gui()

        self.menu.menu_action.connect(self.handle_menu)

    def generate_menu(self):
        self.menu = MenuBar()
        self.setMenuBar(self.menu)

    def generate_gui(self):
        pass

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


