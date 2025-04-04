from lists import get_lowest_list_value, get_highest_list_value

def menu_display():
    print("1- Show the list low/high values")
    print("2-Exit")

def run_menu():
    option = "0"

    while(option != "2"):
        menu_display()

        option = input("Choose option 1 or 2: ")
        handle_menu(option)

def handle_menu(option):
    if(option == "1"):
        input_value = []

        again = "Y"

        for i in range(3):
            ent = int(input("Enter a list value: "))
            input_value.append(ent)

        again = input("Do you want to enter another value? Y or N: ")
        
        while again == "Y" or again == "Y":
            ent = int(input("Enter another value: "))
            input_value.append(ent)

            again = input("Do you want to enter another value? Y or N: ")

        high = get_highest_list_value(input_value)
        low = get_lowest_list_value(input_value)

        print(f"The highest value is {high}")
        print(f"The lowest value is {low}")
        print()

    elif(option == "2"):
        print("Exiting Program")

    else: 
        print("Try again")

run_menu()



