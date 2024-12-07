def singl_root_words (root_word, *other_words):
    same_words = [root_word,]
    t = {i.lower() for i in other_words}
    for i in t:
        if root_word.lower() in i or i in root_word:
            same_words.append(i)
    print(same_words)
singl_root_words('дЕло', "подЕлом", "деловитый", "деловой", "печься")
