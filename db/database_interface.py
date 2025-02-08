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

class DatabaseInterface():
    def __init__(self):
        self.is_connected = False
        self.db_name = ""
        pass

    def connect(self, db_path):
        # if db_path exists, connect and save name as self.db_name
        print(db_path)

    def disconnect(self):
        if self.is_connected:
            # disconnect
            pass