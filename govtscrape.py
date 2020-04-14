# importing the libraries
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.mohfw.gov.in/'

try:
    html_content = requests.get(url).text
     
    soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find("table", attrs={"class": "table table-striped"})

    data = table.tbody.find_all("tr") 
     
    f = open("mohfwscraped.txt", "w")
    for test in data :
        f.write(str(test))
    f.close()
    
except :
    print('Check your internet connection and try again')