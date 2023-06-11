import requests

print("[HTTP Banner Grabber]\n")

while True:
    # Envio da requisição via GET
    print("Digite a URL do site")
    url = input("URL: ")
    resposta = requests.get(url)

    # Resposta do Server
    try:
        servidor = resposta.headers['Server']
        print(f"\n[Server: {servidor}]")
        break

    except KeyError:
        print("\n[Erro Server!]")
        print("(Não foi possível encontrar o server!)\n")
