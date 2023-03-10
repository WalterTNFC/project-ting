import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    # Acessar a lista do texto importado:
    list_to_convert = txt_importer(path_file)

    # Cria dicionário da lista para ser salvo
    new_data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(list_to_convert),
        'linhas_do_arquivo': list_to_convert,
    }

    # Se já existir, não é salvo
    for fileListed in instance.queue:
        if fileListed['nome_do_arquivo'] == new_data['nome_do_arquivo']:
            return None

    instance.enqueue(new_data)
    print(new_data, file=sys.stdout)


def remove(instance: Queue):
    try:
        removed_file = instance.dequeue()['nome_do_arquivo']
        print(f'Arquivo {removed_file} removido com sucesso', file=sys.stdout)
    except IndexError:
        print('Não há elementos')


def file_metadata(instance: Queue, position):
    try:
        search = instance.search(position)
        print(search)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
