import requests
from bs4 import BeautifulSoup

URL = "https://listado.mercadolibre.com.pe/iphone-15"


res = requests.get(URL)
products = {}

if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    titles = soup.find_all("h3", class_="ui-search-item__title")
    prices = soup.find_all("span", class_="andes-money-amount__fraction")
    stars = soup.find_all("span", class_="ui-search-reviews__rating-number")
    distributors = soup.find_all(
        "p",
        class_="ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY",
    )

    counter = 1

    for title, price, star, distributor in zip(titles, prices, stars, distributors):
        product = {
            "title": title.text.strip(),
            "price": price.text.strip(),
            "stars": star.text.strip(),
            "distributor": distributor.text.strip(),
        }
        products[counter] = product
        counter += 1
    print(products)

else:
    print("Error al obtener el contenido de la página:", res.status_code)
