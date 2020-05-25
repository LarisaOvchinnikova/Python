# Создайте класс User в котором будет почти тот же функционал что был в bank app.
# (Сначала нужно просто создать класс, потом уже его вписывать в наше приложение)
# # Атрибуты - имя, пароль, баланс, список из обьектов datetime (
# Все таймп стампы когда юзер логинился).
# # Методы: пополнить счет, переслать деньги, добавить datetime логина,
# поменять пароль (перед этим проверив на соответствие старый пароль
# и новый на сложность функцией password_validator, в случае ошибки raise ValueError).
# # Также добавить __str__ и __repr__

from datetime import datetime, timedelta
def password_validator(password):
    count_lower = 0
    count_digit = 0
    count_upper = 0
    for letter in password:
        if letter.islower():
            count_lower += 1
        if letter.isdigit():
            count_digit += 1
        if letter.isupper():
            count_upper += 1
    vals = {
        'You need at least one uppercase letter': count_upper >= 1,
        'You need at least two lowercase letters': count_lower >= 2,
        'You need at least one digit': count_digit >= 1,
        'Length must be between 6 and 12 characters': 6 <= len(password) <= 12
    }
    output = ""
    for key, value in vals.items():
        if not value:
            output += f"{key}.\n"
    if not output:
        return True
    else:
        return output


class User:
    def __init__(self, first_name, second_name, password, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password
        self.balance = balance
        self.dates_list = [datetime.now()]

    def full_name(self):
        return f"{self.first_name} {self.second_name}"

    def __str__(self):
        return f"{self.first_name} {self.second_name}, balance --> {self.balance}"

    def __repr__(self):
        return f"User('{self.first_name}', '{self.second_name}', {self.password}', {self.balance})"

    def __len__(self):
        return len(self.dates_list)

    def add_register(self, register_day):
        self.dates_list.append(register_day)
        return self.dates_list

    def check_password(self):
        user_password = input("Enter your password: ")
        return user_password == self.password

    def switch_password(self):
        if self.check_password():
            new_password = input(f"{self.full_name()}, enter your new password: ")
            if password_validator(new_password) == True:
                self.password = new_password
                return "Your password is changed successfully!"
            else:
                return password_validator(new_password)
        else:
            return "Wrong password"

    def deposit_money(self):
        add_balance = int(input("Enter amount of money to add to account: "))
        self.balance += add_balance
        return f"Your current balance is {self.balance}"

    def send_money(self):
        send_balance = int(input("Enter amount of money to send: "))
        self.balance -= send_balance
        return f"Your current balance is {self.balance}"


user1 = User("John", "Doe", "qwerty", 10000)
user2 = User("Donald", "Trump", "Melanie", 1000000)
lst = [user1, user2]
print(lst)
print(len(user1))
# print(user1.balance)
# print(user1.full_name())
#
# print(user1.deposit_money())
# print(user1)
# day = datetime(2020,5,24,11,26,00)
# user1.add_register(day)
# print(user1.dates_list)
# print(user1.check_password())
#print(user1.switch_password())
print(user1)
print(user2)