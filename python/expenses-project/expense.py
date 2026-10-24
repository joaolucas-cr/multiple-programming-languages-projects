from uuid import uuid4 as generateUUID
from datetime import date

class Expense():
    # amount, category, description, date
    categories = ['Food', 'Transportation', 'Entertainment', "Education", "Education", "Bills", "Other"]

    def isValidCategory(ctg):
        if(ctg in Expense.categories): 
            return True
        return False

    def _populate(self, amount, description, category, dt):
        if(amount <= 0):
            raise ValueError("Amount must be greater than 0.")
        if(len(description.strip()) == 0):
            raise ValueError("Description must not be empty.")
        if(not Expense.isValidCategory(category)):
            raise ValueError("Category is not valid.")
        self.description = description

        if(dt):
            self.date = date.fromisoformat(dt)
        else:
            self.date = date.today()

        self.amount = amount
        self.category = category

    def __init__(self, amnt, ctgry, dscp, dt):
        self.id = str(generateUUID())
        self._populate(amnt, dscp, ctgry, dt)

    def getID(self):
        return self.id

    def toDict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": str(self.date)
        }

    def update(self, amount, description, category, date):
        self._populate(float(amount), description, category, date)

    def __str__(self):
        return "ID: " + str(self.id) + " Description: " + self.description + " Amount: " + str(self.amount) + " Category: " + self.category + " Date: " + str(self.date)

    