from wordsDb.filter_words_db import palavras_bloqueadas
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Função para filtrar palavras proibidas
def filterWords(text: str, n=3):
    tokens = word_tokenize(text.lower())
    
    # Separa as palavras bloqueadas em ngrams
    blocked_ngrams = []
    for word in palavras_bloqueadas:
        words = word.lower().split(" ")
        lenght = words.__len__()
        blocked_ngrams.extend(list(ngrams(words, lenght)))
    
    # Loop para comparar maioria dos ngrams
    filtered_words_unique = tokens
    while(n > 0):
        
        if(n > len(filtered_words_unique)):
            n-=1
            continue

        text_ngrams = list(ngrams(filtered_words_unique, n))

        
        # Filtragem dos ngrams
        filtered_ngrams = [ngram for ngram in text_ngrams if ngram not in blocked_ngrams]

        # Junta as tuplas em uma array
        filtered_words = []
        for ngram in filtered_ngrams:
            filtered_words.extend(ngram)
        # Eliminar palavras duplicadas, mas mantendo a ordem
        seen = set()
        filtered_words_unique = []
        for word in filtered_words:
            if word not in seen:
                filtered_words_unique.append(word)
                seen.add(word)
        n -= 1
        
    # Substitui as palavras filtradas pelo "*"
    new_text = ""
    for word in tokens:
        if word not in filtered_words_unique:
            n = word.__len__()
            new_text = new_text + ' ' + ("*" * n)
        else:
            new_text =  new_text + ' ' + word

    return new_text
