import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import os

URL_SITE = 'https://www.solucionesparaladiabetes.com/magazine-diabetes/alimentacion/recetas-para-personas-con-diabetes/page/1/'

def get_data(url):
    

    response = requests.get(url)

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
        except:
            print('Error')
            
        data.append((item_title.text, item_link,item_img, item_calories))
        
    # # Convert to Json
    df = pd.DataFrame(data, columns=['title', 'link', 'img', 'calories'])
    df.to_json('recipes1.json', orient='records',indent=4, force_ascii=False,date_unit='ms')
    print(df)

# Upload json file 
json_file = 'recipes_data.json'
data_json = pd.read_json(json_file)
df_json = pd.DataFrame(data_json)
print(df_json.head(5))
print(df_json.shape)