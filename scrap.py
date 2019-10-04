import requests
import cssselect
from lxml import html
import codecs

file = codecs.open('code.sql', 'w+', 'utf-8')

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.94'
}

params = {}

for i in range(1, 80):
    params['page'] = str(i)

    response = requests.get('https://www.urionlinejudge.com.br/judge/en/problems/all', headers=headers, params=params)
    
    page = html.fromstring(response.text)

    for linha in page.cssselect('#element tbody tr'):
        colunas = linha.cssselect('td')

        problem_id =  colunas[0].cssselect('a')[0].text
        name =  colunas[2].cssselect('a')[0].text
        category =  colunas[3].cssselect('a')[0].text
        solved =  colunas[4].text.strip()
        level =  colunas[5].text.strip()

        file.write("insert into problems values ({}, '{}', '{}', {}, {})\n".format(problem_id, name.replace("'", "''"), category, solved.replace(',', ''), level))