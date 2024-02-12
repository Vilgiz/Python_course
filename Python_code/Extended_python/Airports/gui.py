import sys
from PyQt6.QtWidgets import QApplication, QTableWidget, QPushButton, QWidget, QHBoxLayout, QLabel
from PyQt6.QtWidgets import QLineEdit, QTableWidgetItem, QHeaderView, QVBoxLayout, QMainWindow, QComboBox
from PyQt6.QtGui import QDoubleValidator
from PyQt6 import QtCore
from sort import Sorter
from worldmap import Map


class MainWidget(QMainWindow):
    """
    The MainWidget class represents the main application window.
    """

    def __init__(self):
        """
        Initializes the MainWidget object.
        """
        super().__init__()

        self.all_data = sorter.all_data

        self.__init_main_window()
        self.__init_layouts()
        self.__init_widgets()
        self.__init_style()
        self.__init_sizes()
        self.__addition_widgets()
        self.__setting_layers()
        self.__settings()

        self.current_page = 1
        self.items_per_page = 15
        self.total_pages = (len(self.all_data) +
                            self.items_per_page - 1) // self.items_per_page

        self.prev_button.clicked.connect(self.go_to_previous_page)
        self.next_button.clicked.connect(self.go_to_next_page)
        self.fnd_airline_fm_city_btn.clicked.connect(self.find_lines_from_city)

        self.update_table()
        self.populateTableHeader()

    def __init_main_window(self):
        """
        Initializes the main window settings.
        """
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Farmers markets")
        self.resize(200, 200)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 150);")

    def __init_widgets(self):
        """
        Initializes the widgets used in the main window.
        """
        self.lbl_min_lat = QLabel('Минимальная широта:')
        self.edit_min_lat = QLineEdit()
        self.lbl_max_lat = QLabel('Максимальная широта:')
        self.edit_max_lat = QLineEdit()
        self.lbl_min_lon = QLabel('Минимальная долгота:')
        self.edit_min_lon = QLineEdit()
        self.lbl_max_lon = QLabel('Максимальная долгота:')
        self.edit_max_lon = QLineEdit()
        self.table = QTableWidget()
        self.city_find = QLabel('Поиск по городу:')
        self.city_find_edit = QLineEdit()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
        self.messange_label = QLabel(
            "Для поиска введите данные и нажмите на кнопку")
        self.btn_filter = QPushButton('Применить фильтр')
        self.show_airports_button = QPushButton('Показать аэропорты')
        self.fnd_airline_fm_city_btn = QPushButton('Поиск по городу')

    def __init_layouts(self):
        """
        Initializes the layout settings.
        """
        self.input_layout_7 = QVBoxLayout()
        self.main_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.table_layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()
        self.input_layout_1 = QVBoxLayout()
        self.input_layout_2 = QVBoxLayout()
        self.input_layout_3 = QVBoxLayout()
        self.input_layout_4 = QVBoxLayout()

    def __addition_widgets(self):
        """
        Adds widgets to the layouts.
        """
        self.table_layout.addWidget(self.city_find)
        self.table_layout.addWidget(self.city_find_edit)
        self.table_layout.addWidget(self.fnd_airline_fm_city_btn)
        self.table_layout.addWidget(self.messange_label)
        self.table_layout.addWidget(self.btn_filter)
        self.table_layout.addWidget(self.table)
        self.table_layout.addWidget(self.show_airports_button)
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)
        self.input_layout_1.addWidget(self.lbl_min_lat)
        self.input_layout_1.addWidget(self.edit_min_lat)
        self.input_layout_2.addWidget(self.lbl_max_lat)
        self.input_layout_2.addWidget(self.edit_max_lat)
        self.input_layout_3.addWidget(self.lbl_min_lon)
        self.input_layout_3.addWidget(self.edit_min_lon)
        self.input_layout_4.addWidget(self.lbl_max_lon)
        self.input_layout_4.addWidget(self.edit_max_lon)

    def __setting_layers(self):
        """
        Sets up the layout structure.
        """
        self.input_layout.addLayout(self.input_layout_7)
        self.input_layout.addLayout(self.input_layout_1)
        self.input_layout.addLayout(self.input_layout_2)
        self.input_layout.addLayout(self.input_layout_3)
        self.input_layout.addLayout(self.input_layout_4)
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.table_layout)
        self.table_layout.addLayout(self.button_layout)
        self.central_widget.setLayout(self.main_layout)

    def __settings(self):
        """
        Performs additional settings.
        """
        self.btn_filter.clicked.connect(self.apply_filter)
        self.table.setRowCount(len(self.all_data)+1)
        self.table.setColumnCount(len(sorter.field_names))
        self.show_airports_button.clicked.connect(self.show_airports)

        self.edit_min_lat.setValidator(QDoubleValidator())
        self.edit_max_lat.setValidator(QDoubleValidator())
        self.edit_min_lon.setValidator(QDoubleValidator())
        self.edit_max_lon.setValidator(QDoubleValidator())

    def __init_style(self):
        """
        Initializes the style settings.
        """
        pass

    def __init_sizes(self):
        """
        Initializes the sizes of certain elements.
        """
        self.table.setMinimumSize(900, 600)

    def go_to_previous_page(self):
        """
        Moves to the previous page in the table.
        """
        if self.current_page > 1:
            self.current_page -= 1
            self.update_table()

    def go_to_next_page(self):
        """
        Moves to the next page in the table.
        """
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_table()

    def update_table(self):
        """
        Updates the displayed table based on the current page.
        """
        self.start_index = (self.current_page - 1) * self.items_per_page
        self.end_index = self.start_index + self.items_per_page
        visible_data = self.all_data[self.start_index:self.end_index]

        self.table.setRowCount(len(visible_data))
        for row, row_data in enumerate(visible_data):
            for col, value in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(value))

        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                if item is not None:
                    item.setFlags(item.flags() & ~
                                  QtCore.Qt.ItemFlag.ItemIsEditable)

        header_horizontal = self.table.horizontalHeader()
        header_horizontal.setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        header_vertical = self.table.verticalHeader()
        header_vertical.setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

    def populateTableHeader(self):
        """
        Populates the header of the table with field names.
        """
        for i, item in enumerate(sorter.field_names):
            item = QTableWidgetItem(str(item))
            self.table.setHorizontalHeaderItem(i, item)

    def apply_filter(self):
        """
        Applies the filter based on user input.
        """
        def convert_to_float(text):
            try:
                return float(text.replace(',', '.'))
            except ValueError:
                return None

        name_field = ("min_lat", "max_lat", "min_lon", "max_lon")
        filter_values = {}
        for name in name_field:
            if getattr(self, f"edit_{name}").text() != '':
                value = convert_to_float(getattr(self, f"edit_{name}").text())
                value = float(value)
            else:
                value = float(0)
            filter_values[name] = value

        if (filter_values['max_lat'] <= filter_values['min_lat']
                or filter_values['max_lon'] <= filter_values['min_lon']):
            self.messange_label.setText(
                "Минимальное значение больше максимального, введите корректные данные")
        else:
            self.all_data = sorter.filter_lat_lon(filter_values)
            self.messange_label.setText(
                f"Поиск выполнен, найдено {len(self.all_data)} результата(ов)")
        self.update_table()

    def show_airports(self):
        """
        Displays airports on the map.
        """
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        visible_airports = sorter.coordinates[start_index:end_index]
        map.plot(visible_airports)
        map.show()

    def reset_settins(self):
        """
        Resets the settings.
        """
        self.all_data = sorter.all_data
        for i, item in enumerate(sorter.field_names):
            item = QTableWidgetItem(str(item))
            self.table.setHorizontalHeaderItem(i, item)
        self.table.setRowCount(len(self.all_data)+1)
        self.table.setColumnCount(len(sorter.field_names))
        self.update_table()

    def find_lines_from_city(self):
        """
        Finds airlines based on the entered city name.
        """
        city = self.city_find_edit.text()
        self.all_data = sorter.filter_airlines_by_city(city)
        for i, item in enumerate(sorter.field_names_airlines):
            item = QTableWidgetItem(str(item))
            self.table.setHorizontalHeaderItem(i, item)
        self.table.setRowCount(len(self.all_data)+1)
        self.table.setColumnCount(len(sorter.field_names_airlines))
        self.update_table()


if __name__ == "__main__":
    sorter = Sorter()
    map = Map()
    app = QApplication(sys.argv)
    input_window = MainWidget()
    input_window.show()
    sys.exit(app.exec())
