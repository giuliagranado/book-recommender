import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carrega o dataset
df = pd.read_csv('data/livros.csv', skip_blank_lines=True)

# Aplica TF-IDF nas sinopses
vetor = TfidfVectorizer(stop_words='portuguese')
matriz_tfidf = vetor.fit_transform(df['sinopse'])

# Função de recomendação
def recomendar_livros(descricao, top_n=3):
    try:
        entrada = vetor.transform([descricao])
        similaridades = cosine_similarity(entrada, matriz_tfidf).flatten()
        indices = similaridades.argsort()[::-1][:top_n]
        recomendados = df.iloc[indices][['titulo', 'autor', 'genero']]
        return recomendados
    except Exception as e:
        print(f"Erro ao processar recomendação: {e}")
        return pd.DataFrame()

# Exemplo de uso
if __name__ == '__main__':
    try:
        entrada = input("Digite uma descrição ou sinopse: ")
        resultado = recomendar_livros(entrada)
        if not resultado.empty:
            print("\n📚 Recomendações:")
            print(resultado.to_string(index=False))
        else:
            print("Não foi possível gerar recomendações.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


