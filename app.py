from flask import Flask, request, send_file, jsonify
from pdf_generator import gerar_boleto_pdf
import io

app = Flask(__name__)

@app.route('/boleto', methods=['POST'])
def gerar_boleto():
    data = request.json
    required_fields = ['pagador', 'beneficiario', 'valor', 'vencimento', 'nosso_numero']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes.'}), 400
    pdf_stream = gerar_boleto_pdf(data)
    return send_file(
        pdf_stream,
        as_attachment=True,
        download_name='boleto.pdf',
        mimetype='application/pdf'
    )

@app.route('/boleto', methods=['GET'])
def boleto_info():
    return '''
        <h1>API de geração de boletos</h1>
        <p>Use o método POST neste endpoint para enviar os dados do boleto e gerar o PDF.<br>
        Exemplo: envie um JSON via script ou ferramenta como Postman, curl ou o script <code>testar_boleto.py</code>.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
