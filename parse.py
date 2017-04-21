# Парсинг таблицы с сайта
from bs4 import BeautifulSoup
import requests


URL = 'http://snow-motion.ru/tablica-bzhu-kalorijnost'


def get_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    return soup.prettify()


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")

    products = []

    for row in soup.table.find_all('tr')[1:]:
        td = row.find_all('td')
        products.append({
                "name": td[0].text.strip(),
                "protein": float(td[1].text.strip().replace(",", ".")),
                "fat": float(td[2].text.strip().replace(",", ".")),
                "carbohydrates": float(td[3].text.strip().replace(",", ".")),
                "calories": float(td[5].text.strip().replace(",", ".")),
            })

    return products


def print_table(products):
    for pr in products:
        print("{0} {1} {2} {3} {4}"
              .format(pr["name"], pr["protein"], pr["fat"], pr["carbohydrates"], pr["calories"]))


def main():
    html = get_html(URL)
    products = parse_html(html)
    print_table(products)

if __name__ == '__main__':
    main()
