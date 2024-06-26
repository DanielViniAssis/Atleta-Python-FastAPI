import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH / "novo-diretorio")

try:
    with open(ROOT_PATH / "novo.txt", "w", encoding= "utf-8") as arquivo:
        arquivo.write("Aprendendo a escrever e ler")
except IOError as exc:
    print(f"Não foi possivel abrir o arquivo {exc}")

try:
    with open(ROOT_PATH / "novo.txt", "r", encoding= "ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Não foi possivel abrir o arquivo {exc}")
# arquivo.close()

# os.remove(ROOT_PATH / "textodoido.txt")

# shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
