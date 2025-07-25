def remove_extra_spaces(s):
    result = ""
    prev_space = False
    
    for char in s:
        if char == ' ':
            if not prev_space:
                result += ' '
                prev_space = True
        else:
            result += char
            prev_space = False
    
    return result

input_string = input()
print(remove_extra_spaces(input_string))