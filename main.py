from utils.AddReminder import AddReminder
from utils.Disease import AddDisease, RemoveDisease
from utils.Recognition import Recognition
from utils.Speak import Speak
from utils.AddDiet import AddDiet
import random
import json
import webbrowser
from datetime import datetime
import tkinter as tk


# * Add Reminder
# * Add Sickness
# * Remove Sickness
# * Add Meal
# * Check what user should eat


class Main:
    def __init__(self) -> None:
        now = datetime.now()
        self.current_time = now.strftime("%H:%M")

    def run(self, name):
        # Todo: uncomment this if you want to use speechrecognition
        command = Recognition()
        # Todo: comment this to remove command line inputs
        # command = input("Enter command: ")

        # Add Diet to the database
        if "add diet" in command:
            Speak("What did you had for your meal?")
            # Todo: uncomment this if you want to use speechrecognition
            command = Recognition()
            # Todo: comment this to remove command line inputs
            # command = input("What did you had for your meal?")

            with open('./data/health.json', 'r') as file:
                health_data = json.load(file)

            if health_data['disease'] != "":
                # Speak("You should eat healthy when you are sick.")
                print('You should eat healthy when you are sick.')

            # AddDiet(current_time=self.current_time, food=command)
            Speak("Your meal has been recorded.")

        # Add Sickness to the database
        if "add sickness" in command:
            Speak("What is your sickness?")
            # Todo: uncomment this if you want to use speechrecognition
            command = Recognition()
            # Todo: comment this to remove command line inputs
            # command = input("What is your sickness?")
            AddDisease(disease=command)
            Speak("Your sickness has been recorded.")

        # Remove Sickness from the database
        if "remove sickness" in command:
            RemoveDisease()
            Speak("I am glad you are healthy again.")

        # Get the food to eat if you have a disease
        if "what should i eat" in command:
            with open('./data/health.json', 'r') as file:
                health = json.load(file)

                if health['disease'] == "":
                    Speak("You are healthy. You can eat anything.")
                else:
                    with open('./data/disease.json', 'r') as file:
                        disease = json.load(file)

                        for sickness in disease['disease']:
                            foods = sickness['food']
                            food = random.choice(foods)
                            Speak(f"You should eat {food}.")
                            print(food)

        # Add Reminder to the database
        if "add reminder" in command:
            Speak("Please set the time for the reminder.")
            # Speak('Currently I am not able to add reminders. I can remind you at eight in the morning on your set day.')
            # Speak('What day do you want me to remind you?')
            # day = input('What day do you want me to remind you? ')
            # AddReminder(day)
            root = tk.Tk()
            AddReminder(root)
            root.mainloop()

        # Open a playlist of meditation music on youtube
        if "relax" in command:
            url = 'https://www.youtube.com/watch?v=tFqcIREC8P8&list=PL988EAD3E24365240'
            webbrowser.open(url, new=0)

        if "exit" in command:
            Speak(f'Goodbye! {name}')
            exit()


if __name__ == "__main__":
    Speak('Hey, I am your personal assistant. What\'s your name')
    # Todo: uncomment this if you want to use speechrecognition
    name = Recognition()
    # Todo: comment this to remove command line inputs

    # Save user's name
    name = input('What\'s your name: ')
    Speak(f'Hello {name}')

    main = Main()

    while True:
        main.run(name=name)
