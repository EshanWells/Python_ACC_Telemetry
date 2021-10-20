"""

"""

from dataclasses import dataclass

@dataclass
class SPageFilePhysics:
    packetId:           int
    gas:                float
    brake:              float
    fuel:               float
    gear:               int
    rpm:                int
    steerAngle:         float
    speedKMH:           float
    velocity:           float * 3
    accG:               float * 3
    wheelSlip:          float * 3

@dataclass
class SPageFileStatic:
    smVersion:          str
    acVersion:          str
    numberOfSessions:   str
    numCars:            int
    carModel:           str

@dataclass
class Stefan:
    name: str = "stoyfan1"
    age: float = 69.420
    message: str = "hi John's mum"

print(Stefan.name)
print(Stefan.age)
print(Stefan.message)
