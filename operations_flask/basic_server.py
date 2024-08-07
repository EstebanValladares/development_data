from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/op", methods=['GET'])
def operations():
    number1 = float(request.args.get('number1', 0))
    number2 = float(request.args.get('number1', 0))

    suma = number1 + number2
    resta = number1 - number2
    multiplicacion = number1 * number2
    division = number1 / number2 if number2 != 0 else "No se puede dividir por cero"

    return jsonify({
        "number1": number1,
        "number2": number2,
        "suma": suma,
        "resta": resta,
        "multiplicacion": multiplicacion,
        "division": division
    })
