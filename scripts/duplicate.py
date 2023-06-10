import platform, re, subprocess, time

from core import Log

class FindDuplicateMac:
    def run():
        print('\n\033[35m[*]\033[0m Press Ctrl+C to stop detection')
    
        while True:
            if platform.system() == 'Linux':
                cache = subprocess.check_output(['arp', '-n']).decode('utf-8')
                extr = re.findall('[0-9.]+\s+[a-z]+\s+[0-9:a-zA-Z]{17}', cache)

            elif platform.system() == 'Darwin':
                cache = subprocess.check_output(['arp', '-n']).decode('utf-8')
                extr = re.findall('[0-9.]+\s+[a-z]+\s+[0-9:a-zA-Z]{17}', cache)

            elif platform.system() == 'Windows':
                cache = subprocess.check_output(['arp', '-a']).decode('utf-8')
                extr = re.findall('[0-9.]+\s+[0-9-a-zA-Z]{17}', cache)

            arp_table = ' '.join(extr)

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

            list_of_duplicate_mac_addr = [key for (key, value) in group_table.items() if len(value) > 1]

            for i in list_of_duplicate_mac_addr: 
                list_of_duplicate_mac_addr = str(i)

            try:
                if list_of_duplicate_mac_addr in group_table:
                    list_of_ip_addr = group_table[list_of_duplicate_mac_addr]
                    list_of_ip_addr = ', '.join(list_of_ip_addr)

                    print('\n\033[31m[!]\033[0m ARP Spoofing Attack Detected')
                    print('\033[0m[!]\033[0m', f'{list_of_duplicate_mac_addr} belongs to > {list_of_ip_addr}')

                    Log.log(f'{list_of_duplicate_mac_addr} belongs to > {list_of_ip_addr}')
                    break

            except TypeError:
                print('\n\033[36m[-]\033[0m No ARP Spoofing Attack Detected')
                time.sleep(.7)
