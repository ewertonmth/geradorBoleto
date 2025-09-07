from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
from reportlab.lib import colors
from boleto_utils import formatar_valor, gerar_linha_digitavel
import io

def gerar_boleto_pdf(data):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    pagador = data['pagador']
    beneficiario = data['beneficiario']
    valor = float(data['valor'])
    vencimento = data['vencimento']
    nosso_numero = data['nosso_numero']

    linha_digitavel = gerar_linha_digitavel(nosso_numero)

    # Fontes
    c.setFont("Helvetica-Bold", 14)
    c.drawString(20 * mm, 270 * mm, "BOLETO BANCÁRIO")

    # Linha digitável destacada
    c.setFont("Courier-Bold", 12)
    c.setFillColor(colors.black)
    c.drawString(20 * mm, 260 * mm, f"Linha Digitável: {linha_digitavel}")

    # Vencimento e valor
    c.setFont("Helvetica", 10)
    c.drawString(20 * mm, 250 * mm, f"Vencimento: {vencimento}")
    c.drawRightString(190 * mm, 250 * mm, f"Valor: {formatar_valor(valor)}")

    # Beneficiário (antes pagador)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20 * mm, 235 * mm, "Beneficiário:")
    c.setFont("Helvetica", 10)
    c.drawString(25 * mm, 223 * mm, f"{pagador['nome']} | CPF: {pagador['cpf']}")
    c.drawString(25 * mm, 210 * mm, f"Banco: {beneficiario['banco']} | Agência: {beneficiario['agencia']} | Conta: {beneficiario['conta']}")

    # Pagador (antes beneficiário)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20 * mm, 190 * mm, "Pagador:")
    c.setFont("Helvetica", 10)
    c.drawString(25 * mm, 178 * mm, f"{beneficiario['nome']} | CNPJ: {beneficiario['cnpj']}")
    c.drawString(25 * mm, 165 * mm, f"Endereço: {pagador['endereco']}")

    # Caixas ao redor dos blocos
    c.setLineWidth(0.5)
    c.rect(18 * mm, 205 * mm, 174 * mm, 40 * mm)  # Beneficiário
    c.rect(18 * mm, 160 * mm, 174 * mm, 35 * mm)  # Pagador

    # Código de barras
    barcode = code128.Code128(linha_digitavel, barHeight=30 * mm, barWidth=0.8)
    barcode.drawOn(c, 20 * mm, 115 * mm)

    # Linha separadora
    c.line(18 * mm, 110 * mm, 192 * mm, 110 * mm)

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
