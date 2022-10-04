from bs4 import BeautifulSoup
import requests
import pandas as pd
from csv import writer
import states

url = 'https://ucr.fbi.gov/hate-crime/2019/tables/table-13-state-cuts/'

with open('hate_crime_data.csv', 'w', encoding='utf8', newline='') as f:         #This part will iterate through each th or td element and extract the text information we want.
    file_writer = writer(f)                                                      #Which would be the city names and their corresponding # of hate crimes per category.
    header = ['City', 'Ethnicity/Race', 'Religion', 'Sexual Orientation']        #The information will get written to a csv for us to use.
    file_writer.writerow(header)

    for state in states.states_list:                  #This will iterate through each state (with exceptions)
        page = requests.get(url + state + '.xls')     #String ending for each web page
        soup = BeautifulSoup(page.text, 'lxml')

        table = soup.find('table', {'class':'data'}) 
        for city in table.find_all('tbody'):
            rows = city.find_all('tr')

            for row in rows:
                city_names = row.find('th').text.strip()
                ethnicity_race = row.find_all('td')[0].text.strip()
                religion = row.find_all('td')[1].text.strip()
                sexual_orientation = row.find_all('td')[2].text.strip()
                each_city = [city_names, ethnicity_race, religion, sexual_orientation]
                file_writer.writerow(each_city)