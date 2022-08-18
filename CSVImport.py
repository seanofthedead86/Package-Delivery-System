import csv


def address_csv(filename):
    with open(filename) as csvfile_2:
        address_data = list(csv.reader(csvfile_2, delimiter=','))


def distance_csv(filename):
    with open(filename, newline='') as f_input:
        return [list(map(float, row)) for row in csv.reader(f_input)]
