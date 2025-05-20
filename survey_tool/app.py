from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (adjust URI accordingly)
client = MongoClient("mongodb://localhost:27017/")
db = client['survey_db']
collection = db['participants']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = request.form.get('age')
        gender = request.form.get('gender')
        total_income = request.form.get('total_income')

        # Expense categories and amounts
        expenses = {}
        categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']

        for category in categories:
            if request.form.get(category):  # checkbox checked
                amount = request.form.get(f'{category}_amount')
                try:
                    amount = float(amount)
                except (TypeError, ValueError):
                    amount = 0.0
                expenses[category] = amount

        # Create document to insert
        participant_data = {
            "age": int(age) if age else None,
            "gender": gender,
            "total_income": float(total_income) if total_income else None,
            "expenses": expenses
        }

        # Insert into MongoDB
        collection.insert_one(participant_data)

        return redirect(url_for('thank_you'))

    return render_template('survey_form.html')

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting your data!"

if __name__ == '__main__':
    app.run(debug=True)
