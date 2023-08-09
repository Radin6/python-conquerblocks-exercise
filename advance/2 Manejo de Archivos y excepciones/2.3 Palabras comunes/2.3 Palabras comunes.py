'''PALABRAS COMUNES
Averigua cuántas veces aparece una palabra o frase en el texto (puedes usar el método count()).'''

def words_counter(file, word):
    counter = 0

    with open(file) as text:
        content = text.read()
        words = content.split()
        
        for _word in words:
            
            if _word == word:
                counter += 1

    print(f"The word '{word}' is {counter} times.")

word_search = input("Insert word to search for: ")

words_counter("text1.txt", word_search)