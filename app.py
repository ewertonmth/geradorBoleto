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

if __name__ == '__main__':
    app.run(debug=True)
