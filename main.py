import os

from contests import get_contests
from divisions import get_divisions
from download import download


def main():
    download_path = input("Download path (e.g., C:\\USACO_Downloads): ").strip()

    if not os.path.exists(download_path):
        try:
            os.makedirs(download_path)
            print(f"Directory created: {download_path}")

        except Exception as e:
            print(f"Failed to create directory: {download_path}. Error: {e}")

            return

    url = "https://usaco.org/index.php?page=contests"
    contests_list = get_contests(url)

    if contests_list:
        for contest in contests_list:
            save_directory = os.path.join(download_path, f"{contest['name'].replace(' ', '_')}_downloads")
            divisions_dictionary = get_divisions(contest['url'])

            if divisions_dictionary:
                download(divisions_dictionary, save_directory)

                """
                print(f"Results for {contest['name']}:")
                for division, data_list in divisions_dictionary.items():
                    print(f"  {division} Division:")
                    for data in data_list:
                        print(f"    Problem {data['problem_number']}: {data['problem_name']}")
                        print(f"      Problem Link: {data['problem_link']}")
                        print(f"      Test Data: {data['test_data_link']}")
                        print(f"      Solution: {data['solution_link']}")
                    print()
                """

            else:
                print(f"Failed to fetch divisions for {contest['name']}")
            """
            print("-----------------------------------------------------")
            """


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
