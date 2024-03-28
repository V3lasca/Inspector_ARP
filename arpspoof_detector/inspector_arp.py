#!/usr/bin/env python3

import os, platform, sys

from core import FindDuplicateMac, Menu

Menu()

def extract_arp_cache():
    while True:
        try:
            choice = input('\n\033[4miarp\033[0m > ').lower().strip()

            if choice == '1' or choice == 'linux':
                if platform.system() == 'Linux':
                    FindDuplicateMac()
                else:
                    print('\033[31mWrong System\033[0m')

            elif choice == '2' or choice == 'macos':
                if platform.system() == 'Darwin':
                    FindDuplicateMac()
                else:
                    print('\033[31mWrong System\033[0m')

            elif choice == '3' or choice == 'windows':
                if platform.system() == 'Windows':
                    FindDuplicateMac()
                else: 
                    print('\033[31mWrong System\033[0m')
                    
            elif choice == 'help' or choice == '*':
                print('\n\033[35m[*]\033[0m Type \033[1mcls\033[0m to clear screen'
                      '\n\033[35m[*]\033[0m Type \033[1mexit\033[0m to exit program'
                      '\n\033[35m[*]\033[0m Entering words are case-insensitive'
                      '\n\033[35m[*]\033[0m Enter words, or numbers to select a system'
                      )
                
            elif choice == 'cls' or choice == 'clear': 
                if platform.system() == 'Linux': 
                    os.system('clear')
                    Menu()
                                        
                elif platform.system() == 'Darwin': 
                    os.system('clear')
                    Menu()
                                                         
                elif platform.system() == 'Windows': 
                    os.system('cls')
                    Menu()
                    
            elif choice == 'exit': 
                sys.exit("\nBE SEEING YOU, \033[32mHACKER\033[0m")

            elif choice.strip() == '' : 
                print('\033[31mEmpty Input\033[0m')

            else: 
                print('\033[31mWrong Input\033[0m')
        except KeyboardInterrupt:
            sys.exit("\n\nBE SEEING YOU, \033[32mHACKER\033[0m")
        
if __name__ == '__main__':
    extract_arp_cache()