def swap_case(string):
    toggled_string = ''
    for index in string:
        if index.isupper():
            toggled_string+= index.lower()
        elif index.islower():
            toggled_string+= index.upper()

        else:
            toggled_string+=index

    
    return toggled_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
