from flask import jsonify, request


def otp_evaluation():
    data = request.get_json()

    # Comprobar si todos los campos requeridos están presentes
    required_fields = ['idUsuarioEntidad', 'codProducto', 'codParametrizacion', 'nit', 'xmlGenerarEvaluacionDeRiesgoOTP']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en la solicitud'}), 400

    # Comprobar si todos los campos requeridos están presentes en xmlGenerarEvaluacionDeRiesgoOTP
    required_fields = ['GenerarEvaluacionDeRiesgoOTP']
    if not all(field in data['xmlGenerarEvaluacionDeRiesgoOTP'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en xmlGenerarEvaluacionDeRiesgoOTP'}), 400

    # Comprobar si todos los campos requeridos están presentes en GenerarEvaluacionDeRiesgoOTP
    required_fields = ['DatosCuestionario', 'Identificacion', 'DatosEvaluacion', 'DatosCodigoEmailOTP', 'Solucion']
    if not all(field in data['xmlGenerarEvaluacionDeRiesgoOTP']['GenerarEvaluacionDeRiesgoOTP'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en GenerarEvaluacionDeRiesgoOTP'}), 400

    # Si todo está bien, devolver la respuesta predefinida
    response = {
        "codParametrizacion": "2740",
        "ResultadoValidacion": {
            "enviadoOtpCorreo": "true",
            "enviadoOtpCelular": "true",
            "riesgoCorreo": "bajo",
            "riesgoCelular": "medio",
            "rankingReconocer": "1",
            "numeroValido": "true"
        },
        "ResultadoGeneracion": {
            "requiereCuestionario": "true",
            "timestampOTP": "2022/02/23 15:03:30",
            "codResultadoOTP": "4",
            "idTransaccionOTP": "ff5f7f18-2bab-4d4e-9015-6cb58e47a0ed",
            "resultadoOTP": "true"
        },
        "DatosCuestionario": {
            "procesoEvidente": "VALDCN",
            "regValidacion": "5834433"
        }
    }
    return jsonify(response)