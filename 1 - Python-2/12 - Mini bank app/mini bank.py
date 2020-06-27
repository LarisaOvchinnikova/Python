
data_base = {

    "user1": {
        "password": "qwerty123",
        "balance": 0
        },

    "user2": {
        "password": "abcdeg123",
        "balance": 100
        }
}
while True:
    action = input("Welcome to the Bank! Would you like to Log in[1], Register[2] or Quit[3]?")
    if action == "3":
        break
    if action == "2":
        username = input("Enter your username: ")
        if username in data_base:
            print("User is already exists")
        else:
            password = input("Enter password: ")
            data_base[username] = {
                "password": password,
                "balance": 0,
            }
            print("You are registered")
    if action == "1":
        username = input("Enter your username: ")
        password = input("Enter password: ")
        if not username in data_base or data_base[username]["password"] != password:
            print("Wrong username or password")

        if username in data_base and data_base[username]["password"] == password:
            while True:
                print(f"Hello, {username}, your balance is {data_base[username]['balance']}")
                user_action = input("What would you like to do? Sign out [1], Add money [2], Send money [3]? ")
                if user_action == "1":
                    break
print(data_base)