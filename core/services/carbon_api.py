import requests


BASE_URL = "https://api.carbonintensity.org.uk"


def fetch_current_intensity():
    response = requests.get(f"{BASE_URL}/intensity", timeout=20)
    response.raise_for_status()
    return response.json()