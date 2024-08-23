def get_information(title):
    history_panel = title.find_next_sibling()

    data_list = []

    while history_panel and not (history_panel.name in ['h2', 'h3']):
        if history_panel.name == 'div' and 'historypanel' in history_panel.get('class', []):
            problem_number = history_panel.find('h1').text.strip()
            problem_name = history_panel.find('b').text.strip()
            links = history_panel.find_all('a')

            problem_link = None
            test_data_link = None
            solution_link = None

            for link in links:
                href = link['href']

                if 'viewproblem' in href:
                    problem_link = "https://usaco.org/" + href
                elif 'zip' in href:
                    test_data_link = "https://usaco.org/" + href
                elif 'sol_' in href:
                    solution_link = "https://usaco.org/" + href

            data_list.append({
                "problem_number": problem_number,
                "problem_name": problem_name,
                "problem_link": problem_link,
                "test_data_link": test_data_link,
                "solution_link": solution_link
            })

        history_panel = history_panel.find_next_sibling()

    return data_list
