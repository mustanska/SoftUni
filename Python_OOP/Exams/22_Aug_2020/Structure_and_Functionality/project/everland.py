from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: list = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def get_monthly_consumptions(self) -> str:
        total_consumption = sum([r.expenses + r.room_cost for r in self.rooms])

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self) -> str:
        result = []

        for room in self.rooms:
            consumption = room.expenses + room.room_cost
            if room.budget >= consumption:
                room.budget -= consumption
                result.append(f"{room.family_name} paid {consumption:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return "\n".join(result)

    def status(self) -> str:
        result = f"Total population: {sum([r.members_count for r in self.rooms])}\n"

        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. " \
                      f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"

            if room.children:
                for i, child in enumerate(room.children):
                    result += f"--- Child {i + 1} monthly cost: {child.cost * 30:.2f}$\n"

            result += f"--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in room.appliances]):.2f}$\n"

        return result
