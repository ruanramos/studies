import csv

with open('Apadrinhamento LoL UFRJ - Página1.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')

	for row in readCSV:
		print(row)