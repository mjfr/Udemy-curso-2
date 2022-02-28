# Uma "Application Programming Interface" (API) é um conjunto de comandos, funções, protocolos e objetos que os
# programadores podem usar para criar softwares ou interagir com sistemas externos.

# Trazendo para o mundo real, uma API seria como um menu de restaurante, onde você consegue ver tudo o que você pode
# pedir. O menu (API) acaba servindo como uma barreira entre o cliente e a cozinha.

# Endpoints são localizações de uma API. É onde há um terminal de conexão entre uma API e o Cliente. Em geral, são URLs.

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
