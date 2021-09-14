import csv

def get_csv(csv_name):
    with open(csv_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
        data_read.pop(0)
        return data_read
    
data = get_csv("data-1.csv")
for i in data:
    if i[1] == '110':
        del data[i]

print(data)