from flask import Flask, render_template
print(dir(Flask))
from markupsafe import escape
prendas = [
    {'id':1, 'tipo':'pantalon', 'talle': 42},
    {'id':2, 'tipo':'pantalon', 'talle': 56}
]
app = Flask(__name__)

#@app.get('/')
@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')

#tarea: armar la ruta /prendas que muestre todos los items de prendas
@app.route('/', methods=['GET'])
def mostrar_prendas():
    catalogo =''
    for prenda in prendas:
        catalogo += 'Prenda {prenda[id]}: Tipo{prenda[tipo]}, Talle {prenda[talle]}'

@app.route('/prendas', methods=["GET"])
def get_all_prendas():
    return '<p>Mostrando todas las prendas<p>'

@app.route('/prendas/<id>', methods=["GET"])
def get_prenda(id):
    return f'<p>Mostrando la prenda {id}<p>'