from __future__ import absolute_import
import os
import json
import re
import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class InstagramUser:

	def __init__(self,username):

		logging.debug('Retrieving valid access_token for API access')
		
		insta_user='instagramagile@gmail.com'
		insta_password='instagramagile12018'
		client_id='328c70d43d374d15b3d4887fcf51514c'
		redirect_uri='https://github.com/unb-cic-esw/instagram-data-monitor/'

		authorize_login_url = 'https://api.instagram.com/oauth/authorize/?client_id=%s&redirect_uri=%s&response_type=token&scope=basic+public_content'	% (client_id, redirect_uri)
		print('\n')
		print("URL de autorizacao::")
		print(authorize_login_url)

		options = Options()  
		options.add_argument("--headless")
		options.binary_location = '/usr/bin/google-chrome'

		driver = webdriver.Chrome(executable_path=os.path.abspath("drivers/linux-64/chromedriver"), options=options)
		driver.get(authorize_login_url)

		user_fld = driver.find_element_by_xpath('//*[@name="username"]')
		pass_fld = driver.find_element_by_xpath('//*[@name="password"]')
		login_btn = driver.find_element_by_xpath('//*[@value="Log in"]')
		user_fld.send_keys(insta_user)
		pass_fld.send_keys(insta_password)

		login_btn.click()
		current_url = driver.current_url

		print(current_url + '\n\n')

		access_token = re.match('.*#access_token=(.*)',current_url).group(1)

		logging.debug('access_token retrieved: %s' % access_token)

		# Buscar user_id a partir de um user_name.
		logging.debug('Retrieving %s\'s user id' % username)
		response = requests.get('https://www.instagram.com/%s/?__a=1' % username)
		user = response.json()
		# print("json resposta::")
		# print(user)
		# print("\n\n")
		# # user_id = user['user']['id']
		# print('\n\ngraphql::')
		# print(user['graphql'])
		# print('\n\ngraphql user')
		# print(user['graphql']['user'])
		# print('\n\ngraphql user id')		
		# print(user['graphql']['user']['id'])
		user_id = user['graphql']['user']['id']

		logging.debug('%s\'s id is %s' % (username,user_id))
		# Buscar o que interessa.
		logging.debug('Retrieving %s\'s user data' % username)
		response = requests.get('https://api.instagram.com/v1/users/%s/?access_token=%s' % (user_id,access_token))
		user = response.json()
		logging.debug('%s\'s user data: %s' % (username, user))

		self.id = user['data']['id']
		self.username = user['data']['username']
		self.name = 'oimundoembr'