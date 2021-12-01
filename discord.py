import discord
from colorama import Fore

token = ''
client = discord.Client()


def on_run(token=None):
    if token == '':
        token = input(f'''{Fore.YELLOW}[!]{Fore.RESET} No token detected\n {Fore.LIGHTMAGENTA_EX}Please enter your 
        token: {Fore.RESET}''')


def massdm():
    id = input(f'{Fore.MAGENTA}Enter guild id: ')


@client.event
async def on_ready():
    print(f'''{Fore.CYAN}
██╗██████╗░██╗░░██╗
██║██╔══██╗██║░██╔╝
██║██║░░██║█████═╝░
██║██║░░██║██╔═██╗░
██║██████╔╝██║░╚██╗
╚═╝╚═════╝░╚═╝░░╚═╝''')
    print(f'''{Fore.LIGHTBLUE_EX}Logged in as: {Fore.GREEN}{client.user}''')
    print(f'''{Fore.RED}[1]{Fore.LIGHTRED_EX} Mass dm server''')
    var69 = input(f'''{Fore.LIGHTGREEN_EX} Choose an option: ''')
    if var69 == '1':
        massdm()


if __name__ == '__main__':
    on_run()

client.run(token)
