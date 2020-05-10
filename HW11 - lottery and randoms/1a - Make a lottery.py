from random import randint

secret_lst = set()
while len(secret_lst) < 5:
   secret_lst.add(randint(1,10))
# print(secret_lst)

print("I have a list of 5 numbers from 1 to 10, try to guess it")
user_guess = [int(input("Enter number")) for i in range(5)]
# print(user_guess)

guessed = secret_lst & set(user_guess)
total_score = 0
# print(guessed)
for i in guessed:
   total_score += 5
total_score *= len(guessed)
print(f"You guessed {len(guessed)} numbers: {guessed}")
print(f"List of numbers was: {secret_lst}")
print(f"You have {total_score} points")