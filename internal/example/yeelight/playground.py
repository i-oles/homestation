import time

from yeelight import discover_bulbs


if __name__ == "__main__":
    start = time.time()
    x = discover_bulbs()
    print(x)
    end = time.time()
    print(end - start)
