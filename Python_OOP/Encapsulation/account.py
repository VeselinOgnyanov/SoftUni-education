class Account:
    def __init__(self, id: int, balance: int, pin: int ) -> None:
        self.__id = id
        self.balance = balance
        self.__pin = pin

    # @property
    # def id(self):
    #     return self.__id

    # @id.setter
    # def id(self):
    #     id = self.__id

    # @property
    # def pin(self):
    #     return self.__pin

    # @pin.setter
    # def pin(self):
    #     pin = self.__pin

    def get_id(self, pin_to_check: int):
        if pin_to_check == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
