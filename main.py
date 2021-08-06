import requests
from bs4 import BeautifulSoup
from snils import snils

url = 'https://gumrf.ru/reserve/abitur/hod/?type=111'

m = []
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

tables = soup.find('table', {'class': 'table'})
for i in range(6, 751):
    table = tables.findAll('tr')[i].find_all('td')
    if table[1].text == snils:
        m = [table[i].text for i in range(len(table))]
        print("место: ", m[0])
        print("снилс: ", m[1])
        print("общий балл: ", m[2])
        print("есть ли согласие: ", m[-3])
        print("согласие на другом направлении: ", m[-2])
        #тут прога принтанет количество согласий, и моё место в списке согласий, а пока coming soon




