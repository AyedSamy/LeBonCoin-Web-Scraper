import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.leboncoin.fr/voitures/offres/p-1'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def main():
    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    all_products = soup.select('div[class=_2heYd]')

    product_names = []
    product_prices = []
    secure_payments = []
    professional_sales = []
    product_locations = []
    publication_dates = []

    def get_name(product):
        return product.select('p[data-qa-id=aditem_title]')[0].text
    
    def get_price(product):
        return product.select('span._1C-CB')[0].text.replace('\xa0', '')
    
    def get_secure_payment(product):
        try:
            return product.select('span.KS-Pr._3O-wP')[0].text
        except:
            return 'none'
    
    def get_professional(product):
        if product.select('div._3u7dT._1cC_m'):
            return 'pro'
        else:
            return 'standard'
    
    def get_location(product):
        return product.select('div._1UzWr')[1].text

    def get_date(product):
        return product.select('div._1UzWr')[2].text

    for v in all_products:
        product_names.append(get_name(v))
        product_prices.append(get_price(v))
        secure_payments.append(get_secure_payment(v))
        professional_sales.append(get_professional(v))
        product_locations.append(get_location(v))
        publication_dates.append(get_date(v))

    print(len(product_names), len(product_prices), len(secure_payments), len(professional_sales), len(product_locations), len(publication_dates))
    print(product_names)
    print(product_prices)
    print(secure_payments)
    print(professional_sales)
    print(product_locations)
    print(publication_dates)
    

if __name__ == '__main__':
    main()