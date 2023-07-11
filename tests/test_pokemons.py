import requests
import pytest
import json

def test_status_code():
    response = requests.get('https://api.pokemonbattle.me:9104/pokemons')
    assert response.status_code == 200

def test_string():
    response_string = requests.get('https://api.pokemonbattle.me:9104/pokemons', params = {'pokemon_id': '1525'})
    assert response_string.json()['name'] == 'Delawere'

@pytest.mark.parametrize('key, value', [('name', 'Delawere'), ('trainer_id', '1237')])

def test_params(key, value):
    response_params = requests.get('https://api.pokemonbattle.me:9104/pokemons', params = {'pokemon_id': '1525'})
    assert response_params.json()[key] == value