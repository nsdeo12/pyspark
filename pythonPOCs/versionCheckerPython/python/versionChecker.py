import csv
filename="pythonPackageDetails.csv"
fields=[]
rows=[]
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        print(row)
