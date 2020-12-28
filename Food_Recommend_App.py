def ordinal_numbers(i):
    if i == 1:
        return ("")
    elif i == 2:
        return (" 2nd")
    elif i == 3:
        return (" 3rd")
    else:
        return(" " + str(i) + "th ")

def print_list(l):
    for i in range(0, len(l)):
        print(str(i) + " : " + l[i])

def create_family():
    family_list = []
    print("hi")
    number_people_family = int(input("How many people are in your family: "))
    for i in range(0, number_people_family):
        family_list.append(input("what is the name of the" + ordinal_numbers(i + 1) + " oldest person in you family: "))
    return (family_list)

def create_foods():
    food = {}
    categories_list = []
    print("The number and names of the categories can not be changed ")
    number_categories = int(input("How many yoes of food do you eat: "))
    for i in range(0, number_categories):
        categories_list.append(input("what is the name of the" + ordinal_numbers(i + 1) + " most varied category"))
    for i in range(0, len(categories_list)):
        food [categories_list[i]] = {}

def add_foods():
    print("If you are just starting out, add entries to the less varied categories, before adding")
    c
    food.get()[""] = {}