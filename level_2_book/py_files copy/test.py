import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QListWidget


class SearchDeleteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('جستجو و حذف کتاب از دیتابیس')

        self.search_label = QLabel('کلمه جستجو:', self)
        self.search_entry = QLineEdit(self)
        self.search_button = QPushButton('جستجو', self)
        self.results_list = QListWidget(self)
        self.delete_button = QPushButton('حذف انتخاب شده', self)
        self.results_text = QTextEdit(self)
        self.results_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_entry)
        layout.addWidget(self.search_button)
        layout.addWidget(self.results_list)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.results_text)

        self.setLayout(layout)

        self.search_button.clicked.connect(self.search_database)
        self.delete_button.clicked.connect(self.delete_from_database)

    def search_database(self):
        search_term = self.search_entry.text()
        conn = sqlite3.connect('db_files\\book_database.db')
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT title FROM Books
            WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ? OR year_published LIKE ?
        """, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        results = cursor.fetchall()
        conn.close()

        self.results_list.clear()
        for row in results:
            self.results_list.addItem(row[0])

    def delete_from_database(self):
        selected_item = self.results_list.currentItem()
        if selected_item:
            delete_title = selected_item.text()
            conn = sqlite3.connect('db_files\\book_database.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Books WHERE title = ?",
                           (delete_title,))
            if cursor.rowcount == 0:
                self.results_text.setText("کتاب با این عنوان یافت نشد.")
            else:
                conn.commit()
                self.results_text.setText("کتاب با موفقیت حذف شد.")
            conn.close()
            self.results_list.takeItem(self.results_list.row(selected_item))
        else:
            self.results_text.setText("هیچ کتابی انتخاب نشده است.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SearchDeleteApp()
    ex.show()  # نمایش پنجره اصلی
    sys.exit(app.exec_())  # اجرای حلقه اصلی برنامه
