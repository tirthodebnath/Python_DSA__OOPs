##### Count the occurrences of each word in a given text string

# text = "apple banana apple orange banana apple"

# word_list = text.split()
# word_count = {}

# for i in word_list:
#     if i in word_count:
#         word_count[i] += 1
#     else:
#         word_count[i] = 1
        
#### Count the occurrences of each vowel in a given text string  
# a = "Programming is amazing"

# b = ["A","E","I","O","U","a","e","i","o","u"]

# vowels = {}

# for i in a:
#     if i in b and i in vowels:
#         vowels[i] += 1
#     else:
#         vowels[i] = 1
# print(vowels)


# Input = [4, 5, 2, 4, 2, 3, 5, 1]
# a= []

# for i in Input:
#     if i not in a:
#         a.append(i)
# print(a)
        
# a = "Tirtho"
# print(a[::-1])


prices = [7, 1, 5, 3, 6, 4]

min_price = float('inf')
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

print(max_profit)   # Output: 5

        

