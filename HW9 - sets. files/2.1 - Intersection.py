yesterday_users = ['user32', 'user46', 'user22', 'user16', 'user21', 'user4', 'user6', 'user29', 'user1', 'user39']
users_yesterday = set(yesterday_users)
today_users = ['user2', 'user39', 'user41', 'user38', 'user50', 'user48', 'user22', 'user44', 'user6', 'user9']
users_today = set(today_users)
yesterday_and_today = users_yesterday & users_today
print(yesterday_and_today)
