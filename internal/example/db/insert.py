from tinydb import TinyDB, Query

db = TinyDB("/Users/ioles/PycharmProjects/homestation/db/db.json")
User = Query()

bulbs_to_insert = [
    {
        "id": "salon_main_lamp",
        "ip": "192.168.0.18",
        "type": "white",
        "preset": {
            "single": 30,
            "cleaning": 100,
        },
    },
    {
        "id": "sofa_lamp",
        "ip": "192.168.0.22",
        "type": "white",
        "preset": {
            "cozy": 10,
            "cleaning": 100,
        },
    },
    {
        "id": "table_lamp",
        "ip": "192.168.0.23",
        "type": "white",
        "preset": {
            "single": 30,
            "cinema": 5,
            "cozy": 10,
            "cleaning": 100,
        },
    },
]

for bulb in bulbs_to_insert:
    db.insert(bulb)
