from flask import jsonify, request

def validar_identificacion():
    data = request.get_json()

    # Comprobar si todos los campos requeridos están presentes
    required_fields = ['idUsuarioEntidad', 'paramProducto', 'producto', 'canal', 'datosValidacion']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en la solicitud'}), 400

    # Comprobar si todos los campos requeridos están presentes en datosValidacion
    required_fields = ['identificacion', 'PrimerApellido', 'Nombres', 'FechaExpedicion']
    if not all(field in data['datosValidacion'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en datosValidacion'}), 400

    # Comprobar si todos los campos requeridos están presentes en identificacion
    required_fields = ['numero', 'tipo']
    if not all(field in data['datosValidacion']['identificacion'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en identificacion'}), 400

    # Si todo está bien, devolver la respuesta predefinida

    if(data['datosValidacion']['identificacion']['numero'] == "79974476"):

        response = {
            "valApellido": "true",
            "valNombre": "true",
            "valFechaExp": "true",
            "excluirCliente": "false",
            "alertas": "false",
            "respuestaAlerta": "03",
            "codigoAlerta": "00",
            "resultado": "01",
            "regValidacion": "8319717",
            "resultadoProceso": "true",
            "consultasDisponibles": "1",
            "Identificacion": {
                "numero": "00079974476",
                "tipo": "1"
            },
            "Nombre": "GUATAVA CASTIBLANCO MIGUEL FAIR",
            "FechaExpedicion": {
                "timestamp": "885945600000"
            }
        }

        return jsonify(response)
    
    response = {
            "valApellido": "true",
            "valNombre": "false",
            "valFechaExp": "true",
            "excluirCliente": "false",
            "alertas": "false",
            "respuestaAlerta": "04",
            "codigoAlerta": "00",
            "resultado": "01",
            "regValidacion": "5834433",
            "resultadoProceso": "true",
            "consultasDisponibles": "1",
            "Identificacion": {
                "numero": data['datosValidacion']['identificacion']['numero'],
                "tipo": "1"
            },
            "Nombre": "URANGO HOYOS ANA DOLORES",
            "FechaExpedicion": {
                "timestamp": "714697200000"
            }
        }
        
    return jsonify(response)
