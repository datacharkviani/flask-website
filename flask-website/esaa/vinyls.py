import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint


def get_vinyls():
    result = []

    for ind in range(1, 2):
        url = "https://vinyl.ge/product-category/rock/page/" + str(ind) + "/?orderby=rating"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        all_vinyl = soup.find('ul', class_='products columns-4')
        vinyls = all_vinyl.find_all('li', class_='product-type-simple')

        for vinyl in vinyls:
            v_features = vinyl.find('a', class_='woocommerce-LoopProduct-link')
            v_title = v_features.h2.text.strip()
            v_price = vinyl.find('bdi').text.strip()  # Get the text of the price

            result.append({'title': v_title, 'price': v_price})

        sleep(randint(1, 5))

    return result
