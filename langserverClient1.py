import requests
response = requests.post(
    "http://localhost:8018/joke/invoke",
    json={'input': {'topic': 'cats'}}
)
#response.json()
print(response)