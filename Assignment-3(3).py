input_string=input("Input your string: ")
def upper_and_lower(input_string):
    input_string=input_string.split(' ')
    lower_case=0
    upper_case=0
    for i in input_string:
        for j in i:
            if ord(j) >= 65 and ord(j) <= 90:
                upper_case+=1
            elif ord(j) >= 96 and ord(j) <= 122:
                lower_case+=1
            else:
                continue
    print(f"No. of upper case={upper_case}")
    print(f"No. of lower case={lower_case}")
    return lower_case,upper_case
upper_and_lower(input_string)