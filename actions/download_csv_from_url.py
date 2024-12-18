import urllib.request, pandas

url = f'url_que_recebe_um_csv_como_resposta'
filePath = 'arquivo.csv'
urllib.request.urlretrieve(url, filePath)

df = pandas.read_csv(filePath, header=0)
print(df) 

for indice in df.index:
  for coluna in df.columns:
    print(df[coluna][indice])