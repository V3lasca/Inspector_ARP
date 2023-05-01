from colorama import Fore
import os, platform, time

logo = '''
   ____                           __               ___    ___   ___ 
  /  _/___   ___  ___  ___  ____ / /_ ___   ____  / _ |  / _ \ / _ \\
 _/ / / _ \ (_-< / _ \/ -_)/ __// __// _ \ / __/ / __ | / , _// ___/
/___//_//_//___// .__/\__/ \__/ \__/ \___//_/   /_/ |_|/_/|_|/_/
               /_/
'''

menu = (Fore.YELLOW + '+' + '-' * 38 + '+\n'
      '| Which system do you wish to test on? |\n' 
      '+' + '-' * 38 + '+')

linux = (Fore.GREEN + '1) Linux')
mac = (Fore.RED + '2) macOS')
win = (Fore.BLUE + '3) Windows')
help = (Fore.WHITE + '*) Help')

def log_event(event):
    user_name = os.getlogin()
    date_time = time.strftime('%A, %B %d, %Y / %I:%M %p')
    choice = input('\n\033[33m[?]\033[0m Do you want to save event as a text file? (y/n) > ').lower()
    
    if choice != 'y' and choice != 'yes':
        if platform.system() == 'Linux': 
            os.system('clear')
            print(f'{logo}\n{menu}\n{linux}\n{mac}\n{win}\n{help}')

        elif platform.system() == 'Darwin': 
            os.system('clear')
            print(f'{logo}\n{menu}\n{linux}\n{mac}\n{win}\n{help}')
            
        elif platform.system() == 'Windows': 
            os.system('cls')
            print(f'{logo}\n{menu}\n{linux}\n{mac}\n{win}\n{help}')

    elif platform.system() == 'Linux':
        print(Fore.GREEN + '\n[+]', '"ALERT" file was created in the desktop directory')
        with open(f'/home/{user_name}/Desktop/ALERT.txt', 'a') as file: 
            file.write(f'{date_time}\n{event}\n\n')
            
    elif platform.system() == 'Darwin':
        print(Fore.GREEN + '\n[+]', '"ALERT" file was created in the desktop directory')
        with open(f'/Users/{user_name}/Desktop/ALERT.txt', 'a') as file:
            file.write(f'{date_time}\n{event}\n\n')
            
    elif platform.system() == 'Windows':
        path = (f'\\Users\\{user_name}\\OneDrive\\Desktop')

        if os.path.exists(path):
            print(Fore.GREEN + '\n[+]', '"ALERT" file was created in the desktop directory')
            with open(f'\\Users\\{user_name}\\OneDrive\\Desktop\\ALERT.txt', 'a') as file:
                file.write(f'{date_time}\n{event}\n\n')
        else:
            print(Fore.GREEN + '\n[+]', '"ALERT" file was created in the desktop directory')
            with open(f'\\Users\\{user_name}\\Desktop\\ALERT.txt', 'a') as file:
                file.write(f'{date_time}\n{event}\n\n')

if __name__ == '__main__':
    log_event()
