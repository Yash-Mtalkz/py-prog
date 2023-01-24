def swap_chars(string):
    for i in range(len(string)):
        if string[i].isdigit():
            if i > 0 and i < len(string) - 1:
                string = string[:i-1] + string[i+1] + \
                    string[i] + string[i-1] + string[i+2:]
                i += 2  # change index to check next digit
    return string


print(swap_chars("Hello12Wo2rld3"))
