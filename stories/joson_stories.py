import csv
import json
import time
import re
csvfile = open('stories.csv', 'r')
jsonfile = open('stories.json', 'w')

fieldnames = ("Username","Data","Stories")
reader = csv.DictReader( csvfile, fieldnames)
i=1
for row in reader:
	if i ==1:
		i+=1	
	else:	
		json.dump(row, jsonfile, indent=3)
		jsonfile.write('\n')