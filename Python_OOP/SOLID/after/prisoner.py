import copy


class Person:
    def __init__(self, position):
        self.position = position


class FreePerson(Person):
    def __init__(self, position):
        super().__init__(position)
        self.is_free = True

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


prisoner = Prisoner()

print("The prisoner trying to walk to north by 10 and east by -3.")
try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

free_person = FreePerson([0, 0])
print("The person trying to walk to north by 10 and east by -3.")
print(f"The location of the person: {free_person.position}")

try:
    free_person.walk_north(10)
    free_person.walk_east(-3)
except:
    pass

print(f"The current location of the person: {free_person.position}")