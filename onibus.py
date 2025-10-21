import os
import requests
from folium import Map, Marker
from dotenv import load_dotenv

load_dotenv(".env") # o nome dentro do parenteses deve ser o nome do arquivo onde sua chave de API está salva

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

res = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha=2506"
)
paradas = res.json()
paradas[:3]

m = Map(location=[paradas[3]["py"], paradas[3]["px"]], zoom_start=14)
for i in paradas:
    Marker(location=[i["py"], i["px"]], popup=i["np"]).add_to(m)
#m.show_in_browser()

pos = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1//Posicao/Linha?codigoLinha=2506"
)
pos.json()