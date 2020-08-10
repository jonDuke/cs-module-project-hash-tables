# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# Established letter frequency (most to least)
frequency_order = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# Read the input file
with open("ciphertext.txt") as f:
    ciphertext = f.read()

# The example input is already in upper case, but this would be needed
# if the input was lower case.
ciphertext = ciphertext.upper()

# Count letter frequency in the input
counts = {}
for char in ciphertext:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

# Sort those counts to get the most frequent letters in the cipher
count_items = list(counts.items())
count_items.sort(key=lambda x: x[1], reverse=True)  # sort each (key, value) pair by value

# Get a string with just the letters in that order
cipher_order = ""
for item in count_items:
    if item[0] in frequency_order:  # if it is a letter
        cipher_order += item[0]

# use the str.translate() method to decode the cipher
translator = str.maketrans(cipher_order, "".join(frequency_order))
print(ciphertext.translate(translator))
