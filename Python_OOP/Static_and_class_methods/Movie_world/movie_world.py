from customer import Customer
from dvd import DVD


class MovieWorld:

    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name) -> None:
        self.name = name
        self.customers = []
        self.dvds =[]

    @staticmethod
    def dvd_capacity():
        return int(MovieWorld.DVD_CAPACITY)

    @staticmethod
    def customer_capacity():
        return int(MovieWorld.CUSTOMER_CAPACITY)

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [c for c in self.customers if customer_id == c.id][0]
        current_dvd = [d for d in self.dvds if dvd_id == d.id][0]

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return "DVD is already rented"

        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [c for c in self.customers if customer_id == c.id][0]
        current_dvd = [d for d in self.dvds if dvd_id == d.id][0]

        if current_dvd in current_customer.rented_dvds:
            current_dvd.is_rented = False
            current_customer.rented_dvds.remove(current_dvd)
            return f"{current_customer.name} has successfully returned {current_dvd.name}"

        return f"{current_customer.name} does not have that DVD"

    def __repr__(self) -> str:
        list_to_return = []
        for c in self.customers:
            list_to_return.append(repr(c))
        for s in self.dvds:
            list_to_return.append(repr(s))
        string_to_return = "\n".join(list_to_return)
        return string_to_return
