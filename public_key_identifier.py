import requests
import os
import json
data = os.getenv('GITHUB_CONTEXT')


if data:
    data_json = json.loads(data)
    username = data["triggering_actor"]
    x = requests.get(f'https://github.com/{username}.keys', timeout=10)
    print(f"Request came back with {x.status_code} code")
    print(f"Here are {username} public keys")
    print("\n".join(x.content.decode().split("\n")))
