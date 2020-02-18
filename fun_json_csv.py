import json
import csv



def fileReader(filepath):
    with open(filepath,'rb') as f:
        return json.loads(f.read())

def generateCsvHeader(filepath):
    header=[]
    return list(map(lambda item: iterateJsonRow(item,"header"),[data[0]]))[0]

def generateCsv(filepath):
    fileWriter=open(filepath,'w')
    csv_file=csv.writer(fileWriter)
    header=generateCsvHeader(filepath)
    print(header)
    csv_file.writerow(header)
    for row in list(map(lambda item:iterateJsonRow(item,"row"),data)):
        csv_file.writerow(row)
        print(row)

def iterateJsonRow(jsonRow,mode):
    row=[]
    first_keys=list(jsonRow.keys())
    for key in first_keys:
        if mode == 'header':
            if isinstance(jsonRow[key],dict):
                row+=jsonRow[key].keys()
            else:
                row.append(key)
        if mode == 'row':
            if isinstance(jsonRow[key],dict):
                row+=jsonRow[key].values()
            else:
                row.append(jsonRow[key])
    return row

data = fileReader("data2.json")
generateCsv("data1.csv")


