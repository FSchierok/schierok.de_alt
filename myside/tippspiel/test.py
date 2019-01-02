from time import localtime, strftime
import requests
from bs4 import BeautifulSoup


RESULTS_PAGE_URL = 'https://www.hltv.org/results?stars=1'
current_date = strftime('%B %d %Y')

html_source = requests.get(RESULTS_PAGE_URL).text
soup = BeautifulSoup(html_source, 'lxml')

print(soup.title.get_text())
print(f'Results for {current_date}\n')


def current_games(tag):
    is_result_tag = tag.name == 'div' and 'result-con' in tag.get('class', [])
    if not is_result_tag:
        return False

    timestamp = int(tag['data-zonedgrouping-entry-unix']) / 1000
    return strftime('%B %d %Y', localtime(timestamp)) == current_date


for result in soup(current_games):
    losing_team = result.select_one('.team').get_text()
    losing_team_score = result.select_one('.score-lost').get_text()

    winning_team = result.select_one('.team.bold').get_text()
    winning_team_score = result.select_one('.score-won').get_text()

    event = result.select_one('.event-name').get_text()

    print(f'{winning_team} {winning_team_score} - {losing_team_score} {losing_team}')
    print(f'{event}\n')
