# Test your understanding of list comprehensions by redoing 'remove_duplicate.py' code using 
# list comprehensions. For an extra challenge, see if you can figure out how to remove the duplicates.

word_list = ["cat", "dog", "rabbit"]

letter_list = [char for char in ''.join(word_list)]
print(letter_list)
# remove duplicate
unique_list = list(set(letter_list))
print(unique_list)