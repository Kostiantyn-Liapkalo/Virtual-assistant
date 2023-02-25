from collections import UserDict
from datetime import datetime


class Field:

    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        
    
# Creating "name" field.
class Name(Field):
    
    def __str__(self):
        return self._value.title()


# Creating "phone" field.
class Phone(Field):
  
  # Change phone number to standart format.
    @staticmethod
    def sanitize_phone_number(phone):

        new_phone = str(phone).strip().removeprefix("+").replace(
            "(", "").replace(")", "").replace("-", "").replace(" ", "")
        try:
            new_phone = [str(int(i)) for i in new_phone]
        except ValueError:
            print("Number is not correct!")

        else:
            new_phone = "".join(new_phone)
            if len(new_phone) == 12:
                return f"+{new_phone}"
            elif len(new_phone) == 10:
                return f"+38{new_phone}"
            else:
                print("Length of number is wrong")

    def __init__(self, value):
        self._value = Phone.sanitize_phone_number(value)

    @Field.value.setter
    def value(self, value):
        self._value = Phone.sanitize_phone_number(value)


# Creating 'birthday' field.
class Birthday(datetime):

    @staticmethod
    def validate_date(year, month, day):
        try:
            birthday = datetime(year=year, month=month, day=day)
        except ValueError:
            print("Date is not correct")
        else:
            return str(birthday.date())

    def __init__(self, year, month, day):
        self.__birthday = self.validate_date(year, month, day)

    def __str__(self):
        return self.__birthday.strftime('%Y-%m-%d')

    def __repr__(self):
        return self.__birthday.strftime('%Y-%m-%d')

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, year, month, day):
        self.__birthday = self.validate_date(year, month, day)


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
