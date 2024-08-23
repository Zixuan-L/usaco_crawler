import os
import requests
from bs4 import BeautifulSoup


def download(division_dictionary, save_directory):
    os.makedirs(save_directory, exist_ok=True)

    for division, data_list in division_dictionary.items():
        division_dir = os.path.join(save_directory, division)
        os.makedirs(division_dir, exist_ok=True)

        for data in data_list:
            problem_name = data['problem_name'].replace(' ', '_')

            if data['problem_link']:
                download_text_html((data['problem_link'] + '&lang=en'),
                                   os.path.join(division_dir, f"{problem_name}_problem_en.txt"))
                download_text_html((data['problem_link'] + '&lang=zh'),
                                   os.path.join(division_dir, f"{problem_name}_problem_zh.txt"))
            if data['test_data_link']:
                download_file(data['test_data_link'], os.path.join(division_dir, f"{problem_name}_test_data.zip"))
            if data['solution_link']:
                download_text_html(data['solution_link'], os.path.join(division_dir, f"{problem_name}_solution.txt"))


def download_file(url, save_path):
    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Downloaded: {save_path}")

    else:
        print(f"Failed to download: {url} (Status code: {response.status_code})")


def download_text_html(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text(separator='\n', strip=True)

        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(text_content)
        print(f"Saved text from: {url} to {save_path}")

    except requests.RequestException as e:
        print(f"Failed to download: {url}. Error: {e}")
    except Exception as e:
        print(f"Failed to save text from: {url}. Error: {e}")
