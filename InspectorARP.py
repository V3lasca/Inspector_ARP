from termcolor import colored, cprint
from datetime import datetime
from re import findall
import platform as p
import os

print(logo := '''
   ____                           __               ___    ___   ___ 
  /  _/___   ___  ___  ___  ____ / /_ ___   ____  / _ |  / _ \ / _ \\
 _/ / / _ \ (_-< / _ \/ -_)/ __// __// _ \ / __/ / __ | / , _// ___/
/___//_//_//___// .__/\__/ \__/ \__/ \___//_/   /_/ |_|/_/|_|/_/
               /_/
''')
menu = colored( 
'+' + '-' * 38 + '+\n' + 
'| Which system do you wish to test on? |\n'
'+' + '-' * 38 + '+', 'yellow'); print(menu)

linx = colored('1) Linux', 'green'); print(linx)
mac = colored('2) macOS', 'red'); print(mac)
win = colored('3) Windows', 'blue'); print(win)
help = colored('*) Help\n', 'white'); print(help)

alert = colored('[!]', 'red')
plus = colored('[+]', 'green')
minus = colored('[-]', 'cyan')
star = colored('[*]', 'magenta')

while True:
    #ARP table extraction
    extr = []

    def arpTable():
        global extr
        while True:
            choice = input('\033[4mIARP\033[0m > ').lower()
            if choice == '1' or choice == 'linux':
                if p.system()[0] == 'L':
                    cache = os.popen('arp -e').read()
                    extr = (findall('[0-9.]+\s+[a-zA-Z]+\s+[0-9:a-z]{17}', cache))
                    break
                else:
                    cprint('Wrong System', 'red')
            elif choice == '2' or choice == 'macos':
                if p.system()[0] == 'D':
                    cache = os.popen('arp -e').read()
                    extr = (findall('[0-9.]+\s+[a-zA-Z]+\s+[0-9:a-z]{17}', cache))
                    break
                else:
                    cprint('Wrong System', 'red')
            elif choice == '3' or choice == 'windows':
                if p.system()[0] == 'W':
                    cache = os.popen('arp -a').read()
                    extr = (findall('[0-9.]+\s+[0-9-a-z]{17}', cache))
                    break
                else:
                    cprint('Wrong System', 'red')
            elif choice == 'help' or choice == '*':
                print('\n' + star, 'Type "cls" to clear screen',
                      '\n' + star, 'Type "exit" to exit program',
                      '\n' + star, 'Type "menu" to show options',
                      '\n' + star, 'Enter a word, number, or symbol to use program',
                      '\n' + star, 'Entering words are case-insensitive\n')
            elif choice == 'exit': exit()
            elif choice == 'menu': print('\n' + menu + '\n' + linx + '\n' 
                                         + mac + '\n' + win + '\n' + help )
            elif choice == 'cls': 
                if p.system()[0] == 'L': os.system('clear'); print(logo)
                elif p.system()[0] == 'M': os.system('clear'); print(logo)              
                else: os.system('cls'); print(logo)
            else: cprint('Wrong Input', 'red')
    arpTable()

    #Splits listTable
    listTable = ''

    for i in extr:
        listTable += i + ' '

    listTable = listTable.split()
    
    listTable = [i for i in listTable if i != 'ether']

    #Converts list into a dictionary
    ip_list = []
    mac_list = []

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

        #List of duplicate MAC address(s)
        duplicate_mac = [key for key, value in checkTable.items() if len(value) > 1]
        
        for j in duplicate_mac:
            duplicate_mac_str = str(j)

        #Date and time
        dt = datetime.now().strftime('%A, %B %d, %Y / %I:%M %p')

        #Finds duplicate match in the checkTable dictionary
        try:
            if duplicate_mac_str in checkTable.keys():
                IP = checkTable[duplicate_mac_str]
                IP = ', '.join(IP)
                print(f'\n{dt}')
                print('\n' + alert, f'{duplicate_mac_str} belongs to: {IP}')

                #Logs event
                user_name = os.getlogin()

                if p.system()[0] == 'L':
                    print('\n' + plus, '\"ALERT\" file was created in the desktop directory\n')
                    with open('/home/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                        file.write(f'{duplicate_mac_str} belongs to > {IP} \n')
                elif p.system()[0] == 'D':
                    print('\n' + plus, '\"ALERT\" file was created in the desktop directory\n')
                    with open('/Users/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                        file.write(f'{duplicate_mac_str} belongs to > {IP} \n')
                elif p.system()[0] == 'W':
                    path = 'C:/Users/' + user_name + '/OneDrive/Desktop'

                    if os.path.exists(path):
                        print('\n' + plus, '\"ALERT\" file was created in the desktop directory\n')
                        with open('/Users/' + user_name + '/OneDrive/Desktop/ALERT.txt', 'a') as file:
                            file.write(f'{duplicate_mac_str} belongs to > {IP} \n')
                    else:
                        print('\n' + plus, '\"ALERT\" file was created in the desktop directory\n')
                        with open('/Users/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                            file.write(f'{duplicate_mac_str} belongs to > {IP} \n')
        except Exception:
             print('\n' + minus, 'No ARP Spoofing Attack Detected\n')
    duplicateMAC()
