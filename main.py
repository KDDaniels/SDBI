#!/usr/bin/env python

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

import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

title = "EComDB"
version = "0.0.1"

def main():
    app = QApplication(sys.argv)
    win = MainWindow(title, version)
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()