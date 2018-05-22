from converter import FileConverter
from flask import Flask, jsonify
import json

converter = FileConverter()
converter.convert_all_collected_data_in_csv_to_json()
converter.convert_all_actors_from_csv_to_json()
converter.convert_all_stories_data_from_csv_to_json()
