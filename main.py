!python -m spacy download pt_core_news_sm

# main.py
import re
import spacy
import nltk
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

# --- Pré-processamento ---
nltk.download("stopwords")
stopwords = set(nltk.corpus.stopwords.words("portuguese"))

# Carregar modelo do spaCy
nlp = spacy.load("pt_core_news_sm")

# --- Texto do Hino Nacional Brasileiro ---
hino = """
Ouviram do Ipiranga as margens plácidas
De um povo heróico o brado retumbante,
E o sol da liberdade, em raios fúlgidos,
Brilhou no céu da pátria nesse instante.
Se o penhor dessa igualdade
Conseguimos conquistar com braço forte,
Em teu seio, ó liberdade,
Desafia o nosso peito a própria morte!
Ó Pátria amada,
Idolatrada,
Salve! Salve!
Brasil, um sonho intenso, um raio vívido
De amor e de esperança à terra desce,
Se em teu formoso céu, risonho e límpido,
A imagem do Cruzeiro resplandece.
Gigante pela própria natureza,
És belo, és forte, impávido colosso,
E o teu futuro espelha essa grandeza.
Terra adorada,
Entre outras mil,
És tu, Brasil,
Ó Pátria amada!
Dos filhos deste solo és mãe gentil,
Pátria amada,
Brasil!
Parte II

Deitado eternamente em berço esplêndido,
Ao som do mar e à luz do céu profundo,
Fulguras, ó Brasil, florão da América,
Iluminado ao sol do Novo Mundo!
Do que a terra, mais garrida,
Teus risonhos, lindos campos têm mais flores;
"Nossos bosques têm mais vida",
"Nossa vida" no teu seio "mais amores."
Ó Pátria amada,
Idolatrada,
Salve! Salve!
Brasil, de amor eterno seja símbolo
O lábaro que ostentas estrelado,
E diga o verde-louro dessa flâmula
- "Paz no futuro e glória no passado."
Mas, se ergues da justiça a clava forte,
Verás que um filho teu não foge à luta,
Nem teme, quem te adora, a própria morte.
Terra adorada,
Entre outras mil,
És tu, Brasil,
Ó Pátria amada!
Dos filhos deste solo és mãe gentil,
Pátria amada,
Brasil!
"""

# --- Limpeza e tokenização ---
tokens = [t.lower() for t in re.findall(r"\b\w+\b", hino)]
tokens_sem_stop = [t for t in tokens if t not in stopwords]

# --- Frequência de palavras ---
freq = Counter(tokens_sem_stop)

# --- Frequência por classe gramatical ---
doc = nlp(hino)
pos_counts = Counter([token.pos_ for token in doc])

# --- Vocabulário ---
vocab_size = len(set(tokens))
type_token_ratio = vocab_size / len(tokens)

# --- Comprimento médio ---
avg_word_len = sum(len(t) for t in tokens) / len(tokens)
versos = [v.strip() for v in hino.split("\n") if v.strip()]
avg_line_len = sum(len(v.split()) for v in versos) / len(versos)

# --- Rimas (última palavra de cada verso) ---
ultimas_palavras = [v.split()[-1].lower() for v in versos if v]
rimas = Counter([p[-3:] for p in ultimas_palavras])  # últimas 3 letras

# --- Repetições ---
repeticoes = {k: v for k, v in freq.items() if v > 1}

# --- Resultados ---
print("\n=== MÉTRICAS DO HINO NACIONAL BRASILEIRO ===")
print("Total de palavras:", len(tokens))
print("Vocabulário único:", vocab_size)
print("Type-Token Ratio:", round(type_token_ratio, 3))
print("Comprimento médio das palavras:", round(avg_word_len, 2))
print("Comprimento médio dos versos (em palavras):", round(avg_line_len, 2))
print("Classes gramaticais mais frequentes:", pos_counts.most_common(5))
print("Palavras mais comuns:", freq.most_common(10))
print("Repetições:", repeticoes)
print("Rimas mais comuns (últimas 3 letras):", rimas.most_common(5))

# --- Nuvem de palavras ---
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(tokens_sem_stop))
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Nuvem de Palavras - Hino Nacional Brasileiro")
plt.show()
