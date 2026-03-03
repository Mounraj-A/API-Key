# amazon_api.py

import requests
from config import RAPIDAPI_KEY, RAPIDAPI_HOST


def search_products(keyword):

    url = "https://real-time-amazon-data.p.rapidapi.com/search"

    querystring = {
        "query": keyword,
        "country": "IN",
        "page": "1",
        "sort_by": "RELEVANCE",
        "product_condition": "ALL"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        print("Error:", response.text)
        return []

    data = response.json()

    products = []

    if "data" in data and "products" in data["data"]:

        for item in data["data"]["products"]:

            product = {
                "title": item.get("product_title", "No Title"),
                "image": item.get("product_photo", ""),
                "price": item.get("product_price", "Not Available"),
                "old_price": item.get("product_original_price", ""),
                "rating": item.get("product_star_rating", "No Rating"),
                "reviews": item.get("product_num_ratings", "0"),
                "offer": item.get("product_badge", ""),
                "url": item.get("product_url", "#")
            }

            products.append(product)

    return products