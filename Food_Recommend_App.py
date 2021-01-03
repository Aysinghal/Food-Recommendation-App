food = {"sabji" : {"aloo gobi": [0, {"Calories" : 100, "Carbs" : 100, "Protein" : 100, "Fat" : 100}], "paneer shimlamirch" : [0, {"Calories" : 100, "Carbs" : 100, "Protein" : 100, "Fat" : 100}], "baingan bhartha": [0, {"Calories" : 100, "Carbs" : 100, "Protein" : 100, "Fat" : 100}]}, "dal" : {"chana dal": [0, {"Calories" : 100, "Carbs" : 100, "Protein" : 100, "Fat" : 100}], "black dal": [0, {"Calories" : 100, "Carbs" : 100, "Protein" : 100, "Fat" : 100}], "urad dal" : [0, {"Calories" : 100, "Carbs" : 100, "Protein" : 100, "Fat" : 100}]}, "bread" : {"roti" : [0, {"Calories" : 100, "Carbs" : 100, "Protein" : 100, "Fat" : 100}], "naan": [0, {"Calories" : 100, "Carbs" : 100, "Protein" : 100, "Fat" : 100}]}}
family_list = ["Sanju", "Sukriti", "Vishrut", "Vihaan"]

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
    number_people_family = int(input("How many people are in your family: "))
    for i in range(0, number_people_family):
        family_list.append(input("what is the name of the" + ordinal_numbers(i + 1) + " oldest person in you family: "))
    return family_list

def create_categories():
    food = {}
    categories_list = []
    print("The number and names of the categories can not be changed ")
    number_categories = int(input("How many categories of food do you eat: "))
    for i in range(0, number_categories):
        categories_list.append(input("what is the name of the" + ordinal_numbers(i + 1) + " most varied category: "))
    for i in range(0, len(categories_list)):
        food[categories_list[i]] = {}
    return food

def add_foods(food, family_list):
    categories_list = list(food.keys())
    family_ratings = {}

    print("If you are just starting out, add entries to the less varied categories, before adding to the main course")
    print_list(categories_list)

    food_nutrient_names = ["Calories","Carbs","Protein","Fat"]
    food_nutrients = []

    print("")
    food_category = int(input("What category is this food a part of (enter the number): "))

    print("")
    food_name = input("What is the name of the food you would like to add: ")
    print("")
    
    for i in food_nutrient_names:
        nutrient_quantity = float(input("How many " + i + " are in this food (in grams and per portion): "))
        food_nutrients.append(nutrient_quantity)
    print("")
    category_chosen = categories_list[food_category]

    linked_food_dictionary = {}

    if food_category == 0:
        for i in range (1, len(categories_list)):
            print(categories_list[i] + ":")
            print_list(list(food.get(categories_list[i]).keys()))
            print("If it goes with none of these, then write 'nothing'.")
            print("")
            food_link = str(input("Enter the number of food it goes with in this category (split the numbers with a comma and a space): "))
            if food_link != "nothing":
                food_link_list = food_link.split(", ")
            else:
                food_link_list = []
            for j in range (0, len(food_link_list)):
                food_link_list[j] = list(food.get(categories_list[i]).keys())[int(food_link_list[j])]

            linked_food_dictionary[categories_list[i]] = food_link_list

    for i in range (0, len(family_list)):
        person_rating = float(input("How much does " + family_list[i] + " like " + food_name + " out of 10 stars: "))
        family_ratings[family_list[i]] = person_rating


    food.get(category_chosen)[food_name] = [1, {"Calories" : food_nutrients[0], "Carbs" : food_nutrients[1], "Protein" : food_nutrients[2], "Fat" : food_nutrients[3]}, linked_food_dictionary, family_ratings]
    
    print("")
    return food

def choose_dish(food_list, prob_list):
    for i in range (0,len(prob_list)):
        if (numpy.random.binomial(1, prob_list[i]/sum(prob_list[i:])) == 1):
            return food_list[i]
            break

def alterProb(food_nutrient, target, prob, is_calorie):
    if target < 1:
        target = 1
    diff = abs(target - food_nutrient)
    diff_percent = diff / target
    if is_calorie:
        diff_percent *= 2
    multiplier = 1 - diff_percent
    #return (prob * multiplier)
    
def equalizeAverage(l):
    equalized_list = []
    average = sum(l) / len(l)
    for i in range(0, len(l)):
        equalized_list.append(l[i]/average)
        
     
    


def set_category_weights(food, nutrient):
    
    category_nutrients = {}
    nutrient_list = ["Calories","Carbs","Protein","Fat"]
    for i in range(0, len(nutrient_list)):
        if nutrient == nutrient_list[i]:
            nutrient_number = i
            break

    for i in list(food.keys()):
        category_nutrients[i] = []

    for i in list(food.keys()):
        nutrient_sum = 0
        for j in range (0, len(list(food.get(i).keys()))):
            nutrient_sum += list(food.get(i).get(list(food.get(i).keys())[j])[1].values())[nutrient_number]
        category_nutrients[i] = [nutrient_sum, len(food.get(i).keys())]

    total_nutrient_sum = 0

    for i in list(category_nutrients.keys()):
        category_nutrients[i] = [(category_nutrients[i][0]/category_nutrients[i][1])]
        total_nutrient_sum += category_nutrients[i][0]

    category_weight_list = []

    for i in list(category_nutrients.keys()):
        category_weight_list.append(category_nutrients.get(i)[0] / total_nutrient_sum)

    return category_weight_list
    
def create_weekly_meal():

    for i in range (0, len(categories_list)):
        for j in list(food.get(categories_list[i]).keys()):
            food.get(categories_list[0])[j][0] = 1

    sum_list =  #total sum for each nutrient so far
    day_number =  #what day it is
    recommend_list =  #recommended daily intake for each nutrient
    categories_list = #a list if all the categories

    categories_list = list(food.keys())
    nutrient_list = ["Calories","Carbs","Protein","Fat"]

    for i in range(0,len(nutrient_list)):
        nutrient_target = recommend_list[i] * day_number - sum_list[i]
        weights = set_category_weights(food, nutrient_list(i))
        for j in range(0, len(weights)):
          category_target = nutrient_target * weights[i]
          alterProb(categories_list[j])