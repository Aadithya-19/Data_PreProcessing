import csv

data = []

with open("dataset_2.csv", "r") as f:
    csv_reader = csv.reader(f)
    for a in csv_reader:
        data.append(a)

headers = data[0]

planet_data = data[1:]

for x in planet_data:
    x[2] = x[2].lower()

planet_data.sort(key = lambda planet_data:planet_data[2])

with open("moreDataSorted.csv", "a+") as f:
    csv_write = csv.writer(f)
    csv_write.writerow(headers)
    csv_write.writerow(planet_data)