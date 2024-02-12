from PyQt6 import QtCore
import sys
from PyQt6.QtWidgets import QApplication, QTableWidget, QPushButton, QWidget, QHBoxLayout, QListWidget
from PyQt6.QtWidgets import QTextEdit, QMessageBox, QSpinBox, QLineEdit ,QTableWidgetItem, QHeaderView
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QMainWindow, QLabel
from Sorting import Sorter
import json
import re

class NameInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Введите ваше имя:")
        self.last_name_label = QLabel("Введите вашу фамилию:")

        self.name_input = QLineEdit()
        self.last_name_input = QLineEdit()

        self.confirm_button = QPushButton("Подтвердить")
        self.confirm_button.clicked.connect(self.on_confirm_button_clicked)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def on_confirm_button_clicked(self):
        first_name = self.name_input.text()
        last_name = self.last_name_input.text()
        
        if first_name and last_name != '':
            self.main_window = MainWidget(sorter, first_name, last_name)
            self.main_window.show()
            self.close()
        else:
            print("Введите корректные данные!")

class MainWidget(QMainWindow):

    def __init__(self, sorter, first_name, last_name):                                             
        super().__init__()
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.__init_mainWindow()
        self.__init_layouts()
        self.__init_widgets()
        self.__init_style()
        self.__init_sizes()
        self.__addition_widgets()
        self.__setting_layers()
        self.__table_settings()
        
        self.mn_min_to_max = True
        self.city_min_to_max = True
        self.ytb_min_to_max = True
        self.wbs_min_to_max = True
        self.str_min_to_max = True
        self.cnty_min_to_max = True
    
        self.current_page = 1
        self.items_per_page = 25
        self.total_pages = (len(sorter.now_data) + self.items_per_page - 1) // self.items_per_page
        
        self.prev_button.clicked.connect(self.go_to_previous_page)
        self.next_button.clicked.connect(self.go_to_next_page)
        self.reviews_button.clicked.connect(self.show_reviews)
        self.reviews_list.clicked.connect(self.go_to_review)
        self.table.horizontalHeader().sectionClicked.connect(self.on_header_clicked)
        
        self.update_table()
        self.populateTableHeader()
        self.table.itemClicked.connect(self.openParametersWindow)

    def __init_mainWindow(self):
        self.central_widget = QWidget(self)                         
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Farmers markets")
        self.resize(200, 200) 
        self.setStyleSheet("background-color: rgba(255, 255, 255, 150);")

    def __init_layouts(self):
        self.main_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()
        
    def __init_widgets(self):          
        self.user = QLabel(f"User: {self.first_name} {self.last_name}")
        self.table = QTableWidget()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
        self.reviews_button = QPushButton("Update reviews")
        self.reviews_list = QListWidget()
    
    def __init_style(self):
        self.user.setStyleSheet("font: 8pt \"Adobe Fan Heiti Std B\";\n")
        
    def __init_sizes(self):
        self.user.setMaximumSize(250, 30)
        self.table.setMinimumSize(1200, 700)

    def __addition_widgets(self):
        self.table_layout.addWidget(self.user) 
        self.table_layout.addWidget(self.table)
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)  
        self.table_layout.addWidget(self.reviews_button)
        self.main_layout.addWidget(self.reviews_list)     
        
    def __setting_layers(self):
        self.main_layout.addLayout(self.table_layout)
        self.table_layout.addLayout(self.button_layout)
        self.central_widget.setLayout(self.main_layout)   
        
    def __table_settings(self):
        self.table.setRowCount(len(sorter.now_data)+1)
        self.table.setColumnCount(len(sorter.name_colomns))
    
    def update_reviews(self):  
        self.reviews_list.clear()  
        try:
            with open('Reviews.json', 'r', encoding='utf-8', errors='ignore') as file:
                data = json.load(file)
                if 'Reviews' in data:
                    reviews = data['Reviews']
                else:
                    reviews = []
        except (FileNotFoundError, json.JSONDecodeError):
            reviews = []
        for review in reviews:
            for key, value in review.items():
                if key != "rate" and value:
                    shop = key
                    rate = review["rate"]
                    item = (f"{shop} - shop - rate {rate}")    
                    self.reviews_list.addItem(item)
        
    def go_to_previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_table()
        
    def go_to_next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_table()   
                    
    def update_table(self):
        self.update_reviews()
        self.start_index = ((self.current_page - 1) * self.items_per_page)
        self.end_index = self.start_index + self.items_per_page
        visible_data = sorter.now_data[self.start_index:self.end_index]
        
        self.table.setRowCount(len(visible_data))
        for row, rowData in enumerate(visible_data):
            for col, value in enumerate(rowData):
                self.table.setItem(row, col, QTableWidgetItem(value))   
                
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                if item is not None:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                    
        header_horizontal = self.table.horizontalHeader()
        header_horizontal.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header_vertical = self.table.verticalHeader()
        header_vertical.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.populateTableHeader()
        
    def populateTableHeader(self):
        for i, item in enumerate(sorter.name_colomns):
            item = QTableWidgetItem(str(item))
            self.table.setHorizontalHeaderItem(i, item) 
        
    def openParametersWindow(self, item):
        self.clicked_row = item.row() + self.start_index+1
        print(self.clicked_row)
        self.parametersWindow = ParametersWindow(self.clicked_row, 
                                                 sorter.all_data[self.clicked_row-1], 
                                                 sorter.field_names,
                                                 self.first_name, self.last_name)
        self.parametersWindow.show()

    def show_reviews(self):
        self.update_reviews()
    
    def go_to_review(self, index):
        selected_item_text = index.data()
        self.review = ReviewWindow(selected_item_text)
        self.review.show()
    
    def on_header_clicked(self, logical_index):  
        sort_options = {
            0: ('mn_min_to_max', sorter.sort_by_marketname),
            1: ('wbs_min_to_max', sorter.sort_by_website),
            2: ('ytb_min_to_max', sorter.sort_by_youtube),
            3: ('str_min_to_max', sorter.sort_by_street),
            4: ('city_min_to_max', sorter.sort_by_city),
            5: ('cnty_min_to_max', sorter.sort_by_county),
        }
        option = sort_options.get(logical_index)
        if option:
            attribute, sort_function = option
            setattr(self, attribute, not getattr(self, attribute))
            sort_function(getattr(self, attribute))
            self.update_table()
    
