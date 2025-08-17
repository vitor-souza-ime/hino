# Análise Linguística do Hino Nacional Brasileiro

Este projeto realiza uma **análise linguística detalhada** do Hino Nacional Brasileiro, explorando diversos parâmetros textuais e métricos utilizando Python e bibliotecas de NLP.

## Funcionalidades

O programa `main.py` realiza as seguintes análises:

- **Frequência de palavras:** conta palavras mais usadas, com remoção opcional de stopwords.
- **Frequência de classes gramaticais:** substantivos, verbos, adjetivos, usando NLP (spaCy).
- **Palavras únicas:** tamanho do vocabulário.
- **Complexidade do texto:** comprimento médio de palavras e versos.
- **Diversidade lexical:** cálculo do type-token ratio.
- **Estrutura poética e musical:**
  - Identificação de rimas (últimas sílabas iguais nos versos)
  - Contagem de sílabas poéticas por verso
  - Repetições de palavras e expressões
- **Aspectos semânticos:**
  - Geração de nuvem de palavras (wordcloud)

## Tecnologias Utilizadas

- Python 3.x
- [NLTK](https://www.nltk.org/) – para stopwords e pré-processamento
- [spaCy](https://spacy.io/) – para análise gramatical
- [matplotlib](https://matplotlib.org/) – para gráficos
- [wordcloud](https://github.com/amueller/word_cloud) – para visualização de palavras

## Como Rodar

1. Clone o repositório:

```bash
git clone https://github.com/vitor-souza-ime/hino.git
cd hino
````

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Baixe o modelo de linguagem português do spaCy:

```bash
python -m spacy download pt_core_news_sm
```

4. Execute o programa:

```bash
python main.py
```

## Resultados

* O programa gera **gráficos de frequência**, **tabelas com métricas de complexidade** e uma **nuvem de palavras** do Hino Nacional Brasileiro.
* Os resultados podem ser usados para **análise literária, educacional ou estudos culturais**.

## Referências

* Manning, C. D., & Schütze, H. (1999). *Foundations of Statistical Natural Language Processing*. MIT Press.
* Duque Estrada, J. O., & Silva, F. M. da. *Hino Nacional Brasileiro*.


