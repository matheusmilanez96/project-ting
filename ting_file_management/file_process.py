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
    sys.stdout.write(f"{output}")


def remove(instance):
    if len(instance) < 1:
        print("Não há elementos", file=sys.stdout)
        return None

    file = instance.dequeue()
    print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)

        print(f"{file}")

    except IndexError:
        print("Posição inválida", file=sys.stderr)
