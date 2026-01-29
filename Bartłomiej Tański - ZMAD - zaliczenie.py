import csv
import random
from collections import Counter
import math

def headers_zone(filepath, has_header=True):     #Wczytanie datasetu
    labels = []
    data = []

    with open(filepath, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        if has_header:
            labels = next(reader)

        for row in reader:
            data.append(row)

    return labels, data

def labels_zone(labels):                            #Wypisanie etykiet
        print("Nazwy kolumn:", labels)

def data_zone(data, x=None, y=None):                #Wypisanie danych datasetu
    if x is None and y is None:
        for row in data:
            print(row)
    else:
        for row in data[x:y]:
            print(row)

def data_split(data, train_pct=0.6, test_pct=0.3, val_pct=0.1): #Podział datasetu na zbiór treningowy, testowy i walidacyjny

    total = train_pct + test_pct + val_pct
    assert math.isclose(total, 1.0)

    random.shuffle(data)

    train_last_index = int(len(data) * train_pct)
    test_last_index = int(len(data) * (train_pct + test_pct))

    train_data = data[:train_last_index]
    test_data = data[train_last_index:test_last_index]
    valid_data = data[test_last_index:]

    return train_data, test_data, valid_data

def counter_zone(filepath):                              #Wypisz liczbę klas decyzyjnych
    with open(filepath) as file:
        next(file)
        count_data = [line.strip().split(',')[-1] for line in file]
    return count_data

def class_zone(data, class_value):                       #Wypisz dane dla podanej wartości klasy decyzyjnej
    for row in data:
        if row[-1] == class_value:
            print(row)

def filesaver(data, filename):                           #Zapisanie danych do pliku csv
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == "__main__":
    filepath = "iris.csv"

    labels, data = headers_zone(filepath)
    labels_zone(labels)
    print(dict(Counter(counter_zone(filepath))))
    data_zone(data, 0, 5)
    train_data, test_data, val_data = data_split(data)
    filesaver(train_data, "train.csv")
    class_zone(data, "Iris-versicolor")

    for subset in data_split(data):
        print(f"Ilość elementów w zbiorze: {len(subset)}")

    for subset in data_split(data,0.7, 0.2, 0.1):
        print(f"Ilość elementów w zbiorze: {len(subset)}")

    for subset in data_split(data,0.8, 0.1, 0.1):
        print(f"Ilość elementów w zbiorze: {len(subset)}")
