def get_sum(a,b):
   s = 0
   first = min(a,b)
   second = max(a,b)

   for i in range(first, second+1):
      s += i
   return s


print(get_sum(1,2))
print(get_sum(1,0))