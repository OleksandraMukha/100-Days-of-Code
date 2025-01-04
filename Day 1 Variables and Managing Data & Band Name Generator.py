print("Welcome to the Band Name Generator")
city_input = input("What's the name of the city you grew up in? ")
print(city_input)
pet_check = input("Do you have a pet? Type 'yes' or 'no.'").lower
if pet_check == "yes":
    pet_name = input("What's your pet's name? ")
else:
    pet_name = input("What would your pet's name be if you had one? ")
print(pet_name)

print("Your band name could be " + city_input + " " + pet_name + ".")
