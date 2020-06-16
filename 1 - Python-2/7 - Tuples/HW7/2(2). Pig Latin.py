def pig_it(string):
  lst = string.split()
  return " ".join([el[1:]+el[0]+"ay" for el in lst])

print(pig_it('Pig latin is cool'))
print(pig_it('Hello world'))