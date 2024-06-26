import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# try:
#     with open(ROOT_PATH/ "usuarios.csv", "w", newline="", encoding= "utf-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(["id", "Nome"])
#         escritor.writerow(["1", "jose"])
#         escritor.writerow(["2", "maria"])
# except IOError as exc:
#     print(f"Erro ao carregar arquivo {exc}")


try:
    with open(ROOT_PATH/ "usuarios.csv", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['Nome']}")
except IOError as exc:
    print(f"Erro ao carregar arquivo {exc}")