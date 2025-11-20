import os
import requests
import folium
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
py = posicao_atual["vs"][0]["py"]
px = posicao_atual["vs"][0]["px"]

m = folium.Map(location= [py, px], zoom_start=14)
folium.Marker(location=[py, px], popup=("Ônibus"), icon=folium.Icon(color='green', icon='bus', prefix='fa')).add_to(m)

m.show_in_browser()
