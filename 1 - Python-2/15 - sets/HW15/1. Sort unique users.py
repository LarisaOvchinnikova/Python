def unique_users(users):
    return sorted(set(users))

users = ['user62', 'user37', 'user34', 'user42',
         'user42', 'user76', 'user34', 'user37',
         'user76', 'user68', 'user34', 'user27',
         'user62', 'user93', 'user26', 'user42']

print(unique_users(users))

