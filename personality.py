import json

def load_personality(name):
    with open("mock_data/personalities.json") as f:
        data = json.load(f)
    return data.get(name, {})