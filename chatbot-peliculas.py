import requests
import random
from unidecode import unidecode

# Configuración de la API de TMDb
TMDB_API_KEY = 'e909857b267f93f8ce19a41582249573'  # Reemplaza esto con tu propia API key de TMDb

def obtener_generos_disponibles():
    # Hacer una solicitud a la API de TMDb para obtener la lista de géneros
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=es'
    response = requests.get(url)
    data = response.json()

    # Extraer la lista de géneros del resultado
    generos = data.get('genres', [])
    return generos

def obtener_id_genero_por_nombre(nombre_genero):
    generos = obtener_generos_disponibles()
    for genero in generos:
        if unidecode(nombre_genero.lower()) in unidecode(genero['name'].lower()):
            return genero['id']
    return None

def obtener_recomendacion_pelicula(genero):
    # Hacer una solicitud a la API de TMDb para obtener una lista de películas del género especificado
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&language=es&with_genres={genero}'
    response = requests.get(url)
    data = response.json()

    # Extraer la lista de películas del resultado
    peliculas = data.get('results', [])

    # Si hay películas en la lista, elige una al azar
    if peliculas:
        pelicula = random.choice(peliculas)
        titulo = pelicula.get('title', 'Título no disponible')
        sinopsis = pelicula.get('overview', 'Sinopsis no disponible')
        fecha_estreno = pelicula.get('release_date', 'Fecha de estreno no disponible')
        return f'Título: {titulo}\nSinopsis: {sinopsis}\nFecha de estreno: {fecha_estreno}'
    else:
        return 'No se pudo obtener una recomendación en este género.'

def main():
    print('¡Bienvenido al chatbot de recomendación de películas!')
    while True:
        entrada = input('¿En qué puedo ayudarte?: ').lower()
        if 'hola' in entrada:
            print('¡Hola! ¿En qué puedo ayudarte?')
        elif 'que puedes hacer' in entrada or 'que haces' in entrada:
            print('Puedo recomendarte películas o mostrarte los géneros disponibles.')
        elif 'recomendación' in unidecode(entrada.lower()) or 'recomendacion' in unidecode(entrada.lower()) or 'película' in unidecode(entrada.lower()) or 'recomiendame' in unidecode(entrada.lower()) or 'peliculas' in unidecode(entrada.lower()) or 'recomienda' in unidecode(entrada.lower()) or 'dime peliculas' in unidecode(entrada.lower()):
            genero = input('Por favor, ingresa el nombre o número del género de película (o "salir" para terminar): ')
            if genero.lower() == 'salir':
                print('Gracias por usar el chatbot de recomendación de películas. ¡Hasta luego!')
                break
            id_genero = obtener_id_genero_por_nombre(genero)
            if id_genero:
                recomendacion = obtener_recomendacion_pelicula(id_genero)
                print('Te recomiendo ver la siguiente película:')
                print(recomendacion)
            else:
                print('El género ingresado no es válido. Por favor, intenta nuevamente.')
        elif 'generos' in unidecode(entrada.lower()) or 'géneros' in unidecode(entrada.lower()) or 'género' in unidecode(entrada.lower()) or 'genero' in unidecode(entrada.lower()) or 'categoría' in unidecode(entrada.lower()) or 'categorias' in unidecode(entrada.lower()) or 'categorías' in unidecode(entrada.lower()):
            generos = obtener_generos_disponibles()
            print('Géneros disponibles:')
            for genero in generos:
                print(f"{genero['name']} (ID: {genero['id']})")
        else:
            if entrada.lower() == 'salir':
                print('Gracias por usar el chatbot de recomendación de películas. ¡Hasta luego!')
                break
            id_genero = obtener_id_genero_por_nombre(entrada)
            if id_genero:
                recomendacion = obtener_recomendacion_pelicula(id_genero)
                print('Te recomiendo ver la siguiente película:')
                print(recomendacion)

if __name__ == "__main__":
    main()
