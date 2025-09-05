# Caminho do JSON de entrada e do PDF de saída
$jsonPath = "boleto.json"
$pdfPath = "boleto_gerado.pdf"
$uri = "http://127.0.0.1:5000/boleto"

# Verifica se o arquivo JSON existe
if (!(Test-Path $jsonPath)) {
    Write-Host "Arquivo boleto.json não encontrado!" -ForegroundColor Red
    exit
}

# Envia requisição POST para a API Flask
try {
    Invoke-RestMethod -Uri $uri `
                      -Method Post `
                      -ContentType "application/json" `
                      -InFile $jsonPath `
                      -OutFile $pdfPath

    Write-Host "✅ Boleto gerado com sucesso: $pdfPath" -ForegroundColor Green
    Start-Process $pdfPath
}
catch {
    Write-Host "❌ Erro ao gerar boleto. Verifique se a API Flask está rodando." -ForegroundColor Red
}  
