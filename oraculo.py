import requests
from deep_translator import GoogleTranslator

def obtener_sabiduria_digital():
    """
    Esta función se conecta a una API, obtiene una cita y la traduce al español.
    VERSIÓN 5.0 - Salida Bilingüe.
    """
    api_url = "https://zenquotes.io/api/random"
    
    try:
        respuesta = requests.get(api_url)
        respuesta.raise_for_status()
        
        datos = respuesta.json()
        
        cita_original = datos[0]['q']
        autor = datos[0]['a'] # El autor no necesita traducción.
        
        # Traducimos la cita al español.
        cita_traducida = GoogleTranslator(source='auto', target='es').translate(text=cita_original)
        
        # Devolvemos un diccionario con ambas versiones.
        return {
            "original": f'"{cita_original}"',
            "traducida": f'"{cita_traducida}"',
            "autor": autor
        }

    except Exception as e:
        return {"error": f"Error en la operación del Oráculo: {e}"}

# Punto de entrada del programa.
if __name__ == "__main__":
    resultado = obtener_sabiduria_digital()
    
    print("\nEl Oráculo Digital dice:")
    print("-------------------------")
    
    # Verificamos si hubo un error antes de intentar imprimir la cita.
    if "error" in resultado:
        print(resultado["error"])
    else:
        print(f"Original: {resultado['original']}")
        print(f"Traducción: {resultado['traducida']}")
        print(f"- {resultado['autor']}")
        
    print("-------------------------")
