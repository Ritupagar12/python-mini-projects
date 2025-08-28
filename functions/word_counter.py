def word_counter(sentence):
    words = sentence.split()
    return len(words)

text = input("Enter a sentence: ")
print("Word Count = ", word_counter(text))
