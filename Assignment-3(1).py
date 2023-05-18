list_limit=int(input("How many numbers are you going to enter?"))
user_list = []
for i in range(list_limit):
    user_input=int(input("Enter the numbers"))
    user_list.append(user_input)
print(user_list)
def sum_of_list(user_list):
    sum=0
    for i in user_list:
        sum+=i
    print(f'Sum of list={sum}')
    return sum
sum_of_list(user_list)