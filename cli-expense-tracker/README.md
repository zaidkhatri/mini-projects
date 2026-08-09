# Expense Tracker (CLI)

A simple command-line app for tracking personal expenses, built in Python
using only the standard library. Add expenses, sort them into categories,
view your spending, and delete entries you no longer need. Everything is
saved automatically so your data is still there the next time you run it.

## Features

- Add expenses with a category, description, and amount
- View all expenses, or filter by category
- Delete an expense by its ID
- See your total spending, overall or per category
- See a breakdown of spending grouped by category
- Data is saved to `data/expenses.json`, so nothing is lost between runs
- Basic logging of what the app does, written to `expense_tracker.log`

## Project structure

```
expense_tracker/
├── main.py              # Entry point — run this. Handles the menu and user input.
├── expense_tracker.py    # Expense and ExpenseTracker classes — the actual logic.
├── data/
│   └── expenses.json     # Created automatically the first time you add an expense.
└── expense_tracker.log   # Created automatically once the app runs.
```

Just two Python files, each with a clear job:

- **`expense_tracker.py`** — defines what an expense *is* (`Expense`) and
  handles adding, deleting, listing, totaling, and saving/loading expenses
  (`ExpenseTracker`). This is the only file that reads or writes files.
- **`main.py`** — shows the menu, reads what you type, and calls the right
  method on `ExpenseTracker`. It doesn't know anything about how expenses
  are stored — it just asks the tracker to do things.

## Requirements

- Python 3.8 or later
- No external packages needed — everything used is from the standard library
  (`json`, `os`, `logging`, `datetime`)

## Running the app

From inside the `expense_tracker` folder:

```bash
python main.py
```

You'll see a menu like this:

```
==== Expense Tracker ====
1. Add expense
2. View all expenses
3. View expenses by category
4. Delete expense
5. View total spending
6. View spending by category
7. Exit
```

Type the number of the option you want and press Enter, then follow the
prompts. For example, adding an expense looks like:

```
Choose an option (1-7): 1
Category (e.g. Food, Rent, Transport): Food
Description: Groceries
Amount ($): 45.20
Added: [1] 2026-07-31  Food         Groceries                 $45.20
```

## Where your data goes

- **Expenses** are stored in `data/expenses.json`, as plain JSON. You can
  open this file in a text editor to see your data directly. It's created
  automatically the first time you add an expense — no setup needed.
- **Logs** are written to `expense_tracker.log` in the project folder. This
  file records things like when an expense was added or deleted, and any
  invalid input along the way (e.g. trying to delete an ID that doesn't
  exist). It's useful for seeing a history of what happened without
  cluttering the terminal itself.

Neither file needs to exist before you run the app — both are created the
first time they're needed.

## Possible extensions

Ideas if you want to keep building on this project:

- Add a monthly budget with warnings when you go over
- Export expenses to a CSV file
- Add date-range filtering (e.g. "this month")
- Add an `edit_expense` method to update an existing entry
- Add colored terminal output for a nicer-looking menu