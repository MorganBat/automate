def collatz(number):
    try:
        number = int(number)
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
            else:
                number = 3 * number + 1
                print(number)
    except ValueError:
        print('Please enter a valid number')
print('Please enter a number: ')
input = input()
collatz(input)
