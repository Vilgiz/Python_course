from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton

class PaginationTable(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.table = QTableWidget(10, 10, self)
        self.create_table_data(1)  # Создаем данные для первой страницы

        # Кнопки для переключения страниц
        prev_button = QPushButton("Предыдущая страница", self)
        prev_button.clicked.connect(self.show_prev_page)

        next_button = QPushButton("Следующая страница", self)
        next_button.clicked.connect(self.show_next_page)

        self.layout.addWidget(self.table)
        self.layout.addWidget(prev_button)
        self.layout.addWidget(next_button)

        self.setLayout(self.layout)

    def create_table_data(self, page_number):
        # Здесь вы можете заполнить таблицу данными для конкретной страницы
        for i in range(10):
            for j in range(10):
                item = QTableWidgetItem(f"Строка {i + (page_number - 1) * 10}, столбец {j}")
                self.table.setItem(i, j, item)

    def show_prev_page(self):
        # Показываем предыдущую страницу
        print("Показываем предыдущую страницу")

    def show_next_page(self):
        # Показываем следующую страницу
        print("Показываем следующую страницу")

# Создаем приложение и отображаем окно с таблицей
app = QApplication([])
pagination_table = PaginationTable()
pagination_table.show()
app.exec()
