import requests
from bs4 import BeautifulSoup

# La URL objetivo que me proporcionaste.
URL = "https://www.linkedin.com/jobs/view/4281668286/?alternateChannel=search&eBP=CwEAAAGYsS1fONP6jfT_-MCYMoH0vKYgSQc06oyS2dgl9JPzkhYzW8YyDobDfMNBueoKbWMQfzGNWyPYYGPuhYaNkRreriOr7ttU43x3IkE1a6FlGHZYmhQFLaXEJaDyK_t0JXxcd2Xlhastm2Mv_O64xQGkouFNlwtLt6J731lB6NfLkWMHXrrreeAFEZ0jIn6d9Q0SuIt_MTsOGpJtlTrJ6T7GLEhhOz5S4dIZAjSTcv9yaZSZz-BTWO_65iWbsysD4_6Cz0trZUb0NxpOz0DmcRIVV29As7Lf6wqB0wBI4e6422anM_iSIKUReisVYPWC4TlWvu1IbllXkv0N2DkSQFeK_RPM8rar6Y5tcAYnR9UmoUZLzgAPDJZfwz7IaQPiaJY2ScD7G49jWdgVL4zEPL5Xtd5_QfrwOXD4FKKTBo5XY-vK0zSBPNueawfaCM3p5g1LqWnyALdBjL0BGpowXHfuG8jez1Gqf6HvBtRWy_px4w&refId=V9ZWZANi3bW4fHsH1LkbQ%3D%3D&trackingId=8xHiSXOeToIo7oluhTLamg%3D%3D"

# Añadimos cabeceras para simular que somos un navegador real. Es un paso crucial.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # Hacemos la petición GET a la URL, incluyendo las cabeceras.
    respuesta = requests.get(URL, headers=headers)
    respuesta.raise_for_status() # Verifica si la petición fue exitosa.

    # Usamos BeautifulSoup para analizar el contenido HTML de la página.
    soup = BeautifulSoup(respuesta.content, "lxml")

    # Buscamos el contenedor del título que identificaste.
    contenedor_titulo = soup.find('div', class_='job-details-jobs-unified-top-card__job-title')
    
    # Verificamos si encontramos el contenedor.
    if contenedor_titulo:
        # Dentro del contenedor, buscamos la etiqueta 'a' del link.
        titulo_trabajo = contenedor_titulo.find('a')
        if titulo_trabajo:
            # .strip() limpia espacios en blanco al principio y al final.
            print("\n--- INFORME DEL CENTINELA ---")
            print(f"Título del Puesto Encontrado: {titulo_trabajo.text.strip()}")
            print("----------------------------")
        else:
            print("Error: Se encontró el contenedor del título, pero no el link (etiqueta 'a') adentro.")
    else:
        print("Misión fallida: No se encontró el contenedor del título en la página. La estructura del HTML puede haber cambiado.")

except requests.exceptions.RequestException as e:
    print(f"Error de conexión: No se pudo contactar al objetivo. {e}")
