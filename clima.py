import os
import requests
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtener la API Key desde las variables de entorno
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obtener_clima(ciudad):
    if not API_KEY:
        print("Error: No se encontró la API_KEY en el archivo .env.")
        return

    # Parámetros para la petición HTTP
    params = {
        'q': ciudad,
        'appid': API_KEY,
        'units': 'metric',  # Muestra la temperatura en grados Celsius
        'lang': 'es'        # Devuelve la descripción en español
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        # Manejo de respuestas HTTP según el código de estado
        if response.status_code == 200:
            data = response.json()
            nombre_ciudad = data.get('name')
            pais = data.get('sys', {}).get('country')
            temp = data['main']['temp']
            sensacion = data['main']['feels_like']
            humedad = data['main']['humidity']
            descripcion = data['weather'][0]['description']

            print("\n" + "="*40)
            print(f" 🌤️  Clima en {nombre_ciudad}, {pais}")
            print("="*40)
            print(f"• Temperatura actual : {temp} °C")
            print(f"• Sensación térmica  : {sensacion} °C")
            print(f"• Humedad            : {humedad}%")
            print(f"• Condición          : {descripcion.capitalize()}")
            print("="*40 + "\n")

        elif response.status_code == 404:
            print(f"\n❌ Error 404: La ciudad '{ciudad}' no fue encontrada. Verifica el nombre.")
        elif response.status_code == 401:
            print("\n❌ Error 401: API Key inválida o no autorizada. Revisa tu archivo .env.")
        elif response.status_code == 429:
            print("\n❌ Error 429: Has superado el límite de peticiones de tu API Key.")
        else:
            print(f"\n❌ Error inesperado ({response.status_code}): {response.text}")

    except requests.exceptions.ConnectionError:
        print("\n❌ Error de conexión: No se pudo conectar con los servidores de OpenWeatherMap.")
    except requests.exceptions.Timeout:
        print("\n❌ Error de timeout: La solicitud tardó demasiado tiempo en responder.")
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error en la petición: {e}")

def main():
    print("=== Consulta del Clima (OpenWeatherMap) ===")
    ciudad = input("Ingresa el nombre de la ciudad a consultar: ").strip()
    
    if ciudad:
        obtener_clima(ciudad)
    else:
        print("No ingresaste ningún nombre de ciudad.")

if __name__ == "__main__":
    main()