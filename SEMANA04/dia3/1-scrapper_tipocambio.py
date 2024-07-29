import requests
from bs4 import BeautifulSoup

url = "https://www.bcrp.gob.pe/"

def obtener_tipocambio():
    response = requests.get(url)
    if(response.status_code == 200):
        html = BeautifulSoup(response.text,'html.parser')
        ul_dolar = html.find('table',{'class':'tip-table'})
        print(ul_dolar)
    else:
        print(f"error : {response.status_code}")

if __name__ == "__main__":
    obtener_tipocambio()