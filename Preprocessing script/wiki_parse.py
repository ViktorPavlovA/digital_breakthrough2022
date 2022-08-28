""" Код для парсинга численности населения региона и площади региона с википедии.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def get_digits_population(my_string):
    # При парсинге с википедии, кроме цифр парсятся еще лишние знаки, которые убираем
    digits = re.findall("\d+", my_string)
    if isinstance(digits, list):
        digits = ''.join(digits)
    return digits

def del_spaces_area(my_string):
    # Удаляем лишние пробелы при парсинге площади региона
    area = re.sub(r"\s+", "", my_string)
    return area

def wiki_parse(URL):
    page = requests.get(URL)
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')
    # Заходим в таблицу, где указаны нужные данные
    # в разрезе по регионам
    tables = soup.find_all('table')

    #  Ищем в классе 'standard' и 'sortable'
    table = soup.find('table', class_='standard sortable')
    # Создаем датафрейм для записи результата
    # subject_name - название региона
    df = pd.DataFrame(columns=['subject_name', 'population', 'area'])

    # Собираем данные по регионам по очереди
    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')
        if (columns != []):
            subject_name = columns[1].text.strip()
            population = get_digits_population(columns[2].text.strip())
            area = del_spaces_area(columns[8].text)

            df = df.append(
                {'subject_name': subject_name, 'population': population, 'area': area}, ignore_index=True)

    df['population'] = df['population'].astype(int)
    df['area'] = df['area'].astype(int)

    df.to_csv('subject_name_data.csv', index=False)

if __name__ == '__main__':
    URL = r"https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D1%83%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8"
    wiki_parse(URL)
