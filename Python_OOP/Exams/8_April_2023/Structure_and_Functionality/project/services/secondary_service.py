from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        robots = " ".join([r.name for r in self.robots]) if self.robots else "none"

        return f"{self.name} Secondary Service:\n" \
               f"Robots: {robots}"