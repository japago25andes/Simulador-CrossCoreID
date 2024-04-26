from flask import jsonify, request

def otp_initialize():
    data = request.get_json()

    # Comprobar si todos los campos requeridos están presentes
    required_fields = ['idUsuarioEntidad', 'xmlIniciarTransaccionOTP']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en la solicitud'}), 400

    # Comprobar si todos los campos requeridos están presentes en xmlIniciarTransaccionOTP
    required_fields = ['IniciarTransaccionOTPSolicitud']
    if not all(field in data['xmlIniciarTransaccionOTP'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en xmlIniciarTransaccionOTP'}), 400

    # Comprobar si todos los campos requeridos están presentes en IniciarTransaccionOTPSolicitud
    required_fields = ['codParametrizacion', 'Identificacion', 'DatosCuestionario']
    if not all(field in data['xmlIniciarTransaccionOTP']['IniciarTransaccionOTPSolicitud'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en IniciarTransaccionOTPSolicitud'}), 400

    # Si todo está bien, devolver la respuesta predefinida
    response = {
        "codParametrizacion": "2740",
        "DatosCuestionario": {
            "procesoEvidente": "VALDCN",
            "regValidacion": "5834433"
        },
        "ResultadoGeneracion": {
            "codResultadoOTP": "4",
            "idTransaccionOTP": "ff5f7f18-2bab-4d4e-9015-6cb58e47a0ed",
            "resultadoOTP": "true"
        }
    }
    return jsonify(response)
