import os
import requests
from folium import Map, Marker
from dotenv import load_dotenv

load_dotenv(".env") # o nome dentro do parenteses deve ser o nome do arquivo onde sua chave de API está salva

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

pos = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1//Posicao/Linha?codigoLinha=2506"
)
posicao_atual = pos.json()
py = posicao_atual["vs"][0]["py"]
px = posicao_atual["vs"][0]["px"]

'''m = Map(location= py, px, zoom_start=14)
for i in paradas:
    Marker(location=[i["py"], i["px"]], popup=i["np"]).add_to(m)'''
#m.show_in_browser()
