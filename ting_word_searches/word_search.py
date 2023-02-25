from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def add_data(count, word, file_name):
    word_data = []
    if len(count) > 0:
        word_data.append({
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": count
        })
    return word_data


def verifyOccurrence(word, file_lines):
    count = []
    for i in range(len(file_lines)):
        line = file_lines[i].lower()
        if word.lower() in line:
            count.append({"linha": i + 1})
    return count


def exists_word(word, instance: Queue):
    for element in instance.queue:
        file_lines = element["linhas_do_arquivo"]
        file_name = element["nome_do_arquivo"]
        count = verifyOccurrence(word, file_lines)
        result = add_data(count, word, file_name)

    return result


project = Queue()
process("statics/nome_pedro.txt", project)
exists_word("pedro", project)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
