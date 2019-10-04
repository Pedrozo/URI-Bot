import requests
import cssselect
import codecs

from lxml import html

cookies = {
    'judge': 'usjahq4ht3tb8scrhcu5o5ftqk',
    'csrfToken': '83f7e1301f98c1259bcebabd25df85097b3c07e5a2de7ea396f2b283285400d7263a8e83f7c4a85ef634cbe754d853fc726ca264cac4922eb1e1d110aec727c9'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.94'
}

response = requests.get('https://www.urionlinejudge.com.br/judge/en/runs/add', headers=headers, cookies=cookies)
print(response)


data = {
    '_method': 'POST',
    '_csrfToken': cookies['csrfToken'],
    'problem_id': 1001,
    'language_id': 16,
    'template': 1,
    'source_code': '''
#include <iostream>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    cout << "X = " << a + b << endl;
 
    return 0;
}'''
}

response = requests.post('https://www.urionlinejudge.com.br/judge/en/runs/add', headers=headers, cookies=cookies, data=data)

print(response)