import requests, os, threading, random, time, json
from colorama import Fore, Back, Style
from pystyle import Colors, Colorate, Center

clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
usernames = open('check.txt', 'r').read().split('\n')
clear()
count = 0
free = 0
taken = 0
proxyDebug = False

# Vanity Generator Logo
logo = """
░█████╗░██╗░░██╗███████╗░██████╗░██████╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔════╝██╔════╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░╚█████╗░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗░╚═══██╗  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝"""

def printLogo():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo, 1)))

def check():
    global count, free, taken
    while True:
        try:
            for user in usernames:
                proxy = random.choice(open("proxies.txt","r").read().splitlines()); proxyDict = {"http": f"http://{proxy}"}
                if proxyDebug == True:
                    print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.GREEN}{proxyDict}{Fore.RESET}")
                else:
                    pass
                r = requests.get(f"https://api.chess.com/pub/player/{user}", proxies=proxyDict)
                json_data = r.json()
                json.dumps(json_data, indent=4)
                if not "last_online" in json_data:
                    count +=1
                    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Taken: " + user)
                    with open('taken.txt', 'a') as f:
                        f.write(user + '\n')
                        taken += 1
                else:
                    count +=1
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Free: " + user)
                    with open('free.txt', 'a') as f:
                        f.write(user + '\n')
                        free += 1
                os.system(f"title Chess.com Username Checker - Status: {count}/{len(usernames)} - Free: {free} - Taken: {taken}")
        except Exception as e:
            print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Error: " + str(e))
            continue

clear()
printLogo()
try:
    while True:
        check()
        print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting.")
        time.sleep(1)
        exit()
except KeyboardInterrupt:
    clear()
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting.")
    time.sleep(1)
    exit()