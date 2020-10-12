import sys
import os
from PyQt5.QtWidgets import QTableView, QApplication, QWidget, QPushButton, QMainWindow, QAction, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery, QSqlRelationalTableModel, QSqlRelation, \
    QSqlRelationalDelegate
from main_window import Ui_MainWindow


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.db_path = r'database\sklad_db.sqlite3'
        self.ui.path_db.setText(self.db_path)

        self.save_db = QAction(QIcon('icon/save.png'), 'Сохранить', self)
        self.find_db_file = QAction(QIcon('icon/open_db.png'), 'Открыть БД', self)
        self.add_rec = QAction(QIcon('icon/add.png'), 'Добавить запись', self)
        self.del_rec = QAction(QIcon('icon/del.png'), 'Удалить запись', self)
        self.ui.toolBar.addAction(self.save_db)
        self.ui.toolBar.addAction(self.find_db_file)
        self.ui.toolBar.addAction(self.add_rec)
        self.ui.toolBar.addAction(self.del_rec)
        self.db = None
        self.table_model = None

        self.open_db()

        self.add_rec.triggered.connect(self.add_record_action)
        self.del_rec.triggered.connect(self.del_record_action)
        self.save_db.triggered.connect(self.save_change_db)
        self.find_db_file.triggered.connect(self.find_db_file_action)
        self.ui.comboBox.currentIndexChanged.connect(self.show_table)

    def open_db(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.db_path)
        self.db.open()
        self.get_table_name()
        self.show_table()

    def get_table_name(self):
        self.ui.comboBox.clear()
        table_name_ru = None
        for table_name in self.db.tables():
            if table_name == 'goods':
                table_name_ru = 'Товары'
            elif table_name == 'categories':
                table_name_ru = 'Категории'
            elif table_name == 'units':
                table_name_ru = 'Единица измерения'
            elif table_name == 'employees':
                table_name_ru = 'Персонал'
            elif table_name == 'positions':
                table_name_ru = 'Должности'
            elif table_name == 'vendors':
                table_name_ru = 'Поставщики'
            self.ui.comboBox.addItem(table_name_ru)

    def show_table(self):
        self.table_model = QSqlRelationalTableModel()
        table = self.ui.comboBox.currentText()
        if table == 'Товары':
            self.create_goods_table_model()
        elif table == 'Персонал':
            self.create_employees_table_model()
        else:
            if table == 'Единица измерения':
                table = 'units'
            elif table == 'Категории':
                table = 'categories'
            elif table == 'Должности':
                table = 'positions'
            elif table == 'Поставщики':
                table = 'vendors'
            self.table_model.setTable(table)
            self.table_model.select()
        self.table_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        view = self.ui.tableView
        view.setModel(self.table_model)
        view.setItemDelegate(QSqlRelationalDelegate(view))

    def create_goods_table_model(self):
        self.table_model.setTable('goods')
        self.table_model.setRelation(2, QSqlRelation('units', 'unit_id', 'unit'))
        self.table_model.setRelation(3, QSqlRelation('categories', 'category_id', 'category_name'))
        self.table_model.select()

    def create_employees_table_model(self):
        self.table_model.setTable('employees')
        self.table_model.setRelation(2, QSqlRelation('positions', 'position_id', 'position'))
        self.table_model.select()

    def add_record_action(self):
        self.ui.statusbar.clearMessage()
        self.table_model.insertRows(self.table_model.rowCount(), 1)

    def del_record_action(self):
        self.ui.statusbar.clearMessage()
        rs = list(map(lambda x: x.row(), self.ui.tableView.selectedIndexes()))
        #print(rs)
        for i in rs:
            self.table_model.removeRows(i, 1)

    def find_db_file_action(self):
        self.db_path = QFileDialog.getOpenFileName(self, "Open file")[0]
        self.ui.path_db.setText(self.db_path)
        self.db.close()
        self.open_db()

    def save_change_db(self):
        if self.table_model.submitAll():
            self.ui.statusbar.showMessage('Изменения сохранены')
        else:
            self.ui.statusbar.showMessage(f'{self.table_model.lastError().text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MyWindow()
    wnd.show()
    sys.exit(app.exec())
