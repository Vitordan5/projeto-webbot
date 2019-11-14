import csv


def searchl_ista():
    series = csv.reader(open('listadeseries.csv', 'r'), delimiter=';')

    for row in series:

        if search == row[0]:
            print('Serie: ', row[0], 'Nota: ', row[1], 'Ano de lançamento: ', row[2])


def search_popular():
    series = csv.reader(open('popular.csv', 'r'), delimiter=';')

    for row in series:

        if search == row[0]:
            print('Serie: ', row[0], 'Nota: ', row[1])


def search_new():
    series = csv.reader(open('new.csv', 'r'), delimiter=';')

    for row in series:

        if search == row[0]:
            print('Serie: ', row[0], 'Nota: ', row[1])


search = input('Buscar por nome: ')
search_new()
search_popular()
searchl_ista()
