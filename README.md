# Python CLI Utility Toolkit

A menu-driven Python CLI app that includes:

- ✅ To-Do List
- ✅ Currency Converter (Using API)
- ✅ Mini Quiz Game
- ✅ Password Generator
- ✅ Alarm Clock

## Project Flowchart

You can view the flowchart here: https://www.canva.com/design/DAGtPGkyLjI/OcvNAURE_qMAAIDFgV3MVQ/view?utm_content=DAGtPGkyLjI&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hd6e92cc4f3

## Getting Started

Run the main program with:

```bash
python main.py
```

or download the .exe that can be found on release section

## Project Structure

```bash
/python_cli_app/
├── main.py                          # Entry point of the CLI
├── emoji_util.py                    # Shared emoji constants across modules
├── .gitignore
# Modules
├── currency_converter/
│   ├── __init__.py                  # Contains run() to launch the currency converter
│   ├── converter_api.py             # handles the fetching exchange rates
├── todo_list/
│   ├── __init__.py                  # Contains run() to launch the To-Do List
│   ├── add.py                       # add_task() function
│   ├── view.py                      # view_tasks() function
│   ├── delete.py                    # delete_task() function
│   ├── mark_done.py                 # mark_done() function
│   ├── utils.py                     # load_tasks(), save_task()
├── todo.json                        # (Generated) This is your saved task data (excluded from Git)
├── mini_quiz_game/
│   ├── __init__.py                  # Contains run() to launch the Mini quiz game
│   ├── questions.json               # contains the set of questions
│   ├── quiz_game_utils.py           # utilities for the  quiz game like load, display, save of scores
│   ├── quiz_game.py                 # the quiz_game() function locates here
├── password_generator/
│   ├── __init__.py                  # Contains run() to launch the password generator
│   ├── password_util.json           # contains the utilities used to password generator (eg. generate_password() and custom_password_generator())
├── alarm_clock/                     # contains the run() for lunching the alarm clock logic
```

## Future Plans

- GUI version (Tkinter or PyQt)
- Rich CLI interface
