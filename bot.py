import sys
import requests
import cssselect
from lxml import html
import codecs

languages = {
    'c': 1,
    'c++': 2,
    'java7': 3,
    'python2': 4,
    'python3': 5,
    'ruby': 6,
    'c#': 7,
    'scala': 8,
    'lua': 9,
    'javascript': 10,
    'java8': 11,
    'go': 12,
    'c99': 14,
    'kotlin': 15,
    'c++17': 16,
    'haskell': 17,
    'ocaml': 18,
    'pascal': 19
}

with open(sys.argv[3]) as file:
    code = file.read()

with open('session') as file:
    cookies = dict(c.split('=') for c in file.readline().replace(';', '').strip().split(' '))

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.94'
}

data = {
    '_method': 'POST',
    'problem_id': sys.argv[1],
    'language_id': languages[sys.argv[2].lower()],
    'template': 1,
    '_csrfToken': cookies['csrfToken'],
    'source_code': code
}

response = requests.post('https://www.urionlinejudge.com.br/judge/en/runs/add', headers=headers, cookies=cookies, data=data)

if response.status_code != 200:
    print('Erro ao submeter código')
    exit(0)

while True:
    page = html.fromstring(requests.get('https://www.urionlinejudge.com.br/judge/pt/runs', headers=headers, cookies=cookies).text)
    result = page.cssselect('#element tbody tr td')[4].text_content().strip()
    executiontime = page.cssselect('#element tbody tr td')[6].text_content().strip()

    if result != '- In queue -':
        print(result)
        print(executiontime)
        break