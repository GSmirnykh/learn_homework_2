"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    with open('export.csv', 'w', encoding='utf-8', newline='') as file:
        fields = ['name', 'age', 'job']
        content = [{'name': 'Mikhail', 'age': '30', 'job': 'developer'},
                   {'name': 'Gennadiy', 'age': '31', 'job': 'engineer'},
                   {'name': 'Alexey', 'age': '32', 'job': 'project manager'},
                   {'name': 'Oleg', 'age': '33', 'job': 'manager'}
                   ]
        writer = csv.DictWriter(file, fields, delimiter=',')
        writer.writeheader()
        for row in content:
            writer.writerow(row)
        


if __name__ == "__main__":
    main()
