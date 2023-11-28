from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from articles import articles #aca conectos los articulos con mi archivo app.py
from usuarios import usuarios
from fechasRecital import fechasRecital
from zonas import zonas
from entradas import entradas

# app = Flask(__name__)
# CORS(app, origins="http://localhost:8080")  # Configura los orígenes permitidos, permito todos

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

# @app.route('/available-days', methods=['OPTIONS'])
# def options_available_days():
#     response = jsonify({'message': 'CORS preflight request handled'})
#     response.headers.add('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#     return response

# Resto de la configuración y rutas de la aplicación...
# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/articles')
def getArticles():
    # return jsonify(products)
    return jsonify({'articles': articles})
    # me devuelve los articulos 


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        article for article in articles if article['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

# Create Data Routes
@app.route('/articles', methods=['POST'])
def addArticle():
    new_article = {
        'id': request.json['id'],
        'title': request.json['title'],
        'body': request.json['body'],
        'fecha': request.json['fecha']
    }
    articles.append(new_article)
    return jsonify({"message":"Artículo agregado satisfactoriamente", 'artcles': articles})

# Update Data Route
@app.route('/products/<string:article_name>', methods=['PUT'])
def editProduct(article_name):
    productsFound = [article for article in articles if article['title'] == article_name]
    if (len(productsFound) > 0):
        productsFound[0]['title'] = request.json['title']
        productsFound[0]['body'] = request.json['body']
        productsFound[0]['fecha'] = request.json['fecha']
        return jsonify({
            'message': 'Article Updated',
            'article': productsFound[0]
        })
    return jsonify({'message': 'Article Not found'})

# DELETE Data Route
@app.route('/products/<string:article_name>', methods=['DELETE'])
def deleteProduct(article_name):
    productsFound = [article for article in articles if article['name'] == article_name]
    if len(productsFound) > 0:
        articles.remove(productsFound[0])
        return jsonify({
            'message': 'Article Deleted',
            'article': articles
        })

# #agrego ruta Login
# @app.route('/api/login', methods=['POST'])
# def login():
#     data = request.get_json();

#     username = data["nombreUsuario"],
#     password = data ["contrasenia"],

#     user = next((user for user in usuarios if user["name"]== username and user["password"]== password), None)
#     if user:
#         return jsonify({"status": "success", "user": user}), 200
#     else:
#         return jsonify({"status": "error"}), 401

@app.route('/login')
def getUsuarios():
    # return jsonify(products)
    return jsonify({'usuarios': usuarios})

# Get Data Routes
@app.route('/select-days')
def getAvailableDays():
    return jsonify(fechasRecital)

@app.route('/zones')
def getZones():
    return jsonify(zonas)

@app.route("/buy", methods=["POST"])
def buy():
    entrada = request.get_json();
    print("entrada: ", entrada)
    entradas.append(entrada)
    print("entradas: ", entradas)

    return jsonify({"message": "Compra exitosa"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)