import os
import requests
from folium import Map, Marker, Icon
from dotenv import load_dotenv

load_dotenv(".env")

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

pos = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1//Posicao/Linha?codigoLinha=2304"
)
posicao_atual = pos.json()
py_bus = posicao_atual["vs"][0]["py"]
px_bus = posicao_atual["vs"][0]["px"]

res = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha=2304"
)
paradas = res.json()

m = Map(location=[py_bus, px_bus], zoom_start=14)
for i in paradas:
    Marker(location=[i["py"], i["px"]], popup="PARADA " + i["np"]).add_to(m)
Marker(location=[py_bus, px_bus], popup="ÔNIBUS", icon=Icon(color='green', icon='bus', prefix='fa')).add_to(m)

m.show_in_browser()