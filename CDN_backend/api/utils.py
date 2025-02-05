import requests


def get_city_coordinates(city_name):
    """ Получает координаты города. """
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city_name, "format": "json", "limit": 1}
    headers = {
        "User-Agent": "CDN/1.0 (daniil.esakov@mail.ru)"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        if response.json():
            data = response.json()[0]
            latitude = float(data["lat"])
            longitude = float(data["lon"])
            return latitude, longitude
        else:
            return None

    except requests.exceptions.RequestException:
        return None
