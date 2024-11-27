### Create a dictionary of five countries and their capitals. Then write a simple quiz program that asks the user to name the capital of a randomly selected country. Keep track of the user's score and display it at the end.

import random

# create a dictionary of countries and capitals
countries = {
    "USA": "Washington",
    "Afghanistan": "Kabul",
    "Iran": "Tehran",
    "Egypt": "Cairo"
}

## initialize the score
score = 0

## Number of questions to ask
num_questions = 5

print("Welcome to the Capital City Quiz!")
print("You will be asked to name the capitals of 5 randomly selected countries. ")

# Quiz loop
for i in range(num_questions):
    # Randomly select a country
    country = random.choice(list(countries.keys()))
    correct_capital = countries[country]
    
    ## Ask the question
    user_answer = input(f"\nWhat is the capital of {country}?".strip().title())
    
    ## check the answer
    
    if user_answer == correct_capital:
        print("Correct!")
        score += 1
        
    else: 
        print(f"Sorry, the correct answer is {correct_capital}.")
        
print(f"\nQuiz complete! Your score is {score} out of {num_questions}")
        