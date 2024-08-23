import requests
from bs4 import BeautifulSoup


def get_contests(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')

        contests_list = []

        for paragraph in paragraphs:
            link_tag = paragraph.find('a')

            if link_tag and 'href' in link_tag.attrs:
                contest_link = link_tag['href']

                if contest_link.endswith('results'):
                    contest_name = link_tag.text.strip()
                    full_contest_url = "https://usaco.org/" + contest_link
                    contests_list.append({
                        "name": contest_name,
                        "url": full_contest_url
                    })

        return contests_list

    else:
        print(f"Failed to retrieve the main page. Status code: {response.status_code}")

        return None
