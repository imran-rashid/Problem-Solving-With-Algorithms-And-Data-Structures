# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
# Modify the code from Activecode 8 so that the final list only contains a single copy of each letter.

word_list = ["cat", "dog", "rabbit"]
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list:
            letter_list.append(a_letter)
print(letter_list)