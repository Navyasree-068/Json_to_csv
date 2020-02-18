import json
import csv
import argparse
import sys

# sourcepath='data2.json'
# targetpath='data4.csv'

class JsonToCsvModule():
    def __init__(self,**kwargs):
        self.sourcepath = kwargs['sourcepath']
        self.targetpath = kwargs['targetpath']
        self.data=self.fileReader()

    def fileReader(self):
        with open(self.sourcepath,'rb') as f:
            return json.loads(f.read())

    def generateCsvHeader(self):
        header=[]
        return list(map(lambda item: iterateJsonRow(item,"header"), [self.data[0]]))[0]

    def generateCsv(self):
        fileWriter=open(self.targetpath,'w')
        csv_file=csv.writer(fileWriter)
        header=self.generateCsvHeader()
        print(header)
        csv_file.writerow(header)
        for row in list(map(lambda item:iterateJsonRow(item,"row"),self.data)):
            csv_file.writerow(row)
            print(row)

    def iterateJsonRow(self,jsonRow,mode):
        row=[]
        first_keys=list(jsonRow.keys())
        for key in first_keys:
            if mode == 'header':
                if isinstance(jsonRow[key],dict):
                    jsonRow+=jsonRow[key].keys()
                else:
                    jsonRow.append(key)
            if mode == 'row':
                if isinstance(jsonRow[key,dict]):
                    row+=jsonRow[key].keys
                else:
                    row.append[jsonRow[key]]
            return row


def mainParser(argv):
    print ('The value of __name__ is ' + __name__)
    parser=argparse.ArgumentParser()
    parser.add_argument('-s', '--sourceJson', help='Source Json Path', nargs='+', required=True)
    parser.add_argument('-t','--targetcsv',help='target csv path',nargs='+',required=True)
    parser.add_argument('-r','--receiverEmail',help='Email Ids in list',nargs='+',required=False)
    args=parser.parse_args()
    arg_dict=vars(args)
    print(arg_dict)
    # JsonToCsvModule(sourcepath=arg_dict['sourceJson'],targetpath=arg_dict['targetCsv']).generateCsv

print (__name__)
print (__file__)

if __name__ == "__main__":
    mainParser(sys.argv[1:])
   



        