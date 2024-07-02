import requests
import json

def get_access_token(client_id, client_secret, scope, token_url):
    token_request_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope,
    }

    response = requests.post(token_url, data=token_request_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})

    if response.status_code == 200:
        token_response = response.json()
        access_token = token_response.get('access_token', None)
        if access_token:
            return access_token
        else:
            print("Failed to obtain access token. Response:")
            print(json.dumps(token_response, indent=4))
            return None
    else:
        print("Failed to obtain access token. Response:")
        print(response.text)
        return None
