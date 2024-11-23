# pip install requests
# pip install fastapi 
# pip install uvicorn
# pip install jinja2
# pip install python-multipart

import logging
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests

# Configuração do logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = "8e20087c6d1fa3d1ffa71e3592d93e54"
GEOCODE_URL = "http://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    logger.info("Página inicial acessada")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    logger.info(f"Solicitação de previsão do tempo para a cidade: {city}")
    try:
        # Passo 1: Obter latitude e longitude da cidade
        print(city)
        response = requests.get(GEOCODE_URL, params= {'q':city, 'appid': API_KEY})
        data = response.json()
        print(data)
        
        # Passo 2: Obter dados do tempo usando latitude e longitude
        
        # Extração de dados relevantes para exibição

        # Passar dados relevantes para o template
        return templates.TemplateResponse(
            "weather.html",
            {"request": request, "city_name": city, "weather": weather}
        )

    except requests.RequestException as e:
        logger.error(f"Erro ao fazer requisição às APIs: {e}")
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error_message": "Erro ao obter dados do tempo. Por favor, tente novamente."}
        )

    except KeyError as e:
        logger.error(f"Erro ao processar dados das APIs: {e}")
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error_message": "Erro ao processar dados do tempo. Por favor, tente novamente."}
        )

    except Exception as e:
        logger.exception(f"Erro inesperado: {e}")
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error_message": "Ocorreu um erro inesperado. Por favor, tente novamente mais tarde."}
        )
    
# COMANDO PARA SUBIR O SERVIDOR
# uvicorn previsao_tempo:app --reload
# http://127.0.0.1:8000/docs