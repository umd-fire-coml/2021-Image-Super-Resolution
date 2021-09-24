#Code based on https://stereopickle.medium.com/how-to-download-unzip-zip-files-in-python-5f326bb1a829 and https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
from bs4 import BeautifulSoup
import requests
import re
import os
#from io import BytesIO
from zipfile import ZipFile
#from urllib.request import urlopen

html_page = requests.get('https://data.vision.ee.ethz.ch/cvl/DIV2K/')
soup = BeautifulSoup(html_page.content, 'html.parser')

# find all a href links that contain ".zip" available on this page
file_urls = soup.findAll('a', href = re.compile(".zip"))
links = [link.get('href') for link in file_urls] 

# make directory to store all the images
div2kpath = os.path.join(os.curdir, "DIV2K")
if not os.path.isdir(div2kpath):
	os.mkdir(div2kpath)

for link in links:
	# make directory name
	name = link[40:-4]
	# open url
	print('Starting download of 'f'{name}')
	zipath = os.path.join(div2kpath, name + ".zip")
	with requests.get(link, stream=True) as r:
		r.raise_for_status()
		with open(zipath, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)
	print(f'{name} Downloaded')
	# read zipfile
	zipfile = ZipFile(zipath)
	# extract image files to the div2k directory
	zipfile.extractall(path = div2kpath)
	# let me know how much it is completed.
	print(f'{name} Extracted')
	# close zipfile we don't need
	zipfile.close()
	os.remove(zipath)
