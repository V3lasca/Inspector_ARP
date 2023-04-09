from colorama import Fore
from scripts import log_event

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
            
            log_event(f'{list_of_duplicate_mac_addr} belongs to > {list_of_ip_addr}')
    except:
        print(Fore.CYAN + '\n[-]', 'No ARP Spoofing Attack Detected')

if __name__ == '__main__':
    find_duplicate_mac()
    log_event