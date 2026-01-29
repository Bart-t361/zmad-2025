import csv
from collections import Counter
from sklearn.model_selection import train_test_split

def headers_zone(pathway):
    labels=[]
    data=[]

    try:
        with open(pathway,encoding="utf-8") as file:

            sniffer = csv.Sniffer()
            header = sniffer.has_header(file.read(2048))
            file.seek(0)

            if header:
                    column = csv.DictReader(file, delimiter=',')
                    labels.extend(column.fieldnames)
                    for row in column:
                            data.append([row[field] for field in column.fieldnames])
            else:
                print('Nie wykryto nagłówków')
    except IOError as err:
            print(f"Błąd odczytu pliku z danymi: {err}")
    return labels, data, column

def counter_zone(pathway):
    with open(pathway) as file:
        next (file)
        count_data = [line.strip().split(',')[-1] for line in file]
    return count_data
def data_split(data, train_pct=0.6, test_pct=0.2, val_pct=0.2):

    import random


    random.shuffle(data)

    train_last_index = int(len(data) * train_pct)
    test_last_index = int(len(data) * (train_pct + test_pct))

    train_data = data[:train_last_index]
    test_data = data[train_last_index:test_last_index]
    valid_data = data[test_last_index:]

    return train_data, test_data, valid_data


if __name__ == "__main__":
    pathway = "iris.csv"


labels, data, column = headers_zone(pathway)
count_data = counter_zone(pathway)

print('\nplik posiada nagłówki. Liczba kolumn w zbiorze wynosi ', len(column.fieldnames))
print('\n', column.fieldnames)

print('\n', dict(Counter(count_data)), '\n')

for subset in data_split(data):
    print(f"Ilość elementów w zbiorze: {len(subset)}")

for subset in data_split(data, 0.7, 0.2, 0.1):
    print(f"Ilość elementów w zbiorze: {len(subset)}")

for subset in data_split(data, 0.8, 0.1, 0.1):
    print(f"Ilość elementów w zbiorze: {len(subset)}")