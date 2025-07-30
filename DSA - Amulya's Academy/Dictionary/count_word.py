## Count uniq letters of a word

word = "tirtho"
char_dict = {i: word.count(i) for i in word}
print(char_dict)

# for i in word:
#     print(word.count(i))
