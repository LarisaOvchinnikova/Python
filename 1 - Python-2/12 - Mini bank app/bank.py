data_base = {
    "user1": {
        "password": "qwerty",
        "balance": 0},
    "user2": {
        "password": "123122",
        "balance": 0}
}
print(data_base["user2"]) # {'password': '123122', 'balance': 0}
print(data_base["user2"]["password"])  # 123122

entered_password = input("Enter password")
data_base["user3"] = {
    "password": entered_password,
    "balance": 0,
}
print(data_base)