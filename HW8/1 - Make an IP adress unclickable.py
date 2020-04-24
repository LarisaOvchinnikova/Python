# Make an IP adress unclickable
# Replace every period in IP " . " with " [ . ] "

def ip_address(address):
    return '[.]'.join(address.split('.'))

print(ip_address("1.1.1.1"))

def ip(address):
    return address.replace('.','[.]')
print(ip('1.1.1.1'))
