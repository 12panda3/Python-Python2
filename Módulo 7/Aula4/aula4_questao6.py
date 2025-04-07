import pandas

dados = pandas.read_csv('spotify-2023.csv', encoding='latin-1')
dados = dados[dados['released_year'].between(2012, 2022)]

dados = dados[~dados['track_name'].astype(str).str.contains('"')]
dados = dados[~dados['artist(s)_name'].astype(str).str.contains('"')]

dados['streams'] = dados['streams'].astype(int)

topAno = dados.loc[dados.groupby('released_year')['streams'].idxmax()]
topAno = topAno[['track_name', 'artist(s)_name', 'released_year', 'streams']]
topAno = topAno.sort_values('released_year')

result = topAno.values.tolist()

for i in result:
    print(i)