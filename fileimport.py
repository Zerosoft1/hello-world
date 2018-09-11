import csv
with open('device.csv) as csvfile:
	testreader = csv.reader(csvfile)
	for row in testreader:
		print ','.join(row)