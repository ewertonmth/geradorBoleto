from flask import Flask, request, send_file, render_template
from pdf_generator import gerar_boleto_pdf
import io
import time  # Para gerar número automático

app = Flask(__name__)

@app.route('/boleto', methods=['GET'])
def boleto_form():
    return render_template('form.html')

@app.route('/boleto', methods=['POST'])
def gerar_boleto():
    nosso_numero = str(int(time.time()))  # Número automático baseado no timestamp

    data = {
        "pagador": {
            "nome": request.form.get("pagador_nome", ""),
            "cpf": request.form.get("pagador_cpf", ""),
            "endereco": request.form.get("pagador_endereco", "")
        },
        "beneficiario": {
            "nome": request.form.get("beneficiario_nome", ""),
            "cnpj": request.form.get("beneficiario_cnpj", ""),
            "banco": request.form.get("beneficiario_banco", ""),
            "agencia": request.form.get("beneficiario_agencia", ""),
            "conta": request.form.get("beneficiario_conta", "")
        },
        "valor": float(request.form.get("valor", 0)),
        "vencimento": request.form.get("vencimento", ""),
        "nosso_numero": nosso_numero
    }

    required_fields = ['pagador', 'beneficiario', 'valor', 'vencimento', 'nosso_numero']
    if not all(data.get(field) for field in required_fields):
        return "Campos obrigatórios ausentes.", 400

    pdf_stream = gerar_boleto_pdf(data)
    return send_file(
        pdf_stream,
        as_attachment=True,
        download_name='boleto.pdf',
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
