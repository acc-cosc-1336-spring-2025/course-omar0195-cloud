def get_lowest_list_value(input_value):
    list = input_value
    lowest = int(list[0])

    for i in range(len(list)):
        if lowest > int(list[i]):
            lowest = int(list[i])
    
    return lowest


def get_highest_list_value(input_value):
    list = input_value
    highest = int(list[0])

    for i in range(len(list)):
        if highest < int(list[i]):
            highest = int(list[i])

    return highest 