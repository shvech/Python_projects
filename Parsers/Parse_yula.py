import requests


def parse_yula():
    # В этом примере я использую API Юлы, отправляя GET-запрос на URL
    # "https://api.yula.by/v1/listings" с определенными параметрами. Затем я получаю ответ в формате JSON и
    # извлекаю нужные данные о товарах.
    url = "https://api.yula.by/v1/listings"
    params = {
        "category_id": 2,  # Идентификатор категории (детские товары)
        "limit": 10,  # Количество товаров для вывода
        "sort": "-creation_time",  # Сортировка по времени создания (сначала новые)
    }
    # Добавил headers в запрос, что может помочь обойти защитные механизмы сайта
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36",
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    for item in data['listings']:
        title = item['title']
        price = item['price']
        location = item['location']['address']
        print("Title:", title)
        print("Price:", price)
        print("Location:", location)
        print()


if __name__ == "__main__":
    parse_yula()
