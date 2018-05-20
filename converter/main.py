import csv
import json
import glob
import re
import os

class CSVConverter:

    def convert_all_collected_data_in_csv_to_json(self):
        files = self.__get_all_files_names_path_with_type__('./csv/*.csv')

        for file in files:
            fieldnames = self.__field_name_for_file__(file)
            json_name = file[6:33] + '.json'
            self.__convert_csv_to_json__(file, json_name, fieldnames)

    def convert_all_actors_from_csv_to_json(self):
        fieldnames = ("name", "link", "followers", "following", "posts", 'username')
        self.__convert_csv_to_json__('./src/csv_to_json/atores.csv', 'atores.json', fieldnames)
        

    def convert_all_stories_data_from_csv_to_json(self):
        files = self.__get_all_files_names_path_with_type__('./src/stories/stories/*.csv')

        for file in files:
            fieldnames = ("username", "data", "stories")
            json_name = file[22:38] + '.json'
            self.__convert_csv_to_json__(file, json_name, fieldnames)


    def __convert_csv_to_json__(self, csvname, jsonname, fieldnames):
        csv_file = open(csvname, 'r')
        json_file = open('./json/' + jsonname, 'w', encoding='utf8')
        self.__create_json__(fieldnames, csv_file, json_file)
        csv_file.close()
        json_file.close()


    def __field_name_for_file__(self, filename):
        fieldnames = ''
        file = open(filename, 'r')
        for text in file:
            fieldnames = text.split(',')
            break
        fieldnames[-1] = fieldnames[-1][:-1]
        file.close()
        return fieldnames


    def __get_all_files_names_path_with_type__(self, path):
        files = []
        for file in glob.glob(path):
            files.append(file)
        return files


    def __create_json__(self, fieldnames, csvfile, jsonfile):
        reader = csv.DictReader(csvfile, fieldnames)
        counter = 0
        for row in reader:
            if counter == 0:
                counter = 1
            else:
                json.dump(row, jsonfile, ensure_ascii = False)
                jsonfile.write('\n')
    
