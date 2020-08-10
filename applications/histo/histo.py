# Read the input file
with open("robin.txt") as f:
    txt = f.read()

# Strip special characters
txt = ''.join(c for c in txt if c not in '":;,.-+=/\\|[]{}()*^&')

# Count the words
counts = {}
for word in txt.lower().split():
    if word in counts:
        counts[word] += 1  # existing word, increment count
    else:
        counts[word] = 1  # found new word, add it as a key

# Sort the words by count
count_words = list(counts.items())
count_words.sort(key=lambda x: x[1], reverse=True)

# Print the histogram
for pair in count_words:
    if len(pair[0]) < 8:  # align tabs correctly
        space = '\t\t'
    else:
        space = '\t'

    print(pair[0] + space + "".join('#' for _ in range(pair[1])))
