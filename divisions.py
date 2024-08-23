import requests
from bs4 import BeautifulSoup

from data import get_information


def get_divisions(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2')

        divisions_dictionary = {"Platinum": [], "Gold": [], "Silver": [], "Bronze": []}

        for title in titles:
            header = title.get_text().strip().lower()

            if "platinum" in header:
                current_division = "Platinum"
            elif "gold" in header:
                current_division = "Gold"
            elif "silver" in header:
                current_division = "Silver"
            elif "bronze" in header:
                current_division = "Bronze"
            else:
                continue

            division_data = get_information(title)
            divisions_dictionary[current_division].extend(division_data)

        return divisions_dictionary

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

        return None
