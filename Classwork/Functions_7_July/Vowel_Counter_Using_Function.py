# Function to count vowels
def count_vowels(text):

    count = 0

    # Check every character
    for ch in text.lower():

        if ch in "aeiou":
            count += 1

    return count


# Main Program

sentence = input("Enter a sentence: ")

# Call the function
total = count_vowels(sentence)

# Display result
print("Total Vowels =", total)