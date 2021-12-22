import psycopg2
import sys
from datetime import datetime, timedelta

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox)


def week_num():
    now = datetime.now()
    sep = datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)

    d1 = sep - timedelta(days=sep.weekday())
    d2 = now - timedelta(days=now.weekday())

    parity = ((d2 - d1).days // 7) % 2
    week = ("{}".format("down" if parity else "Up"))
    return week

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Shedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_monday_tab()
        self._create_tuesday_tab()
        self._create_wednesday_tab()
        self._create_thursday_tab()
        self._create_friday_tab()

    week = week_num()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="tg_tables",
                                     user="postgres",
                                     password="1234",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_monday_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Monday")

        self.monday_gbox = QGroupBox("Monday")

        self.svbox = QVBoxLayout()
        self.shbox_monday = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.adder = QHBoxLayout()

        self.svbox.addLayout(self.shbox_monday)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.adder)

        self.shbox_monday.addWidget(self.monday_gbox)

        self._create_monday_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.adder_button = QPushButton("Add")
        self.adder.addWidget(self.adder_button)
        self.adder_button.clicked.connect(lambda: self.adder_func("Понедельник"))

        self.shedule_tab.setLayout(self.svbox)

    def _create_tuesday_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Tuesday")

        self.tuesday_gbox = QGroupBox("Tuesday")

        self.svbox = QVBoxLayout()
        self.shbox_tuesday = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.adder = QHBoxLayout()

        self.svbox.addLayout(self.shbox_tuesday)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.adder)

        self.shbox_tuesday.addWidget(self.tuesday_gbox)

        self._create_tuesday_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.adder_button = QPushButton("Add")
        self.adder.addWidget(self.adder_button)
        self.adder_button.clicked.connect(lambda: self.adder_func("Вторник"))

        self.shedule_tab.setLayout(self.svbox)

    def _create_wednesday_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Wednesday")

        self.wednesday_gbox = QGroupBox("Wednesday")

        self.svbox = QVBoxLayout()
        self.shbox_wednesday = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.adder = QHBoxLayout()

        self.svbox.addLayout(self.shbox_wednesday)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.adder)

        self.shbox_wednesday.addWidget(self.wednesday_gbox)

        self._create_wednesday_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.adder_button = QPushButton("Add")
        self.adder.addWidget(self.adder_button)
        self.adder_button.clicked.connect(lambda: self.adder_func("Среда"))

        self.shedule_tab.setLayout(self.svbox)

    def _create_thursday_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Thursday")

        self.thursday_gbox = QGroupBox("Thursday")

        self.svbox = QVBoxLayout()
        self.shbox_thursday = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.adder = QHBoxLayout()

        self.svbox.addLayout(self.shbox_thursday)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.adder)

        self.shbox_thursday.addWidget(self.thursday_gbox)

        self._create_thursday_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.adder_button = QPushButton("Add")
        self.adder.addWidget(self.adder_button)
        self.adder_button.clicked.connect(lambda: self.adder_func("Четверг"))

        self.shedule_tab.setLayout(self.svbox)

    def _create_friday_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Friday")

        self.friday_gbox = QGroupBox("Friday")

        self.svbox = QVBoxLayout()
        self.shbox_friday = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.adder = QHBoxLayout()

        self.svbox.addLayout(self.shbox_friday)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.adder)

        self.shbox_friday.addWidget(self.friday_gbox)

        self._create_friday_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.adder_button = QPushButton("Add")
        self.adder.addWidget(self.adder_button)
        self.adder_button.clicked.connect(lambda: self.adder_func("Пятница"))

        self.shedule_tab.setLayout(self.svbox)


#ФУНКЦИИ СОЗДАНИЯ ТАБЛИЦ ДЛЯ КАЖДОГО ДНЯ


    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(4)
        self.monday_table.setHorizontalHeaderLabels(["Subject", "Time", "Join", "Delete"])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(4)
        self.tuesday_table.setHorizontalHeaderLabels(["Subject", "Time", "Join", "Delete"])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.mvbox)

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(4)
        self.wednesday_table.setHorizontalHeaderLabels(["Subject", "Time", "Join", "Delete"])

        self._update_wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.mvbox)

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(4)
        self.thursday_table.setHorizontalHeaderLabels(["Subject", "Time", "Join", "Delete"])

        self._update_thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.mvbox)

    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(4)
        self.friday_table.setHorizontalHeaderLabels(["Subject", "Time", "Join", "Delete"])

        self._update_friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.mvbox)


