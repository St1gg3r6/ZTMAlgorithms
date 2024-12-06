def reverse_string(str):
    rev = ''
    for i in range(len(str) - 1, -1, -1):
        rev += str[i]
    return rev


def reverse_string_recursive(str):
    if len(str) == 1:
        return str
    return str[-1] + reverse_string_recursive(str[:-1])


print(reverse_string("yoyo master"))
print(reverse_string_recursive("yoyo master"))
