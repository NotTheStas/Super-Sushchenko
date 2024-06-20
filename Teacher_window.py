# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Teacher_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 651)
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
        self.subjects_label = QtWidgets.QLabel(self.centralwidget)
        self.subjects_label.setStyleSheet("color: rgb(255, 221, 172);")
        self.subjects_label.setObjectName("subjects_label")
        self.verticalLayout_3.addWidget(self.subjects_label)
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
        self.groups_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.groups_ComboBox.setStyleSheet("background-color: rgb(255, 221, 172);\n"
"color: rgb(31, 31, 147);")
        self.groups_ComboBox.setObjectName("groups_ComboBox")
        self.verticalLayout.addWidget(self.groups_ComboBox)
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
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("color: rgb(255, 221, 172);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setStyleSheet("color: rgb(250, 170, 120);")
        self.login_label.setObjectName("login_label")
        self.verticalLayout_6.addWidget(self.login_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setStyleSheet("color: rgb(255, 221, 172);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.login_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_lineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_lineEdit.sizePolicy().hasHeightForWidth())
        self.login_lineEdit.setSizePolicy(sizePolicy)
        self.login_lineEdit.setStyleSheet("background-color: rgb(255, 221, 172);\n"
"color: rgb(31, 31, 147);")
        self.login_lineEdit.setText("")
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.verticalLayout_5.addWidget(self.login_lineEdit)
        self.login_changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.login_changeButton.setStyleSheet("background-color: rgb(153, 72, 87);\n"
"color: rgb(255, 221, 172);")
        self.login_changeButton.setObjectName("login_changeButton")
        self.verticalLayout_5.addWidget(self.login_changeButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setStyleSheet("color: rgb(255, 221, 172);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setStyleSheet("color: rgb(250, 170, 120);")
        self.password_label.setObjectName("password_label")
        self.verticalLayout_8.addWidget(self.password_label)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setStyleSheet("color: rgb(255, 221, 172);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setStyleSheet("color: rgb(255, 221, 172);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.oldpass_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.oldpass_lineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldpass_lineEdit.sizePolicy().hasHeightForWidth())
        self.oldpass_lineEdit.setSizePolicy(sizePolicy)
        self.oldpass_lineEdit.setStyleSheet("background-color: rgb(255, 221, 172);\n"
"color: rgb(31, 31, 147);")
        self.oldpass_lineEdit.setText("")
        self.oldpass_lineEdit.setObjectName("oldpass_lineEdit")
        self.verticalLayout_7.addWidget(self.oldpass_lineEdit)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setStyleSheet("color: rgb(255, 221, 172);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_7.addWidget(self.label_16)
        self.newpass_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.newpass_lineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newpass_lineEdit.sizePolicy().hasHeightForWidth())
        self.newpass_lineEdit.setSizePolicy(sizePolicy)
        self.newpass_lineEdit.setStyleSheet("background-color: rgb(255, 221, 172);\n"
"color: rgb(31, 31, 147);")
        self.newpass_lineEdit.setText("")
        self.newpass_lineEdit.setObjectName("newpass_lineEdit")
        self.verticalLayout_7.addWidget(self.newpass_lineEdit)
        self.lab = QtWidgets.QLabel(self.centralwidget)
        self.lab.setStyleSheet("color: rgb(255, 0, 0);")
        self.lab.setText("")
        self.lab.setObjectName("lab")
        self.verticalLayout_7.addWidget(self.lab)
        self.pass_changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.pass_changeButton.setStyleSheet("background-color: rgb(153, 72, 87);\n"
"color: rgb(255, 221, 172);")
        self.pass_changeButton.setObjectName("pass_changeButton")
        self.verticalLayout_7.addWidget(self.pass_changeButton)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
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
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.MainTable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainTable.sizePolicy().hasHeightForWidth())
        self.MainTable.setSizePolicy(sizePolicy)
        self.MainTable.setStyleSheet("/* цвет заголовков столбцов и строк */\n"
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
        self.MainTable.setObjectName("MainTable")
        self.MainTable.setColumnCount(0)
        self.MainTable.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.MainTable)
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
        self.subjects_label.setText(_translate("MainWindow", "Ваши предметы:"))
        self.groups_label.setText(_translate("MainWindow", "Ваш группы:"))
        self.label_7.setText(_translate("MainWindow", "Группа:"))
        self.label_9.setText(_translate("MainWindow", "Ваш логин:"))
        self.login_label.setText(_translate("MainWindow", "Ilia"))
        self.label_13.setText(_translate("MainWindow", "Изменить логин:"))
        self.login_changeButton.setText(_translate("MainWindow", "Изменить"))
        self.label_12.setText(_translate("MainWindow", "Ваш пароль:"))
        self.password_label.setText(_translate("MainWindow", "***"))
        self.label_14.setText(_translate("MainWindow", "Изменить пароль:"))
        self.label_15.setText(_translate("MainWindow", "Старый пароль"))
        self.label_16.setText(_translate("MainWindow", "Новый пароль"))
        self.pass_changeButton.setText(_translate("MainWindow", "Изменить"))
        self.save_button.setText(_translate("MainWindow", "Сохранить"))
        self.exit_button.setText(_translate("MainWindow", "Выйти"))
        self.label_8.setText(_translate("MainWindow", "Электронный дневник"))