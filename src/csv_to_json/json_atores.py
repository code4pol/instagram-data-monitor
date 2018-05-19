import csv
import json
import time
import re

csvfile = open('atores.csv', 'r')
jsonfile = open('atores.json', 'w', encoding='utf8')

fieldnames = ("Nome Real","Conta","Seguidores", "Seguindo", "Postagens")
reader = csv.DictReader( csvfile, fieldnames)
i=1
for row in reader:
	row["Nome Real"] = re.sub("(;/s)", "", row["Nome Real"])
	if i ==1:
		i+=1
	else:	
		json.dump(row, jsonfile, indent=5, ensure_ascii=False)
		jsonfile.write('\n')
	