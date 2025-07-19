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
    
def quiz_highscores():
    highscores = load_highscores()

    print("\n== Highscores ==")
    print(f"{'Username':<15}{'Correct':<10}{'Wrong':<10}{'Games':<10}{'Accuracy':<10}")
    for user, stats in sorted(highscores.items(), key=lambda x: x[1]['total_correct'] / max((x[1]['total_correct'] + x[1]['total_wrong']), 1), reverse=True):
        correct = stats['total_correct']
        wrong = stats['total_wrong']
        games = stats['total_games']
        accuracy = (correct / (correct + wrong)) * 100 if correct + wrong > 0 else 0
        print(f"{user:<15}{correct:<10}{wrong:<10}{games:<10}{accuracy:.2f}%")