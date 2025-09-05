def formatar_valor(valor):
    return f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

def gerar_linha_digitavel(nosso_numero, banco='341', agencia='1234', conta='1234567'):
    # Geração fake de linha digitável apenas para demonstração
    campo1 = f"{banco}{agencia[:4]}"
    campo2 = f"{conta[:5]}{nosso_numero[:5]}"
    campo3 = f"{nosso_numero[5:]}00000"
    campo4 = "9"  # DV fake
    campo5 = "20250722"  # vencimento fake
    return f"{campo1}.{campo2} {campo3}.{campo4} {campo5}"
