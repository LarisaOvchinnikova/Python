from random import choice

arr = ['cat','dog','monkey','sparrow','elephant','rino','dinosour','giraffe','antilope','octopus','donkey','camel','zebra','spider','crocodile','alligator','panda','lion','armadillo','racoon']

score = 0
secret = choice(arr)
# print(secret)
dashes = len(secret)*['-']
print('Guess the word!')
print( " ".join(dashes))
while '-' in dashes:
  letter = input('Enter your letter guess: ')
  if letter in secret:
    score += 1
    for i,el in enumerate(secret):
      if el == letter:
        dashes[i] = letter
    print(" ".join(dashes))
  else:
    score -= 1
print(f'Yay you guessed it the word was {secret}!')
print(f'You got {score}/{len(secret)} points!')
