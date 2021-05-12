import csv 

data_set_1 = []
data_set_2 = []

with open("final.csv", "r") as f:
    csv_reader = csv.reader(f)
    for a in csv_reader:
        data_set_1.append(a)

with open("moreDataSorted.csv", "r") as g:
    csv_reader_1 = csv.reader(g)
    for b in csv_reader_1:
        data_set_2.append(b)

headers_1 = data_set_1[0]

headers_2 = data_set_2[0]

planet_data_1 = data_set_1[1:]

planet_data_2 = data_set_2[1:]

headers = headers_1+headers_2

planet_data = []

for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("FinalAllComibinedData.csv", "a+") as k:
    csv_write = csv.writer(k)
    csv_write.writerow(headers)
    csv_write.writerow(planet_data)