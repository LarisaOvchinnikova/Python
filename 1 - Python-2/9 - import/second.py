#import first
#from first import hi, hello
from first import *
from first import hey as simple_hey  # дали импортир.функии другое имя


#first.hello()

#first.hi("Ann")
hi("Ann")
hello()
hey()

# можно переписать импортированную функцию, тогда она уже будет недоступна
def hey(user):
    print("Hey", user)

hey("nama")
simple_hey()