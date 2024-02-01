from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MainWindow(QWidget):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Метка для отображения имени и фамилии
        self.info_label = QLabel(f"Привет, {self.first_name} {self.last_name}!")

        # Добавляем метку в макет
        layout.addWidget(self.info_label)

        # Устанавливаем созданный макет для окна
        self.setLayout(layout)

class NameInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Метки для имени и фамилии
        self.name_label = QLabel("Введите ваше имя:")
        self.last_name_label = QLabel("Введите вашу фамилию:")

        # Поля для ввода имени и фамилии
        self.name_input = QLineEdit()
        self.last_name_input = QLineEdit()

        # Кнопка для подтверждения ввода
        self.confirm_button = QPushButton("Подтвердить")
        self.confirm_button.clicked.connect(self.on_confirm_button_clicked)

        # Добавляем виджеты в макет
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.confirm_button)

        # Устанавливаем созданный макет для окна
        self.setLayout(layout)

    def on_confirm_button_clicked(self):
        # Обработка нажатия кнопки подтверждения
        first_name = self.name_input.text()
        last_name = self.last_name_input.text()
        
        if first_name and last_name is not None:
            self.main_window = MainWindow(first_name, last_name)
            self.main_window.show()
            self.close()
        else:
            print("Введите корректные данные!")

# Создание приложения и отображение окна запроса ввода имени и фамилии
app = QApplication([])
input_window = NameInputWindow()
input_window.show()
app.exec()
