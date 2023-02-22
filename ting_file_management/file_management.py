# Referencia [1]
from pathlib import Path
import sys


def txt_importer(path_file):
    try:
        # Formato diferente de .txt;
        if Path(path_file).suffix != '.txt':
            return print('Formato inválido', file=sys.stderr)
        # Referencia [2]
        with open(path_file, mode='r') as file:
            content = file.readlines()
        content = [line.rstrip('\n') for line in content]
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
# Referencias:
# [1]-https://pt.stackoverflow.com/questions/382049
# [2]- https://horadecodar.com.br/2021/03/13/
#     como-ler-um-arquivo-linha-por-linha-em-uma-lista-python/
