# {'id': '1237', 'trainer_name': 'Alex2323', 'trainer_token': 'cf539fb0ecaa74e37c7bc9384af80215'}

import requests
import json

token = 'cf539fb0ecaa74e37c7bc9384af80215'

pokemons = requests.get('https://api.pokemonbattle.me:9104/pokemons', params = {'pokemon_id': '1525'})
strings = json.loads(pokemons.text)
print(strings)