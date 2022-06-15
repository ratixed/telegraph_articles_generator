import requests

method = 'createAccount'
url = f'https://api.telegra.ph/{method}'

params = {
    'short_name': '@usaffiliate',
    'author_name': 'Усатый Арбитражник',
    'author_url': 'https://t.me/usaffiliate',
}

response = requests.get(url, params=params)

print(response.json())

token = response.json()['result']['access_token']
print(token)




