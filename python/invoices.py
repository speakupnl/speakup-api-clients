from auth import get_access_token
import requests

# To get an client id and secret, contact the Speakup service desk
# at support [at] speakup [dot] nl or at https://speakup.nl/contact/
CLIENT_ID = ''
CLIENT_SECRET = ''

TOKEN_URL = 'https://account.speakup.nl/auth/realms/Speakup/protocol/openid-connect/token'
SCOPE = 'portaal-sso'

access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, SCOPE, TOKEN_URL)

headers = {
  'accept': '*/*',
  'Authorization': f'Bearer {access_token}',
}

# Make the GET request
response = requests.get('https://api.speakup.nl/business/v1/invoices', headers=headers)
print(response.text)
