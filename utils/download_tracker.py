import json
import os

TRACKER = "downloaded_files.json"


def load_tracker():

    if not os.path.exists(TRACKER):
        return []

    with open(TRACKER, "r") as f:
        return json.load(f)


def save_tracker(data):

    with open(TRACKER, "w") as f:
        json.dump(data, f, indent=4)
