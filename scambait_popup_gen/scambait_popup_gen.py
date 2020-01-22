import webbrowser
import random
import os, sys
import subprocess
from getch import pause
from ask_question import ask_question

print('~~~~ Scambaiting Popup Link Generator by nimaid ~~~~')
print('\n!!! ONLY USE THIS INSIDE A VIRTUAL MACHINE !!!')
print('!!! THESE LINKS MAY INSTALL MALWARE, USE WITH EXTREME CAUTION !!!')
print('\nMany of these links will not redirect to malicious websites unless you appear as a naive, vulnerable user.')
print('Because of this, all links will be opened with Internet Explorer. IE will be automatically closed before opening a link.')
print('You must also make sure your VPN is off, and that all web shields are turned off (client AND host machines).')
print('Additionally, a link may cycle through different re-directs, so it\'s worth trying each 2-3 times.')
print('\nIf you do find a live scam site, be warned that the original link may only re-direct to a malicious site a certain number of times before it will start re-directing to an innocuous site.')
print('If this happens to you, it will usually start redirecting to the scam site again after some time.')
print('Meanwhile, try the next link.')

print()
run_gen = ask_question(question='Do you wish to continue with opening malicious links?', default='N')
if run_gen == 'N':
    sys.exit('Exiting...')

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

# Get and randomize links from .txt file
scam_links_filename = os.path.join(PATH, 'scambait_megalist.txt')
with open(scam_links_filename, 'r') as f:
    read_links = f.read().splitlines()
scam_links = []
for link in read_links:
    link = link.strip()
    if link not in ['', None]:
        scam_links.append(link)
random.shuffle(scam_links)

# Use Internet Explorer to open links
ie = ie = webbrowser.get('C:\\Program Files\\Internet Explorer\\iexplore.exe')

devnull = open(os.devnull, 'w')
def close_all_ie():
    sts = subprocess.call('taskkill /F /IM iexplore.exe /T', shell=True, stdout=devnull, stderr=devnull)

# Loop through randomized links
for i, scam_link in enumerate(scam_links):
    scam_link = "http://" + scam_link
    print('')
    print('Opening link {}/{}: {}'.format(i+1, len(scam_links), scam_link))
    reopen = True;
    while reopen:
        close_all_ie()
        ie.open_new(scam_link)
        user_resp = ask_question(question='[R]e-open current link, [N]ext link, or [Q]uit?', options=['R','N','Q'], default='Q')
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
