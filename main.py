from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


# Creating contacts
class Record:
    
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if isinstance(phone, Phone):
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phone.append(phone)

    def change_phone(self, phone):
        self.phones = phone

    def delete_phone(self):
        self.phones = []

    def show_contact(self):
        return {"name": self.name, "phone": self.phones}
