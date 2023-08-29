import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for file in range(len(instance)):
        if instance.search(file)["nome_do_arquivo"] == path_file:
            return None

    content = txt_importer(path_file)

    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content
    }

    instance.enqueue(output)
    sys.stdout.write(f"{output}")  # test


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
