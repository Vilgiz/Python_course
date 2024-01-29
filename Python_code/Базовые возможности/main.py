from Final_task_manager import Manager, os
from Final_task_csv import CSVReader
from decimal import Decimal


def hello_message():

    print("1. Add")
    print("2. Show all")
    print("3. Show for date")
    print("4. Show by category")
    print("5. Show by min-max")
    print("6. Show by max-min")
    print("7. Show sorted by date")
    print("8. Show sorted by category")
    print("9. Delete")
    print("10. Save to CSV")
    print("0. Exit")


def switch(lang):
    if lang == "1":
        category = input("Category:")
        product = input("Product:")
        cost = Decimal(input("Cost:"))
        date = input("Date:")
        manager.add(category, product, cost, date)
    elif lang == "2":
        manager.show()
    elif lang == "3":
        filter = input("Type date in format Y-M-D:")
        manager.show_products_by_filter(filter, 0)
    elif lang == "4":
        filter = input("Type name of category:")
        manager.show_products_by_filter(filter, 1)
    elif lang == "5":
        manager.show_products_by_filter(flag=2)
    elif lang == "6":
        manager.show_products_by_filter(flag=3)
    elif lang == "7":
        manager.show_products_by_filter(flag=4)
    elif lang == "8":
        manager.show_products_by_filter(flag=5)
    elif lang == "9":
        position = int(input("What row in csv you want to delete?:"))
        manager.remove(position)
    elif lang == "10":
        path = input("Choose the file save name:")
        manager.save(path)
    else:
        print("Goodbye")
        exit(0)


if __name__ == "__main__":
    filename = input("Type path to your csv file:")
    if os.path.isfile(filename):
        try:
            csv_reader = CSVReader(filename)
            print(f"File '{filename}' exists.")
            manager = Manager(csv_reader.products)
            print("Hello user! \n")
            while (True):
                hello_message()
                lang = input("What would you like to do?:")
                switch(lang)
        except FileExistsError as e:
            print(f"Error occurred while reading file '{filename}': {e}")
    else:
        print(f"File '{filename}' does not exist.")
    
