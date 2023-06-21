from flask import Flask, render_template
print(dir(Flask))
from markupsafe import escape
prendas = [
    {'id':1, 'tipo':'pantalon', 'talle': 42},
    {'id':2, 'tipo':'pantalon', 'talle': 56}
]
app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template('home_tp.html')