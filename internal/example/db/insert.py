from tinydb import TinyDB, Query

db = TinyDB("/Users/ioles/PycharmProjects/homestation/db/db.json")
User = Query()
db.insert(
    {
        "id": "table_lamp",
        "ip": "192.168.0.18",
        "preset": {
            "salon_main_lamp": 30,
            "cleaning": 100,
        }
    },
)


