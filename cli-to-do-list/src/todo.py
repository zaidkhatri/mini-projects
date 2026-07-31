import argparse
import json
import os

class TodoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def _save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, description):
        task = {"description": description, "done": False}
        self.tasks.append(task)
        self._save_tasks()
        print(f"Added task '{description}'")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet. Add one with the add command")
            return

        for i, task in enumerate(self.tasks, start=1):
            status = "x" if task["done"] else " "
            print(f"{status} {i}. {task['description']}")

    def complete_task(self, task_number):
        index = task_number - 1
        if index < 0 or index >= len(self.tasks):
            print(f"No task found with task number {task_number}")
            return

        self.tasks[index]["done"] = True
        self._save_tasks()
        print(f"Marked task {task_number} as done.")

    def delete_task(self, task_number):
        index = task_number - 1
        if index < 0 or index >= len(self.tasks):
            print(f"No task found with task number {task_number}")
            return

        removed = self.tasks.pop(index)
        self._save_tasks()
        print(f"Deleted task {removed['description']}")

def build_parser():
    parser = argparse.ArgumentParser(description="A simple command line Todo list app")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")

    subparsers.add_parser("list", help="List all tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("task_number", type=int, help="Number of the task to mark as done")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_number", type=int, help="Number of the task to delete")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    app = TodoApp()

    if args.command == "add":
        app.add_task(args.description)
    elif args.command == "list":
        app.list_tasks()
    elif args.command == "done":
        app.complete_task(args.task_number)
    elif args.command == "delete":
        app.delete_task(args.task_number)


if __name__ == "__main__":
    main()
   