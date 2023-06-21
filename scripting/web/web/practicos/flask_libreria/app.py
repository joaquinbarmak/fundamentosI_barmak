from flask import Flask, render_template
print(dir(Flask))
from markupsafe import escape

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template('home_libreria.html')