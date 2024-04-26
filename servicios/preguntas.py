from flask import jsonify, request

def preguntas_identificacion():
    data = request.get_json()

    # Comprobar si todos los campos requeridos están presentes
    required_fields = ['idUsuarioEntidad', 'paramProducto', 'producto', 'canal', 'solicitudCuestionario']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en la solicitud'}), 400

    # Comprobar si todos los campos requeridos están presentes en solicitudCuestionario
    required_fields = ['tipoId', 'identificacion', 'regValidacion']
    if not all(field in data['solicitudCuestionario'] for field in required_fields):
        return jsonify({'error': 'Faltan campos requeridos en solicitudCuestionario'}), 400

    # Si todo está bien, devolver la respuesta predefinida
    response = {
        "id": "50047294",
        "resultado": "01",
        "registro": "4434791",
        "excluirCliente": "false",
        "alertas": "false",
        "respuestaAlerta": "03",
        "codigoAlerta": "00",
        "Pregunta": [
            {
                "id": "005006002",
                "texto": "HACE CUANTO TIEMPO TIENE USTED UN/UNA CREDITO DE VEHICULOS O MOTOS  CON ASTROMOTOS S.A.",
                "orden": "1",
                "idRespuestaCorrecta": "06",
                "peso": "1",
                "Respuesta": [
                    {
                        "id": "001",
                        "texto": "MENOR O IGUAL A 1 AÑO"
                    },
                    {
                        "id": "002",
                        "texto": "ENTRE 1 Y 2 AÑOS"
                    },
                    {
                        "id": "003",
                        "texto": "ENTRE 2 Y 3 AÑOS"
                    },
                    {
                        "id": "004",
                        "texto": "ENTRE 3 Y 4 AÑOS"
                    },
                    {
                        "id": "005",
                        "texto": "MAYOR A 4 AÑOS"
                    },
                    {
                        "id": "006",
                        "texto": "NO TENGO CREDITO DE VEHICULOS O MOTOS CON LA ENTIDAD"
                    }
                ]
            },
            {
                "id": "001004003",
                "texto": "CUAL ES EL DEPARTAMENTO DE EXPEDICION DE SU DOCUMENTO DE IDENTIDAD?",
                "orden": "2",
                "idRespuestaCorrecta": "04",
                "peso": "1",
                "Respuesta": [
                    {
                        "id": "001",
                        "texto": "CAUCA"
                    },
                    {
                        "id": "002",
                        "texto": "TOLIMA"
                    },
                    {
                        "id": "003",
                        "texto": "ARAUCA"
                    },
                    {
                        "id": "004",
                        "texto": "CORDOBA"
                    },
                    {
                        "id": "005",
                        "texto": "RISARALDA"
                    },
                    {
                        "id": "006",
                        "texto": "NINGUNA DE LAS ANTERIORES"
                    }
                ]
            },
            {
                "id": "006003002",
                "texto": "EN LOS ULTIMOS 6 MESES SOBRE SU CUENTA DE AHORRO CON BANCAMIA S.A. - BANCO DE LAS MICROFINANZAS USTED RECLAMO ANTE DATACREDITO SOLICITANDO:",
                "orden": "3",
                "idRespuestaCorrecta": "06",
                "peso": "1",
                "Respuesta": [
                    {
                        "id": "001",
                        "texto": "ACTUALIZAR INFORMACION"
                    },
                    {
                        "id": "002",
                        "texto": "RECTIFICAR LA INFORMACION"
                    },
                    {
                        "id": "003",
                        "texto": "CONOCER LA INFORMACION"
                    },
                    {
                        "id": "004",
                        "texto": "OTROS  "
                    },
                    {
                        "id": "005",
                        "texto": "NO HE COLOCADO RECLAMOS"
                    },
                    {
                        "id": "006",
                        "texto": "NO TENGO CUENTA DE AHORRO CON BANCAMIA S.A. - BANCO DE LAS MICROFINANZAS"
                    }
                ]
            },
            {
                "id": "008003004",
                "texto": "USTED HA SOLICITADO PERSONALMENTE O POR CARTA INFORMACION DE SU HISTORIAL A DATACREDITO EN LOS ULTIMOS 6 MESES?",
                "orden": "4",
                "idRespuestaCorrecta": "02",
                "peso": "1",
                "Respuesta": [
                    {
                        "id": "001",
                        "texto": "SI HE SOLICITADO"
                    },
                    {
                        "id": "002",
                        "texto": "NO HE SOLICITADO"
                    }
                ]
            }
        ]
    }
    return jsonify(response)
