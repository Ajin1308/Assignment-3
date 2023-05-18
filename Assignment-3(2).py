input_string=input("input your string: ")
def reverse_of_string(input_string):
    reverse_string=input_string[::-1]
    print(f'Reversed string: {reverse_string}')
    return reverse_string
reverse_of_string(input_string)