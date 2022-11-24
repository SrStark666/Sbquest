import configs
from colorama import Fore, init


init(convert=True)
try:
    while True:
        game = str(input(f"{Fore.YELLOW}Digite o nome do jogo: {Fore.RESET}").replace(" ", "-")).lower()
        obj = configs.req(game)
        for codes in obj:
            print(f"{Fore.CYAN}{codes}{Fore.RESET} >>> {Fore.MAGENTA}{obj[codes]}{Fore.RESET}")
        print(f"{Fore.GREEN}Códigos encontrados: {len(obj)}{Fore.RESET}")

        choice = str(input(f"{Fore.YELLOW}Deseja salvar em um arquivo? S/n {Fore.RESET}")).lower()
        if choice == "s" or choice == "sim":
            archive = str(input(f"{Fore.YELLOW}Nome do arquivo: {Fore.RESET}"))
            configs.archive(archive)
            break
        elif choice == "n":
            break
        else:
            print(f"{Fore.RED}Erro na entrada de dados{Fore.RESET}")
            break
except KeyboardInterrupt:
    print(f"{Fore.RESET}Programa encerrado{Fore.RESET}")