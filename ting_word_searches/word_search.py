from ting_file_management.queue import Queue


def add_file(count, file, word):
    return count.append({
        "palavra": word,
        "arquivo": file["nome_do_arquivo"],
        "ocorrencias": count
    })


def verifyOccurrence(word, file, lines):
    count = []
    for i in range(len(lines)):
        if word.lower() in lines[i].lower():
            count.append({"linha": i + 1})
            add = add_file(count, file, word)
    return add


def exists_word(word, instance: Queue):
    for i in range(len(instance)):
        search_file = instance.search(i)
        lines = search_file["linhas_do_arquivo"]

        count_and_add = verifyOccurrence(word, search_file, lines)
    return count_and_add


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
