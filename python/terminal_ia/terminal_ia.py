import chave_api_openai
import json
import requests

headers = {
    "Authorization": f"Bearer {chave_api_openai.API_KEY_OPENAI}",
    "Content-Type": "application/json"
}

link = "https://api.openai.com/v1/chat/completions"

modelo_chat = "gpt-3.5-turbo"

corpo_da_mensagem = {
    "model": modelo_chat,
    "messages": [
        {
            "role": "user",
            "content": "" #aqui vai a pergunta (você pode optar por criar uma variável para receber o input)
        }
    ]
}

corpo_da_mensagem = json.dumps(corpo_da_mensagem)

requisicao = requests.post(link, headers=headers, data=corpo_da_mensagem)
print(requisicao)

resposta = requisicao.json()

mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)