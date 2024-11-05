def single_root_words(root_word, *other_words):
    same_words = []
    all_words = other_words
    for i in range(len(all_words)):
        if root_word in all_words[i] or all_words[i].upper() in root_word.upper():
            same_words.append(all_words[i])
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)