from flask import jsonify, request


def otp_verify():
    data = request.get_json()

    # Comprobar si todos los campos requeridos están presentes
    required_fields = ['idUsuarioEntidad', 'xmlVerificarCodigoOTP']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en la solicitud'}), 400

    # Comprobar si todos los campos requeridos están presentes en xmlVerificarCodigoOTP
    required_fields = ['VerificarCodigoOTPSolicitud']
    if not all(field in data['xmlVerificarCodigoOTP'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en xmlVerificarCodigoOTP'}), 400

    # Comprobar si todos los campos requeridos están presentes en VerificarCodigoOTPSolicitud
    required_fields = ['codParametrizacion', 'DatosCuestionario', 'Identificacion', 'DatosCodigoOTP']
    if not all(field in data['xmlVerificarCodigoOTP']['VerificarCodigoOTPSolicitud'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en VerificarCodigoOTPSolicitud'}), 400

    if data['xmlVerificarCodigoOTP']['VerificarCodigoOTPSolicitud']['DatosCodigoOTP']['codigoOTP'] == "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92":
        response = {
            "VerificarCodigoOTPRespuesta": {
                "resultadoValidacion": "1",
                "codParametrizacion": "2740",
                "mensajeValidacion": "Validación del código OTP exitoso.",
                "codigoValido": "true",
                "idTransaccionOTP": "ff5f7f18-2bab-4d4e-9015-6cb58e47a0ed"
            }
        }
        return jsonify(response)


    # Si todo está bien, devolver la respuesta predefinida
    response = {
        "VerificarCodigoOTPRespuesta": {
            "resultadoValidacion": "1",
            "codParametrizacion": "2740",
            "mensajeValidacion": "Validación del código OTP exitoso.",
            "codigoValido": "false",
            "idTransaccionOTP": "ff5f7f18-2bab-4d4e-9015-6cb58e47a0ed"
        }
    }
    return jsonify(response)
