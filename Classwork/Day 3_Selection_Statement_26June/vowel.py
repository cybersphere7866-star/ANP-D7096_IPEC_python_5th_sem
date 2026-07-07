#input of sentence
sentence = input("Enter a sentence: ")
#initialize vowel count
vowel = 0
for x in sentence:
    if x in 'aeiouAEIOU':
        vowel += 1
print("Number of vowels in the sentence:", vowel)