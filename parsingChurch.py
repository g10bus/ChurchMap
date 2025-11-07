# https://map.patriarchia.ru/api/index.php?token=c2cbe8cd873f8e4751a7f7bb5292e68a&country=&church=&ctype=&t=0&s=&params=[]&zf=8&z=11&geo=[[55.5914663790916,37.42492761718748],[55.858853917119234,37.919312382812464]]&_=1762025201992

import requests
import json
from bs4 import BeautifulSoup
req = requests.get("https://map.patriarchia.ru/api/index.php?token=c2cbe8cd873f8e4751a7f7bb5292e68a&country=&church=&ctype=&t=0&s=&params=[]&zf=8&z=11&geo=[[55.5914663790916,37.42492761718748],[55.858853917119234,37.919312382812464]]&_=1762025201992", )


data = json.loads(req.text)

churchData = {}
for i in data["features"]:

    id = i['id']
    cordinates = i['geometry']['coordinates']
    name = i['properties']['hintContent']
    url = f"https://map.patriarchia.ru/?infoid={id}"
    print(id, cordinates, name ,url)
    



# храмы и часвони, подворья,