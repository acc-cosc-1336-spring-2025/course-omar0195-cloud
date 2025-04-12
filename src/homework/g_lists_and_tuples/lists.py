
def get_p_distance(list1, list2):

    p_distance = 0

    for item in range(len(list1)):
        if list1[item] != list2[item]:
            p_distance += 1

    return p_distance

def get_p_distance_matrix(list1):

    n = len(list1)

    p_distance_matrix = [[0] * n for _ in range(n)]
 
    for i in range(n):
        for j in range(i, n):
            distance = get_p_distance(list1[i], list1[j])/10
            p_distance_matrix[i][j] = distance
            p_distance_matrix[j][i] = distance

    return p_distance_matrix
        
def display_menu():
    
    print("1- Get p distance matrix")
    print("2-Exit")

def run_menu():
   
    menu_option = 0
    exit = ''

    while (menu_option != '0'):

        display_menu()
        menu_option = input("Enter Menu option: ")

        handle_menu(menu_option)

        if (menu_option == '2'):
            exit = input("Do you want to exit program? Y or N: ")

        if (exit == 'Y' or exit == 'y'):
            print("Exiting...")
            menu_option = '0'

def handle_menu(option):
    
    if (option == '1'):

        string_list = []
        sub_list = 4
        nucs = 0

        while (nucs < 2 or nucs > 10):
            nucs = int(input("How many nucleotides do you want in your DNA Sequence? (2-10): "))
            
        for i in range(sub_list):
            sublist = []
            for j in range(nucs):
                element = input(f'Enter a DNA nucleotide (A,G,C,T) ({j+1})) for DNA sequence {i+1}: ').upper()
                sublist.append(element)
            string_list.append(sublist)

        print(f'The distance matrix for your string [string_list] is below.')

        matrix = get_p_distance_matrix(string_list)

        for row in matrix:
            print(row)




