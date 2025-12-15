from flask import Flask
from tasks import add

app = Flask(__name__)

@app.route("/")
def home():
    result = add.delay(2, 3)
    return "Task triggered!"

if __name__ == "__main__":
    app.run(debug=True)
