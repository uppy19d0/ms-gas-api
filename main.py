# 2023 04/01/2023

# Luis Aneuris Tavarez De Jesus

# Api Scraper Precio de gasolina de Republica Dominicana


# Importamos las librerias
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import time
import os
import uvicorn
from fastapi import FastAPI

from tools.lenguage import Translate


app = FastAPI()
lenguage = Translate()


@app.get("/products")
async def products():

    # Capturamos la url
    url = "https://www.revistamercado.do/economia/precios-de-los-combustibles-rd"

    # Capturamos el hml de la pagina web y creamos un objeto Response
    r = requests.get(url)
    data = r.text

    # Creamos el objeto soup y le pasamos lo capturado con request
    soup = BeautifulSoup(data, 'lxml')

    # Buscamos el table
    table1 = soup.find('table')

    products = []
    for i in table1.find_all('tr'):
        element = i.text.split("\n")
        if element[1] is not None and element[2] is not None and element[3] is not None:
            product = {element[1], element[2], element[3]}
            products.append(product)

    return {"response": products, "code": 200, "source url": "https://www.revistamercado.do/economia/precios-de-los-combustibles-rd", "dateRequest": datetime.now(), "language": "en"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
