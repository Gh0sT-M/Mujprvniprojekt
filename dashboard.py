import os
import psutil 

#Definice barev
RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"

#Kod pro baner
banner = f"""{RED}
 ██████╗ ██╗  ██╗  ██████╗  ███████╗ ████████╗      ███╗   ███╗
██╔════╝ ██║  ██║ ██╔═══██╗ ██╔════╝ ╚══██╔══╝      ████╗ ████║
██║  ███╗███████║ ██║   ██║ ███████╗    ██║   █████╗██╔████╔██║
██║   ██║██╔══██║ ██║   ██║ ╚════██║    ██║   ╚════╝██║╚██╔╝██║
╚██████╔╝██║  ██║ ╚██████╔╝ ███████║    ██║         ██║ ╚═╝ ██║
 ╚═════╝ ╚═╝  ╚═╝  ╚═════╝  ╚══════╝    ╚═╝         ╚═╝     ╚═╝
{RESET}"""

#Vycisteni obrazovky
os.system('clear')

print(banner)
print(f"{CYAN}--- [ SYSTEM DASHBOARD ] ---{RESET}")
def check_process(process_name):
    """Zjisti, jestli v systemu bezi dany program."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

user = "Gh0sT-M"
print(f"--- [ CYBERPUNK DASHBOARD READY ] ---")
print(f"Welcome back, {user}\n ")

#Vypis vyuzitipameti RAM
ram = psutil.virtual_memory()
print(f"Memory Usage: {ram.percent}% used ({ram.available // (1024**2)} MB free)")

#Kontrola CAVA
if check_process("cava"):
    print(f"STATUS: CAVA is currently [ {GREEN}ACTIVE{RESET} ]")
else:
    print(f"STATUS: CAVA is [ {RED}OFFLINE{RESET} ]")
    #Tady se muze skript zeptat
    choice = input("Do you want to launch CAVA (y/n): ")
    if choice.lower() == 'y':
        #Spusti CAVU v novem okne terminalu
        os.system("/usr/bin/cava")