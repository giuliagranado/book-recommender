# 📚 book-recommender
Este projeto aplica conceitos de **Álgebra Linear** para recomendar livros com base na **similaridade entre sinopses**. Utilizando a técnica de **TF-IDF (Term Frequency–Inverse Document Frequency)**, o sistema transforma textos em vetores, depois compara suas distâncias para identificar obras com temas semelhantes.

---
## 🧠 Objetivo
Demonstrar a aplicação de vetorização textual e comparação de similaridade usando Álgebra Linear, com foco em:

- Representação de sinopses como vetores numéricos
- Cálculo de similaridade entre vetores
- Recomendação de livros com base em proximidade textual

---

## 🗂️ Estrutura do Projeto
<pre>
recomendador_livros_tfidf/
 ├── data/
 │ └── livros.csv         # Dataset com sinopses 
 ├── scripts/ 
 │ └── recomendador.py    # Código principal 
 ├── README.md 
 └── requirements.txt
</pre>

---
## 📄 Dataset
O arquivo `livros.csv` contém colunas como:
- `titulo`: Nome do livro
- `autor`: Nome do autor
- `genero`: Gênero literário
- `sinopse`: Breve descrição da obra
> ⚠️ As sinopses foram coletadas apenas de fontes públicas.

---
## ⚙️ Como executar
1. Clone o repositório
   ```bash
   git clone https://github.com/giuliagranado/book-recommender.git
   cd book-recommender
2. Instale as dependências
    ```bash
     pip install -r requirements.txt
3. Execute o script
     ```bash
      python scripts/recomendador.py
4. Digite uma descrição, sinopse ou tema para receber recomendações!

---
## 📚 Recomendações:
Título: Orgulho e Preconceito | Autor: Jane Austen | Gênero: Romance
Título: O Morro dos Ventos Uivantes | Autor: Emily Brontë | Gênero: Romance
Título: Dom Casmurro | Autor: Machado de Assis | Gênero: Romance

---
## 📌 Tecnologias utilizadas
* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Similaridade de Cosseno

## 📘 Licença
Este projeto é de uso educacional e não possui fins comerciais. As sinopses utilizadas são públicas e foram incluídas apenas para fins de demonstração.