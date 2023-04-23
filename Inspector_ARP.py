from colorama import Fore, init
from re import findall
from scripts import find_duplicate_mac
import os, platform, sys

init(autoreset = True)

print(logo := '''
   ____                           __               ___    ___   ___ 
  /  _/___   ___  ___  ___  ____ / /_ ___   ____  / _ |  / _ \ / _ \\
 _/ / / _ \ (_-< / _ \/ -_)/ __// __// _ \ / __/ / __ | / , _// ___/
/___//_//_//___// .__/\__/ \__/ \__/ \___//_/   /_/ |_|/_/|_|/_/
               /_/
''')

print(menu := Fore.YELLOW + '+' + '-' * 38 + '+\n'
      '| Which system do you wish to test on? |\n' 
      '+' + '-' * 38 + '+')

print(linux := Fore.GREEN + '1) Linux')
print(mac := Fore.RED + '2) macOS')
print(win := Fore.BLUE + '3) Windows')
print(help := Fore.WHITE + '*) Help')

while True:
    def extract_arp_cache():
        while True:
            try:
                choice = input('\n\033[4mIARP\033[0m > ').lower()

                if choice == '1' or choice == 'linux':
                    if platform.system() == 'Linux':
                        cache = os.popen('arp -n').read()
                        extr = findall('[0-9.]+\s+[a-z]+\s+[0-9:a-z]{17}', cache)
                        find_duplicate_mac(extr)
                    else:
                        print(Fore.RED + 'Wrong System')

                elif choice == '2' or choice == 'macos':
                    if platform.system() == 'Darwin':
                        cache = os.popen('arp -n').read()
                        extr = findall('[0-9.]+\s+[a-z]+\s+[0-9:a-z]{17}', cache)
                        find_duplicate_mac(extr)
                    else:
                        print(Fore.RED + 'Wrong System')

                elif choice == '3' or choice == 'windows':
                    if platform.system() == 'Windows':
                        cache = os.popen('arp -a').read()
                        extr = findall('[0-9.]+\s+[0-9-a-z]{17}', cache)
                        find_duplicate_mac(extr)
                    else: 
                        print(Fore.RED + 'Wrong System')

                elif choice == 'help' or choice == '*':
                    print(Fore.MAGENTA + '\n[*]', 'Type "cls" to clear screen',
                          Fore.MAGENTA + '\n[*]', 'Type "exit" to exit program',
                          Fore.MAGENTA + '\n[*]', 'Type "menu" to show options',
                          Fore.MAGENTA + '\n[*]', 'Entering words are case-insensitive',
                          Fore.MAGENTA + '\n[*]', 'Enter words, numbers, or a symbol to use program')
                    
                elif choice == 'cls': 
                    if platform.system() == 'Linux': 
                        os.system('clear'); print(logo)
                        
                    elif platform.system() == 'Darwin': 
                        os.system('clear'); print(logo)
                                      
                    elif platform.system() == 'Windows': 
                        os.system('cls'); print(logo)

                elif choice == 'exit': 
                    sys.exit()

                elif choice == 'menu': 
                    print(f'\n{menu}\n{linux}\n{mac}\n{win}\n{help}')

                elif choice.strip() == '' : 
                    print(Fore.RED + 'Empty Input')

                else: 
                    print(Fore.RED + 'Wrong Input')
            except KeyboardInterrupt:
                print('^C')
                sys.exit()
    
    if __name__ == '__main__':
        extract_arp_cache()
