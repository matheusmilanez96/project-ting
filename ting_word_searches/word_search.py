def exists_word(word, instance):
    found_instances = []
    for i in range(len(instance)):
        ocorrencias = []
        file = instance.search(i)
        index = 1
        for line in file["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                ocorrencias.append({"linha": index})
            index += 1
        if ocorrencias != []:
            data = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            }
            found_instances.append(data)
    return found_instances


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
