def mock_discover_bulbs() -> list[dict]:
    return [
        {
            "ip": "192.168.0.20",
            "port": 55443,
            "capabilities": {
                "id": "0x000000001be3b3cf",
                "model": "monoa",
                "fw_ver": "9",
                "support": "get_prop set_default set_power toggle set_bright set_scene cron_add cron_get cron_del start_cf stop_cf set_name set_adjust adjust_bright",
                "power": "off",
                "bright": "10",
                "color_mode": "2",
                "ct": "2700",
                "rgb": "0",
                "hue": "0",
                "sat": "0",
                "name": "",
            },
        },
        {
            "ip": "192.168.0.23",
            "port": 55443,
            "capabilities": {
                "id": "0x000000001be3a66e",
                "model": "monoa",
                "fw_ver": "9",
                "support": "get_prop set_default set_power toggle set_bright set_scene cron_add cron_get cron_del start_cf stop_cf set_name set_adjust adjust_bright",
                "power": "on",
                "bright": "5",
                "color_mode": "2",
                "ct": "2700",
                "rgb": "0",
                "hue": "0",
                "sat": "0",
                "name": "",
            },
        },
        {
            "ip": "192.168.0.15",
            "port": 55443,
            "capabilities": {
                "id": "0x000000001be46fb3",
                "model": "monoa",
                "fw_ver": "9",
                "support": "get_prop set_default set_power toggle set_bright set_scene cron_add cron_get cron_del start_cf stop_cf set_name set_adjust adjust_bright",
                "power": "off",
                "bright": "30",
                "color_mode": "2",
                "ct": "2700",
                "rgb": "0",
                "hue": "0",
                "sat": "0",
                "name": "",
            },
        },
    ]
