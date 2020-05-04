import random
for i in range(10):
    x = random.random()  # [0.0 - 1.0]
    y = random.uniform(0,20) #random real
    z = random.randint(0,20) # random integer
    c = random.choice("monkey") # random from str, list, set
    a = random.randrange(0,10,2) # random from 0 to 10 step 2(even)
    print(x,y,z,c, a)