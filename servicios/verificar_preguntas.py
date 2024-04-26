from flask import jsonify, request

def verificar_preguntas():
    data = request.get_json()

    # Comprobar si todos los campos requeridos están presentes
    required_fields = ['idUsuarioEntidad', 'paramProducto', 'producto', 'respuestas']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en la solicitud'}), 400

    # Comprobar si todos los campos requeridos están presentes en respuestas
    required_fields = ['idCuestionario', 'regCuestionario', 'identificacion', 'respuesta']
    if not all(field in data['respuestas'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en respuestas'}), 400

    # Si todo está bien, devolver la respuesta predefinida
    response = {
        "resultado": "true",
        "aprobacion": "false",
        "preguntasCompletas": "true",
        "score": "000",
        "codigoSeguridad": "OXQ6HG6",
        "idCuestionario": "50090799",
        "regCuestionario": "4530561",
        "aprobado100PorCientoOK": "false"
    }
    return jsonify(response)