#ФУНКЦИИ ОБНОВЛЕНИЯ ТАБЛИЦ ДЛЯ КАЖДОГО ДНЯ


    def _update_monday_table(self):
        self.cursor.execute("SELECT * FROM tables.timetable WHERE day = '%s' AND week = '%s' OR day = '%s' AND week = 'Any'" % ('Понедельник', week_num(), 'Понедельник'))
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.monday_table.setCellWidget(i, 2, joinButton)
            self.monday_table.setCellWidget(i, 3, deleteButton)

            joinButton.clicked.connect(
                lambda: self._change_day_from_table(i, "Понедельник"))
            deleteButton.clicked.connect(
                lambda: self.deleter("Понедельник"))

    def _update_tuesday_table(self):
        self.cursor.execute("SELECT * FROM tables.timetable WHERE day = '%s' AND week = '%s' OR day = '%s' AND week = 'Any'" % ('Вторник', week_num(), 'Вторник'))
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.tuesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.tuesday_table.setCellWidget(i, 2, joinButton)
            self.tuesday_table.setCellWidget(i, 3, deleteButton)

            joinButton.clicked.connect(
                lambda: self._change_day_from_table(i, "Вторник"))
            deleteButton.clicked.connect(
                lambda: self.deleter("Вторник"))

    def _update_wednesday_table(self):
        self.cursor.execute("SELECT * FROM tables.timetable WHERE day = '%s' AND week = '%s' OR day = '%s' AND week = 'Any'" % ('Среда', week_num(), 'Среда'))
        records = list(self.cursor.fetchall())

        self.wednesday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.wednesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.wednesday_table.setCellWidget(i, 2, joinButton)
            self.wednesday_table.setCellWidget(i, 3, deleteButton)

            joinButton.clicked.connect(
                lambda: self._change_day_from_table(i, "Среда"))
            deleteButton.clicked.connect(
                lambda: self.deleter("Среда"))

    def _update_thursday_table(self):
        self.cursor.execute("SELECT * FROM tables.timetable WHERE day = '%s' AND week = '%s' OR day = '%s' AND week = 'Any'" % ('Четверг', week_num(), 'Четверг'))
        records = list(self.cursor.fetchall())

        self.thursday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.thursday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.thursday_table.setCellWidget(i, 2, joinButton)
            self.thursday_table.setCellWidget(i, 3, deleteButton)

            joinButton.clicked.connect(
                lambda: self._change_day_from_table(i, " Четверг"))
            deleteButton.clicked.connect(
                lambda: self.deleter("Четверг"))

    def _update_friday_table(self):
        self.cursor.execute("SELECT * FROM tables.timetable WHERE day = '%s' AND week = '%s' OR day = '%s' AND week = 'Any'" % ('Пятница', week_num(), 'Пятница'))
        records = list(self.cursor.fetchall())

        self.friday_table.setRowCount(len(records))

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.friday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.friday_table.setCellWidget(i, 2, joinButton)
            self.friday_table.setCellWidget(i, 3, deleteButton)

            joinButton.clicked.connect(
                lambda: self._change_day_from_table(i, " Пятница"))
            deleteButton.clicked.connect(
                lambda: self.deleter("Пятница"))


