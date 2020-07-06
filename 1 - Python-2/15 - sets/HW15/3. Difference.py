today_users = ['user1', 'user4', 'user3', 'user6', 'user9', 'user10', 'user6', 'user7', 'user5', 'user2']
yesterday_users = ['user4', 'user3', 'user9', 'user10', 'user1', 'user8', 'user1', 'user4', 'user10', 'user8']

new_users_gained_from_yesterday = set(today_users) - set(yesterday_users)
print(new_users_gained_from_yesterday)

users_lost = set(yesterday_users) - set(today_users)
print(users_lost)