from colorama import init, Back, Fore
from datetime import datetime
from re import findall
import os
import platform as p

init(autoreset = True)

print(logo := '''
   ____                           __               ___    ___   ___ 
  /  _/___   ___  ___  ___  ____ / /_ ___   ____  / _ |  / _ \ / _ \\
 _/ / / _ \ (_-< / _ \/ -_)/ __// __// _ \ / __/ / __ | / , _// ___/
/___//_//_//___// .__/\__/ \__/ \__/ \___//_/   /_/ |_|/_/|_|/_/
               /_/
''')

menu = (Fore.YELLOW + '+' + '-' * 38 + '+\n'
        '| Which system do you wish to test on? |\n'
        '+' + '-' * 38 + '+'); print(menu)

linux = (Fore.GREEN + '1) Linux'); print(linux)
mac = (Fore.RED + '2) macOS'); print(mac)
win = (Fore.BLUE + '3) Windows'); print(win)
help = (Fore.WHITE + '*) Help'); print(help)

while True:
    extr = []
    
    #ARP table extraction
    def arpTableExtraction():
        global extr
        while True:
            try:
                choice = input('\n\033[4mIARP\033[0m > ').lower()
                if choice == '1' or choice == 'linux':
                    if p.system()[0] == 'L':
                        cache = os.popen('arp -n').read()
                        extr = findall('[0-9.]+\s+[a-z]+\s+[0-9:a-z]{17}', cache)
                        break
                    else:
                        print(Fore.RED + 'Wrong System')
                elif choice == '2' or choice == 'macos':
                    if p.system()[0] == 'D':
                        cache = os.popen('arp -n').read()
                        extr = findall('[0-9.]+\s+[a-z]+\s+[0-9:a-z]{17}', cache)
                        break
                    else:
                        print(Fore.RED + 'Wrong System')
                elif choice == '3' or choice == 'windows':
                    if p.system()[0] == 'W':
                        cache = os.popen('arp -a').read()
                        extr = findall('[0-9.]+\s+[0-9-a-z]{17}', cache)
                        break
                    else:
                        print(Fore.RED + 'Wrong System')
                elif choice == 'help' or choice == '*':
                    print(Fore.MAGENTA + '\n[*]', 'Type "cls" to clear screen',
                          Fore.MAGENTA + '\n[*]', 'Type "exit" to exit program',
                          Fore.MAGENTA + '\n[*]', 'Type "menu" to show options',
                          Fore.MAGENTA + '\n[*]', 'Enter words, numbers, or a symbol to use program',
                          Fore.MAGENTA + '\n[*]', 'Entering words are case-insensitive')
                elif choice == 'exit': exit()
                elif choice == 'menu': print('\n' + menu + '\n' + linux + '\n' + mac + '\n'
                                              + win + '\n' + help)
                elif choice == 'cls': 
                    if p.system()[0] == 'L': os.system('clear'); print(logo)
                    elif p.system()[0] == 'D': os.system('clear'); print(logo)              
                    elif p.system()[0] == 'W': os.system('cls'); print(logo)          
                else: print(Fore.RED + 'Wrong Input')
            except KeyboardInterrupt:
                exit()
    arpTableExtraction()

    listTable = ''

    #Splits list
    for i in extr: listTable += i + ' '
    listTable = listTable.split()

    listTable = [i for i in listTable if i != 'ether']

    ip_list = []
    mac_list = []

    #Converts list into a dictionary
    for k in range(len(listTable)):
        if k % 2:
            mac_list.append(listTable[k])
        else:
            ip_list.append((listTable[k]))
    filterTable = dict(zip(ip_list, mac_list))
    
    def duplicateMAC():
        checkTable = {}

        #Groups IP addresses with same MAC address
        for key, value in filterTable.items():
            checkTable.setdefault(value, set()).add(key)
        
        #Removes broadcast address
        while 'ff-ff-ff-ff-ff-ff' in checkTable:
            checkTable.pop('ff-ff-ff-ff-ff-ff')
        while 'ff:ff:ff:ff:ff:ff' in checkTable:
            checkTable.pop('ff:ff:ff:ff:ff:ff')

        #List of duplicate MAC address(es)
        duplicate_mac = [key for key, value in checkTable.items() if len(value) > 1]

        for j in duplicate_mac:
            duplicate_mac = str(j)

        try:
            #Finds duplicate match in the checkTable dictionary
            if duplicate_mac in checkTable.keys():
                IP = checkTable[duplicate_mac]
                IP = ', '.join(IP)
                print('\n[!] ARP Spoof Detected')
                print(f'\n[!] {duplicate_mac} belongs to: {IP}')

                #Date and time
                dt = datetime.now().strftime('%A, %B %d, %Y / %I:%M %p')
                
                #Logs event
                user_name = os.getlogin()
                choice = input('\nDo you want to save event as a text file? (y/n) > ').lower()
                if choice != 'y' or choice != 'yes':
                    if p.system()[0] == 'L': os.system('clear'); print(logo)
                    elif p.system()[0] == 'D': os.system('clear'); print(logo)
                    elif p.system()[0] == 'W': os.system('cls'); print(logo)
                elif p.system()[0] == 'L':
                    print('\n[+] \"ALERT\" file was created in the desktop directory')
                    with open('/home/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                        file.write(f'{dt}\n{duplicate_mac} belongs to > {IP}\n\n')
                elif p.system()[0] == 'D':
                    print(Fore.GREEN + '\n[+]', '\"ALERT\" file was created in the desktop directory')
                    with open('/Users/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                        file.write(f'{dt}\n{duplicate_mac} belongs to > {IP}\n\n')
                elif p.system()[0] == 'W':
                    path = 'C:/Users/' + user_name + '/OneDrive/Desktop'

                    if os.path.exists(path):
                        print(Fore.GREEN + '\n[+]', '\"ALERT\" file was created in the desktop directory')
                        with open('/Users/' + user_name + '/OneDrive/Desktop/ALERT.txt', 'a') as file:
                            file.write(f'{dt}\n{duplicate_mac} belongs to > {IP}\n\n')
                    else:
                        print(Fore.GREEN + '\n[+]', '\"ALERT\" file was created in the desktop directory')
                        with open('/Users/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                            file.write(f'{dt}\n{duplicate_mac} belongs to > {IP}\n\n')
        except Exception: 
            print(Fore.CYAN + '\n[-]', 'No ARP Spoofing Attack Detected')
    duplicateMAC()
