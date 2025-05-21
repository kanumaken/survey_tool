# survey_tool

# 🧾 Survey Tool - Income and Spending Tracker

A simple web application built with **Flask** and **MongoDB** to collect survey data on income and spending habits. This project can be used to analyze financial patterns across age groups and demographics.

## 🔧 Features

- Collects user demographic data (age, gender)
- Captures total income and optional spending categories
- Interactive form with dynamic expense inputs
- Stores all responses in MongoDB
- Lightweight and easy to deploy

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Database:** MongoDB
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** AWS EC2 or ECS

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kanumaken/survey_tool.git
cd survey_tool
````

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist yet, use:

```bash
pip install flask pymongo
```

### 4. Configure MongoDB

By default, the app connects to a local MongoDB instance:

```python
client = MongoClient('mongodb://localhost:27017/')
```

If you're using **MongoDB Atlas**, update your connection string in `app.py` accordingly.

### 5. Run the Application

```bash
python app.py
```



## 📂 Project Structure

```
survey_tool/
│
├── app.py                         # Main Flask application
├── requirements.txt              # List of dependencies
├── .env                          # Environment variables (e.g., MongoDB URI)
│
├── templates/
│   └── survey.html               # HTML form template
│
├── static/
│   └── style.css                 # Optional CSS for styling
│
├── data/                         # Data storage folder
│   ├── survey_data.csv           # Exported data from MongoDB
│   └── charts/                   # Saved visualizations for PowerPoint
│       ├── ages_highest_income.png
│       └── gender_spending_distribution.png
│
├── scripts/                      # Python scripts for data processing
│   ├── extract_and_export.py     # Script: MongoDB → CSV
│   └── user_model.py             # User class definition
│
└── notebooks/                    # Jupyter Notebooks for analysis
    └── data_analysis.ipynb       # Visualizations and insights



---

## 📤 Deployment

You can deploy this project to:

* 🖥️ **AWS EC2** or ECS (using Docker)
* ☁️ **Heroku**, **Render**, or other cloud providers
* 🐳 Docker (containerized deployments)

Let me know if you'd like deployment support.

---

## ✅ To Do

* [ ] Add form validation
* [ ] Visualize collected data
* [ ] User authentication (optional)
* [ ] Export data to CSV/Excel

---



## 🙋‍♂️ Author

**KANUMA RUKEBA KEN**
🔗 [GitHub: @kanumaken](https://github.com/kanumaken)
📧 Email: [kenkanuma0@gmail.com](mailto:kenkanuma0@gmail.com)

---