class ParametersWindow(QMainWindow):
    def __init__(self, clicked_row, data, field_names, first_name, last_name):
        super().__init__()

        self.clicked_row = clicked_row
        self.data = data
        self.field_names = field_names
        self.first_name = first_name
        self.last_name = last_name

        self.__init_mainWindow()
        self.__init_layouts()
        self.__init_widgets()
        self.__init_style()
        self.__init_sizes()
        self.__addition_widgets()
        self.__setting_layers()

        self.set_data()
        self.__table_settings_clicked()
        self.update_table()

    def __table_settings_clicked(self):
        self.table_clicked_data.setRowCount(1)
        self.table_clicked_data.setColumnCount(len(self.field_names))
        self.rate_box.setRange(0, 5)
        self.add_review_button.clicked.connect(self.save_review)

    def update_table(self):
        self.table_clicked_data.setRowCount(1)
        for col, value in enumerate(self.data):
            item = QTableWidgetItem(str(value))
            self.table_clicked_data.setItem(0, col, item)

        for row in range(self.table_clicked_data.rowCount()):
            for column in range(self.table_clicked_data.columnCount()):
                item = self.table_clicked_data.item(row, column)
                if item is not None:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)

        header_horizontal = self.table_clicked_data.horizontalHeader()
        header_horizontal.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header_vertical = self.table_clicked_data.verticalHeader()
        header_vertical.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.populateTableHeader_clicked()

    def __init_mainWindow(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Farmers markets")
        self.resize(200, 200)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 150);")

    def __init_layouts(self):
        self.main_layout = QVBoxLayout()
        self.table_clicked_data_layout = QHBoxLayout()
        self.under_table_clicked_layout = QHBoxLayout()
        self.review_layout = QVBoxLayout()

    def __init_widgets(self):
        self.number = QLabel(f"Номер в базе данных:")
        self.rating_label = QLabel("Поставьте оценку от 1 до 5: ")
        self.table_clicked_data = QTableWidget()
        self.add_review_button = QPushButton("Добавить рецензию")
        self.user_name = QLabel(f"Оставить рецензию под именем пользователя: "
                                f"{self.first_name} {self.last_name}")
        self.text_review = QTextEdit(self)
        self.rate_box = QSpinBox(self)

    def __init_style(self):
        self.number.setStyleSheet("font: 8pt \"Adobe Fan Heiti Std B\";\n")

    def __init_sizes(self):
        self.number.setMinimumSize(200, 50)
        self.table_clicked_data.setMaximumSize(1300, 150)
        self.add_review_button.setMinimumSize(200, 100)
        self.text_review.setMinimumSize(1000, 200)

    def __addition_widgets(self):
        self.main_layout.addWidget(self.number)
        self.table_clicked_data_layout.addWidget(self.table_clicked_data)
        self.under_table_clicked_layout.addWidget(self.add_review_button)
        self.review_layout.addWidget(self.user_name)
        self.review_layout.addWidget(self.text_review)
        self.review_layout.addWidget(self.rating_label)
        self.review_layout.addWidget(self.rate_box)

    def __setting_layers(self):
        self.central_widget.setLayout(self.main_layout)
        self.main_layout.addLayout(self.table_clicked_data_layout)
        self.main_layout.addLayout(self.under_table_clicked_layout)
        self.under_table_clicked_layout.addLayout(self.review_layout)

    def set_data(self):
        self.number.setText((f"Number in BD: {self.clicked_row}"))

    def populateTableHeader_clicked(self):
        for i, item in enumerate(self.field_names):
            item = QTableWidgetItem(str(item))
            self.table_clicked_data.setHorizontalHeaderItem(i, item)

    def save_review(self):
        review_text = self.text_review.toPlainText()
        review_rate = self.rate_box.value()
        if review_rate == 0:
            self.rating_label.setText("Чтобы оставить отзыв, необходимо указать оценку.\n"
                                      "Пожалуйста, поставьте оценку от 1 до 5:")
            return 0
        data = {'Reviews': []}
        try:
            with open('Reviews.json', 'r', encoding='utf-8', errors='ignore') as file:
                data = json.load(file)
                if 'Reviews' in data:
                    reviews = data['Reviews']
                else:
                    reviews = []
        except (FileNotFoundError, json.JSONDecodeError):
            reviews = []
        new_review = {
            f'{self.first_name, self.last_name}': review_text,
            'rate': review_rate
        }

        reviews.append(new_review)

        data['Reviews'] = reviews

        with open('Reviews.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        self.text_review.clear()
        QMessageBox.information(self, 'Сохранено', 'Отзыв успешно сохранен')
        self.close()

class ReviewWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
    
        self.target_key = data
        self.find_review()
        
        self.__init_mainWindow()
        self.__init_layouts()
        self.__init_widgets()
        self.__init_style()
        self.__init_sizes()
        self.__addition_widgets()
        self.__setting_layers()
        self.__settings()
        
    def __init_mainWindow(self):
        self.central_widget = QWidget(self)                         
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Users reviews")
        self.resize(200, 200) 
        self.setStyleSheet("background-color: rgba(255, 255, 255, 150);") 
    
    def __init_layouts(self):
        self.main_layout = QVBoxLayout()
    
    def __init_widgets(self):
        self.users_reviews_label = QLabel(f"{self.result_string}")
        self.delete_review_button = QPushButton("Удалить отзыв")

    def __init_style(self):
        pass
    
    def __init_sizes(self):
        pass
    
    def __addition_widgets(self):
        self.main_layout.addWidget(self.users_reviews_label)
        self.main_layout.addWidget(self.delete_review_button)
    
    def __setting_layers(self):
        self.central_widget.setLayout(self.main_layout)
        #self.main_layout.addLayout(self.)
    
    def __settings(self):
        self.delete_review_button.clicked.connect(self.remove_review)
    
    def find_review(self):
        try:
            self.match = re.match(r"\('([^']+)', '([^']+)'\) - shop - rate (\d+)", self.target_key)
            if self.match:
                target_tuple = (self.match.group(1), self.match.group(2))
                target_rate = int(self.match.group(3))
                with open('Reviews.json', 'r') as file:
                    data = json.load(file)
                for index, review in enumerate(data["Reviews"]):
                    review_tuple = eval(list(review.keys())[0]) 
                    i = list(review.keys())[0]
                    if review_tuple == target_tuple and review["rate"] == target_rate:
                        self.index = index
                        self.review = review[i]
                        self.result_string = (f"Отзыв от пользователя {self.match.group(1)} "
                                        f"{self.match.group(2)} о рынке __, с оценкой рынка в " 
                                        f"{self.match.group(3)}: {self.review}")
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
            
    def remove_review(self):
        try:
            with open('Reviews.json', 'r') as file:
                data = json.load(file)
            del data["Reviews"][self.index]
            with open('Reviews.json', 'w') as write_file:
                json.dump(data, write_file, indent=2)
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
        QMessageBox.information(self, 'Успешно', 'Отзыв успешно удален')
        self.close()

if __name__ == "__main__":
    sorter = Sorter()
    app = QApplication(sys.argv)
    input_window = NameInputWindow()
    input_window.show()
    sys.exit(app.exec())
    
