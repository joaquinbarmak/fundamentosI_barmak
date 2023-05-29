from flask import Flask
print(dir(Flask))
'''prendas = [
    {'id':1, 'tipo':'pantalon', 'talle': 42},
    {'id':2, 'tipo':'pantalon', 'talle': 56}
]'''
app = Flask(__name__)

#@app.get('/')
@app.route('/', methods=["PUT"])
def home():
    return '<p> Te damos la bienvenida a MacoWins</p>'

if __name__ == '__main__':
    app.run(debug=True)

#tarea: armar la ruta /prendas que muestre todos los items de prendas