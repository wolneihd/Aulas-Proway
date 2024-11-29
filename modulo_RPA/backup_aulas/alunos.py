from bs4 import BeautifulSoup
import pandas as pd

html = '''
<table>
    <tr>
        <th>Nome</th>
        <th>Idade</th>
    </tr>
    <tr>
        <td>João</td>
        <td>20</td>
    </tr>
    <tr>
        <td>Ana</td>
        <td>22</td>
    </tr>
</table>'''

soup = BeautifulSoup(html, features='html.parser')
table = soup.find("table")

data = {}
for linha in table.find_all('tr')[1:]:
    cols = linha.find_all('td')
    chave = cols[0].text
    valor = cols[1].text
    data[chave] = valor

df = pd.Series(data, name='tabela de alunos')
print(df.head())

isAna = 'Ana' in df.index
print('Ana presente na lista' if isAna else 'Ana não está presente')

