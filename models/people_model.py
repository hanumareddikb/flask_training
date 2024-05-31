
class PeopleModel:
    def __init__(self, name=None, age=None, city=None):
        self._name = name
        self._age = age
        self._city = city

    @property
    def name(self):
        # print("getter called")
        return self._name

    @name.setter
    def name(self, name):
        # print("setter called")
        self._name = name.lower()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = str(age)

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city.lower()

    def to_dict(self):
        return {
            'name': self._name,
            'age': self._age,
            'city': self._city
        }
    # git practice
    # stash

    # reddi branch