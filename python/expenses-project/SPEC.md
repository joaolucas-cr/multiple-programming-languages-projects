run by running expenses_tracker.py
# Project 1: Personal Expense Tracker

## Objective

Build a command-line Python application that allows users to record expenses, manage spending, and view financial summaries.

## Business Rules

### BR01 — Add an Expense

- Every expense must have a description, amount, category, and date.
- The amount must be greater than zero.
- The description cannot be empty.
- Every expense must receive a unique ID.
- If no date is provided, use the current date.

### BR02 — Expense Categories

- Supported categories:
  - Food
  - Transportation
  - Entertainment
  - Education
  - Bills
  - Other
- Users must select an existing category.
- Invalid categories must be rejected.
- Category names must be case-insensitive.

### BR03 — View Expenses

- Users must be able to view all registered expenses.
- Display the ID, description, amount, category, and date.
- Sort expenses by date, newest first.
- Display an appropriate message if no expenses exist.

### BR04 — Edit Expenses

- Users must be able to edit an expense using its ID.
- Users can modify the description, amount, category, or date.
- All updated information must be validated.
- Editing a nonexistent expense must display an error.

### BR05 — Delete Expenses

- Expenses must be deleted using their unique ID.
- The application must ask for confirmation before deleting.
- Deleted expenses must no longer appear in reports.
- Attempting to delete a nonexistent expense must display an error.

### BR06 — Spending Summary

- The application must calculate total expenses.
- Users must be able to see spending totals by category.
- Users must be able to filter expenses by month.
- All monetary values must display two decimal places.

### BR07 — Monthly Budget

- Users must be able to establish a monthly spending limit.
- The budget must be greater than zero.
- The system must calculate how much of the budget remains.
- If expenses exceed the budget, display a warning.
- Expenses must still be allowed when the budget is exceeded.

### BR08 — Data Persistence

- Expenses must be saved to a local JSON file.
- Data must automatically load when the application starts.
- Every successful modification must be saved.
- If the file does not exist, start with an empty expense list.
- Corrupted files must produce a clear error without silently overwriting existing data.

## Required Application Menu

```text
===== PERSONAL EXPENSE TRACKER =====

1. Add Expense
2. View All Expenses
3. Edit Expense
4. Delete Expense
5. View Spending Summary
6. Filter Expenses
7. Set Monthly Budget
8. View Budget Status
9. Exit

Select an option:
```

## Example Expense Data

```json
{
  "id": 1,
  "description": "Lunch",
  "amount": 15.50,
  "category": "Food",
  "date": "2026-10-24"
}
```

## Development Requirements

- Use Python's standard library only.
- Build a terminal application.
- Organize functionality into reusable functions.
- Use JSON for data storage.
- Use `Decimal` for monetary calculations.
- Handle invalid inputs without crashing.
- Do not use a database or external frameworks.

## Acceptance Tests

- [ ] Add a valid expense successfully.
- [ ] Reject negative or zero amounts.
- [ ] Reject empty descriptions.
- [ ] Reject invalid categories.
- [ ] Display an error for nonexistent expense IDs.
- [ ] Require confirmation before deleting expenses.
- [ ] Display a warning when the budget is exceeded.
- [ ] Preserve expenses after restarting the application.

## Definition of Done

The project is complete when all eight business rules are implemented, all acceptance tests pass, and the application preserves data between executions.
