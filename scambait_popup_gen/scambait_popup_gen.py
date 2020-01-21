import webbrowser
import random
import os, sys
from getch import pause

# Test if this is a PyInstaller executable or a .py file
if getattr(sys, 'frozen', False):
    IS_EXE = True
    PROG_FILE = sys.executable
    PROG_PATH = os.path.dirname(PROG_FILE) 
    PATH = sys._MEIPASS
else:
    IS_EXE = False
    PROG_FILE = os.path.realpath(__file__)
    PROG_PATH = os.path.dirname(PROG_FILE)
    PATH = PROG_PATH

# Get and randomize links
scam_links_filename = os.path.join(PATH, 'scambait_megalist.txt')
with open(scam_links_filename, 'r') as f:
    read_links = f.read().splitlines()
scam_links = []
for link in read_links:
    link = link.strip()
    if link not in ['', None]:
        scam_links.append(link)
random.shuffle(scam_links)

print('~~~~ Scambaiting Popup Link Generator by nimaid ~~~~')
print('\n!!! ONLY USE THIS INSIDE A VIRTUAL MACHINE !!!')
print('!!! THESE LINKS MAY INSTALL MALWARE, USE WITH EXTREME CAUTION !!!')
print('\nMany of these links will not redirect to malicious websites unless you appear as a naive, vulnerable user.')
print('Make sure you are using Internet Explorer, your VPN is off, and your web protections are turned off.')

def ask_question(question='Y/N', options=['Y', 'N'], default=None):
    options = [x.upper() for x in options]
    default = default.upper()
    answer = None
    error_string = 'Please enter one of the following:'
    while answer not in options:
        answer = input(question + ': ').strip().upper()
        if answer in options:
            return answer
        else:
            if answer == '':
                if (default == None) or (default not in options):
                    print(error_string, options)
                else:
                    return default
            else:
                print(error_string, options)

run_gen = ask_question(question='\nDo you wish to continue with opening malicious links? (Y/[N])', default='N')
if run_gen == 'N':
    print('Exiting...\n')
    exit()

for i, scam_link in enumerate(scam_links):
    print('')
    print('Opening link {}/{}: {}'.format(i+1, len(scam_links), scam_link))
    reopen = True;
    while reopen:
        webbrowser.open_new(scam_link)
        user_resp = ask_question(question='[R]e-open current link, [N]ext link, or [Q]uit? (R/N/[Q])', options=['R','N','Q'], default='Q')
        if user_resp == 'R':
            print('Re-opening {}'.format(scam_link))
            reopen = True
        elif user_resp == 'N':
            reopen = False
        else:
            sys.exit('Exiting...')

print('\n\nAll links exausted.')
pause("Press any key to exit...")
sys.exit('Exiting...')
