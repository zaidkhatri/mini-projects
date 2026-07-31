# To-Do CLI

A simple command-line to-do list application written in Python. Tasks are stored in a local JSON file, so your list persists between runs.

Built with only the Python standard library — no dependencies to install.

## Features

- Add tasks
- List tasks with their completion status
- Mark tasks as done
- Delete tasks
- Tasks persist in a local `tasks.json` file

## Requirements

- Python 3.6+

## Installation

Clone the repository and you're ready to go — no dependencies to install.

```bash
git clone https://github.com/your-username/todo-cli.git
cd todo-cli
```

## Usage

### Add a task

```bash
python todo.py add "Buy groceries"
```

### List all tasks

```bash
python todo.py list
```

```
[ ] 1. Buy groceries
[ ] 2. Write report
```

### Mark a task as done

```bash
python todo.py done 1
```

### Delete a task

```bash
python todo.py delete 2
```

## How it works

- `TodoApp` is the single class responsible for managing tasks: loading them from disk, saving them, and adding, listing, completing, or deleting them.
- Tasks are stored as a JSON list of objects, each with a `description` and a `done` flag.
- On startup, the app loads `tasks.json` from the current directory (creating an empty list if the file doesn't exist yet). Every change is saved back to the file immediately.
- Task numbers shown in `list` are 1-based and are used directly by the `done` and `delete` commands.

## Project structure

```
todo-cli/
├── todo.py       # Main application (TodoApp class + CLI)
├── tasks.json    # Created automatically to store your tasks
└── README.md
```

## License

MIT