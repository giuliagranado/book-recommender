import pandas as pd
import os
import csv

CAMINHO_CSV = 'data/livros.csv'

def validar_csv():
    """Valida e corrige o arquivo CSV existente"""
    try:
        # Tenta ler com pandas primeiro
        df = pd.read_csv(CAMINHO_CSV, encoding='utf-8', on_bad_lines='skip')
        
        # Garante que temos apenas as colunas necessárias
        colunas = ['titulo', 'autor', 'genero', 'sinopse']
        df = df[colunas]
        
        # Remove linhas duplicadas e reseta o index
        df = df.drop_duplicates().reset_index(drop=True)
        
        # Salva o arquivo corrigido
        df.to_csv(CAMINHO_CSV, index=False, quoting=csv.QUOTE_ALL, encoding='utf-8')
        return True
    except Exception as e:
        print(f"Erro ao validar CSV: {e}")
        return False

def adicionar_livro():
    print("\n📘 Adicionando novo livro")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    genero = input("Gênero: ").strip()
    sinopse = input("Sinopse: ").strip()

    # escapar aspas duplas na sinopse para evitar problemas no CSV
    sinopse = sinopse.replace('"', '""')

    # validação básica
    if not all([titulo, autor, genero, sinopse]):
        print("❌ Todos os campos são obrigatórios!")
        return

    # validação de tamanho da sinopse
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

    try:
        # Valida o CSV existente antes de adicionar
        if os.path.exists(CAMINHO_CSV) and not validar_csv():
            print("❌ Arquivo CSV corrompido. Corrija-o antes de continuar.")
            return

        if os.path.exists(CAMINHO_CSV):
            df = pd.read_csv(CAMINHO_CSV, encoding='utf-8')
            # Verifica se o livro já existe
            if not df[df['titulo'].str.lower() == titulo.lower()].empty:
                print("⚠️ Livro com este título já existe!")
                return
            df = pd.concat([df, pd.DataFrame([novo_livro])], ignore_index=True)
        else:
            df = pd.DataFrame([novo_livro])

        # Usa QUOTE_ALL para garantir que todos os campos estejam entre aspas
        df.to_csv(CAMINHO_CSV, index=False, quoting=csv.QUOTE_ALL, encoding='utf-8')
        print("✅ Livro adicionado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao salvar o livro: {str(e)}")
        print("💡 Tente validar o arquivo CSV manualmente:")
        print(f"   1. Abra {CAMINHO_CSV} em um editor de texto")
        print("   2. Verifique se cada linha tem exatamente 4 campos")
        print("   3. Certifique-se que todas as aspas estão corretamente fechadas")

if __name__ == '__main__':
    try:
        while True:
            adicionar_livro()
            continuar = input("\n➕ Deseja adicionar outro livro? (s/n): ")
            if continuar.lower() != 's':
                break
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado pelo usuário.")
