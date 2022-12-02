from database import TinyDB, Query

db = TinyDB("/Users/ioles/PycharmProjects/homestation/db/db.json")
User = Query()
db.insert(
    {
        "id": "table_lamp",
        "ip": "192.168.0.222",
        "preset": [
            {
                "salon_main_lamp": 30
            },
            {
                "something": 100
            }
        ],
    },
)
