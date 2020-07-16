from colorama import *
init()

print(Fore.YELLOW + "hello, how are you")
print(Fore.CYAN + "hi")
print(Fore.CYAN + Style.BRIGHT + "hi")
print(Fore.MAGENTA + Back.LIGHTGREEN_EX + "ho-ho")

print(Back.LIGHTYELLOW_EX+ Fore.GREEN, end='')
print("Nice ti see you!")

print(Style.RESET_ALL) # отмена цветов
print("hi")