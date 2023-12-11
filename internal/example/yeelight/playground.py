import time

from yeelight import discover_bulbs, Bulb


def show_all_active_bulbs():
    print(discover_bulbs())


def toggle_bulb():
    bulb = Bulb('192.168.0.20')
    bulb.toggle()


def get_properties():
    bulb = Bulb('192.168.0.20')
    bulb.get_properties()


def get_capabilities():
    bulb = Bulb('192.168.0.20')
    print(bulb.get_capabilities().get("power"))


if __name__ == "__main__":
    start = time.time()

    get_capabilities()

    end = time.time()
    print(end - start)
