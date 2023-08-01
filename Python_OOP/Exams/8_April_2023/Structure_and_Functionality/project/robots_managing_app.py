from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    valid_services = {"MainService": MainService, "SecondaryService": SecondaryService}
    valid_robots = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.valid_services:
            raise Exception("Invalid service type!")

        service = self.valid_services[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.valid_robots:
            raise Exception("Invalid robot type!")

        robot = self.valid_robots[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robots_suitable_services = {"MainService": "MaleRobot", "SecondaryService": "FemaleRobot"}

        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))

        for key, value in robots_suitable_services.items():
            if key == service.__class__.__name__ and value == robot.__class__.__name__:
                break
        else:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")

        self.robots.append(robot)
        service.robots.remove(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        number_of_robots_fed = 0

        for robot in service.robots:
            value = robot.weight
            robot.eating()

            if robot.weight != value:
                number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        total_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join([s.details() for s in self.services])

