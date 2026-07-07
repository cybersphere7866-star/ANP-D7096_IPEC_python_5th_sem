 #Word Frequency Counter Problem Statement: Accept a sentence from the user and create a dictionary that stores the frequency of each word. Example: Input: python is easy and python is powerful  Output: { 'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1 } Additionally: • Display the most frequently occurring word.  • Display all words in alphabetical order. 
sentence = input("Enter a sentence: ")
words = sentence.split()
word_freq = {}
for i in words:
     if i in word_freq:
         word_freq[i] += 1
     else:
         word_freq[i] = 1
    print("Word Frequency:", word_freq)
# Display the most frequently occurring word
max_freq = max(word_freq.values())
most_frequent_words = [word for word, freq in word_freq.items() if freq == max_freq]
print("Most frequently occurring word(s):", most_frequent_words)
# Display all words in alphabetical order
sorted_words = sorted(word_freq.keys()) 
print("Words in alphabetical order:", sorted_words)
