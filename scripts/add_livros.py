import pandas as pd
import os

CAMINHO_CSV = 'data/livros.csv'

def adicionar_livro():
    print("\n📘 Adicionando novo livro:")
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")
    sinopse = input("Sinopse: ")

    # Validação de tamanho do tamanho da sinopse
    if len(sinopse) > 800:
        print(f"⚠️ Sinopse muito longa ({len(sinopse)} caracteres). Limite de 800 caracteres.")
        confirmar = input("Deseja continuar mesmo assim? (s/n): ")
        if confirmar.lower() != 's':
            print("❌ Livro não adicionado. Tente novamente com uma sinopse mais curta.")
            return
    novo_livro = {
        'titulo': titulo,
        'autor': autor,
        'genero': genero,
        'sinopse': sinopse
    }

    if os.path.exists(CAMINHO_CSV):
        df = pd.read_csv(CAMINHO_CSV)
        df = pd.concat([df, pd.DataFrame([novo_livro])], ignore_index=True)
    else:
        df = pd.DataFrame([novo_livro])

    df.to_csv(CAMINHO_CSV, index=False)
    print("✅ Livro adicionado com sucesso!")

if __name__ == '__main__':
    while True:
        adicionar_livro()
        continuar = input("➕ Deseja adicionar outro livro? (s/n): ")
        if continuar.lower() != 's':
            break
