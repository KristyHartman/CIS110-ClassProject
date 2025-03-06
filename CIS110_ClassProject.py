    # Saying Hello and Introduce chatbot!
    print("Hello!")
    print("I am Kristy, your chatbot.")
    # Instructions
    print("When I ask you a question, please answer and press Enter afterwards.")
    
    # Asking the user name and 5 story questions
    name = input("\nWhat is your name:  ")
    animal = input("What main character would you like to have, a dog or a cat?  ")
    animal_kind =input("What is the {animal}, a boy or girl?  ")
    pet_name = input("What would you like to name your {animal}:  ")
    restaurent = input("What is your favorite restaurent?  ")
    city = input("What is your favorite city?  ")
    
    #exploring the stream and forest
    explore_field(name, animal, animal_name):
    print(f"\n{animal_name} was outside in the backyard playing when they came across a hole in the fence.")
    print(f"Curiosity got the better of {animal_name}, and they started digging. Before {animal_name} knew it, they were across the fence into the big wide world of adventure.")
    print(f"After walking out into the wild open field, {animal_name} ran right into a big black fluffy cat named Whiskers.")
    while True:
        choice = input(f"Does {animal_name} want to explore the stream or the forest? (stream/forest) ").lower()
        if choice == "stream":
            explore_stream(animal_name)
            break  # Exit the loop after exploring the stream
        elif choice == "forest":
            explore_forest(animal_name)
            break  # Exit the loop after exploring the forest
        else:
            print("Invalid choice. Please choose 'stream' or 'forest'.")

def explore_stream(animal_name):
    print(f"\n{animal_name} discovered a sparkling stream, where they played and splash in the cool water.")
    print(f"The two quickly became really good friends.")
    print("As they played, they met a wise old owl who shared stories of the forest.")

def explore_forest(animal_name):
    print(f"\n{animal_name} ventured into the forest, where they encountered various creatures and discovered hidden paths.")
    print(f"The two quickly became really good friends.")
    print("As they explored, they met a wise old owl who shared stories of the forest.")

def add_challenge(animal_name):
    print(f"Suddenly, {animal_name} and Whiskers heard a rustling in the bushes. They cautiously approached and found a small, frightened rabbit.")
    while True:
        choice = input(f"Does {animal_name} help the rabbit find its way home? (yes/no) ").lower()
        if choice == "yes":
            print(f"\n{animal_name} and Whiskers decided to help the rabbit. They followed the rabbit through the forest, facing various challenges along the way.")
            print("After a long journey, they finally reached the rabbit's home. The rabbit thanked them, and they all became friends.")
            break
        elif choice == "no":
            print(f"\n{animal_name} and Whiskers decided not to help the rabbit and continued their adventure.")
            break
        else:
            print("Invalid choice. Please answer 'yes' or 'no'.")

def big_city(city, animal_name):
    print(f"The owl guided {animal_name} and Whiskers back to what looked like big and little people playing.")
    print(f"That was when {animal_name} realized they were staring at the big city of {city}.")
    smell_food(animal_name)

def smell_food(animal_name):
    print(f"\nAs {animal_name} and Whiskers explored, they smelled delicious food coming from a picnic table nearby.")
    while True:
        choice = input(f"Does {animal_name} want to eat the food on the picnic table? (yes/no) ").lower()
        if choice == "yes":
            print(f"\n{animal_name} and Whiskers happily ate the food on the picnic table, enjoying the delicious treats.")
            break
        elif choice == "no":
            print(f"\n{animal_name} and Whiskers decided not to eat the food and continued their adventure.")
            break
        else:
            print("Invalid choice. Please answer 'yes' or 'no'.")
    return_home(animal_name)

def return_home(animal_name):
    print(f"\nAs the sun began to set, {animal_name} realized they needed to find their way back home.")
    print(f"Whiskers, being a wise cat, led {animal_name} back to the hole in the fence.")
    print(f"{animal_name} squeezed through and ran straight to their owner, who was waiting with open arms.")
    print(f"From that day on, {animal_name} and Whiskers would meet at the fence every afternoon, ready for new adventures.")

def create_another_story():
    while True:
        choice = input("\nWould you like to create another story? (yes/no) ").lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    print("Hello World!")
    print("Welcome to my CIS110_CourseProject!")
    print("I am Katie, your chatbot.")
    print("When I ask you a question, please answer and press Enter afterwards.")
    
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
        
        # Giving the user options on a dog or cat
        animal = input("What main character would you like to have, a dog or a cat? ").lower()
        while animal not in ["dog", "cat"]:
            print("Please choose either 'dog' or 'cat'.")
            animal = input("What main character would you like to have, a dog or a cat? ").lower()
        
     
      
        
     
    print("Thanks for playing!")

if __name__ == "__main__":
    main()