#ФУНКЦИЯ ИЗМЕНЕНИЯ ДНЯ В ТАБЛИЦЕ


    def _change_day_from_table(self, rowNum, day):
        row = list()
        self.cursor.execute("SELECT * FROM tables.timetable WHERE day = '%s' ORDER BY id" % (day))
        records = list(self.cursor.fetchall())
        if day == 'Понедельник':
            for j in range(rowNum + 1):
                for i in range(self.monday_table.columnCount()):
                    try:
                        row.append(self.monday_table.item(j, i).text())
                    except:
                        row.append(None)
                try:
                    self.cursor.execute("UPDATE tables.timetable SET subject = '%s', start_time = '%s' WHERE id = '%s'" % (str(row[0]), str(row[1]), int(records[j][0])))
                    self.conn.commit()
                except:
                    self.cursor.execute("rollback")
                    QMessageBox.about(self, 'Error', 'Enter all fields')
                    break
                row = []
        elif day == 'Вторник':
            for j in range(rowNum + 1):
                for i in range(self.tuesday_table.columnCount()):
                    try:
                        row.append(self.tuesday_table.item(j, i).text())
                    except:
                        row.append(None)
                try:
                    self.cursor.execute("UPDATE tables.timetable SET subject = '%s', start_time = '%s' WHERE id = '%s'" % (str(row[0]), str(row[1]), int(records[j][0])))
                    self.conn.commit()
                except:
                    self.cursor.execute("rollback")
                    QMessageBox.about(self, 'Error', 'Enter all fields')
                    break
                row = []
        elif day == 'Среда':
            for j in range(rowNum + 1):
                for i in range(self.wednesday_table.columnCount()):
                    try:
                        row.append(self.wednesday_table.item(j, i).text())
                    except:
                        row.append(None)
                try:
                    self.cursor.execute("UPDATE tables.timetable SET subject = '%s', start_time = '%s' WHERE id = '%s'" % (str(row[0]), str(row[1]), int(records[j][0])))
                    self.conn.commit()
                except:
                    self.cursor.execute("rollback")
                    QMessageBox.about(self, 'Error', 'Enter all fields')
                    break
                row = []
        elif day == 'Четверг':
            for j in range(rowNum + 1):
                for i in range(self.thursday_table.columnCount()):
                    try:
                        row.append(self.thursday_table.item(j, i).text())
                    except:
                        row.append(None)
                try:
                    self.cursor.execute("UPDATE tables.timetable SET subject = '%s', start_time = '%s' WHERE id = '%s'" % (str(row[0]), str(row[1]), int(records[j][0])))
                    self.conn.commit()
                except:
                    self.cursor.execute("rollback")
                    QMessageBox.about(self, 'Error', 'Enter all fields')
                    break
                row = []
        elif day == 'Пятница':
            for j in range(rowNum + 1):
                for i in range(self.friday_table.columnCount()):
                    try:
                        row.append(self.thursday_table.item(j, i).text())
                    except:
                        row.append(None)
                try:
                    self.cursor.execute("UPDATE tables.timetable SET subject = '%s', start_time = '%s' WHERE id = '%s'" % (str(row[0]), str(row[1]), int(records[j][0])))
                    self.conn.commit()
                except:
                    self.cursor.execute("rollback")
                    QMessageBox.about(self, 'Error', 'Enter all fields')
                    break
                row = []

    def deleter(self, day):
        self.cursor.execute("SELECT * FROM tables.timetable WHERE day = '%s' ORDER BY id" % (day))
        records = list(self.cursor.fetchall())
        print("Расписание на %s" % (day))
        for i in records:
            print(i[2], i[4])
        print("Введите предмет, который хотите удалить:")
        sub = input()
        print("Введите время:")
        time = input()
        try:
            self.cursor.execute("DELETE FROM tables.timetable WHERE day = '%s' AND subject = '%s' AND start_time = '%s'" % (day, sub, time))
            self.conn.commit()
        except:
            self.cursor.execute("rollback")
            QMessageBox.about(self, 'Error', 'Такого нет в расписании')


#ФУНКЦИИ ДЛЯ ДРУГИХ ФУНКЦИЙ


    def _update_shedule(self):
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()

    def adder_func(self, day):
        print('Введите предмет, который хотите добавить:')
        sub = input()
        print('Введите кабинет')
        room_numb = input()
        print('Введите время начала')
        time = input()
        print('Введите неделю Up, down, Any')
        week = input()
        try:
            self.cursor.execute(
                "INSERT INTO tables.timetable (day, subject, room_numb, start_time, week) VALUES ('%s', '%s', '%s', '%s', '%s')" % (day, sub, room_numb, time, week))
            self.conn.commit()
        except:
            self.cursor.execute("rollback")
            QMessageBox.about(self, 'Error', 'Такое нельзя добавить')


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())