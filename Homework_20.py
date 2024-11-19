import requests
import json


# Function to get the list of episodes for a character
def get_character_episodes(character_url):
    response = requests.get(character_url)
    character_data = response.json()
    episode_urls = character_data['episode']

    # Fetch the episode names
    episodes = []
    for episode_url in episode_urls:
        episode_response = requests.get(episode_url)
        episode_data = episode_response.json()
        episodes.append(episode_data['name'])

    return episodes


# Function to fetch all characters and their episodes
def fetch_characters_and_episodes():
    characters = {}
    url = "https://rickandmortyapi.com/api/character"

    while url:
        response = requests.get(url)
        data = response.json()

        # For each character in the response, get their episodes
        for character in data['results']:
            character_name = character['name']
            episodes = get_character_episodes(character['url'])
            characters[character_name] = episodes

        # Check if there's a next page to fetch
        url = data['info'].get('next')

    return characters


# Fetch data and write to a JSON file
def save_characters_to_json():
    characters = fetch_characters_and_episodes()

    with open('characters_episodes.json', 'w') as f:
        json.dump(characters, f, indent=4)


# Run the function to save data
save_characters_to_json()
