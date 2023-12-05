#Write a program that takes a sentences as input and prints the count of each word along with its index in the sentence

sentence = input("Enter a sentence: ")
# Split the sentence into a list of words
words = sentence.split()
# Initialize a dictionary to store the count of each word
word_count = {}
# Iterate over the list of words using enumerate() to get the index
for i, word in enumerate(words):
    # Check if the word is already in the dictionary
    if word in word_count:
        # If it is, increment its count
        word_count[word] += 1
    else:
        # If it's not, add it to the dictionary with a count of 1
        word_count[word] = 1
# Print the count of each word along with its index in the sentence
for word, count in word_count.items():
    print(f"{word}: {count}, Index: {list(word_count.keys()).index(word)}")