from colorama import Fore, init
from re import findall
import os, platform, sys, time

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
                sys.exit()

    def find_duplicate_mac(extr):
        arp_table = ''

        for i in extr: 
            arp_table += i + ' '

        arp_table = arp_table.split()

        # Removes HWtype (type of link) from list
        arp_table = [i for i in arp_table if i != 'ether']
        
        ip_addr = []
        mac_addr = []

        for i in range(len(arp_table)):
            if i % 2:
                mac_addr.append(arp_table[i])
            else:
                ip_addr.append((arp_table[i]))

        dict_table = dict(zip(ip_addr, mac_addr))

        group_table = {}
        # Groups MAC addresses with corresponding IP addresses 
        for key, value in dict_table.items(): 
            group_table.setdefault(value, set()).add(key)
        
        # Removes broadcast address
        while 'ff-ff-ff-ff-ff-ff' in group_table: 
            group_table.pop('ff-ff-ff-ff-ff-ff')
        while 'ff:ff:ff:ff:ff:ff' in group_table: 
            group_table.pop('ff:ff:ff:ff:ff:ff')

        list_of_duplicate_mac_addr = [key for key, value in group_table.items() if len(value) > 1]
        
        for i in list_of_duplicate_mac_addr: 
            list_of_duplicate_mac_addr = str(i)

        try:
            if list_of_duplicate_mac_addr in group_table.keys():
                list_of_ip_addr = group_table[list_of_duplicate_mac_addr]
                list_of_ip_addr = ', '.join(list_of_ip_addr)
                
                print(Fore.RED + '\n[!]', 'ARP Spoofing Attack Detected')
                print(Fore.RED + '[!]', f'{list_of_duplicate_mac_addr} belongs to > {list_of_ip_addr}')

                log(f'{list_of_duplicate_mac_addr} belongs to > {list_of_ip_addr}')
        except:
            print(Fore.CYAN + '\n[-]', 'No ARP Spoofing Attack Detected')
             
    def log(event):
        date_time = time.strftime('%A, %B %d, %Y / %I:%M %p')
        user_name = os.getlogin()
        choice = input('\033[33m\n[?]\033[0m Do you want to save event as a text file? (y/n) > ').lower()

        if choice != 'y' and choice != 'yes':
            if platform.system() == 'Linux': 
                os.system('clear'); print(logo)

            elif platform.system() == 'Darwin': 
                os.system('clear'); print(logo)
                
            elif platform.system() == 'Windows': 
                os.system('cls'); print(logo)

        elif platform.system() == 'Linux':
            print(Fore.GREEN + '\n[+]', '\"ALERT\" file was created in the desktop directory')
            with open('/home/' + user_name + '/Desktop/ALERT.txt', 'a') as file: 
                file.write(f'{date_time}\n{event}\n\n')
                
        elif platform.system() == 'Darwin':
            print(Fore.GREEN + '\n[+]', '\"ALERT\" file was created in the desktop directory')
            with open('/Users/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                file.write(f'{date_time}\n{event}\n\n')
                
        elif platform.system() == 'Windows':
            path = '/Users/' + user_name + '/OneDrive/Desktop'

            if os.path.exists(path):
                print(Fore.GREEN + '\n[+]', '\"ALERT\" file was created in the desktop directory')
                with open('/Users/' + user_name + '/OneDrive/Desktop/ALERT.txt', 'a') as file:
                    file.write(f'{date_time}\n{event}\n\n')
            else:
                print(Fore.GREEN + '\n[+]', '\"ALERT\" file was created in the desktop directory')
                with open('/Users/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                    file.write(f'{date_time}\n{event}\n\n')
    extract_arp_cache()
