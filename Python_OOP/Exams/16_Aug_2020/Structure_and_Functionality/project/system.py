from typing import List, Optional

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int) -> None:
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int) -> None:
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int) -> Optional[str]:
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                es = ExpressSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(es)
                System._software.append(es)
                break
        else:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int) -> Optional[str]:
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                ls = LightSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(ls)
                System._software.append(ls)
                break
        else:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str) -> Optional[str]:
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]

            hardware.uninstall(software)
            System._software.remove(software)

        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_operational_memory = f"{sum([s.memory_consumption for s in System._software])} / " \
                                   f"{sum([h.memory for h in System._hardware])}"
        total_capacity_taken = f"{sum([s.capacity_consumption for s in System._software])} / " \
                               f"{sum(h.capacity for h in System._hardware)}"
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_operational_memory}\n" \
               f"Total Capacity Taken: {total_capacity_taken}"

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            express_software = len([s for s in hardware.software_components if s.software_type == 'Express'])
            light_software = len([s for s in hardware.software_components if s.software_type == "Light"])
            total_memory_from_software = sum([s.memory_consumption for s in hardware.software_components])
            total_capacity_from_software = sum([s.capacity_consumption for s in hardware.software_components])
            software_components = ", ".join(
                [s.name for s in hardware.software_components]) if hardware.software_components else None

            result += f"Hardware Component - {hardware.name}\n" \
                      f"Express Software Components: {express_software}\n" \
                      f"Light Software Components: {light_software}\n" \
                      f"Memory Usage: {total_memory_from_software} / {hardware.memory}\n" \
                      f"Capacity Usage: {total_capacity_from_software} / {hardware.capacity}\n" \
                      f"Type: {hardware.hardware_type}\n" \
                      f"Software Components: {software_components}\n"

        return result
