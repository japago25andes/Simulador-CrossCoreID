from flask import Flask
from flask import Flask
from servicios.validar import validar_identificacion
from servicios.iniciar_transaccion_OTP import otp_initialize
from servicios.evaluacion_riesgo_OTP import otp_evaluation
from servicios.verificar_codigo_OTP import otp_verify
from servicios.preguntas import preguntas_identificacion
from servicios.verificar_preguntas import verificar_preguntas


app = Flask(__name__)

@app.route('/api/hola', methods=['GET'])
def hola():
    return 'Hola, mundo!'

#1
app.route('/op/evidentemaster/v1/identificacion/validar', methods=['POST'])(validar_identificacion)
#2
app.route('/da/evidente/v3/otp/initialize', methods=['POST'])(otp_initialize)
#3
app.route('/da/evidente/v3/otp/evaluation', methods=['POST'])(otp_evaluation)
#4
app.route('/da/evidente/v3/otp/verify', methods=['POST'])(otp_verify)
#5
app.route('/op/evidentemaster/v1/identificacion/preguntas', methods=['POST'])(preguntas_identificacion)
#6
app.route('/op/evidentemaster/v1/identificacion/verificar', methods=['POST'])(verificar_preguntas)


if __name__ == '__main__':
    app.run(debug=True)
