import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
words = words.split()  # change to a list of words
word_table = {}

# for all but the last word...
for i in range(len(words)-1):
    # add the word after it to the table
    if words[i] in word_table:
        word_table[words[i]].append(words[i+1])
    else:
        word_table[words[i]] = [words[i+1]]


# TODO: construct 5 random sentences
for _ in range(5):
    word = random.choice(list(word_table.keys()))
    sentence = word + " "

    # while the last word added does not end with punctuation
    while word[-1] not in ".?!":
        word = random.choice(word_table[word])  # get next word randomly
        sentence += word + " "  # add to the sentence

    print(sentence, '\n')
