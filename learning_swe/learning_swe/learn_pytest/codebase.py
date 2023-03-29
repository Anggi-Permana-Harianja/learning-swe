def add(num1: int, num2: int) -> int:
    return num1 + num2


def is_even(num: int) -> bool:
    return num % 2 == 0


def zipcode(zip: str) -> str:
    return zip.lower()


# mock and (monkey)patch usually for testing class
class MyId:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        return f"my name is {self.name}, and my age is {self.age}"


def get_age(obj_my_id: MyId) -> int:
    return obj_my_id.age


def get_name(obj_my_id: MyId) -> str:
    return obj_my_id.name


def get_name_lowercase(obj_my_id: MyId) -> str:
    return obj_my_id.name.lower()
