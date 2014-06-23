
import json
import csv
import os
import datetime

def is_non_zero_file(fpath):  
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False
seen_dates = []

number = 0
with open('temp/temp_data.json') as temp_file:
	json_data = json.load(temp_file)
	for line in json_data:
		comp =line['company']
		date = datetime.datetime.strptime(line['date'],"%Y/%m/%d").strftime('%Y-%m-%d')
		if date not in seen_dates:
			seen_dates.append(date)

		with open('data/'+comp+'.csv','a+') as datafile:
			d = csv.writer(datafile)
			if not is_non_zero_file('data/'+comp+'.csv'):
				d.writerow(['Date','Open','High','Low','Close','Volume', 'Adj Close','Num_deals','Value','Change','Change_per'])
			d = csv.writer(datafile)
			info = [date, line['opening'], line['high'],line['low'], line['close'],line['volume'],line['close'],line['num_deals'],line['value'],line['change'],line['change_per']]
			d.writerow(info)

with open('added_dates.txt', 'a+') as f:
	for d in seen_dates:
		f.write(d+'\n')

os.remove('temp/temp_data.json')

# with open('temp/temp_data.csv', 'rbU') as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter=',')
# 	next(spamreader)

# 	for row in spamreader:
# 		with open(row[0]+'.csv','a+') as datafile:
# 			d = csv.writer(datafile)
# 			if not is_non_zero_file('data/'+row[0]+'.csv'):
# 				d.writerow(['Date','Open','High','Low','Close','Volume', 'Adj Close','Num_deals','Value','Change','Change_per'])
# 			d = csv.writer(datafile)
# 			d.writerow(row[1:])



print "####Done"