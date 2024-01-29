from PyQt6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Pagination Example")
        self.setGeometry(100, 100, 400, 300)
        
        # Создаем прокручиваемую область
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        # Создаем виджет для таблицы
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        
        # Заполняем таблицу данными
        self.data = []
        for i in range(100):
            self.data.append([f"Row {i+1}", f"Value {i+1}-1", f"Value {i+1}-2"])
        
        self.current_page = 1
        self.items_per_page = 20
        self.total_pages = (len(self.data) + self.items_per_page - 1) // self.items_per_page
        
        self.update_table()
        
        # Размещаем таблицу в прокручиваемой области
        scroll_area.setWidget(self.table_widget)
        
        # Размещаем прокручиваемую область на главном виджете
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # Создаем кнопки для навигации по страницам
        prev_button = QPushButton("Previous")
        prev_button.clicked.connect(self.go_to_previous_page)
        main_layout.addWidget(prev_button)
        
        next_button = QPushButton("Next")
        next_button.clicked.connect(self.go_to_next_page)
        main_layout.addWidget(next_button)
        
    def update_table(self):
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        visible_data = self.data[start_index:end_index]
        
        self.table_widget.setRowCount(len(visible_data))
        for row, rowData in enumerate(visible_data):
            for col, value in enumerate(rowData):
                self.table_widget.setItem(row, col, QTableWidgetItem(value))
        
    def go_to_previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_table()
        
    def go_to_next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_table()

# Создаем приложение и запускаем главное окно
app = QApplication([])
window = MainWindow()
window.show()
app.exec()