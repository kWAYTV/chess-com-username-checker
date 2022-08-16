import requests, os, threading, random, time, json
from colorama import Fore, Back, Style

clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
usernames = open('check.txt', 'r').read().split('\n')
clear()
count = 0
proxyDebug = False

def check():
    global count
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
                else:
                    count +=1
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Free: " + user)
                    with open('free.txt', 'a') as f:
                        f.write(user + '\n')
                os.system(f"title Chess.com Username Checker ^- Checked: " + str(count) + " ^- Remaining: " + str(len(usernames) - count))
        except Exception as e:
            print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Error: " + str(e))
            continue

clear()
try:
    check()
except KeyboardInterrupt:
    clear()
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting.")
    time.sleep(1)
    exit()