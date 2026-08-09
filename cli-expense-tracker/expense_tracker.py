import json
import os
import logging
from datetime import date

logger = logging.getLogger(__name__)

class Expense:
    """A single expense: a category, description, and amount."""
    def __init__(self, id, date, category, description, amount):
        self.id = id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount


    def to_dict(self):
        """Convert this expense into a dictionary, ready for JSON storage."""
        return {
            "id": self.id,
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }

    def __str__(self):
        return (
            f"[{self.id}] {self.date} "
            f"{self.category:<12} "
            f"{self.description:<24} "
            f"${self.amount:,.2f}"
        )

class ExpenseTracker:
    """Keeps track of expenses and saves them to a JSON file."""
    def __init__(self, filename="data/expenses.json"):
        self.filename = filename
        self.expenses = self._load()

    def _load(self):
        """Load expenses from the JSON file, if it exists."""
        if not os.path.exists(self.filename):
            return []

        with open(self.filename) as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                logger.error("Could not parse %s — starting with an empty list.", self.filename)
                return []

            logger.info("Loaded %d expense(s) from %s.", len(data), self.filename)
            return [Expense(**item) for item in data]

    def _save(self):
        """Write the current list of expenses to the JSON file."""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "w") as file:
            json.dump([expense.to_dict() for expense in self.expenses], file, indent=2)

    def _next_id(self):
        """Work out the next free ID to use for a new expense."""
        if not self.expenses:
            return 1
        return max(expense.id for expense in self.expenses) + 1

    def add_expense(self, category, description, amount):
        """Add a new expense and save it to disk."""
        if amount <= 0:
            logger.warning("Rejected expense with non-positive amount: %s", amount)
            raise ValueError("Amount must be greater than zero.")

        expense = Expense(
            id=self._next_id(),
            date=date.today().isoformat(),
            category=category.strip().title(),
            description=description.strip(),
            amount=round(amount, 2)
        )
        self.expenses.append(expense)
        self._save()
        logger.info("Added expense %d: %s ($%.2f)", expense.id, expense.category, expense.amount)
        return expense

    def delete_expense(self, expense_id):
        """Delete an expense by ID. Returns True if something was deleted."""
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                self._save()
                logger.info("Deleted expense %d.", expense_id)
                return True
        logger.warning("Tried to delete expense %d, but it doesn't exist.", expense_id)
        return False

    def list_expenses(self, category=None):
        """Return expenses sorted by date, optionally filtered by category."""
        expenses = self.expenses
        if category:
            expenses = [e for e in expenses if e.category.lower() == category.strip().lower()]
        return sorted(expenses, key=lambda e:e.date)

    def total_spending(self, category=None):
        """Return the total amount spent, optionally filtered by category."""
        expenses = self.list_expenses(category)
        return round(sum(expense.amount for expense in expenses), 2)

    def spending_by_category(self):
        """Return a dictionary of total spending per category."""
        summary = {}
        for expense in self.expenses:
            summary[expense.category] = round(summary.get(expense.category, 0) + expense.amount, 2)
        return summary
            


            