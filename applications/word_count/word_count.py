def word_count(s):
    """
    Returns a dictionary of words and their counts

    Outputs all keys in lowercase
    """
    # ignore certain characters, according to the readme
    for char in s:
        if char in '":;,.-+=/\\|[]{}()*^&':
            s = s.replace(char, '')
    
    words = s.lower().split() # get a list of all words in lower case
    output = {}
    for word in words:
        if word in output:
            output[word] += 1  # existing word, increment count
        else:
            output[word] = 1  # found new word, add it as a key

    return output


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))