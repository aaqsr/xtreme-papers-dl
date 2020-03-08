from bs4 import BeautifulSoup
import multiprocessing
from functools import partial
import time
import requests
import urllib  
import os
from XTRME import *




''' handles input and outputs '''

# get code
print('please provide the syllabus number of the papers you wants to download:', end ='')
url_key = input()

# local code
if url_key in url_list:
	print('detected syllabus code, processing...')
	get_papers(url_list[url_key])

# online code
elif url_key.isdigit():
	print('syllabus code did not match local database, do you wish to get online database for syllabus code?')

	ans = input()
	if ans == 'y' or ans == 'yes':
		# seraching online
		print('Searching at online data base at {}'.format(online_url))
		get_code()
		if url_key in url_online:
			print('detected syllabus code, processing...')
			get_papers(url_online[url_key])
		else:
			print('invalid syllabus code.')
	else:
		print('invalid syllabus code.')
# provide url
elif url_key.startswith('http://') or url_key.startswith('https://'):

	print('url detected')
	print('downloading form the website {}'.format(url_key))
	get_papers(url_key)

else:
	print('invalid input please check your syllabus code / start your url with http')
