# SPDX-FileCopyrightText: 2025 Kendall Daniels <kendall.daniels.dev@gmail.com>
# SPDX-License-Identifier: MIT

#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

title = "SDBI - Simple Database Interface"
version = "0.0.1"

def main():
    app = QApplication(sys.argv)
    win = MainWindow(title, version)
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()