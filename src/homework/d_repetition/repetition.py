def get_factorial(num):
    factorial = 1

    for i in range(0, num):
        factorial *= i +1 
    
    return factorial 

def sum_odd_numbers(num):
    index = 1 
    sum = 0 

    while(index<= num):
        sum = index + sum
        index = index + 2

    return sum

def display_menu():
    print('1-Factorial')
    print('2-Sum odd numbers')
    print('3-Exit')

def run_menu():
    option = '0'
    exit_option = ''

    while(option != '3'):

        display_menu()
        option = input("Enter a menu option: ")

        handle_menu_option(option)

        if(option == '3'):
            exit_option= input('Do you want to exit? Yes or No? ')

        if(exit_option == 'No'):
            option = 0


def handle_menu_option(option):
    if (option =='1'):
        num = 0

        while (num < 1 or num > 9):
            num = int(input('Enter a number: '))

        factorial = get_factorial(int(num))
        print("Factorial is ", factorial)
        print('')
        
    elif (option == '2'):
        num = 0

        while(num <1 or num > 99):
            num = int(input('Enter a number: '))

        result = sum_odd_numbers(int(num))
        print("Sum Odd Number is ", result)
        print('')
        
    elif(option == '3'):
        print('Exiting Program')
        print('')
        