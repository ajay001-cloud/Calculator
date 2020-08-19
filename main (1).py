def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print('Select Operation')
print('1.Addion')
print('2.subraction')
print('3.Multiply')
print('4.Divide')

while True:
    choice = input('Enter your choice')
    if choice in ('1', '2', '3', '4'):
        x = float(input('Enter a number'))
        y = float(input('Enter a number'))
        if choice == '1':
            print('The Addition of the given values is = ', add(x, y))
        elif choice == '2':
            print('The Subraction of the given values is = ', sub(x, y))
        elif choice == '3':
            print('The Multiplication of the given values is = ', mul(x, y))
        elif choice == '4':
            print('The Division of the given values is = ', div(x, y))
        break
    else:
        print('Select other options')



