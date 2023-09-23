import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import os

URL_SITE = 'https://www.solucionesparaladiabetes.com/magazine-diabetes/alimentacion/recetas-para-personas-con-diabetes/page/2/'

response = requests.get(URL_SITE)

# print(response)

html_soup = BeautifulSoup(response.text, 'html.parser')

# print(html_soup)
data = []

for item in html_soup.find_all('div', class_='td_module_10'):
    # Obtener informacion basica de cada receta
    item_title = item.find('div', class_='item-details').h3.a
    item_img = item.find('div', class_='td-module-thumb').img.get('src')
    item_link = item_title.get('href')
    try:
        response_item = requests.get(item_link)
        html_soup_item = BeautifulSoup(response_item.text, 'html.parser')
        item_calories = (html_soup_item.find('div', class_='ERSNutrionDetails')).find('span',itemprop='calories').text
        # print(html_soup_item)
    except:
        print('Error')
        
    data.append((item_title.text, item_link,item_img, item_calories))
    # print(item_title.text, item_link,item_img, item_calories)
    

print(data[0][1])

# # Convert to Json
# df = pd.DataFrame(data, columns=['title', 'link', 'img', 'calories'])
# df.to_json('recipes3.json', orient='records',indent=4, force_ascii=False,date_unit='ms')
# print(df)