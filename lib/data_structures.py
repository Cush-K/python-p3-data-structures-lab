spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy = [food["name"] for food in spicy_foods]
    return spicy
# print(get_names(spicy_foods))

def sort_by_heat(food):
    return food["heat_level"]



def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"]> 5]
    sorted_foods = sorted(spiciest_foods, key=sort_by_heat, reverse=True)
    return sorted_foods
# print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    
# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"]== cuisine:
            return food

# print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food["heat_level"]>5]
    
    for food in spiciest:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

# print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat=[food["heat_level"] for food in spicy_foods]
    return sum(total_heat)/len(total_heat)

# print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
    }


# print(create_spicy_food(spicy_foods, spicy_food))
