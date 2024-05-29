# Prompt user to enter a sentence up to 10 words
sentence = input("Please enter a sentence (up to 10 words): ")

# Split the sentence into words
words = sentence.split()

# Check if the sentence has more than 10 words
if len(words) > 10:
    print("The sentence should not have more than 10 words.")
else:
    # Write each word to a new file
    for i, word in enumerate(words):
        with open(f"word{i+1}.txt", "w") as file:
            file.write(word)
        print(f"{word} has been written to word{i+1}.txt")

    # Prompt user to enter any of the words of the sentence
    word_to_find = input("Please enter any of the words from the sentence: ")

    # Check if the word is in the sentence
    if word_to_find in words:
        print(
            f"The word '{word_to_find}' was found in the sentence at position {words.index(word_to_find)+1} and has been written to word{words.index(word_to_find)+1}.txt"
        )
    else:
        print(f"The word '{word_to_find}' was not found in the sentence.")

    print("All words have been written to their respective files.")

    # # Close all files
    # for i in range(len(words)):
    #     with open(f"word{i+1}.txt", "w") as file:
    #         file.close()

    # print("All files have been closed.")
