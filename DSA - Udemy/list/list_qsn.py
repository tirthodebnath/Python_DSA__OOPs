##List Comprehensions
##we need to create a list of integers which specify the length of each word in a certain sentence,
##but only if the word is not the word "the".

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []

for word in words:
      if word != "the":
          word_lengths.append(len(word)) 
print(words)
print(word_lengths)