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

    # Fundo branco
    c.setFillColor(colors.white)
    c.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)

    # Título
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.HexColor("#4B3621"))  # Madeira marrom escuro
    c.drawString(20 * mm, 270 * mm, "BOLETO BANCÁRIO")

    # Linha digitável em cinza escuro
    c.setFont("Courier-Bold", 13)
    c.setFillColor(colors.HexColor("#333333"))
    c.drawString(20 * mm, 260 * mm, f"Linha Digitável: {linha_digitavel}")

    # Vencimento e valor
    c.setFont("Helvetica", 11)
    c.drawString(20 * mm, 250 * mm, f"Vencimento: {vencimento}")
    c.drawRightString(190 * mm, 250 * mm, f"Valor: {formatar_valor(valor)}")

    # Beneficiário (dados do pagador trocados conforme antes)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20 * mm, 235 * mm, "Beneficiário:")
    c.setFont("Helvetica", 10)
    c.drawString(25 * mm, 223 * mm, f"{pagador['nome']} | CPF: {pagador['cpf']}")
    c.drawString(25 * mm, 210 * mm, f"Banco: {beneficiario['banco']} | Agência: {beneficiario['agencia']} | Conta: {beneficiario['conta']}")

    # Pagador
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20 * mm, 190 * mm, "Pagador:")
    c.setFont("Helvetica", 10)
    c.drawString(25 * mm, 178 * mm, f"{beneficiario['nome']} | CNPJ: {beneficiario['cnpj']}")
    c.drawString(25 * mm, 165 * mm, f"Endereço: {pagador['endereco']}")

    # Caixas estilizadas
    c.setLineWidth(1)
    c.setStrokeColor(colors.HexColor("#6E513D"))
    c.rect(18 * mm, 205 * mm, 174 * mm, 40 * mm)  # Beneficiário
    c.rect(18 * mm, 160 * mm, 174 * mm, 35 * mm)  # Pagador

    # Código de barras preto forte
    barcode = code128.Code128(linha_digitavel, barHeight=30 * mm, barWidth=0.9)
    barcode.drawOn(c, 20 * mm, 115 * mm)

    # Linha separadora marrom
    c.setStrokeColor(colors.HexColor("#6E513D"))
    c.setLineWidth(1.5)
    c.line(18 * mm, 110 * mm, 192 * mm, 110 * mm)

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
