class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        # Add person to the class attribute dictionary
        Person.people[name] = self

def create_person_list(people: list) -> list:
    Person.people.clear()  # Clear any previous data
    result = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        result.append(Person(name, age))
    # Link wives and husbands
    for person_dict in people:
        name = person_dict["name"]
        p = Person.people[name]
        if "wife" in person_dict and person_dict["wife"]:
            wife_name = person_dict["wife"]
            p.wife = Person.people[wife_name]
            Person.people[wife_name].husband = p
        if "husband" in person_dict and person_dict["husband"]:
            husband_name = person_dict["husband"]
            p.husband = Person.people[husband_name]
            Person.people[husband_name].wife = p
    return result
