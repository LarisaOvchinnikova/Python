def both(arr1, arr2):
    return list(set(arr1) & set(arr2))


yesterday_users = ['user32', 'user46', 'user22', 'user16', 'user21', 'user4', 'user6', 'user29', 'user1', 'user39']
today_users = ['user2', 'user39', 'user41', 'user38', 'user50', 'user48', 'user22', 'user44', 'user6', 'user9']
print(both(yesterday_users, today_users))