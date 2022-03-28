from flask import Flask,render_template
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process",methods=["POST"])
def process():
    keys = ["Depressed","Non-Depressed","Doctor's Diagnosis","Final Result"]
    depressed_value = random.randint(65,85)
    response = [
        {"key":0,"property":"Depressed","value":f"{depressed_value}%"},
        {"key":1,"property":"Non-Depressed","value":f"{100-depressed_value}%"},
        {"key":2,"property":"Doctor's Diagnosis","value":"Non-Depressed"},
        {"key":3,"property":"Final Result","value":"Non-Depressed"},
    ]
    return {"prediction":response}
if __name__ == "__main__":
    app.run(debug=True)