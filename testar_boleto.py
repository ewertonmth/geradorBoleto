import requests
import json

# Dados do boleto
payload = {
    "pagador": {
        "nome": "João Silva",
        "cpf": "123.456.789-00",
        "endereco": "Rua das Palmeiras, 123 - São Paulo"
    },
    "beneficiario": {
        "nome": "Empresa XYZ Ltda",
        "cnpj": "12.345.678/0001-90",
        "banco": "Bradesco",
        "agencia": "1234",
        "conta": "567890"
    },
    "valor": 299.90,
    "vencimento": "2025-08-10",
    "nosso_numero": "1234567890"
}

# Envia POST para a API Flask
response = requests.post("http://127.0.0.1:5000/boleto", json=payload)

# Verifica a resposta
if response.status_code == 200:
    with open("boleto_gerado.pdf", "wb") as f:
        f.write(response.content)
    print("✅ Boleto gerado com sucesso: boleto_gerado.pdf")
else:
    print(f"❌ Erro ao gerar boleto. Código: {response.status_code}")
    print(response.text)
