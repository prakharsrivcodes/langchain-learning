from typing import TypedDict
class Person(TypedDict):
    name: str
    age: int
    email: str

new_person: Person = {'name':'praku', 'age':15}
print(new_person)