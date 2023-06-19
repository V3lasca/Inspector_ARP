import os, platform, sys

from core import FindDuplicateMac, Screen

Screen.menu()
    
while True:
    def extract_arp_cache():
        while True:
            try:
                choice = input('\n\033[4miarp\033[0m > ').lower()

                if choice == '1' or choice == 'linux':
                    if platform.system() == 'Linux':
                        FindDuplicateMac.run()
                    else:
                        print('\033[31mWrong System\033[0m')

                elif choice == '2' or choice == 'macos':
                    if platform.system() == 'Darwin':
                        FindDuplicateMac.run()
                    else:
                        print('\033[31mWrong System\033[0m')

                elif choice == '3' or choice == 'windows':
                    if platform.system() == 'Windows':
                        FindDuplicateMac.run()
                    else: 
                        print('\033[31mWrong System\033[0m')
                        
                elif choice == 'help' or choice == '*':
                    print('\n\033[35m[*]\033[0m Type "cls" to clear screen',
                          '\n\033[35m[*]\033[0m Type "exit" to exit program',
                          '\n\033[35m[*]\033[0m Entering words are case-insensitive',
                          '\n\033[35m[*]\033[0m Enter words, numbers, or a symbol to use program')
                    
                elif choice == 'cls': 
                    if platform.system() == 'Linux': 
                        os.system('clear')
                        Screen.menu()
                                            
                    elif platform.system() == 'Darwin': 
                        os.system('clear')
                        Screen.menu()
                                                             
                    elif platform.system() == 'Windows': 
                        os.system('cls')
                        Screen.menu()
                        
                elif choice == 'exit': 
                    sys.exit()

                elif choice.strip() == '' : 
                    print('\033[31mEmpty Input\033[0m')

                else: 
                    print('\033[31mWrong Input\033[0m')
                     
            except KeyboardInterrupt:
                sys.exit()
    
    if __name__ == '__main__':
        extract_arp_cache()
