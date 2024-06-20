import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from Login_window import Ui_Pass
from Admin_window import Ui_MainWindow
from Teacher_window import Ui_Teacher_window
from Student_window import Ui_MainWindow1

# Окно Входа
class LoginWindow(QMainWindow, Ui_Pass):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.label_wrong_answer = QLabel(self)
        self.label_wrong_answer.move(178, 330)
        self.login_button.clicked.connect(self.pushed)

    def pushed(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        self.check = cur.execute("""select * from accounts""").fetchall()
        con.close()

        global FIO, log, password_stud, ident

        for self.request in self.check:
            if self.login_line.text() == self.request[4] and self.pass_line.text() == self.request[5]:
                window.hide()

                if self.request[6] == 3:
                    ident = self.request[0]
                    self.window2 = AdminWindow()
                    self.window2.show()

                elif self.request[6] == 2:
                    ident = self.request[0]
                    password_stud = self.request[5]
                    self.window2 = TeacherWindow()
                    self.window2.show()

                else:
                    ident = self.request[0]
                    FIO = " " + self.request[1] + " " + self.request[2] + " " + self.request[3]
                    log = " " + self.request[4]
                    password_stud = self.request[5]
                    self.window2 = StudentWindow()
                    self.window2.show()


        self.label_wrong_answer.setText("Неправильный пароль или логин")
        self.label_wrong_answer.adjustSize()
        self.label_wrong_answer.setStyleSheet("color: red")

# Окно Админа
class AdminWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(AdminWindow, self).__init__()
        self.setupUi(self)
        self.ComboBox.addItem("Пользователи")
        self.ComboBox.addItem("Группы")
        self.ComboBox.addItem("Предметы")
        self.ComboBox.addItem("Группы и предметы")
        self.ComboBox.addItem("Преподаватели")
        self.ComboBox.addItem("Студенты")

        con = sqlite3.connect("database.db")
        cur = con.cursor()
        fio = cur.execute(f"""select name, lastname, surname, login, password from accounts WHERE id == {ident}""").fetchall()[0]
        self.fio_label.setText(self.fio_label.text() + " " + fio[0] + " " + fio[1] + " " + fio[2])
        con.close()

        self.users_table()
        self.ComboBox.currentTextChanged.connect(self.choose)
        self.add_button.clicked.connect(self.add_row)
        self.exit_button.clicked.connect(self.pushed_ex)
        self.save_button.clicked.connect(self.save_data)
        self.delete_button.clicked.connect(self.delete_rows)

    # Выбор Таблицы
    def choose(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.blockSignals(True)

        if self.ComboBox.currentText() == "Преподаватели":
            self.teacher_table()

        if self.ComboBox.currentText() == "Группы":
            self.groups_table()

        if self.ComboBox.currentText() == "Предметы":
            self.subjects_table()

        if self.ComboBox.currentText() == "Группы и предметы":
            self.subjects_and_groups_table()

        if self.ComboBox.currentText() == "Пользователи":
            self.users_table()

        if self.ComboBox.currentText() == "Студенты":
            self.students_table()

    # Таблица Учителей
    def teacher_table(self):
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["id", "ФИО", "group_id", "subject_id", "group_name", "subject_name"])

        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        sqlquery = cur.execute("""
            SELECT accounts.id, accounts.name || ' ' || accounts.lastname || ' ' || accounts.surname AS full_name, 
                   teacher_assignments.group_id, teacher_assignments.subject_id, 
                   groups.group_name, subjects.subject_name
            FROM accounts
            INNER JOIN teacher_assignments ON accounts.id = teacher_assignments.teacher_id
            INNER JOIN groups ON teacher_assignments.group_id = groups.id
            INNER JOIN subjects ON teacher_assignments.subject_id = subjects.id
        """).fetchall()



        tableIndex = 0
        for row in sqlquery:
            self.table.setRowCount(self.table.rowCount() + 1)

            self.table.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))

            full_name_item = QtWidgets.QTableWidgetItem(row[1])
            full_name_item.setFlags(full_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 1, full_name_item)

            self.table.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.table.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(str(row[3])))

            group_name_item = QtWidgets.QTableWidgetItem(row[4])
            group_name_item.setFlags(group_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 4, group_name_item)

            subject_name_item = QtWidgets.QTableWidgetItem(row[5])
            subject_name_item.setFlags(subject_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 5, subject_name_item)

            tableIndex += 1

        self.table.resizeColumnsToContents()

        try:
            self.table.cellChanged.disconnect(self.cell_changed_SaG)
        except:
            pass

        self.table.cellChanged.connect(self.handle_cell_changed)
        self.table.blockSignals(False)
        connection.close()

    def handle_cell_changed(self, row, column):
        if column == 0:
            self.update_teacher_name(row, column)
        elif column in [2, 3]:
            self.update_group_subject_names(row, column, 2, 3, 4, 5)

    def users_table(self):
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["id", "Имя", "Фамилия", "Отчество", "Логин", "Пароль", "Роль"])

        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        sqlquery = cur.execute("""select * from accounts""").fetchall()

        tableIndex = 0
        for row in sqlquery:
            self.table.setRowCount(self.table.rowCount() + 1)
            id_item = QtWidgets.QTableWidgetItem(str(row[0]))
            id_item.setFlags(id_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 0, id_item)
            self.table.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.table.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.table.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.table.setItem(tableIndex, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.table.setItem(tableIndex, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.table.setItem(tableIndex, 6, QtWidgets.QTableWidgetItem(str(row[6])))

            tableIndex += 1

        self.table.resizeColumnsToContents()
        connection.close()

    def students_table(self):

        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["id", "ФИО", "group_id", "group_name"])

        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        sqlquery = cur.execute("""SELECT accounts.id, accounts.name || ' ' || accounts.lastname || ' ' || accounts.surname AS full_name, groups.id AS group_id, groups.group_name FROM accounts
        INNER JOIN student_groups ON student_groups.account_id = accounts.id
        INNER JOIN groups ON student_groups.group_id = groups.id""").fetchall()

        tableIndex = 0
        for row in sqlquery:
            self.table.setRowCount(self.table.rowCount() + 1)

            self.table.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))

            fio = QtWidgets.QTableWidgetItem(row[1])
            fio.setFlags(fio.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 1, fio)

            self.table.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(str(row[2])))

            group_name = QtWidgets.QTableWidgetItem(row[3])
            group_name.setFlags(group_name.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 3, group_name)

            tableIndex += 1

        self.table.resizeColumnsToContents()
        self.table.cellChanged.connect(self.cell_changed_Students)
        self.table.blockSignals(False)
        connection.close()

    def cell_changed_Students(self, row, column):
        if column == 0:
            self.update_teacher_name(row, column)
        if column == 2:
            self.update_student_group(row, column)

    def groups_table(self):

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["id", "group_name"])

        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        sqlquery = cur.execute("""SELECT id, group_name from groups""").fetchall()

        tableIndex = 0
        for row in sqlquery:
            self.table.setRowCount(self.table.rowCount() + 1)
            id_item = QtWidgets.QTableWidgetItem(str(row[0]))
            id_item.setFlags(id_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 0, id_item)
            self.table.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(row[1]))

            tableIndex += 1

        self.table.resizeColumnsToContents()
        connection.close()

    def subjects_table(self):

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["id", "subject_name"])

        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        sqlquery = cur.execute("""SELECT id, subject_name from subjects""").fetchall()

        tableIndex = 0
        for row in sqlquery:
            self.table.setRowCount(self.table.rowCount() + 1)
            id_item = QtWidgets.QTableWidgetItem(str(row[0]))
            id_item.setFlags(id_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 0, id_item)
            self.table.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(row[1]))

            tableIndex += 1

        self.table.resizeColumnsToContents()
        connection.close()

    # Таблица предметов и групп
    def subjects_and_groups_table(self):

        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["group_id", "subject_id", "group_name", "subject_name"])

        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        sqlquery = cur.execute("""SELECT gs.group_id, gs.subject_id, g.group_name, s.subject_name FROM group_subjects gs
        JOIN groups g ON gs.group_id = g.id
        JOIN subjects s ON gs.subject_id = s.id
        ORDER BY gs.group_id, gs.subject_id;""").fetchall()

        tableIndex = 0
        for row in sqlquery:
            self.table.setRowCount(self.table.rowCount() + 1)
            self.table.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.table.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(str(row[1])))

            group_name_item = QtWidgets.QTableWidgetItem(str(row[2]))
            group_name_item.setFlags(group_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 2, group_name_item)

            subject_name_item = QtWidgets.QTableWidgetItem(str(row[3]))
            subject_name_item.setFlags(subject_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.table.setItem(tableIndex, 3, subject_name_item)

            tableIndex += 1

        self.table.resizeColumnsToContents()
        try:
            self.table.cellChanged.disconnect(self.handle_cell_changed)
        except:
            pass
        self.table.cellChanged.connect(self.cell_changed_SaG)
        self.table.blockSignals(False)
        connection.close()

    def cell_changed_SaG(self, row, col):
        self.update_group_subject_names(row, col, 0, 1, 2, 3)

    # Функция, читает 2 столбца group_id и subject_id и выводит их названия
    def update_group_subject_names(self, row, column, group_id_col, subject_id_col, group_name_col, subject_name_col):
        if column in [group_id_col, subject_id_col]:
            group_id_item = self.table.item(row, group_id_col)
            subject_id_item = self.table.item(row, subject_id_col)
            if group_id_item is None or subject_id_item is None:
                self.show_error_dialog("Должны быть указаны как group_id, так и subject_id.")
                return

            group_id = group_id_item.text().strip()
            subject_id = subject_id_item.text().strip()
            if not group_id or not subject_id:
                self.show_error_dialog("Должны быть указаны как group_id, так и subject_id.")
                return

            connection = sqlite3.connect("database.db")
            cur = connection.cursor()
            cur.execute("SELECT group_name FROM groups WHERE id = ?", (group_id,))
            group_name_result = cur.fetchone()
            cur.execute("SELECT subject_name FROM subjects WHERE id = ?", (subject_id,))
            subject_name_result = cur.fetchone()

            if group_name_result and subject_name_result:
                group_name = group_name_result[0]
                subject_name = subject_name_result[0]
                group_name_item = QtWidgets.QTableWidgetItem(group_name)
                group_name_item.setFlags(group_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.table.setItem(row, group_name_col, group_name_item)

                subject_name_item = QtWidgets.QTableWidgetItem(subject_name)
                subject_name_item.setFlags(subject_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.table.setItem(row, subject_name_col, subject_name_item)
            else:
                self.table.blockSignals(True)
                group_id_item.setText("")
                subject_id_item.setText("")
                self.table.blockSignals(False)
                self.show_error_dialog("Неверные данные указаны в group_id или subject_id.")

            connection.close()

    # Функция, читает id и выводит ФИО
    def update_teacher_name(self, row, column):
        if column == 0:
            self.table.blockSignals(True)
            id_item = self.table.item(row, 0)

            if id_item is None:
                self.show_error_dialog("Необходимо указать id учителя.")
                return

            teacher_id = id_item.text().strip()

            if not teacher_id:
                self.show_error_dialog("Необходимо указать id учителя.")
                return

            connection = sqlite3.connect("database.db")
            cur = connection.cursor()

            cur.execute("SELECT name || ' ' || lastname || ' ' || surname AS full_name FROM accounts WHERE id = ?",
                        (teacher_id,))
            full_name_result = cur.fetchone()

            if full_name_result:
                full_name = full_name_result[0]
                full_name_item = QtWidgets.QTableWidgetItem(full_name)
                full_name_item.setFlags(full_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.table.setItem(row, 1, full_name_item)
            else:
                self.show_error_dialog("Неверные данные указаны в id учителя.")

            self.table.blockSignals(False)
            connection.close()

    # Функция, читает group_id, выводит название
    def update_student_group(self, row, column):
        if column == 2:
            group_id_item = self.table.item(row, column)
            group_id = group_id_item.text()
            connection = sqlite3.connect("database.db")
            cur = connection.cursor()
            group_name_result = cur.execute("SELECT group_name FROM groups WHERE id = ?", (group_id,)).fetchone()

            if group_name_result:
                group_name = group_name_result[0]
                group_name_item = QtWidgets.QTableWidgetItem(group_name)
                group_name_item.setFlags(group_name_item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.table.setItem(row, 3, group_name_item)
            else:
                self.table.blockSignals(True)
                self.table.currentItem().setText("")
                self.table.blockSignals(False)
                self.show_error_dialog("Неверные данные указаны в group_id")
            connection.close()

    def add_row(self):
        self.table.setRowCount(self.table.rowCount() + 1)

    def pushed_ex(self):
        self.close()

    # Удаляет ВЫБРАННЫЕ стобцы
    def delete_rows(self):
        selected_rows = list(set(index.row() for index in self.table.selectedIndexes()))

        if not selected_rows:
            self.show_error_dialog("Пожалуйста, выберите строки для удаления.")
            return

        reply = QtWidgets.QMessageBox.question(self, 'Удаление',
                                               f"Вы уверены, что хотите удалить {len(selected_rows)} строк(и)?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            connection = sqlite3.connect("database.db")
            cur = connection.cursor()

            for row in sorted(selected_rows, reverse=True):
                id_item = self.table.item(row, 0)
                if id_item:
                    record_id = id_item.text()
                    self.table.removeRow(row)

                    if self.ComboBox.currentText() == "Пользователи":
                        cur.execute("DELETE FROM accounts WHERE id = ?", (record_id,))
                    elif self.ComboBox.currentText() == "Группы":
                        cur.execute("DELETE FROM groups WHERE id = ?", (record_id,))
                    elif self.ComboBox.currentText() == "Предметы":
                        cur.execute("DELETE FROM subjects WHERE id = ?", (record_id,))
                    elif self.ComboBox.currentText() == "Группы и предметы":
                        group_id_item = self.table.item(row, 0)
                        subject_id_item = self.table.item(row, 1)
                        if group_id_item and subject_id_item:
                            group_id = group_id_item.text()
                            subject_id = subject_id_item.text()
                            cur.execute("DELETE FROM group_subjects WHERE group_id = ? AND subject_id = ?",
                                        (group_id, subject_id))
                    elif self.ComboBox.currentText() == "Преподаватели":
                        cur.execute("DELETE FROM teacher_assignments WHERE teacher_id = ?", (record_id,))
                    elif self.ComboBox.currentText() == "Студенты":
                        cur.execute("DELETE FROM student_groups WHERE account_id = ?", (record_id,))

            connection.commit()
            connection.close()

    # Сохранение (2 функции)
    def save_data(self):
        current_table = self.ComboBox.currentText()
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()

        if current_table == "Преподаватели":
            self.save_table_data(cur, "teacher_assignments", ["teacher_id", "group_id", "subject_id"], [0, 2, 3])
        elif current_table == "Группы":
            self.save_table_data(cur, "groups", ["id", "group_name"], [0, 1])
        elif current_table == "Предметы":
            self.save_table_data(cur, "subjects", ["id", "subject_name"], [0, 1])
        elif current_table == "Группы и предметы":
            self.save_table_data(cur, "group_subjects", ["group_id", "subject_id"], [0, 1])
        elif current_table == "Пользователи":
            self.save_table_data(cur, "accounts",
                                 ["id", "name", "lastname", "surname", "login", "password", "role"],
                                 [0, 1, 2, 3, 4, 5, 6])
        elif current_table == "Студенты":
            self.save_table_data(cur, "student_groups", ["account_id", "group_id"], [0, 2])

        connection.commit()
        self.show_info_dialog("Данные успешно сохранены.")
        connection.close()

    def save_table_data(self, cursor, table_name, columns, column_indices):
        for row in range(self.table.rowCount()):
            values = []
            for col_idx in column_indices:
                item = self.table.item(row, col_idx)
                if item is None or not item.text().strip():
                    print(item, item.text().strip())
                    self.show_error_dialog(f"Ошибка в строке {row + 1}: все поля должны быть заполнены.")
                    return
                values.append(item.text().strip())

            placeholders = ", ".join("?" for _ in columns)
            columns_str = ", ".join(columns)
            cursor.execute(f"""
                INSERT OR REPLACE INTO {table_name} ({columns_str})
                VALUES ({placeholders})
            """, values)

    # Диалоговые окна
    def show_error_dialog(self, message):
        error_dialog = QtWidgets.QMessageBox(self)
        error_dialog.setIcon(QtWidgets.QMessageBox.Warning)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Предупреждение")
        error_dialog.exec_()

    def show_info_dialog(self, message):
        info_dialog = QtWidgets.QMessageBox(self)
        info_dialog.setIcon(QtWidgets.QMessageBox.Information)
        info_dialog.setText(message)
        info_dialog.setWindowTitle("Информация")
        info_dialog.exec_()

# Окно Учителя
class TeacherWindow(QMainWindow, Ui_Teacher_window):
    def __init__(self):
        super(TeacherWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Электронный дневник')
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        fio = cur.execute(f"""select name, lastname, surname, login, password from accounts WHERE id == {ident}""").fetchall()[0]

        teacher_info = cur.execute(f"""SELECT g.group_name, s.subject_name, group_id
        FROM teacher_assignments ta
        JOIN groups g ON ta.group_id = g.id
        JOIN subjects s ON ta.subject_id = s.id
        WHERE ta.teacher_id = {ident}""").fetchall()

        con.close()

        self.fio_label.setText(self.fio_label.text() + " " + fio[0] + " " + fio[1] + " " + fio[2])
        self.login_label.setText(fio[3])

        self.password_label.setText(len(fio[4]) * "*")

        self.label_9.hide()
        self.login_label.hide()
        self.label_13.hide()
        self.login_lineEdit.hide()
        self.login_changeButton.hide()

        groups = []
        subjects = []
        for info in teacher_info:
            if info[0] not in groups:
                groups.append(info[0])
            if info[1] not in subjects:
                subjects.append(info[1])

        self.groups_label.setText(self.groups_label.text() + " " + ", ".join(groups))
        self.subjects_label.setText(self.subjects_label.text() + " " + ", ".join(subjects))
        self.groups_ComboBox.addItems(groups)
        self.groups_ComboBox.currentTextChanged.connect(self.grade_update)
        self.pass_changeButton.clicked.connect(self.save_password)
        self.exit_button.clicked.connect(self.pushed_exit_button)
        self.save_button.clicked.connect(self.save_grades)
        self.grade_update()

    def save_grades(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        for row in range(self.MainTable.rowCount()):
            student_name = self.MainTable.item(row, 0).text()
            name, lastname, surname = student_name.split(" ")
            student_id = cur.execute(f"""SELECT id FROM accounts WHERE (name = '{name}' AND lastname = '{lastname}' AND surname = '{surname}')""").fetchall()[0][0]

            for col in range(1, self.MainTable.columnCount()):
                subject_name = self.MainTable.horizontalHeaderItem(col).text()
                subject_id = cur.execute(f"""SELECT id FROM subjects WHERE subject_name = '{subject_name}'""").fetchall()[0][0]
                grade_item = self.MainTable.item(row, col)

                if grade_item is not None:
                    new_grade = grade_item.text()
                else:
                    new_grade = ""

                cur.execute(f"""UPDATE grades SET final_grade = '{new_grade}' WHERE (student_id = {student_id} AND subject_id = {subject_id})""")

        con.commit()
        con.close()

    def grade_update(self):

        select_group = self.groups_ComboBox.currentText()

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        select_group_id = cur.execute(f"""SELECT id FROM groups WHERE group_name = '{select_group}'""").fetchall()[0][0]

        subjects = [item[0] for item in cur.execute(f"""SELECT s.subject_name
        FROM teacher_assignments ta
        JOIN subjects s ON ta.subject_id = s.id
        JOIN groups g ON ta.group_id = g.id
        WHERE ta.teacher_id = {ident} AND g.group_name = '{select_group}'""").fetchall()]

        grades = cur.execute(f"""SELECT a.id, a.name, a.lastname, a.surname, s.subject_name, gr.final_grade
        FROM grades gr
        JOIN accounts a ON gr.student_id = a.id
        JOIN subjects s ON gr.subject_id = s.id
        JOIN groups g ON gr.group_id = g.id
        WHERE gr.group_id = {select_group_id}""").fetchall()

        con.close()

        self.MainTable.setColumnCount(len(subjects) + 1)
        self.MainTable.setHorizontalHeaderLabels(["ФИО"] + subjects)

        students_grades = {}
        for grade in grades:
            student_id = grade[0]
            student_name = f"{grade[1]} {grade[2]} {grade[3]}"
            subject_name = grade[4]
            final_grade = grade[5]

            if student_id not in students_grades:
                students_grades[student_id] = {
                    "name": student_name,
                    "grades": {subject: "" for subject in subjects}
                }
            students_grades[student_id]["grades"][subject_name] = final_grade

        self.MainTable.setRowCount(len(students_grades))
        self.MainTable.resizeColumnsToContents()

        row_index = 0
        for student_id, student_info in students_grades.items():
            self.MainTable.setItem(row_index, 0, QTableWidgetItem(student_info["name"]))
            item = self.MainTable.item(row_index, 0)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)

            col_index = 1
            for subject in subjects:
                grade = student_info["grades"].get(subject, "")
                self.MainTable.setItem(row_index, col_index, QTableWidgetItem(str(grade)))
                col_index += 1
            row_index += 1

    def save_password(self):
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()

        sql_update_query = """select password from accounts where id = ?"""
        data = (str(ident))
        password_stud = cur.execute(sql_update_query, data).fetchall()[0][0]

        if self.oldpass_lineEdit.text() == "" or self.newpass_lineEdit.text() == "":
            self.lab.setText("Введите пароль")

        elif password_stud != self.oldpass_lineEdit.text():
            self.lab.setText("Введён неправильный пароль")

        elif password_stud == self.oldpass_lineEdit.text():
            sql_update_query = """update accounts set password = ? where id = ?"""
            data = (str(self.newpass_lineEdit.text()), ident)
            cur.execute(sql_update_query, data)
            self.lab.setText("Пароль успешно изменён")

        connection.commit()
        connection.close()
        self.lab.adjustSize()

    def pushed_exit_button(self):
        self.close()

# Окно Студента
class StudentWindow(QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super(StudentWindow, self).__init__()
        self.setupUi(self)

        self.student_table.setRowCount(0)
        self.student_table.setColumnCount(2)
        self.student_table.setHorizontalHeaderLabels(["Предмет", "Оценка"])

        connection = sqlite3.connect("database.db")
        cur = connection.cursor()

        student_info = cur.execute(("""select subjects.subject_name, grades.final_grade
        from subjects inner join grades
        on subjects.id = grades.subject_id
        where grades.student_id = ?
        """), str(ident)).fetchall()

        tableIndex = 0
        for row in student_info:
            self.student_table.setRowCount(self.student_table.rowCount() + 1)
            self.student_table.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.student_table.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(str(row[1])))

            tableIndex += 1

        connection.close()

        self.fullname.setText("Вы:" + FIO)
        self.group.setText("Ваш логин:" + log)


        self.save_button.clicked.connect(self.save_password)
        self.exit_button.clicked.connect(self.pushed_exit_button)

        self.lab = QLabel(self)
        self.lab.move(60, 470)
        self.lab.setStyleSheet("color: red")

    def save_password(self):
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()

        sql_update_query = """select password from accounts where id = ?"""
        data = (str(ident))
        pas = cur.execute(sql_update_query, data).fetchall()[0][0]

        if self.lineEdit_2.text() == "" or self.lineEdit.text() == "":
            self.lab.setText("Введите пароль")

        elif pas != self.lineEdit_2.text():
            self.lab.setText("Введён неправильный пароль")

        elif pas == self.lineEdit_2.text():
            sql_update_query = """update accounts set password = ? where id = ?"""
            data = (str(self.lineEdit.text()), ident)
            cur.execute(sql_update_query, data)
            self.lab.setText("Пароль успешно изменён")

        connection.commit()
        connection.close()
        self.lab.adjustSize()

    def pushed_exit_button(self):
        self.close()



app = QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec())