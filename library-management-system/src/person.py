class Person:
    def __init__(self, name, age):
        self._name= name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def introduce_yourself(self):
        return f"Hi, I'm {self._name}"

    def __str__(self):
        return f"{self._name} ({self._age} yrs)"