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

# 1. Function to get names of spicy foods
def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

# 2. Function to get spiciest foods
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# 3. Function to print spicy foods
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = '🌶' * food['heat_level']  # Repeat the chili pepper emoji based on heat level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

# 4. Function to get spicy food by cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  # Return None if no match found

# 5. Function to print only spiciest foods
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        heat_level = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

# 6. Function to get the average heat level
def get_average_heat_level(spicy_foods):
    if not spicy_foods:  # Check for empty list to avoid division by zero
        return 0
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat // len(spicy_foods)

# 7. Function to create a new spicy food
def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods