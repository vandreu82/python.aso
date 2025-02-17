#   Ejercicio 4: API
#   Escribe un script que muestre cada hora los siguientes datos sobre la ciudad en la que
#   vives:
#       • Temperatura actual.
#       • Humedad relativa.
#       • Velocidad del tiempo.
#   Puedes usar para ello cualquier API de acceso gratuito que ofrezcan el servicio.
#
#   Víctor Manuel Andreu Felipe


import time
import requests

# obtiene la información del tiempo dada una api key y una ubicación
def get_weather():
    api_key = "zsEzXz44X4qycv1"  # Reemplaza con tu clave de API
    location_id = "3489"  # Cambia por el ID de tu localidad
    url = f"https://api.tutiempo.net/json/?lan=es&apid={api_key}&lid={location_id}"
    
    # hace un get y almacena la respuesta en un json
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # extrae la hora actual, temperatura, humedad y viento de la misma
        current_hour_key = list(data["hour_hour"].keys())[0]
        current_weather = data["hour_hour"][current_hour_key]
        
        temperature = current_weather["temperature"]
        humidity = current_weather["humidity"]
        wind_speed = current_weather["wind"]
        
        print(f"Temperatura: {temperature}°C")
        print(f"Humedad: {humidity}%")
        print(f"Velocidad del viento: {wind_speed} km/h")
    # control de excepciones
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el clima: {e}")
    except KeyError:
        print("Error: No se encontraron datos de clima en la respuesta de la API.")

if __name__ == "__main__":
    while True:
        print("Obteniendo datos meteorológicos...")
        get_weather()
        print("Esperando una hora para la próxima actualización...")
        time.sleep(3600)  # espera 1 hora (3600 segundos) antes de la siguiente ejecución
