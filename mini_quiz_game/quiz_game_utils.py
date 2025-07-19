''' This is where the mini quiz game utilities are located like load_highscores and save_highscores'''

import json
import os

HIGHSCORE_FILE = "highscores.json"

# Loads the highscores
def load_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return{}
    with open(HIGHSCORE_FILE, "r") as file:
        return json.load(file)

# Saves the highscores
def save_highscores(data):
    with open(HIGHSCORE_FILE, "w") as file:
        json.dump(data, file, indent=1)

# load the questions
def load_questions(filename="questions.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)