def get_hamming_distance (dna1, dna2):

    hamming_distance = 0

    if len(dna1) != len(dna2):
        print ("DNA String must be equal length")

    for seq in range(len(dna1)):
        if dna1[seq] != dna2[seq]:
            hamming_distance += 1

    return hamming_distance

def get_dna_complement(dna):

    complement = ""
    
    for num in range (len(dna)):
        
        if dna[num] =="A":
            complement += "T"

        elif dna[num] == "T":
            complement += "A"

        elif dna[num] == "C":
            complement += "G"

        elif dna[num] == "G":
            complement += "C"

        else:
            print ("No DNA Character Found")

    reverse_complement = ""

    for num in range (len(complement) -1, -1, -1):
        reverse_complement += complement[num]

    return reverse_complement
        
def display_menu():
        print ("1- Hamming Distance")
        print ("2- DNA Complement")
        print ("3- Exit")

def run_menu():
        option = 0
        yes_no_option = ""

        while(option != "0"):
            display_menu()
            option = input("Enter menu option: ")

            handle_menu_option(option)

            if (option == "3"):
                yes_no_option = ("Exiting program")
                break

def handle_menu_option(option):
        if(option == "1"):
            dna1 = input("Enter a DNA String: ")
            dna2 = input("Enter the next DNA String: ")

            hamming_distance = get_hamming_distance(dna1, dna2)
        
            print("Hamming Distance: ", hamming_distance)

        elif (option == "2"):
            dna = input("Enter a DNA String ")

            complement = get_dna_complement(dna)
            print("DNA Complement:", complement)
            print("")   
        



    