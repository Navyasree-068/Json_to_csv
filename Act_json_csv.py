import json
import csv

f = open('data2.json')
data = json.loads(f.read())
f.close()
f = open('data3.csv', "w")
csv_file = csv.writer(f)
first_keys=[]
header=[]
for item in data:
    first_keys=item.keys()
    for key in first_keys:
        if isinstance(item[key],dict):
            header+=item[key].keys()
        else:
            header.append(key)
    break;
print (header)
csv_file.writerow(header)
for item in data:
    data1=[]
    for key in first_keys:
        if isinstance(item[key],dict):
            data1+=item[key].values()
        else:
            data1.append(item[key])
    print(data1)
    csv_file.writerow(data1)
