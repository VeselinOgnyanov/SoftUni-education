
from animal import Animal
from caretaker import Caretaker
from cheetah import Cheetah
from keeper import Keeper
from lion import Lion
from tiger import Tiger
from vet import Vet
from worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capcity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and len(self.animals) != self.__animal_capcity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if len(self.animals) != self.__animal_capcity and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) != self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker_to_be_fired = next((worker for worker in self.workers if worker.name == worker_name), None)
        if worker_to_be_fired:
            self.workers.remove(worker_to_be_fired)
            return f"{worker_to_be_fired.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        overall_salaries = [worker.salary for worker in self.workers]
        gross_salaries = sum(overall_salaries)
        if self.__budget >= gross_salaries:
            self.__budget -= gross_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        overall_care_expenses = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= overall_care_expenses:
            self.__budget -= overall_care_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        list_of_lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        list_of_tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        list_of_cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        status_to_print = [
            f"You have {len(self.animals)} animals",
            f"----- {len(list_of_lions)} Lions:",
        ]
        status_to_print.extend(list_of_lions)

        status_to_print.append(f"----- {len(list_of_tigers)} Tigers:")
        status_to_print.extend(list_of_tigers)

        status_to_print.append(f"----- {len(list_of_cheetahs)} Cheetahs:")
        status_to_print.extend(list_of_cheetahs)

        return "\n".join(str(element) for element in status_to_print)

    def workers_status(self):

        list_of_keepers = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        list_of_caretakers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        list_of_vets = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        status_to_print = [
            f"You have {len(self.workers)} workers",
            f"----- {len(list_of_keepers)} Keepers:",
        ]
        status_to_print.extend(list_of_keepers)

        status_to_print.append(f"----- {len(list_of_caretakers)} Caretakers:")
        status_to_print.extend(list_of_caretakers)

        status_to_print.append(f"----- {len(list_of_vets)} Vets:")
        status_to_print.extend(list_of_vets)

        return "\n".join(str(element) for element in status_to_print)


# zoo = Zoo("Zootopia", 3000, 5, 8)

# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]

# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))

# # # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))

# # Tending animals
# print(zoo.tend_animals())

# # Paying keepers
# print(zoo.pay_workers())

# # Fireing worker
# print(zoo.fire_worker("Adam"))

# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
