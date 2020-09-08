from binary_search import binary_search
# funktio, joka lukee suomen sekä englanninkielieset sanat tiedostoista, jotka on määritetty main funktiossa.


def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def main():
    finnish_words = read_words('kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')
    # finnish_words sanalistan pituus
    print(len(finnish_words))
    # sana joka on sekä finnish wordsissa, että english wordsissa printataan ulos
    # Binaarihaku eli puolitushaku, puolitetaan määrää aina
    # Loopissa Left ja Right,
    for word in finnish_words:
        if binary_search(word, english_words):
            print(word)


if __name__ == '__main__':
    main()
