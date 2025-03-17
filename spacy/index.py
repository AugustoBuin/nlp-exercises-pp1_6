import spacy
import nltk
from nltk.corpus import wordnet as wn
import random

# Baixar os dados necessários
nltk.download("wordnet")
nltk.download("omw-1.4")  # Open Multilingual WordNet
nlp = spacy.load("en_core_web_sm")  # Modelo de NLP em inglês


def get_best_synonym(word, pos):
    """Encontra um sinônimo adequado para uma palavra com base no WordNet."""
    synsets = wn.synsets(word, pos=pos)  # Obtém sinônimos com a mesma classe gramatical
    synonyms = set()

    for syn in synsets:
        for lemma in syn.lemmas():
            lemma_name = lemma.name().replace(
                "_", " "
            )  # Substitui underscores por espaços
            if lemma_name.isalpha() and lemma_name.lower() != word.lower():
                synonyms.add(lemma_name)

    # Verifica se há sinônimos válidos
    if synonyms:
        return min(
            synonyms, key=len
        )  # Escolhe o sinônimo mais curto (evita nomes próprios e palavras estranhas)

    return word  # Retorna a palavra original se não houver sinônimos adequados


def pos_spacy_to_wordnet(spacy_pos):
    """Converte POS tags do spaCy para os códigos usados no WordNet."""
    if spacy_pos.startswith("N"):
        return wn.NOUN
    elif spacy_pos.startswith("V"):
        return wn.VERB
    elif spacy_pos.startswith("J"):
        return wn.ADJ
    elif spacy_pos.startswith("R"):
        return wn.ADV
    return None  # Outros casos (ex.: pronomes, preposições) não são substituídos


def replace_with_synonyms(sentence):
    """Reescreve uma frase substituindo algumas palavras por sinônimos."""
    doc = nlp(sentence)  # Processar a frase com spaCy
    new_sentence = []

    for token in doc:
        wordnet_pos = pos_spacy_to_wordnet(token.tag_)  # Converter POS tag
        if wordnet_pos:  # Apenas se for uma classe gramatical relevante
            new_word = get_best_synonym(token.text.lower(), wordnet_pos)
            new_sentence.append(new_word if new_word else token.text)
        else:
            new_sentence.append(token.text)

    return " ".join(new_sentence)


# Permite que o usuário digite uma frase
while True:
    user_input = input("\nDigite uma frase em inglês (ou 'exit' para sair): ")
    if user_input.lower() == "exit":
        print("Encerrando o programa. Até mais!")
        break
    modified_sentence = replace_with_synonyms(user_input)
    print(f"↪ Frase modificada: {modified_sentence}")
