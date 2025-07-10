import sqlite3
import os
from PyQt5.QtWidgets import QFileDialog

class DatabaseInterface():
    def __init__(self, gui):
        self.is_connected = False
        self.db_name = None
        self.active_db = None
        self.active_table = None
        self.cursor = None
        self.gui = gui


    def new(self):
        # open new file dialog
        ...


    def save(self):
        # save db
        ...


    def save_as(self):
        db_data = self.cursor.execute("SELECT * FROM *")
        self.disconnect()
        self.active_db = sqlite3.connect(self.save_file_dialog())
        self.cursor = self.active_db.cursor()
        # self.cursor.execute
        # copy data from table to active_db

    def save_data(self, data):
        self.cursor.execute(f"INSERT INTO {self.active_table} VALUES {data}")

    def open(self):
        # open open file dialog
        self.connect()


    def load_table(self, table_name):
        data = self.cursor.execute(f"SELECT * FROM {table_name}")
        self.active_table = table_name
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
            self.gui.set_title(os.path.basename(file_path))
            return file_path