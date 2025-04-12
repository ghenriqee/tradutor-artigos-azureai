import requests

def traduzir_texto(texto, idioma_destino):
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"
    chave = "SUA_CHAVE"
    regiao = "SUA_REGIAO"

    parametros = {
        "api-version": "3.0",
        "to": idioma_destino
    }

    cabecalhos = {
        "Ocp-Apim-Subscription-Key": chave,
        "Ocp-Apim-Subscription-Region": regiao,
        "Content-Type": "application/json"
    }

    corpo = [{
        "text": texto
    }]

    resposta = requests.post(endpoint, params=parametros, headers=cabecalhos, json=corpo)
    traducao = resposta.json()
    return traducao[0]["translations"][0]["text"]

# Exemplo de uso
texto_original = "Hello, world!"
idioma = "pt"
texto_traduzido = traduzir_texto(texto_original, idioma)
print("Tradução:", texto_traduzido)
