from Final_task_csv import CSVReader, Product, CSVWriter
import os
from decimal import Decimal
from numbers import Number
from typing import List
from datetime import datetime


class Manager():

    def __init__(self, products: List) -> None:
        self.products = products

    def add(self,
            category: str,
            product_name: str,
            cost: Number,
            date: str):
        if not isinstance(cost, Number):
            raise TypeError("Cost type must be decimal")
        if cost < 0:
            raise ValueError("Cost must be more or equal to 0")
        self.products.append(
            Product(str(category),
                    str(product_name),
                    Decimal(cost),
                    str(date)))

    def show(self):
        for product in self.products:
            print(f'Category: {product.category}, Product: {product.product},'
                  f'Cost: {product.cost}, Date: {product.date}')

    def cost_cost_min_to_max(self) -> List:
        return sorted(self.products, key=lambda x: x.cost)

    def cost_cost_max_to_min(self) -> List:
        return sorted(self.products, key=lambda x: x.cost, reverse=True)

    def remove(self, position) -> List:
        del self.products[position]

    def sort_by_date(self) -> List:
        return sorted(self.products, key=lambda x: x.date)

    def sort_by_category(self) -> List:
        return sorted(self.products, key=lambda x: x.category)

    def get_products_by_category(self, filter: str) -> List:
        result = []
        for counter in self.products:
            if counter.category == filter:
                result.append(counter)
        return result

    def get_products_by_date(self, filter: str) -> List:
        result = []
        date = datetime.strptime(filter, "%Y-%m-%d").date()
        for counter in self.products:
            if counter.category == date:
                result.append(counter)
        return result

    def show_products_by_filter(self, filter=None, flag=0):
        """
        For get by date flag = 0, flag = 1 for get by category,
        flag 2 for sort by cost min to max, flag 3 max to min,
        flag 4 sort by date, flag 5 sort by category
        """
        if flag == 0:
            result = self.get_products_by_date(filter)
        elif flag == 1:
            result = self.get_products_by_category(filter)
        elif flag == 2:
            result = self.cost_cost_min_to_max()
        elif flag == 3:
            result = self.cost_cost_max_to_min()
        elif flag == 4:
            result = self.sort_by_date()
        elif flag == 5:
            result = self.sort_by_category()
        else:
            raise ValueError("Flag could be 0 or 1")
        for product in result:
            print(f'Category: {product.category}, Product: {product.product},'
                  f'Cost: {product.cost}, Date: {product.date}')
    
    def save(self, filename):
        csvWriter = CSVWriter(filename, self.products)
        csvWriter.write_csv()


if __name__ == "__main__":

    filename = "DATA.csv"
    if os.path.isfile(filename):
        try:
            csv_reader = CSVReader(filename)
            print(f"File '{filename}' exists.")
        except FileExistsError as e:
            print(f"Error occurred while reading file '{filename}': {e}")
    else:
        print(f"File '{filename}' does not exist.")

    manager = Manager(csv_reader.products)
    manager.add(3, 3, 10, "12/31/2024")
    manager.remove(3)
    manager.show()
    manager.cost_cost_min_to_max()
    manager.show()
    print(manager.get_products_by_category('Tea - English Breakfast'))
    csvWriter = CSVWriter("dataname.csv", manager.products)
    csvWriter.write_csv()
