from bs4 import BeautifulSoup
import requests
import json
import better_exceptions
url = 'http://www.utilityconnection.com/page2c.asp#S'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
companiesArray = []
for company in content.findAll('li'):
    companyObject = {
        "name": company.find('a').text
    }
    (print(companyObject))

    companiesArray.append(companyObject)


with open('companyNames.json', 'w') as outfile:
     json.dump(companiesArray, outfile)
