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
import sqlite3
import os
from PyQt5.QtWidgets import QFileDialog

class DatabaseInterface():
    def __init__(self, gui):
        self.is_connected = False
        self.db_name = None
        self.active_db = None
        self.cursor = None
        self.gui = gui

    def new(self):
        # open new file dialog
        ...

    def save(self):
        # save db
        ...

    def save_as(self):

        ...

    def open(self):
        # open open file dialog
        self.connect()

    def load_table(self, table_name):
        data = self.cursor.execute(f"SELECT * FROM {table_name}")
        return data.fetchall()
    
    def get_fields(self, table_name):
        return self.cursor.execute(f"pragma table_info({table_name})").fetchall()
    
    def get_table_data(self, table_name):
        return self.cursor.execute(f"SELECT * FROM {table_name}").fetchall()

    def connect(self):
        if self.is_connected:
            self.disconnect

        try:
            self.active_db = sqlite3.connect(self.open_file_dialog())
            self.cursor = self.active_db.cursor()
            self.gui.load_tables(self.cursor.execute("SELECT name FROM sqlite_master").fetchall())
            self.is_connected = True

        except Exception as e:
            print(e)
            

    def disconnect(self):
        self.active_db.close()
        self.is_connected = False


    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.gui,
            "Open File",
            "./db",
            "SQLite3 Files (*.sqlite3)"
        )
        if file_path:
            self.gui.set_title(os.path.basename(file_path))
            return file_path
        
    def save_file_dialog(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self.gui,
            "Save File",
            "./db",
            "SQLite3 Files (*.sqlite3)"
        )
        if file_path:
            return file_path