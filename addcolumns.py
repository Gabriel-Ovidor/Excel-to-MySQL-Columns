import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="seu_host",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

tabela_mysql = 'sua_tabela'

nome_coluna_excel = 'nome_coluna_excel'
nome_nova_coluna_mysql = 'nova_coluna_mysql'

caminho_excel = 'caminho_para_o_arquivo_excel.xlsx'
dados_excel = pd.read_excel(caminho_excel)

dados_nova_coluna_mysql = dados_excel[nome_coluna_excel]

cursor = conn.cursor()
try:
    
    cursor.execute(f"ALTER TABLE {tabela_mysql} ADD COLUMN {nome_nova_coluna_mysql} VARCHAR(255)")
    
    for index, valor in enumerate(dados_nova_coluna_mysql):
        cursor.execute(f"UPDATE {tabela_mysql} SET {nome_nova_coluna_mysql} = %s WHERE id = %s", (valor, index+1))
    
    conn.commit()
    print("Coluna adicionada com sucesso e dados inseridos.")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    conn.close()
