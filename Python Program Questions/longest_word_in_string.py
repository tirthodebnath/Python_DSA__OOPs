def longest_even_word(input_string):
    # Remove commas from the input string
    cleaned_string = input_string.replace(",", "")
    
    # Split the string into words
    words = cleaned_string.split()
    
    # Initialize variables to keep track of the longest even word
    longest_even = ""
    
    # Iterate through the words to find the longest even word
    for word in words:
        if len(word) % 2 == 0 and len(word) > len(longest_even):
            longest_even = word
            
    return longest_even

# Sample input
input_string = "Be not afraid of greatness, some are born great, some achieve greatness, and some have greatness thrust upon them."

# Call the function and print the result
result = longest_even_word(input_string)
print("Longest even word (excluding commas):", result)
