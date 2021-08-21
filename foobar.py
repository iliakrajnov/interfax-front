from interfax import *
from json import load, dumps

with open('dataset_public.json', encoding='utf-8') as file:
    data = load(file)

res = []
for i in data:
    now = [i['title']]

    to_tr = []
    for article in i['news']:
        to_tr.append(article['body'])

    now.append(' '.join(train(to_tr).keys()))
    res.append(now)


with open('res.csv', 'w', encoding='utf-8') as file:
    file.write('0;1;\n')
    for i in res:
        file.write(';'.join(i) + ';\n')

