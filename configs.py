from bs4 import BeautifulSoup
from time import sleep
import subprocess
import requests
from googletrans import Translator
from colorama import Fore, init
import re
import os


valid_codes = {}

def req(game):
    init(convert=True)
    tr = Translator()

    agent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/45.0.2454.85 Safari/537.36"}
    get = requests.get(f"https://www.pockettactics.com/{game}/codes", headers=agent)

    if get.status_code != 200:
        print(f"\033[01;31mJogo não encontrado\nVerifique a entrada de dados!!\033[0m")
        sleep(4)
        subprocess.run("cls || clear", shell=True, universal_newlines=True)
        exit(0)

    html = get.text
    soup = BeautifulSoup(html, "html.parser")
    
    div = soup.select_one("#site_wrap > article > div.entry-content")
    tit = div.find("h2")
    h2_trad = tr.translate(tit.text, dest="pt").text
    
    for find_ul in soup.find_all("ul"):
        for find_code in find_ul.find_all("li"):
            for find_strong in find_code.find_all("strong"):
                convert = str(find_code.text).replace(u'\xa0', u' ').split(" – ")
                if len(convert) == 2:
                    valid_codes[convert[0]] = convert[1]
                else:
                    valid_codes[convert[0]] = f"{Fore.RED}Indefinido{Fore.RESET}"

    if len(valid_codes) == 0:
        print(f"{Fore.RED}No momento, não há códigos {game} ativos.{Fore.RESET}")
        exit(0)
    else:
        print(f"{Fore.RED}{'-'*len(h2_trad)}{Fore.RESET}\n{Fore.GREEN}{h2_trad}\n{Fore.RESET}{Fore.RED}{'-'*len(h2_trad)}{Fore.RESET}")
    return valid_codes


def archive(name):
    if not re.search(name, ".txt"):
        name += ".txt"

    if not os.path.exists(f"Codes/"):
        subprocess.run("mkdir Codes", shell=True, universal_newlines=True)

    with open(f"Codes/{name}", "w+") as arq:
        for codes in valid_codes:
            if "\x1b" in valid_codes[codes]:
                valid_codes[codes] = "Indefinido"
            
            wr = f"{codes} >>> {valid_codes[codes]}"
            arq.write(f"{wr}\n")
            
        print(f"{Fore.GREEN}Arquivo criado com sucesso!!{Fore.RESET}")

