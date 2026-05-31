import json

def save_history(data):

    with open(
        "storage/history.json",
        "a"
    ) as f:

        f.write(
            json.dumps(data) + "\n"
        )