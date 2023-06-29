class Account:
    def __init__(self, acc_id: int, balance: int, pin: int):
        self.__id = acc_id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int) -> int or str:
        return self.__id if self.__pin == pin else "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int) ->str:
        if self.__pin == old_pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))