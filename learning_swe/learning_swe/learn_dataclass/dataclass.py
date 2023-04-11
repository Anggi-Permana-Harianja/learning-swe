from dataclasses import dataclass, field
from typing import List, Tuple


# class without dataclass
class PersonWithoutDataclass:
    def __init__(self, name, age, height, email):
        self.name = (name,)
        self.age = (age,)
        self.height = (height,)
        self.email = email


# class with dataclass
@dataclass
class Person:
    name: str
    age: int
    height: float
    email: str


print(Person(name="anggi", age=31, height=180, email="test@email.com"))

# dataclass with default value
@dataclass
class Person:
    name: str = "anggi"
    age: int = 31
    height: float = 180
    email: str = "test@email.com"


print(Person())

# dataclass with tuple data type
@dataclass
class Person:
    name: str
    age: int
    height: float
    email: str
    house_coordinats: Tuple


print(
    Person(
        name="anggi",
        age=31,
        height=180,
        email="test@gmail.com",
        house_coordinats=(1, 2),
    )
)

# we can also have List of classes
@dataclass
class People:
    people: List[Person]


anggi = Person(
    name="anggi", age=31, height=180, email="test@email.com", house_coordinats=(1, 2)
)
permana = Person(
    name="permana", age=30, height=155, email="test2@email.com", house_coordinats=(3, 4)
)

print(People([anggi, permana]))

# dataclass can do sort
@dataclass(order=True)
class Person:
    name: str
    age: int
    height: float
    email: str


joe = Person("Joe", 25, 180, "test@email.com")
mary = Person("Mary", 30, 170, "test2@email.com")

# the comparison started from name, to age, so forth
print(joe < mary)

# dataclass can have field
# This function is used to customize one attribute of a data class individually,
# which allows us to define new attributes that will depend
# on another attribute and will only be created after the object is instantiated.
@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    height: float
    email: str

    # __post_init__ is executed after init
    def __post_init__(self):
        # this make sorting based on age
        self.sort_index = self.age


joe = Person("Joe", 25, 180, "test@email.com")
mary = Person("Mary", 45, 182, "test1@email.com")

# now we can compare based on age
print(joe < mary)

# immutable dataclass
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    height: float
    email: str


joe = Person("Joe", 20, 170, "test@gmail.com")

# line below will return error since .age is immutable
# joe.age = 35
# print(joe)

# inheritance in dataclass
@dataclass(order=True)
class Person:
    name: str
    age: int
    height: float
    email: str


# class Employee inherited from Person
@dataclass(order=True)
class Employee(Person):
    salary: int
    department: str


first_employee = Employee(
    name="Joe",
    age=21,
    height=170,
    email="slave@company.ai",
    salary=3344,
    department="IT",
)

print(first_employee)
