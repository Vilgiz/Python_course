

# TODO: Создайте сценарий, который использует список имен файлов CSV в качестве
# источника для копирования содержимого этих файлов в плоский файл. Текущая дата
# и время должны быть добавлены к имени файла в качестве префикса перед
# копированием. Каждая операция копирования должна быть записана в файл журнала
# на локальном компьютере. Исключения для файлов, которые не были найдены,
# также должны быть записаны в журнал.
# Пояснение к заданию:
# На входе программы должен быть список имён файлов CSV, сами файлы произвольно
# содержания, например те, с которыми вы уже работали. Программа должна принять список,
# скопировать содержимое каждого из них в текстовый файл (на ваше усмотрение в
# отдельные файлы или общий, идея - должна быть копия данных, в задании только есть
# требование к имени этого файла). При выполнении копировании информацию об этом
# программа сохраняет в файле журнала. Может возникнуть ситуация, при которой
# некоторых файлов из исходного списка не окажется, тогда нужно это учесть в программе с
# помощью механизма обработки исключений - если файла нет, то в файл журнал нужно
# сделать запись, что файл не найден.

import logging
import csv
import os
from datetime import datetime

logging.basicConfig(filename="log.log", filemode="w", level=logging.INFO)

def find_files(path_dir, extension):
    finded = []
    for root, dirs, files in os.walk(f"{path_dir}"): 
        for file in files:
            if file.endswith(extension):
                finded.append(os.path.join(root, file))
    return finded


def logger(file_name: str, index_row: int):
    logging.info(f"{file_name} row index is {index_row} copied by time {datetime.now().strftime('%Y-%m-%d_(H%H_M%M_S%S)')}")


def parse_data() -> str:
    return datetime.now().strftime("%Y-%m-%d_(H%H_M%M)")


def task() -> None:
    
    for input in INPUT_FILES:
        data = []
        with open(input, encoding="utf-8") as input_file:
            reader = csv.DictReader(input_file)
            for i, row in enumerate(reader):
                data.append(row)
                logger(input, i)
            with open(f"{parse_data()}_" + OUTPUT_FILENAME, "a",
                      encoding="utf-8") as output_file:
                output_file.write(f"{input} \n")
                for row in data:
                    output_file.write(str(row))
                output_file.write("\n" * 5)


if __name__ == "__main__":
    INPUT_FILES = find_files(r"C:/Projects/Python_course/csv", "csv")
    logging.info(f"find {len(INPUT_FILES)} with path {INPUT_FILES}")
    OUTPUT_FILENAME = "result.txt"
    LOG_FILE = "log.txt"
    task()
