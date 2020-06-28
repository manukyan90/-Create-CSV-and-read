import sys
import numpy as np


def create_numbers():
    numbers = np.arange(1, 200001).reshape(2000, 100)
    import csv
    with open('file.csv', 'w') as csv_file:
        csv = csv.writer(csv_file)

        for num in numbers:
            csv.writerow(num)


def even_numbers():
    list = np.loadtxt('file.csv', dtype=int, delimiter=',')
    list = list.ravel()
    for num in list:
        if num % 2 == 0:
            print(num)

def run():
    for x in sys.argv:
        if x == "create_file":
            print("The file is created")
            return create_numbers()
        if x == "run":
            return even_numbers()
run()
