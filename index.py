def get_indices_of_letter(word, letter):
    return [index for index, char in enumerate(word) if char == letter]
word = input("Enter the word: ")
letter = input("Enter the letter to search for: ")

indices = get_indices_of_letter(word, letter)
    
if indices:
    for index in indices:
        print(index)
else:
    print(-1)
