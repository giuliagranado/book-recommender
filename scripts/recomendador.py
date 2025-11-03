import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CSV_PATH = 'data/livros.csv'

def carregar_dataset(path):
    try:
        df = pd.read_csv(path, encoding='utf-8', engine='python', on_bad_lines='warn', skip_blank_lines=True)
    except Exception as e:
        print(f"Erro ao abrir CSV: {e}")
        sys.exit(1)

    print(f"Colunas detectadas: {list(df.columns)}")
    if 'sinopse' not in df.columns:
        print("Coluna 'sinopse' não encontrada no CSV.")
        sys.exit(1)

    df = df.dropna(subset=['sinopse']).copy()
    df['sinopse'] = df['sinopse'].astype(str).str.strip()
    df = df.reset_index(drop=True)

    if df.empty:
        print("Dataset vazio após limpeza.")
        sys.exit(1)

    print(f"Dataset carregado: {len(df)} linhas")
    return df

df = carregar_dataset(CSV_PATH)

try:
    from nltk.corpus import stopwords
    stop_words_pt = stopwords.words('portuguese')
except Exception:
    stop_words_pt = None
    print("Aviso: NLTK stopwords não disponíveis — usando stop_words=None")

try:
    vetor = TfidfVectorizer(stop_words=stop_words_pt)
    matriz_tfidf = vetor.fit_transform(df['sinopse'])
    print(f"TF-IDF criado: matriz {matriz_tfidf.shape}")
except Exception as e:
    print(f"Erro ao criar TF-IDF: {e}")
    sys.exit(1)

def recomendar_livros(descricao, top_n=3):
    if not descricao or not descricao.strip():
        print("Descrição vazia fornecida.")
        return pd.DataFrame()

    try:
        entrada = vetor.transform([descricao])
        similaridades = cosine_similarity(entrada, matriz_tfidf).flatten()
        indices = similaridades.argsort()[::-1][:top_n]

        # Palavras-chave da descrição
        pesos = entrada.toarray()[0]
        termos = vetor.get_feature_names_out()
        top_indices = np.argsort(pesos)[::-1][:5]
        top_termos = [termos[i] for i in top_indices if pesos[i] > 0]


        print("\n🔍 Palavras-chave da sua descrição:", ', '.join(top_termos))
        # Exibe recomendações em formato de bloco
        print("\n📚 Recomendações:")
        for i in indices:
            livro = df.iloc[i]
            print("\n" + "="*60)
            print(f">> Título: {livro['titulo']}")
            print(f">> Autor: {livro['autor']}")
            print(f">> Gênero: {livro['genero']}")
            print(f">> Similaridade: {similaridades[i]*100:.2f}%")
            print(f">> Sinopse:\n{livro['sinopse']}")

    except Exception as e:
        print(f"Erro ao processar recomendação: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    try:
        entrada = input("Digite uma descrição, sinopse ou palavras chaves: ")
        recomendar_livros(entrada)
    except Exception as e:
        print("Erro inesperado (cole a mensagem completa aqui):")
        import traceback; traceback.print_exc()
