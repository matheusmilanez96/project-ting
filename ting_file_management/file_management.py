import sys


def txt_importer(path_file):
    try:
        if path_file.endswith(".txt"):
            with open(path_file, "r") as file:
                content = file.read().split("\n")
                print(content)
            return content
        else:
            print("Formato inválido", file=sys.stderr)

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
