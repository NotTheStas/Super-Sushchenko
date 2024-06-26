# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 720)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fio_label = QtWidgets.QLabel(self.centralwidget)
        self.fio_label.setStyleSheet("color: rgb(255, 221, 172);")
        self.fio_label.setObjectName("fio_label")
        self.verticalLayout_3.addWidget(self.fio_label)
        self.groups_label = QtWidgets.QLabel(self.centralwidget)
        self.groups_label.setStyleSheet("color: rgb(255, 221, 172);")
        self.groups_label.setObjectName("groups_label")
        self.verticalLayout_3.addWidget(self.groups_label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("color: rgb(255, 221, 172);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.ComboBox.setStyleSheet("background-color: rgb(255, 221, 172);\n"
"color: rgb(31, 31, 147);")
        self.ComboBox.setObjectName("ComboBox")
        self.verticalLayout.addWidget(self.ComboBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setStyleSheet("background-color: rgb(153, 72, 87);\n"
"color: rgb(255, 221, 172);")
        self.add_button.setObjectName("add_button")
        self.verticalLayout_6.addWidget(self.add_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setStyleSheet("background-color: rgb(153, 72, 87);\n"
"color: rgb(255, 221, 172);")
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout_8.addWidget(self.delete_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setStyleSheet("background-color: rgb(153, 72, 87);\n"
"color: rgb(255, 221, 172);")
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_6.addWidget(self.save_button)
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setStyleSheet("background-color: rgb(153, 72, 87);\n"
"color: rgb(255, 221, 172);")
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_6.addWidget(self.exit_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setStyleSheet("/* цвет заголовков столбцов и строк */\n"
"QHeaderView::section {\n"
"    background-color: rgb(153, 72, 87);\n"
"    color: rgb(255, 221, 172)\n"
"}\n"
"\n"
"/* цвет ячейки слева вверху*/\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(153, 72, 87)\n"
"}\n"
"\n"
"/* цвет ячеек с значениями */\n"
"QTableWidget::item {\n"
"    background-color: rgb(255, 221, 172);\n"
"    color: rgb(31, 31, 147);\n"
"}")
        self.table.setObjectName("table")
        self.horizontalLayout_2.addWidget(self.table)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 221, 172);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fio_label.setText(_translate("MainWindow", "Вы:"))
        self.groups_label.setText(_translate("MainWindow", "Ваша роль: администратор"))
        self.label_7.setText(_translate("MainWindow", "Таблица:"))
        self.add_button.setText(_translate("MainWindow", "Добавить строку"))
        self.delete_button.setText(_translate("MainWindow", "Удалить строки"))
        self.save_button.setText(_translate("MainWindow", "Сохранить"))
        self.exit_button.setText(_translate("MainWindow", "Выйти"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "Электронный дневник"))
