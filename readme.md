- AUTH :Luis Aneuris Tavarez De Jesus
- Github: https://github.com
- Linkedlin: https://www.linkedin.com/in/luis-aneuris-tavarez-de-jesus-a2400b174/
- Date 2023 04/01/2023

# LOCAL:

http://localhost:8000/products

# ENDPOINT

    HTTP:GET
    /products
    Description:

Documentacion URL

http://localhost:8000/docs#/

# Production

http://HOST:8000/products

# ENDPOINT

    HTTP:GET
    /products

    # English
    Description:This is a project to make a scraper to find the price of fuels in Dominican Republic.

    # Spanish
    Esto es un proyecto que realizar un scraper para buscar precio de los combutibles de republica dominicana.

    Example Response

http://HOST:8000/docs#/

# Documentacion URL

```JSON
{
    "response": [
        [
            "Precio de esta semana",
            "Combustible",
            "Variación"
        ],
        [
            "Gasolina Premium",
            "RD $293.60",
            "RD$ 0"
        ],
        [
            "RD $241.10",
            "Gasoil Óptimo",
            "RD$ 0"
        ],
        [
            "RD $274.50",
            "Gasolina Regular",
            "RD$ 0"
        ],
        [
            "Gasoil Regular",
            "RD $221.60",
            "RD$ 0"
        ],
        [
            "Kerosene",
            "RD $338.10",
            "RD$ 0"
        ],
        [
            "RD $147.60",
            "Gas Licuado (GLP)",
            "RD$ 0"
        ],
        [
            "Gas Natural (GNV)",
            "RD $28.97",
            "RD$ 0"
        ]
    ],
    "language":"en",
    "code": 200,
    "source url": "https://www.revistamercado.do/economia/precios-de-los-combustibles-rd",
    "dateRequest": "2023-01-04T21:00:38.022352"
}
```

# Corre proyecto

uvicorn main:app --reload