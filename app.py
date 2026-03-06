from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def index():

    student = None

    if request.method == "POST":
        name = request.form.get("name")

        query = f"SELECT * FROM students WHERE name='{name}'"

        result = db.session.execute(query)

        student = result.fetchone()

    return render_template("index.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)