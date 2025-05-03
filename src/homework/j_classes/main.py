from class_a import die

def main():
    d = die()

    while True:
        user_input = input("Roll the die? (y/n): ").lower()

        if user_input == "y":
            d.roll()
            print(d)

        elif user_input == "n":
            print("Exiting Program")

            break
        
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
