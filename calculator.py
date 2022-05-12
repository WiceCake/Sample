def calculator(type, num1, num2):

    if type.lower() == 'sum':
        total = num1 + num2
    elif type.lower() == 'minus':
        total = num1 - num2
    elif type.lower() == 'product':
        total = num1 * num2
    elif type.lower() == 'divide':
        total = num1 / num2

    return total


name = 'daniel'
counter = True
num = 6

# len(name) = 6

# range() 1 range
# range() 2 min range
# range() 3 min max range

for i in name:
    print(i)