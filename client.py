import requests
import time

URL = "http://IP_TWOJEGO_KOMPUTERA:8000/odbierz"

while True:
    payload = {
        "host": "ubuntu-vm",
        "cpu_usage": 14.5,
        "status": "OK"
    }
    try:
        response = requests.post(URL, json=payload, timeout=5)
        print("Odpowiedź serwera:", response.json())
    except Exception as e:
        print("Błąd połączenia:", e)
    
    time.sleep(5)