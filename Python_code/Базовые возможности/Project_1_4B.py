

# TODO: Загрузите данные из файла …\data\orderdata_sample.csv file. На основе столбцов
# “Quantity”, “Price” и “Freight” создайте новый столбец “Total” (например, по
# формуле Quantity * Price + Freight). Отобразите на экран выборочно (на ваше
# усмотрение) столбцы на основе условия (на ваше усмотрение).
# Сохраните все данные в новый файл.

    
import csv

if __name__ == "__main__":

    input_file_path = r'C:/Projects/Python_course/csv/orderdata.csv'
    output_file_path = r'C:/Projects/Python_course/csv/new_orderdata.csv'

    def calculate_total(quantity, price, freight):
        return quantity * price + freight

    data = []
    with open(input_file_path, mode='r', newline='', encoding='utf-8') as input_file:
        csv_reader = csv.DictReader(input_file)
        for row in csv_reader:
            row["Total"] = calculate_total(int(row["Quantity"]), float(row["Price"]), float(row["Freight"]))
            data.append(row)

    selected_columns = ["Quantity", "Price", "Freight", "Total"] 
    for row in data[:5]: 
        selected_data = {key: row[key] for key in selected_columns}
        print(selected_data)

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file:
        fieldnames = csv_reader.fieldnames + ["Total"]  # Добавляем новое поле в заголовок
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)