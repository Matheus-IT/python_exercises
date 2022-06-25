import pandas as pd

file_name: str = '05Explorando_arquivos/salarios.csv'
dados = None

try:
    dados = pd.read_csv(file_name, sep=',')
except (FileNotFoundError, FileExistsError):
    print('Erro ao abrir o arquivo')
df = pd.DataFrame(dados, columns=['Name', 'Position Title', 'Department', 'Employee Annual Salary'])
print(df['Employee Annual Salary'])
