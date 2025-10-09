# Recebe o texto completo do documento, separa as palavras, e conta o número de palavras
def get_num_words(c):
    w = c.split()
    return len(w)


# Recebe o texto, converte para 'lower case', adiciona e conta caracteres do texto
def get_num_char(c):
    num_characters = {}    
    lower_case_text = c.lower()
    for character in lower_case_text:
        if character not in num_characters:
            num_characters[character] = 0
        num_characters[character] += 1
    return num_characters


# Distribui a contagem de caracteres em uma lista e ordena decrescente
def get_sorted_char(characters):
    sorted_characters = []

    for character in characters:
        temp_dict = {
            "char": character,
            "count": characters[character]
            }
        sorted_characters.append(temp_dict)

    def get_num(item):
        return item["count"]

    sorted_characters.sort(reverse = True, key = get_num)
    return sorted_characters