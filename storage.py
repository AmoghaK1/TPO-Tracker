import json
import os

FILE_PATH = "data/companies.json"


def load_old_companies():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_companies(companies):
    with open(FILE_PATH, "w") as f:
        json.dump(companies, f, indent=2)