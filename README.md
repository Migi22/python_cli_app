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
├── quiz/
├── password_generator/
├── alarm_clock/
```

## Future Plans

- GUI version (Tkinter or PyQt)
- Persistent data storage (JSON)
- Rich CLI interface
- Export as .exe using PyInstaller
