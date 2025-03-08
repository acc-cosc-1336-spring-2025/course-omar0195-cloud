#import decisions

from decisions import get_options_ratio, get_faculty_rating

options = float(input("Options Number: "))

total = float(input("Total Number: "))

result = get_options_ratio(options, total)

print("Faculty Rating: ", get_faculty_rating(result))


