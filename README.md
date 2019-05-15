# UtilityScraper's Build Instructions

#Set up Python's virutal environment in terminal

python3 -m venv UtilityScraper-env

source UtilityScraper-env/bin/activate

#Install and import libraries

pip install bs4

pip install requests

from bs4 import BeautifulSoup

import requests

#Run 

python utilityScrape.py

#Results stored in companyNames.json
