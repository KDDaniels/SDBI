"""
+------------------------+-------------------------+
| Search                 |                         |
| [ Search Bar       ]   |       Database          |
| [ Search Button    ]   |    [Scrollable Table]   |
|------------------------+                         |
| Add/Update Component   |                         |
| [ Type: __________ ]   |                         |
| [ Name: __________ ]   |                         |
| [ Quantity: ______ ]   |                         |
| [ Add/Update Button ]  |                         |
+------------------------+-------------------------+
"""
"""
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EComDBMainJnHgNN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(745, 588)

        ==== MAIN =====
        self.centralwidget = QWidget(MainWindow)
        self.gridLayout = QGridLayout(self.centralwidget)


        
        ===== MENU =====
        self.actionNew = QAction(MainWindow)
        self.actionLoad_Database = QAction(MainWindow)
        self.actionExit = QAction(MainWindow)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave = QAction(MainWindow)
        self.actionInfo = QAction(MainWindow)
        self.actionUndo = QAction(MainWindow)
        self.actionRedo = QAction(MainWindow)
        self.actionCopy = QAction(MainWindow)
        self.actionCut = QAction(MainWindow)
        self.actionPaste = QAction(MainWindow)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 745, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuEdit = QMenu(self.menubar)
        self.menuHelp = QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionLoad_Database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionInfo)

        
        
        ======= SEARCH ======
        self.search_frame = QFrame(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.search_frame.sizePolicy().hasHeightForWidth())
        self.search_frame.setSizePolicy(sizePolicy)
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Sunken)
        self.search_frame.setLineWidth(1)
        self.search_frame.setMidLineWidth(0)

        self.pushButton = QPushButton(self.search_frame)
        self.lineEdit = QLineEdit(self.search_frame)


        self.gridLayout_2 = QGridLayout(self.search_frame)
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.search_frame, 0, 0, 1, 1)


        
        ====== INPUT =======
        self.add_button = QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.add_button, 2, 0, 1, 1)



        self.input_scroll_area = QScrollArea(self.centralwidget)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(7)
        sizePolicy2.setHeightForWidth(self.input_scroll_area.sizePolicy().hasHeightForWidth())
        
        self.input_scroll_area.setSizePolicy(sizePolicy2)
        self.input_contents = QWidget()
        self.input_contents.setGeometry(QRect(0, 0, 204, 430))
        self.verticalLayout = QVBoxLayout(self.input_contents)
        self.input_scroll_area.setWidget(self.input_contents)

        self.gridLayout.addWidget(self.input_scroll_area, 1, 0, 1, 1)


        

        ======== TABLE ========



        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)

        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)

        self.db_table.setDragDropOverwriteMode(False)
        self.db_table.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.db_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.db_table.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.db_table.setGridStyle(Qt.DashLine)
        self.db_table.setSortingEnabled(False)
        self.db_table.setCornerButtonEnabled(True)
        self.db_table.setRowCount(1)
        self.db_table.setColumnCount(1)
        self.db_table.horizontalHeader().setVisible(True)
        self.db_table.horizontalHeader().setCascadingSectionResizes(False)
        self.db_table.horizontalHeader().setProperty("showSortIndicator", False)

        self.gridLayout.addWidget(self.db_table, 0, 1, 3, 1)

        



        
        MainWindow.setCentralWidget(self.centralwidget)
        


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New Database", None))
        self.actionLoad_Database.setText(QCoreApplication.translate("MainWindow", u"Load Database...", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"field1", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"test_col", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lineEdit.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Entry", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


"""