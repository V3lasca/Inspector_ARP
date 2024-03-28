import os, platform, time

from core import Menu

class Log:
    def log(event):
        user_name = os.getlogin()
        
        date_time = time.strftime('%A, %B %d, %Y / %I:%M %p')
        
        choice = input('\n\033[33m[?]\033[0m Do you want to save event as a text file? (y/n) > ').lower().strip()

        if choice != 'y' and choice != 'yes' and choice != '':
            if platform.system() == 'Linux': 
                os.system('clear')
                Menu()

            elif platform.system() == 'Darwin': 
                os.system('clear')
                Menu()

            elif platform.system() == 'Windows': 
                os.system('cls')
                Menu()

        elif platform.system() == 'Linux':
            print('\n\033[32m[+]\033[0m "ALERT" file was created in the desktop directory')
            
            with open(f'/home/{user_name}/Desktop/ALERT.txt', 'a') as file: 
                file.write(f'{date_time}\n{event}\n\n')

        elif platform.system() == 'Darwin':
            print('\n\033[32m[+]\033[0m "ALERT" file was created in the desktop directory')
            
            with open(f'/Users/{user_name}/Desktop/ALERT.txt', 'a') as file:
                file.write(f'{date_time}\n{event}\n\n')

        elif platform.system() == 'Windows':
            path = (fr'\Users\{user_name}\OneDrive\Desktop')

            if os.path.exists(path):
                print('\n\033[32m[+]\033[0m "ALERT" file was created in the desktop directory')
                
                with open(fr'\Users\{user_name}\OneDrive\Desktop\ALERT.txt', 'a') as file:
                    file.write(f'{date_time}\n{event}\n\n')
            else:
                print('\n\033[32m[+]\033[0m "ALERT" file was created in the desktop directory')
                
                with open(fr'\Users\{user_name}\Desktop\ALERT.txt', 'a') as file:
                    file.write(f'{date_time}\n{event}\n\n')