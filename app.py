
"""
Travel-in-10 is an AI powered travel recommendation app designed to help the customer find their next dream holiday destination.

By answering 10 questions in a random order, the AI call will try to recommend 2 standard destinations and 1 surprise destination.



"""
"""
Travel-in-10 is an AI powered app to help customers find their next dream holiday destination.

Customers will be asked 10 questions in a random order - they can say as much or as little as they want.

This program was created for the Final Project of the Stanford Code In Place 2025 by Y. Pei

"""

import random
from ai import call_gpt

Q_HOLIDAY_TYPE = "What kind of holiday do you prefer? (e.g. beach holiday, city break, off-the-beaten track)"
Q_BUDGET = "What kind of budget do you have in mind? (e.g. luxury, backpacking)"
Q_JOURNEY_LENGTH = "How long should the journey to your destination be?"
Q_TRAVEL_COMPANIONS = "How many people do you want to travel with? (i.e. with family or alone)"
Q_NEAREST_AIRPORT = "Where is your nearest airport?"
Q_TIME = "When would you like to travel?"
Q_CRAZIEST_THING = "What is the craziest thing you've ever done (and enjoyed)? (e.g. sky diving)"
Q_CULTURAL_ACTIVITIES = "What are your favorite cultural activities (or none)?"
Q_FOOD_PREFERENCES = "What are your food preferences or favorite foods?"
Q_STAR_SIGN = "What is your star sign?"

previously_answered_questions = []

def convert_question_number_to_string(number):
    if number == 1:
        return Q_HOLIDAY_TYPE
    elif number == 2:
        return Q_BUDGET
    elif number == 3:
        return Q_JOURNEY_LENGTH
    elif number == 4:
        return Q_TRAVEL_COMPANIONS
    elif number == 5:
        return Q_NEAREST_AIRPORT
    elif number == 6:
        return Q_TIME
    elif number == 7:
        return Q_CRAZIEST_THING
    elif number == 8:
        return Q_CULTURAL_ACTIVITIES
    elif number == 9:
        return Q_FOOD_PREFERENCES
    elif number == 10:
        return Q_STAR_SIGN
    else:
        return ""

def random_travel_question():
    random_number = random.randint(1, 10)

    while random_number in previously_answered_questions:
        random_number = random.randint(1, 10)
    previously_answered_questions.append(random_number)

    return convert_question_number_to_string(random_number)

def build_prompt(pairs):
    prompt = "You are an expert travel agent. Let's find some exciting destinations for you based on what you've shared:\n\n"
    
    for question, answer in pairs:
        prompt += f"{question}\n{answer}\n\n"
    
    prompt += """Based on this, suggest three travel destinations that really suit them. Use the third option as a wild card to find a surprise destination that doesn't necessarily follow all the requirements (like star sign, activities, crazy things). The surprise destination should be in a geographically different place.
    For each one, give a short, personal reason why it’s a good fit. List the items in bullet
    points and suggest a few activities that may suit them and a price ballpark figure for each activity.
    Before listing the prices for activities also factor in prices like travel, accommodation and transfer costs, keep it short and snappy. 
    If the number of passengers was specified, use total cost. 
    If the user hasn't specified any preference, surprise them! Please do not repeat any activities 
    verbatim as you should take a holistic view on their personality - e.g. if the user specified helicopter ride, it shouldn't 
    be listed multiple times. Keep within the token limit and edit where required. Keep it short and snappy - mobile friendly output"""

    return prompt.strip()

def main():
    print("--- Welcome to Travel-In-10 --- \n\n")

    print("Struggling to find your next dream holiday destination?")
    print("Answer 10 simple questions and let yourself be surprised!")
    print("We will use your unique preferences to tailor some options.")
    print("You can share as much or little as you like - life is an adventure :)")
    print("")

    answers = []
    
    for i in range(10):
        question = random_travel_question()
        user_input = input(question + " \n").strip()

        if user_input:
            answers.append((question, user_input))
    
    print("\n--- Generating your travel suggestions ---\n")

    prompt = build_prompt(answers)
    response = call_gpt(prompt)
    print("\n--- Your Travel Suggestions ---\n")
    print(response)

if __name__ == "__main__":
    main()
