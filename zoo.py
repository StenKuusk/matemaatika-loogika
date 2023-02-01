"""Zoo."""

class Animal:
    """Animal class."""

    def __init__(self, name: str, specie: str, age: int):
        """
        Class constructor.

        Each animal has a name and a specie.
        :param name: animal name
        :param specie: animal specie
        """
        self.name = name
        self.specie = specie
        self.age = age

    def __repr__(self):
        return f"{self.name} {self.specie}"


class Zoo:
    """Zoo class."""

    def __init__(self, name: str, max_number_of_animals: int):
        """
        Class constructor.

        Each zoo has a name and max number of animals the zoo can have.
        There also should be an overview of all animals present in the zoo.

        :param name: zoo name
        :param max_number_of_animals: how many animals can be in the zoo
        """
        self.zoo_name = name
        self.max_animal_count = max_number_of_animals
        self.animals = []

    def can_add_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be added to the zoo.

        Animal can be added to the zoo if:
        1. Adding a new animal does not exceed zoo's max number of animals.
        2. Same Animal object is not present in the zoo.
        3. Animal with same name and specie is not yet present in the zoo.
        :param animal: animal who is checked
        :return: bool describing whether the animal can be added to the zoo or not
        """
        can_add = True
        if len(self.animals) + 1 > self.max_animal_count:
            return False
        else:
            for animal_in_zoo in self.animals:
                if animal.name == animal_in_zoo.name and animal.specie == animal_in_zoo.specie:
                    return False
                else:
                    if animal in self.animals:
                        return False
                    else:
                        return True
        return can_add

    def add_animal(self, animal: Animal):
        """
        Add animal to the zoo if possible.

        :param animal: animal who is going to be added to the zoo
        Function does not return anything
        """
        if self.can_add_animal(animal):
            self.animals.append(animal)
        pass

    def can_remove_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be removed from the zoo.

        Animal can be removed from the zoo if animal is present in the zoo.

        :param animal: animal who is checked
        :return: bool describing whether animal can be removed from the zoo or not.
        """
        # for animal_in_zoo in self.animals:
        #     if animal_in_zoo.name == animal.name and animal_in_zoo.specie == animal.specie:
        #         return True
        can_remove = False
        if animal in self.animals:
            can_remove = True
        return can_remove
    pass


    def remove_animal(self, animal: Animal):
        """
        Remove animal from the zoo if possible.

        :param animal: animal who is going to be removed from the zoo.
        Function does not return anything
        """
        if self.can_remove_animal(animal) == True:
            self.animals.remove(animal)
        pass


    def get_all_animals(self):
        """
        Return a list with all the animals in the zoo.

        :return: list of Animal objects
        """
        return self.animals


    def get_animals_by_age(self):
        """
        Return a list of animals sorted by age (from younger to older).

        :return: list of Animal objects sorted by age
        """
        return sorted(self.animals, key=lambda animal: animal.age)
        pass


    def get_animals_sorted_alphabetically(self):
        """
        Return a list of animals sorted (by name) alphabetically.

        :return: list of Animal objects sorted by name alphabetically
        """
        return sorted(self.animals, key=lambda animal: animal.name)
        pass

zoo = Zoo("Loomaaed", 10)
animal_1 = Animal("Mati", "bear", 5)
animal_2 = Animal("Kati", "bear", 7)
animal_3 = Animal("Mati", "bear", 6)
animal_4 = Animal("Mati", "fox", 5)

zoo.add_animal(animal_1)
zoo.add_animal(animal_2)
zoo.add_animal(animal_3)
zoo.add_animal(animal_4)
zoo.add_animal(animal_1)

print(zoo.get_all_animals())

print(len(zoo.get_all_animals()) == 3)
print(animal_1 in zoo.get_all_animals()) # is True
print(animal_2 in zoo.get_all_animals() )# is True
print(animal_3 in zoo.get_all_animals() ) # is False
print(animal_4 in zoo.get_all_animals() )  # is True
