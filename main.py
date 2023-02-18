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


# Creating addressbooks
class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def remove_record(self, record):
        self.data.pop(record.name.value, None)

    def show_records(self):
        return self.data


if __name__ == '__main__':
    name = Name('Djohny')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Djohny'], Record)
    assert isinstance(ab['Djohny'].name, Name)
    assert isinstance(ab['Djohny'].phones, list)
    assert isinstance(ab['Djohny'].phones[0], Phone)
    assert ab['Djohny'].phones[0].value == '1234567890'

    print('All is well !')
