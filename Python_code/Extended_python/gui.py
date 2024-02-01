from PyQt6 import QtCore
import sys
from PyQt6.QtWidgets import QApplication, QTableWidget, QPushButton, QWidget, QHBoxLayout, QListWidget
from PyQt6.QtWidgets import QSlider, QLineEdit ,QTableWidgetItem, QHeaderView, QVBoxLayout, QTableWidgetItem, QMainWindow, QLabel
from Sorting import Sorter

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
        self.first_name = first_name
        self.last_name = last_name
        self.__init_mainWindow()
        self.__init_layouts()
        self.__init_widgets()
        self.__init_style()
        self.__init_sizes()
        self.__addition_widgets()
        self.__setting_layers()
        self.__table_settings()
    
        self.current_page = 1
        self.items_per_page = 25
        self.total_pages = (len(sorter.now_data) + self.items_per_page - 1) // self.items_per_page
        
        self.prev_button.clicked.connect(self.go_to_previous_page)
        self.next_button.clicked.connect(self.go_to_next_page)
        
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
        self.list_widget = QListWidget()             
        self.user = QLabel(f"Пользователь: {self.first_name} {self.last_name}")
        self.table = QTableWidget()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
    
    def __init_style(self):
        self.user.setStyleSheet("font: 8pt \"Adobe Fan Heiti Std B\";\n")
        
    def __init_sizes(self):
        self.user.setMaximumSize(250, 30)
        self.list_widget.setMinimumSize(300, 200)
        self.table.setMinimumSize(1200, 700)

    def __addition_widgets(self):
        self.table_layout.addWidget(self.user) 
        self.table_layout.addWidget(self.table)
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)        
        

    def __setting_layers(self):
        self.main_layout.addLayout(self.table_layout)
        self.table_layout.addLayout(self.button_layout)
        self.central_widget.setLayout(self.main_layout)   
        
    def __table_settings(self):
        
        self.table.setRowCount(len(sorter.now_data)+1)
        self.table.setColumnCount(len(sorter.name_colomns))
                    
        self.list_widget.addItems(sorter.name_colomns)
        
    def go_to_previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_table()
        
    def go_to_next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_table()   
                    
    def update_table(self):
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
                                                 sorter.field_names)
        self.parametersWindow.show()
    
class ParametersWindow(QMainWindow):
    
    def __init__(self, clicked_row, data, field_names):
        super().__init__()
        self.__init_mainWindow()
        self.__init_layouts()
        self.__init_widgets()
        self.__init_style()
        self.__init_sizes()
        self.__addition_widgets()
        self.__setting_layers()
        
        self.clicked_row = clicked_row
        self.data = data
        self.field_names = field_names
        
        self.current_page_cliked = 1
        self.items_per_page_cliked = 60
        self.total_pages_cliked = (len(self.data) + self.items_per_page_cliked) // self.items_per_page_cliked
        
        self.set_data()
        
        self.__table_settings_cliked()
        self.update_table()
        
    def __table_settings_cliked(self):
            self.table_clicked_data.setRowCount(1)
            self.table_clicked_data.setColumnCount(len(self.field_names))
            
    def update_table(self):
            self.start_index = ((self.current_page_cliked - 1) * self.items_per_page_cliked)
            self.end_index = self.start_index + self.items_per_page_cliked
            visible_data = self.data[self.start_index:self.end_index]
            
            self.table_clicked_data.setRowCount(1)   
            for row in enumerate(visible_data):
                for col, value in enumerate(visible_data):
                    self.table_clicked_data.setItem(0, col, QTableWidgetItem(value))   
                    
            for row in range(self.table_clicked_data.rowCount()):
                for column in range(self.table_clicked_data.columnCount()):
                    item = self.table_clicked_data.item(row, column)
                    if item is not None:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                        
            header_horizontal = self.table_clicked_data.horizontalHeader()
            header_horizontal.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            header_vertical = self.table_clicked_data.verticalHeader()
            header_vertical.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.populateTableHeader_cliked()
         
    def __init_mainWindow(self):
        self.central_widget = QWidget(self)     
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Farmers markets")
        self.resize(200, 200) 
        self.setStyleSheet("background-color: rgba(255, 255, 255, 150);")    
    
    def __init_layouts(self):
        self.main_layout = QVBoxLayout()
        self.table_clicked_data_layout = QHBoxLayout()
        
    def __init_widgets(self):
        self.number = QLabel(f"Номер в базе данных:")
        self.table_clicked_data = QTableWidget()
    
    def __init_style(self):
        self.number.setStyleSheet("font: 8pt \"Adobe Fan Heiti Std B\";\n")
        pass  
    
    def __init_sizes(self):
        self.number.setMinimumSize(200, 50)
        self.table_clicked_data.setMinimumSize(700, 100)
    
    def __addition_widgets(self):
        self.main_layout.addWidget(self.number) 
        self.table_clicked_data_layout.addWidget(self.table_clicked_data)
    
    def __setting_layers(self):
        self.central_widget.setLayout(self.main_layout)
        self.main_layout.addLayout(self.table_clicked_data_layout)
        
    def set_data(self):
        text = (f"Number in BD: {self.clicked_row}")
        for field, value in zip(self.field_names, self.data):
            label_text = f"{field} - {value}\n"
            text_2 = "" + label_text
        self.number.setText(text + text_2)
        
    def populateTableHeader_cliked(self):
        for i, item in enumerate(self.field_names):
            item = QTableWidgetItem(str(item))
            self.table_clicked_data.setHorizontalHeaderItem(i, item) 

if __name__ == "__main__":
    sorter = Sorter()
    app = QApplication(sys.argv) 
    input_window = NameInputWindow()
    input_window.show()
    sys.exit(app.exec())
    
