# (Was present yesterday but not today)
today_users = ['user1', 'user4', 'user3', 'user6', 'user9', 'user10', 'user6', 'user7', 'user5', 'user2']

yesterday_users = ['user4', 'user3', 'user9', 'user10', 'user1', 'user8', 'user1', 'user4', 'user10', 'user8']

users_today = set(today_users)
users_yesterday = set(yesterday_users)
users_lost = users_yesterday - users_today
print(users_lost)