import requests
import os
import json
data = os.getenv('GITHUB_CONTEXT')


if data:
    data_json = json.loads(data)
    username = data_json["triggering_actor"]
    response = requests.get(f'https://github.com/{username}.keys', timeout=10)
    print(f"Request came back with {response.status_code} code")
    print(f"Here are {username} public keys")
    print(response.content.decode())
