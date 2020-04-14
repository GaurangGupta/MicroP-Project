# importing the libraries
from bs4 import BeautifulSoup
import requests
 
url = "https://www.worldometers.info/coronavirus/"
try :
    html_content = requests.get(url).text
     
    soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find("div", attrs={"class": "main_table_countries_div"})
     
    table_data = table.tbody.find_all("tr") 
     
    f = open("worldometersscraped.txt", "w")
    for test in table_data :
        f.write(str(test))
        f.write('\nXXXX\n')
    f.close()
    
except :
    print('Check your internet connection and try again')