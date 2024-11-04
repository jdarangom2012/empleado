import requests
import webbrowser

# Datos de tu cliente OAuth
client_id = 'sb-df24c64b-74b0-4535-bfab-76e504e46d24!b9679|client!b390'
redirect_uri = 'http://localhost'
auth_url = 'https://coronaind.authentication.us20.hana.ondemand.com/oauth/authorize'
            

# Parámetros para la solicitud de autorización
params = {
    'response_type': 'code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'scope': 'openid',
}

# Abrir el navegador para que el usuario autorice la aplicación
webbrowser.open(f"{auth_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=openid")

# Luego de la autorización, el código se devuelve al redirect_uri en la URL.
# Copia el código de la URL para el siguiente paso.

import requests

# URL del servidor de autenticación
token_url = 'https://coronaind.authentication.us20.hana.ondemand.com/oauth/token'

# Datos del cliente OAuth
client_id = 'sb-df24c64b-74b0-4535-bfab-76e504e46d24!b9679|client!b390'
client_secret = '700b4ec2-382f-49cc-9656-3816bc8a8e8b$EO6cm5JD1RCA6bDXXz3LdFligTeRUmWFMdbtQXhGlA0='
redirect_uri = 'http://localhost'
code = 'AUTH_CODE_OBTENIDO'  # Reemplaza con el código que obtuviste del paso anterior

# Payload para la solicitud del token de acceso
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'code': code,
}

# Realiza la solicitud POST para obtener el token de acceso
response = requests.post(token_url, data=data)
print(response)
# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    access_token = response.json().get('access_token')
    print(f"Token de acceso obtenido: {access_token}")
else:
    print(f"Error al obtener el token: {response.status_code}")
    print(response.json())