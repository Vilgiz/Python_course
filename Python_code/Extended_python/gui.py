from PyQt6 import QtCore
import sys
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QSlider, QLabel, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QListWidget
from Sorting import Sorter
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
# engine = create_engine(
#     'postgresql+psycopg2://postgres:cf79db54Q@localhost:6969/test_db', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

class MainWidget(QMainWindow):

    def __init__(self, sorter):                                             
        super().__init__()
        
        self.__init_mainWindow()
        self.__init_layouts()
        self.__init_widgets()
        self.__init_style()
        self.__init_sizes()
        self.__addition_widgets()
        self.__setting_layers()
        self.__table_settings()
    
        self.current_page = 1
        self.items_per_page = 20
        self.total_pages = (len(sorter.list_data) + self.items_per_page - 1) // self.items_per_page
        
        self.prev_button.clicked.connect(self.go_to_previous_page)
        self.next_button.clicked.connect(self.go_to_next_page)
        
        self.update_table()

    def __init_mainWindow(self):
        self.central_widget = QWidget(self)                         
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Farmers markets")
        self.resize(200, 200) 
        self.setStyleSheet("background-color: rgba(255, 255, 255, 150);")

    def __init_layouts(self):
        self.main_layout = QHBoxLayout()
        
    def __init_widgets(self):
        self.list_widget = QListWidget()             
        self.Wasted_plastic =  QLabel("Wasted plastic")
        self.table = QTableWidget()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
    
    def __init_style(self):
        self.Wasted_plastic.setStyleSheet("font: 8pt \"Adobe Fan Heiti Std B\";\n")
        
    def __init_sizes(self):
        self.Wasted_plastic.setMaximumSize(200, 50)
        self.list_widget.setMinimumSize(300, 200)
        self.table.setMinimumSize(600, 400)
        self.table.setMinimumSize(800, 600)
        
    def __addition_widgets(self):
        # self.main_layout.addWidget(self.Wasted_plastic) 
        self.main_layout.addWidget(self.list_widget)
        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.prev_button)
        self.main_layout.addWidget(self.next_button)
        
    
    def __setting_layers(self):
        self.central_widget.setLayout(self.main_layout)   
        
    def __table_settings(self):
        
        self.table.setRowCount(len(sorter.table_rows))
        self.table.setColumnCount(len(sorter.field_names))
        
        for i, item in enumerate(sorter.field_names):
            self.table.setItem(0, i, QTableWidgetItem(item))
        
        # for j, item in enumerate(sorter.table_rows):
        #     self.table.setItem(j+1, 1, QTableWidgetItem(str(item.MarketName)))
        #     self.table.setItem(j+1, 0, QTableWidgetItem(str(item.FMID)))
            
        for j, item in enumerate(sorter.table_rows):
            for index, field in enumerate(sorter.field_names):
                self.table.setItem(j+1, index, QTableWidgetItem(str(getattr(item, field))))   
            

                    
        self.list_widget.addItems(sorter.field_names)
        
    def go_to_previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_table()
        
    def go_to_next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_table()   
                    
    def update_table(self):
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        visible_data = sorter.list_data[start_index:end_index]
        
        self.table.setRowCount(len(visible_data))
        for row, rowData in enumerate(visible_data):
            for col, value in enumerate(rowData):
                self.table.setItem(row, col, QTableWidgetItem(value))   
                
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                if item is not None:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
        
if __name__ == "__main__":
    sorter = Sorter()
    app = QApplication(sys.argv)  
    window = MainWidget(sorter)
    window.show()
    # session.close()
    sys.exit(app.exec())
    
