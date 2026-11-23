from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DaneZVM(BaseModel):
    host: str
    cpu_usage: float
    status: str

@app.post("/odbierz")
def odbierz_dane(dane: DaneZVM):
    print(f"Otrzymano z {dane.host}: CPU {dane.cpu_usage}%, status: {dane.status}")
    return {"wiadomosc": "Dane odebrane poprawnie"}