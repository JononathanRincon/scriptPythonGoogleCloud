import requests

url = "https://api.zippopotam.us/us/15204"

response = requests.get(url)

if response.status_code == 200:
    zipJson = response.json()
    print(zipJson)
    longitud = zipJson["places"][0]["longitude"]
    ciudad = zipJson["places"][0]["place name"]
    print(f"la {ciudad} tiene una de {longitud}")
else: 
    print("error code: "+str(response.status_code))
    exit(response.status_code)
