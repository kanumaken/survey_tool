class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses  # Dictionary of category: amount

    def to_dict(self):
        """Convert the User object into a flat dictionary for CSV export"""
        data = {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
        }

        # Expense categories to flatten
        categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
        for cat in categories:
            data[cat] = self.expenses.get(cat, 0.0)
        
        return data
