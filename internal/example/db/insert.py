from tinydb import TinyDB, Query

db = TinyDB("/Users/ioles/PycharmProjects/homestation/db/db.json")
User = Query()
db.insert(
    # {
    #     "id": "salon_main_lamp",
    #     "ip": "192.168.0.18",
    #     "preset": [
    #         {
    #             "single": 30
    #         },
    #         {
    #             "cleaning": 100
    #         }
    #     ],
    # },
    # {
    #     "id": "sofa_lamp",
    #     "ip": "192.168.0.22",
    #     "preset": [
    #         {
    #             "cozy": 10
    #         }
    #     ],
    # },
    {
        "id": "table_lamp",
        "ip": "192.168.0.23",
        "preset": [
            {
                "single": 30
            },
            {
                "cinema": 5
            },
            {
                "cozy": 10
            }
        ],
    },
)
