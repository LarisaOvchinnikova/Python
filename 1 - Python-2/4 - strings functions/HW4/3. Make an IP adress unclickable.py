# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

def ip_address(address):
    return address.replace(".", "[.]")

print(ip_address("1.1.1.1"))