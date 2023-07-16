from abc import ABC, abstractmethod


class Cable(ABC):
    @abstractmethod
    def connect(self, first_device, second_device):
        ...


class HDMI(Cable):
    def connect(self, first_device, second_device):
        return f"{first_device} and {second_device} are connected via HDMI."


class RCA(Cable):
    def connect(self, first_device, second_device):
        return f"{first_device} and {second_device} are connected via RCA."


class EthernetCable(Cable):
    def connect(self, first_device, second_device):
        return f"{first_device} and {second_device} are connected via Ethernet Cable."


class PowerOutlet(Cable):
    def connect(self, device, _):
        return f"Connect {device} to power."


class EntertainmentDevice:
    def __repr__(self):
        return f"{self.__class__.__name__}"


class Television(EntertainmentDevice):
    ...


class DVDPlayer(EntertainmentDevice):
    ...


class GameConsole(EntertainmentDevice):
    ...


class Router(EntertainmentDevice):
    ...


tv = Television()
dvd = DVDPlayer()
console = GameConsole()
router = Router()

hdmi_cable = HDMI()
rca_cable = RCA()
ethernet_cable = EthernetCable()
power_outlet = PowerOutlet()

print(rca_cable.connect(tv, dvd))
print(hdmi_cable.connect(tv, console))
print(power_outlet.connect(tv, None))
print(ethernet_cable.connect(console, router))
print(ethernet_cable.connect(tv, router))

