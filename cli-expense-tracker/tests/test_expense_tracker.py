import json
import pytest

from expense_tracker import ExpenseTracker


@pytest.fixture
def tracker(tmp_path):
    return ExpenseTracker(tmp_path / "expenses.json")


def test_new_tracker_is_empty(tracker):
    assert tracker.expenses == []


def test_add_expense(tracker):
    expense = tracker.add_expense("food", "Burger", 15.50)

    assert expense.id == 1
    assert expense.category == "Food"
    assert expense.description == "Burger"
    assert expense.amount == 15.50
    assert len(tracker.expenses) == 1


def test_add_multiple_expenses_increments_id(tracker):
    tracker.add_expense("Food", "Pizza", 20)
    second = tracker.add_expense("Fuel", "Gas", 40)

    assert second.id == 2


@pytest.mark.parametrize("amount", [0, -1, -100])
def test_invalid_amount_raises(tracker, amount):
    with pytest.raises(ValueError):
        tracker.add_expense("Food", "Bad", amount)


def test_delete_existing_expense(tracker):
    expense = tracker.add_expense("Food", "Pizza", 20)

    assert tracker.delete_expense(expense.id) is True
    assert tracker.expenses == []


def test_delete_missing_expense_returns_false(tracker):
    assert tracker.delete_expense(999) is False


def test_total_spending(tracker):
    tracker.add_expense("Food", "Pizza", 20)
    tracker.add_expense("Fuel", "Gas", 40)

    assert tracker.total_spending() == 60


def test_total_spending_by_category(tracker):
    tracker.add_expense("Food", "Pizza", 20)
    tracker.add_expense("Food", "Burger", 15)
    tracker.add_expense("Fuel", "Gas", 40)

    assert tracker.total_spending("Food") == 35


def test_spending_by_category(tracker):
    tracker.add_expense("Food", "Pizza", 20)
    tracker.add_expense("Food", "Burger", 15)
    tracker.add_expense("Fuel", "Gas", 40)

    assert tracker.spending_by_category() == {
        "Food": 35,
        "Fuel": 40,
    }


def test_data_persists(tmp_path):
    filename = tmp_path / "expenses.json"

    tracker = ExpenseTracker(filename)
    tracker.add_expense("Food", "Pizza", 20)

    tracker2 = ExpenseTracker(filename)

    assert len(tracker2.expenses) == 1
    assert tracker2.expenses[0].description == "Pizza"