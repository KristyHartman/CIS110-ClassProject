# Saying Hello and Introduce chatbot!
print("Hello!")
print("I am Katie, your chatbot.")
# Instructions
print("When I ask you a question, please answer and press Enter afterwards.")

def explore_field(name, animal, animal_kind, pet_name):
    pronoun = "he" if animal_kind == "boy" else "she"
    print(f"\n{pet_name}, a curious {animal_kind} {animal}, was outside in the backyard playing when {pronoun} came across a hole in the fence.")
    print(f"Curiosity got the better of {pet_name}, and {pronoun} started digging. Before {pet_name} knew it, {pronoun} was across the fence into the big wide world of adventure.")
    print(f"After walking out into the wild open field, {pet_name} ran right into a big black fluffy cat named Whiskers.")
    while True:
        choice = input(f"Does {pet_name} want to explore the stream or the forest? (stream/forest) ").lower()
        if choice == "stream":
            explore_stream(pet_name, animal_kind)
            break
        elif choice == "forest":
            explore_forest(pet_name, animal_kind)
            break
        else:
            print("Invalid choice. Please choose 'stream' or 'forest'.")

def explore_stream(pet_name, animal_kind):
    pronoun = "he" if animal_kind == "boy" else "she"
    print(f"\n{pet_name} discovered a sparkling stream, where {pronoun} played and splashed in the cool water.")
    print(f"The two quickly became really good friends.")
    print("As they played, they met a wise old owl who shared stories of the forest.")

def explore_forest(pet_name, animal_kind):
    pronoun = "he" if animal_kind == "boy" else "she"
    print(f"\n{pet_name} ventured into the forest, where {pronoun} encountered various creatures and discovered hidden paths.")
    print(f"The two quickly became really good friends.")
    print("As they explored, they met a wise old owl who shared stories of the forest.")

def add_challenge(pet_name, animal_kind):
    pronoun = "he" if animal_kind == "boy" else "she"
    print(f"Suddenly, {pet_name} and Whiskers heard a rustling in the bushes. They cautiously approached and found a small, frightened rabbit.")
    while True:
        choice = input(f"Does {pet_name} help the rabbit find its way home? (yes/no) ").lower()
        if choice == "yes":
            print(f"\n{pet_name} and Whiskers decided to help the rabbit. {pet_name}, being a brave {animal_kind}, led the way as they followed the rabbit through the forest, facing various challenges.")
            print(f"After a long journey, they finally reached the rabbit's home. The rabbit thanked them, and {pronoun} wagged {pronoun if animal_kind == 'boy' else 'her'} tail in delight.")
            break
        elif choice == "no":
            print(f"\n{pet_name} and Whiskers decided not to help the rabbit and continued their adventure.")
            break
        else:
            print("Invalid choice. Please answer 'yes' or 'no'.")

def big_city(city, pet_name, animal_kind, restaurant):
    pronoun = "he" if animal_kind == "boy" else "she"
    print(f"The owl guided {pet_name} and Whiskers back to what looked like big and little people playing.")
    print(f"That was when {pet_name} realized {pronoun} was staring at the big city of {city}.")
    smell_food(pet_name, animal_kind, city, restaurant)

def smell_food(pet_name, animal_kind, city, restaurant):
    pronoun = "he" if animal_kind == "boy" else "she"
    print(f"\nAs {pet_name} and Whiskers explored {city}, {pronoun} smelled delicious food coming from a picnic table nearby.")
    print(f"It reminded {pet_name} of the tasty treats from {restaurant}, {pronoun}r favorite place to eat!")
    while True:
        choice = input(f"Does {pet_name} want to eat the food on the picnic table? (yes/no) ").lower()
        if choice == "yes":
            print(f"\n{pet_name} and Whiskers happily ate the food on the picnic table, enjoying treats that tasted just like {restaurant}’s menu.")
            break
        elif choice == "no":
            print(f"\n{pet_name} and Whiskers decided not to eat the food, saving their appetite for {restaurant} another day.")
            break
        else:
            print("Invalid choice. Please answer 'yes' or 'no'.")
    return_home(pet_name, animal_kind)

def return_home(pet_name, animal_kind):
    pronoun = "he" if animal_kind == "boy" else "she"
    print(f"\nAs the sun began to set, {pet_name} realized {pronoun} needed to find {pronoun}r way back home.")
    print(f"Whiskers, being a wise cat, led {pet_name} back to the hole in the fence.")
    print(f"{pet_name} squeezed through and ran straight to {pronoun}r owner, who was waiting with open arms.")
    print(f"From that day on, {pet_name} and Whiskers would meet at the fence every afternoon, ready for new adventures.")

def create_another_story():
    while True:
        choice = input("\nWould you like to create another story? (yes/no) ").lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    # Removed duplicate introduction, keeping only the project welcome
    print("Hello World!")
    print("Welcome to my CIS110_CourseProject!")
    
    # Asking the user name
    name = input("What is your name? ")
    while len(name.strip()) == 0:
        name = input("Name cannot be blank! Please enter your name: ")
    if name.lower() == "kristy hartman":
        print(f"\nMy creator, {name}. Pleasure to serve you!")
    else:
        print(f"\nHello, {name}. Nice to meet you!")
    
    while True:
        print("Let's create a story together!")
        print("When I ask you a question, please answer and press Enter afterwards.")
        
        # Collect story inputs
        animal = input("What main character would you like to have, a dog or a cat? ").lower()
        while animal not in ["dog", "cat"]:
            print("Please choose either 'dog' or 'cat'.")
            animal = input("What main character would you like to have, a dog or a cat? ").lower()
        
        animal_kind = input(f"Is the {animal} a boy or girl? ").lower()
        while animal_kind not in ["boy", "girl"]:
            print("Please choose either 'boy' or 'girl'.")
            animal_kind = input(f"Is the {animal} a boy or girl? ").lower()
        
        pet_name = input(f"What would you like to name your {animal}? ")
        while len(pet_name.strip()) == 0:
            pet_name = input("Name cannot be blank! Please enter a name: ")
        
        restaurant = input("What is your favorite restaurant? ")
        while len(restaurant.strip()) == 0:
            restaurant = input("Restaurant cannot be blank! Please enter a restaurant: ")
        
        city = input("What is your favorite city? ")
        while len(city.strip()) == 0:
            city = input("City cannot be blank! Please enter a city: ")
        
        # Start the story
        explore_field(name, animal, animal_kind, pet_name)
        add_challenge(pet_name, animal_kind)
        big_city(city, pet_name, animal_kind, restaurant)
        
        # Ask to create another story
        if not create_another_story():
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()