
import csv
import os

def is_non_zero_file(fpath):  
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False

number = 0

with open('tadawul_data.csv', 'rbU') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	next(spamreader)

	for row in spamreader:
		with open(row[0]+'.csv','a+') as datafile:
			d = csv.writer(datafile)
			if not is_non_zero_file(row[0]+'.csv'):
				d.writerow(['Date','Open','High','Low','Close','Volume', 'Adj Close','Num_deals','Value','Change','Change_per'])
			d = csv.writer(datafile)
			d.writerow(row[1:])



print "####Done"