from flask import Flask, jsonify, request

app = Flask(__name__) # se crea la instancia de la clase Flask
@app.route("/op", methods=['POST']) # se establece el endpoint y el método HTTP

def operations():# se establece la función que se ejecutará al acceder al endpoint
    data = request.get_json() #se establece la variable data que obtiene los datos enviados en la petición
    number1 = float(data.get('number1')) #se obtiene el valor de la clave number1 y se convierte a float
    number2 = float(data.get('number2')) #se obtiene el valor de la clave number2 y se convierte a float

    #operaciones matemáticas
    suma = number1 + number2;
    resta = number1 - number2;
    multiplicaicion = number1 * number2;
    division = number1 / number2;
    
    return jsonify({ #se retorna un objeto JSON con los resultados de las operaciones
        "number": number1,
        "number2": number2,
        "suma": suma,
        "resta": resta,
        "multiplicacion": multiplicaicion,
        "division": division 
    })
if __name__ == '__main__': #se ejecuta el servidor en el puerto 5000
    app.run(host= '0.0.0.0',port=5000,debug=False,use_reloader=False) 