import os
import requests
from dotenv import load_dotenv

load_dotenv(".env") # o nome dentro do parenteses deve ser o nome do arquivo onde sua chave de API está salva

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)
print(res.text)