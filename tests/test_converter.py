import unittest
from converter import CSVConverter

class TestConverter(unittest.TestCase):
	
    converter = CSVConverter()

    def test_get_all_files_names_path_with_type_for_txt_in_root(self):
        self.assertEqual(self.converter.__get_all_files_names_path_with_type__('./*.txt'),['./requirements.txt'])

    def test_get_all_files_names_path_with_type_for_csv_in_root(self):
        self.assertEqual(self.converter.__get_all_files_names_path_with_type__('./*.csv'), [])

    def test_get_all_files_names_path_with_type_for_json_in_root(self):
        self.assertEqual(self.converter.__get_all_files_names_path_with_type__('./*.json'), [])

    def test_field_name_for_file_with_txt_file(self):
        self.assertEqual(self.converter.__field_name_for_file__('./requirements.txt'), ['decorator==4.0.11'])

    def test_field_name_for_file_with_readme_file(self):
        self.assertEqual(self.converter.__field_name_for_file__('./README.md'), ['# Monitor de Dados do Instagram'])

    def test_field_name_for_file_with_python_file(self):
        self.assertEqual(self.converter.__field_name_for_file__('./__init__.py'), ['from src.flask.main import app'])