data_base = {}
while True:
    action = input("Welcome to the Bank! Would you like to Log in[1], Register[2] or Quit[3]? ")
    if action == "3":
        break
    if action == "2":
        username = input("Enter your username: ")
        if username in data_base:
            print("User with this name already exists")
            continue
        password = input("Enter password: ")
        data_base[username] = {
            "password" : password,
            "balance"  : 0,
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
                if user_action == "2":
                    add_balance = int(input("Enter amount of money: "))
                    data_base[username]['balance'] += add_balance
                    print(f"Your current balance is {data_base[username]['balance']}")
                if user_action == "3":
                    send_amount = int(input("Enter amount of money you want to send: "))
                    #if not send_amount.isdigit():
                    # print("Enter only digits")
                    # continue
                    # print(" , ".join([username for username in data_base.keys()]))

                    recipient = input("Enter recipient: ")
                    if recipient in data_base:
                        data_base[username]['balance'] -= send_amount
                        data_base[recipient]['balance'] += send_amount
                        print("Money sent")
                        print(f"Your current balance is {data_base[username]['balance']}")
                    else:
                        print("Unknown recipient")



print(data_base)