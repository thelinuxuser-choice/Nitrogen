import random, string
import requests
import os
from colorama import Fore



# Idea and help by stackoverflow

print(f"{Fore.RED} ▐ ▄ ▪  ▄▄▄▄▄▄▄▄             ▄▄ • ▄▄▄ . ▐ ▄  ")
print(f"{Fore.RED}•█▌▐███ •██  ▀▄ █·▪         ▐█ ▀ ▪▀▄.▀·•█▌▐█   {Fore.YELLOW} version    :1.1")
print(f"{Fore.RED}▐█▐▐▌▐█· ▐█.▪▐▀▀▄  ▄█▀▄     ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌   {Fore.YELLOW} status     :working")
print(f"{Fore.RED}██▐█▌▐█▌ ▐█▌·▐█•█▌▐█▌.▐▌    ▐█▄▪▐█▐█▄▄▌██▐█▌   {Fore.YELLOW} maintaining:yes")
print(f"{Fore.RED}▀▀ █▪▀▀▀ ▀▀▀ .▀  ▀ ▀█▄▀▪    ·▀▀▀▀  ▀▀▀ ▀▀ █▪   ")

print(f"{Fore.CYAN}▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄")
print(f"{Fore.CYAN}▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
print(f"{Fore.CYAN}▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀")

print(f"{Fore.GREEN}[!]github - https://github.com/thelinuxuser-choice/Nitrogen/")





from time import sleep
import sys

line_1 = "[#]Discord nitrogen by thelinux-userchoice\n"
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)

num = input(f'{Fore.MAGENTA}[?]How many nitro codes you want me to generate:')

f = open("Generatednitro.txt", "a+", encoding='utf-8')

print("")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

print(f"{Fore.LIGHTYELLOW_EX}[>] Generated {num} nitro codes and saved \n[^]now going to check {num} nitro codes are valid are not! ")

with open("Generatednitro.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print("{Fore.RED}wow")
            print("[+]VALID CODE ┇ {} ".format(line.strip("\n")))
            break
        else:
            print("[-]INVALID CODE ┇ {} ".format(line.strip("\n")))

os.remove("Generatednitro.txt")

print(f"{Fore.LIGHTYELLOW_EX}\nbye bye :) please give me a star \n")
