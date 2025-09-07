# 🧾 Gerador de Boletos para Pagamento de Diaristas  

Este projeto foi desenvolvido a pedido de uma empresa que necessita realizar **pagamentos de diaristas sem MEI** de forma formalizada, por meio da emissão de boletos bancários.  

A aplicação gera **boletos em PDF** a partir de dados fornecidos via API ou script, permitindo que a empresa utilize esse método como registro de pagamento e organização financeira.  

---

## 🚀 Funcionalidades  

- API em **Flask** para geração de boletos via requisições HTTP.  
- Geração de **boletos em PDF** utilizando a biblioteca **ReportLab**.  
- Estrutura com **Pagador** (empresa) e **Beneficiário** (diarista).  
- Criação de **linha digitável** e **código de barras** (exemplo simulado).  
- Organização clara dos dados de pagamento no PDF.  

---

## 📂 Estrutura do Projeto  

```
📦 boleto-pagamento-diaristas
├── app.py               # API Flask para geração de boletos
├── boleto.json          # Exemplo de payload com dados do boleto
├── boleto_gerado.pdf    # Exemplo de boleto gerado
├── boleto_utils.py      # Funções auxiliares (formatação e linha digitável)
├── pdf_generator.py     # Lógica de geração do PDF
├── testar_boleto.py     # Script para testar a API localmente
├── gerar_boleto.ps1     # Script PowerShell para execução automatizada
```

---

## ⚙️ Tecnologias Utilizadas  

- **Python 3.11+**  
- **Flask** → API para geração de boletos  
- **ReportLab** → Criação do PDF  
- **Requests** → Testes da API  

---

## 🔧 Como Executar  

### 1. Clonar o repositório  
```bash
git clone https://github.com/seu-usuario/boleto-pagamento-diaristas.git
cd boleto-pagamento-diaristas
```

### 2. Criar e ativar o ambiente virtual  
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Instalar dependências  
```bash
pip install flask reportlab requests
```

### 4. Rodar a API Flask  
```bash
python app.py
```
A API será executada em:  
👉 `http://127.0.0.1:5000/boleto`

### 5. Testar a geração de boleto  
```bash
python testar_boleto.py
```

Se tudo estiver correto, será gerado o arquivo:  
👉 `boleto_gerado.pdf`  

---

## 📌 Exemplo de Requisição  

### Endpoint  
```
POST /boleto
```

### Payload (`boleto.json`)  
```json
{
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
```

### Resposta  
Um **arquivo PDF** contendo o boleto formatado.  

---

## 📄 Exemplo de Boleto Gerado  

**Boleto em PDF** com:  
- Linha digitável  
- Beneficiário (empresa)  
- Pagador (diarista)  
- Valor e vencimento  
- Código de barras  

(veja o arquivo `boleto_gerado.pdf` incluído no repositório).  

---

## ⚠️ Aviso Importante  

Este projeto foi desenvolvido **apenas para fins internos e demonstrativos**.  
- O boleto gerado **não possui validade bancária real**, já que utiliza linha digitável e código de barras fictícios.  
- Para utilização em produção, é necessário integrar com **sistemas bancários oficiais** (ex.: via APIs de bancos ou registradoras de boletos).  

---

## 👨‍💻 Autor  

Desenvolvido por **Ewerton Matheus Conceição da Silva** a pedido de uma empresa privada que busca **formalizar pagamentos a diaristas sem MEI**.  
