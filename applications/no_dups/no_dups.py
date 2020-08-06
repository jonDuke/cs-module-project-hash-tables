def no_dups(s):
    words_found = {}
    output = ""
    for word in s.split():              # for each word
        if word not in words_found:     # if we haven't seen this word before
            words_found[word] = True    # add it to the dict
            output += word + ' '        # and add it to the output
    
    return output[:-1]  # cut off the trailing space


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))