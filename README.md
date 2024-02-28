```markdown
# Adicionar Colunas MySQL a partir de Dados de uma Coluna do Excel

Este script Python permite adicionar colunas a uma tabela MySQL e preenchê-las com dados de uma coluna específica de um arquivo Excel.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas Python: pandas e mysql-connector-python. Você pode instalá-las executando o seguinte comando:
  ```
  pip install pandas mysql-connector-python
  ```
- Um servidor MySQL configurado com uma tabela existente na qual você deseja adicionar as colunas.

## Uso

1. Clone este repositório ou faça o download do arquivo Python `adicionar_colunas_mysql.py`.

2. No arquivo Python `adicionar_colunas_mysql.py`, edite as seguintes variáveis:

   - `host`: O endereço do servidor MySQL.
   - `user`: O nome de usuário do servidor MySQL.
   - `password`: A senha do usuário do servidor MySQL.
   - `database`: O nome do banco de dados MySQL.
   - `tabela_mysql`: O nome da tabela MySQL à qual você deseja adicionar colunas.
   - `nome_coluna_excel`: O nome da coluna no arquivo Excel que contém os dados que você deseja adicionar à coluna MySQL.
   - `nome_nova_coluna_mysql`: O nome da nova coluna que você deseja adicionar à tabela MySQL.
   - `caminho_excel`: O caminho para o arquivo Excel que contém os dados.

3. Execute o script Python:

   ```
   python adicionar_colunas_mysql.py
   ```

4. O script irá adicionar uma nova coluna à tabela MySQL especificada e preenchê-la com os dados da coluna correspondente do arquivo Excel.

## Aviso

- Certifique-se de fazer backup dos seus dados antes de executar qualquer operação de alteração na sua base de dados MySQL.

## Contribuições

Contribuições são bem-vindas! Se você encontrar um problema ou tiver uma ideia para melhorar este script, sinta-se à vontade para abrir uma issue ou enviar um pull request.
