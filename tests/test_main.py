import unittest
from os import system as sys
from src.main import ator_from_url

class TesteAtor(unittest.TestCase):
	def teste_nome(self):
		usuario = ator_from_url('https://www.instagram.com/oimundoembr/')
		self.assertEqual('oimundoembr', usuario.nome)
		sys("rm *.html")
		
	def teste_seguidores(self):
		usuario = ator_from_url('https://www.instagram.com/oimundoembr/')
		self.assertEqual(0, usuario.seg)
		sys("rm *.html")

	def teste_postagens(self):
		usuario = ator_from_url('https://www.instagram.com/oimundoembr/')
		self.assertEqual(0, usuario.post)
		sys("rm *.html")

	def teste_nome_real(self):
		usuario = ator_from_url('https://www.instagram.com/oimundoembr/')
		self.assertEqual('instagram instagram', usuario.real)
		sys("rm *.html")