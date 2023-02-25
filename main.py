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
    
    def __init__(self,
                 name: Name,
                 phone: Phone = None,
                 birthday: Birthday = None):
        self.name = name
        self.birthday = birthday
        self.phones = []
        if isinstance(phone, Phone):
            self.phones.append(phone)

    def days_to_birthday(self):
        cur_date = datetime.now().date()
        cur_year = cur_date.year

        if self.birthday is not None:
            this_year_birthday = datetime(cur_year, self.birthday.month,
                                          self.birthday.day).date()
            delta = this_year_birthday - cur_date
            if delta.days >= 0:
                return f"{self.name}'s birthday will be in {delta.days} days"
            else:
                next_year_birthday = datetime(cur_year + 1,
                                              self.birthday.month,
                                              self.birthday.day).date()
                delta = next_year_birthday - cur_date
                return f"{self.name}'s birthday will be in {delta.days} days"

    def add_birthday(self, year, month, day):
        self.birthday = Birthday.validate_date(year, month, day)

    def add_phone(self, phone):
        phone = Phone(phone)
        if phone:
            self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)

        for phone in self.phones:
            if phone.value == old_phone.value:
                self.phones.remove(phone)
                self.phones.append(new_phone)
                return "phone was changed"

    def delete_phone(self, old_phone):
        old_phone = Phone(old_phone)
        for phone in self.phones:
            if phone.value == old_phone.value:
                self.phones.remove(phone)

    def get_contact(self):
        phones = ", ".join([str(p) for p in self.phones])
        return {
            "name": str(self.name.value),
            "phone": phones,
            "birthday": self.birthday,
        }


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
