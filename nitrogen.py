import random

#nitro generator coded by thelinux-userchoice v1.0
FAIL = '\033[91m' #just shut up
WARNING = '\033[93m' #nothing

print("nitro generator coded by thelinux-userchoice v1.0\n")

print(FAIL +"  ▒███████▒▓█████  ███▄    █ ")
print(FAIL +"  ▒ ▒ ▒ ▄▀░▓█   ▀  ██ ▀█   █ ")
print(FAIL +"  ░ ▒ ▄▀▒░ ▒███   ▓██  ▀█ ██▒")
print(WARNING+"  ▄▀▒   ░▒▓█  ▄ ▓██▒  ▐▌██▒")
print(WARNING+"▒███████▒░▒████▒▒██░   ▓██░")
print(WARNING+"░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒ ")
print(FAIL +"  ░░▒ ▒ ░ ▒ ░ ░  ░░ ░░   ░ ▒░")
print(FAIL +"  ░ ░ ░ ░ ░   ░      ░   ░ ░ ")
print(FAIL +"  ░ ░       ░  ░         ░ ")
print(WARNING+" ░                         \n") 



def gen():
    chars = ['a', 'b', 'c', 'd',  'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '1','2','3','4','5','6','7','8','9','0'
    ]
    return "".join(random.choices(chars, k=16))

link = "https://discord.gift/"



nitro = link + gen()


n = int(input("How many nitro codes you want me to generate:"))
f = open("GeneratedNitro.txt","a+")
for x in range(n):
  f.write(f"{nitro}\n")
f.close()
print("Finished!")
