import json
import os

def clear_json_file(filename):
    if os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump(None, f)    


clear_json_file("data/random_seeds.json")  