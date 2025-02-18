import requests

# URL base da API da OpenAI
url = "https://api.openai.com/v1/engines"

# Configuração do cabeçalho de autenticação
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY'  # Substitua pelo seu token de API
}

try:
    response = requests.get(url, headers=headers)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Erro na solicitação: {e}")
