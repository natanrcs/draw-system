import json
import os

def load_draws(path):
        if not os.path.exists(path):
              return {}
        with open(path, encoding="utf-8") as file:
            return json.load(file)

def save_draws(path, draws):
      with open(path, "w", encoding="utf-8") as file:
            json.dump(draws,file,indent=2,ensure_ascii=False)

if __name__ == "__main__":
      draws = load_draws("draws.json")
      print(draws)
      draws["chocolate"] = {"": "bia", "bia": "ana"}
      save_draws("draws.json",draws)
      print(load_draws("draws.json"))