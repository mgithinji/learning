def fullJustify(words, maxWidth):
    import math
    # packing the wordlines
    num_words = len(words)
    content = []        
    line = []
    nline = 0
    for i, word in enumerate(words):
        word_width = len(word) + 1
        if nline + word_width <= maxWidth + 1:
            line.append(word)
            nline += word_width
        else:
            content.append(line)
            line = []
            nline = 0
            line.append(word)
            nline += word_width

        if i == num_words - 1 and len(line) > 0:
            content.append(line)

    # formating each wordline
    n_lines = len(content)
    res = []
    for i, wordline in enumerate(content):
        # last wordline
        if i == n_lines - 1:
            line = ' '.join(wordline)
            line = line.ljust(maxWidth)
            res.append(line)
        else:        
            n_words = len(wordline)
            # if only one word in wordline
            if n_words == 1:
                line = ' '.join(wordline)
                line = line.ljust(maxWidth)
                res.append(line)
            else:
                # calculate white space available available
                n_letters = 0
                for word in wordline:
                    n_letters += len(word)
                n_spaces = maxWidth - n_letters

                # calculate num spaces to distribute

                word_spacing = math.floor(n_spaces/(n_words - 1))
                rem_spaces = n_spaces - (word_spacing * (n_words - 1))
                line = ''
                for j, word in enumerate(wordline):
                    if j == n_words - 1:
                        line = line + word
                    else:
                        line = line + word + (' ' * word_spacing)
                        if rem_spaces > 0:
                            line = line + ' '
                            rem_spaces -= 1
                res.append(line)

    return res

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
width = 20
result = fullJustify(words, width)
for word in result:
    print(word, end=":\t")
    print(len(word))