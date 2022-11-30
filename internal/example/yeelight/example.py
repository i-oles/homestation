from yeelight import Bulb, discover_bulbs

bulb = Bulb("192.168.0.18")
bulb.turn_off()

print(discover_bulbs())
