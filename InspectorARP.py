import datetime as dt
import os
import platform as p
from re import findall

while True:
    print('\n')
    print('   ____                           __               ___    ___   ___ ')
    print('  /  _/___   ___  ___  ___  ____ / /_ ___   ____  / _ |  / _ \ / _ \\')
    print(' _/ / / _ \ (_-< / _ \/ -_)/ __// __// _ \ / __/ / __ | / , _// ___/')
    print('/___//_//_//___// .__/\__/ \__/ \__/ \___//_/   /_/ |_|/_/|_|/_/')
    print('               /_/')
    print('\33[93m+--------------------------------------+\33[0m')
    print('\33[93m| Which system do you wish to test on? |\33[0m')
    print('\33[93m+--------------------------------------+\33[0m')
    print('\33[92m1) Linux\33[0m')
    print('\33[31m2) macOS\33[0m')
    print('\33[94m3) Windows\33[0m')
    print('*) Help\n')

    # ARP table extraction
    info = []

    def arpTable():
        global info
        while True:
            choice = input('\33[4mIARP\33[0m > ').lower()
            if choice == '1' or choice == 'linux':
                if p.system()[0] == 'L':
                    record = os.popen('arp -e').read()
                    info = (findall('[0-9.]+\s+[a-z]+\s+[0-9:a-z]+', record))
                    break
                else:
                    print('\33[31mWrong System\33[0m')
            elif choice == '2' or choice == 'macos':
                if p.system()[0] == 'D':
                    record = os.popen('arp -e').read()
                    info = (findall('[0-9.]+\s+[a-z]+\s+[0-9:a-z]+', record))
                    break
                else:
                    print('\33[31mWrong System\33[0m')
            elif choice == '3' or choice == 'windows':
                if p.system()[0] == 'W':
                    record = os.popen('arp -a').read()
                    info = (findall('[0-9.]+\s+[0-9-a-z]{17}', record))
                    break
                else:
                    print('\33[31mWrong System\33[0m')
            elif choice == 'help' or choice == '*':
                print('\n[*] Type \'exit\' to quit program',
                      '\n[*] Enter words, numbers, or a symbol to use program',
                      '\n[*] Entering words are case-insensitive\n')
            elif choice == 'exit':
                exit()
            else:
                print('\33[31mWrong Input\33[0m')
    arpTable()

    # Splits listTable
    listTable = ''

    for i in info:
        listTable += i + ' '
    listTable = listTable.split()

    if p.system()[0] == 'L' or p.system()[0] == 'D':
        while 'ether' in listTable:
            listTable.remove('ether')

    # Converts list into a dictionary
    ip_list = []
    mac_list = []

    for k in range(len(listTable)):
        if k % 2:
            mac_list.append(listTable[k])
        else:
            ip_list.append((listTable[k]))
    filterTable = dict(zip(ip_list, mac_list))

    def duplicateMAC():
        try:
            checkTable = {}
            global duplicate_mac_str
            global IP

            # Groups IP addresses with same MAC address
            for key, value in filterTable.items():
                checkTable.setdefault(value, set()).add(key)

            # List of duplicate MAC address(s)
            duplicate_mac = [key for key, value in checkTable.items() if len(value) > 1]

            for j in duplicate_mac:
                duplicate_mac_str = str(j)

            # Finds duplicate match in the checkTable dictionary
            if duplicate_mac_str in checkTable.keys():
                IP = checkTable[duplicate_mac_str]
                print('\n\33[31m[!]\33[0m', duplicate_mac_str, "was duplicated by:", IP)
            
            # Logs event
            user_name = os.getlogin()
            date = dt.datetime.now()

            if p.system()[0] == 'L':
                print('\n\33[92m[+]\33[0m \"ALERT\" file was created in desktop')
                with open('/home/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                    file.write(date.strftime('%A, %B %d, %Y / %I:%M %p') + '\n' + 
                            duplicate_mac_str + ' was duplicated by > ' + str(IP) + '\n')
            elif p.system()[0] == 'D':
                print('\n\33[92m[+]\33[0m \"ALERT\" file was created in desktop')
                with open('/Users/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                    file.write(date.strftime('%A, %B %d, %Y / %I:%M %p') + '\n' + 
                            duplicate_mac_str + ' was duplicated by > ' + str(IP) + '\n')
            elif p.system()[0] == 'W':
                print('\n\33[92m[+]\33[0m \"ALERT\" file was created in desktop')
                with open('/Users/' + user_name + '/Desktop/ALERT.txt', 'a') as file:
                    file.write(date.strftime('%A, %B %d, %Y / %I:%M %p') + '\n' + 
                            duplicate_mac_str + ' was duplicated by > ' + str(IP) + '\n')
        except:
            print('\n\33[94m[*]\33[0m No ARP Spoofing Attack Detected')
    duplicateMAC()
    
    retry = input('\n\33[4mIARP\33[0m > Test again? (y/n): ')
    if retry != 'y':
        break