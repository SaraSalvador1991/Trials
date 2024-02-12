import csv
with open("C:\\Users\\sara\\Desktop\\cars.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)