import csv
from numbers import Number
from datetime import datetime
from typing import List
from dataclasses import dataclass


@dataclass
class Product:

    category: str
    product: str
    cost: Number
    date: str

    def __post_init__(self):
        try:
            self.date = datetime.strptime(self.date, "%m/%d/%Y").date()
        except ValueError:
            self.date = datetime.strptime(self.date, "%Y-%m-%d").date()


class CSVReader:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.products = []
        self.read_csv()

    def read_csv(self) -> None:
        with open(self.filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.products.append(Product(row['Category'], row['Product'],
                                             float(row['Cost']), row['Date']))


class CSVWriter:

    def __init__(self, filename: str, products: List) -> None:
        self.filename = filename
        self.products = products

    def write_csv(self) -> None:
        with open(self.filename, 'w', encoding='utf-8', newline='') as file:
            w = csv.writer(file)
            w.writerow(['Category', 'Product', 'Cost', 'Date'])
            for product in self.products:
                w.writerow([product.category, product.product,
                           product.cost, product.date])


if __name__ == "__main__":
    filename = "C:/Projects/Python_course/Python_code/DATA.csv"
    csv_reader = CSVReader(filename)

    for product in csv_reader.products:
        print(
            f'Category: {product.category},Product: {product.product},'
            f'Cost: {product.cost}, Date: {product.date}')
