import pandas as pd
import requests
from bs4 import BeautifulSoup

name = []
price = []
rating = []
stock = []
category = []

convert = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

headers = {
    'User-Agent': 'Mozilla/5.0'
}

for j in range(1, 51):

    url = f'https://books.toscrape.com/catalogue/page-{j}.html'
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for i in books:
        
        # title
        name.append(i.h3.a['title'])

        # price
        price.append(i.find('p', class_='price_color').text.strip())

        # rating
        rating_class = i.find('p', class_='star-rating')['class'][1]
        rating.append(convert[rating_class])

        # stock
        stock.append(i.find('p', class_='instock availability').text.strip())

        # detail page link
        book_link = i.h3.a['href']
        full_link = "https://books.toscrape.com/catalogue/" + book_link

        # request detail page
        detail_response = requests.get(full_link, headers=headers)
        detail_soup = BeautifulSoup(detail_response.text, 'html.parser')

        # category from breadcrumb
        breadcrumb = detail_soup.find('ul', class_='breadcrumb')
        category_name = breadcrumb.find_all('a')[2].text.strip()
        category.append(category_name)

df = pd.DataFrame({
    'name': name,
    'price': price,
    'rating': rating,
    'stock': stock,
    'category': category
})

df.to_csv('book_data.csv')