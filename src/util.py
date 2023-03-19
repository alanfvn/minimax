import platform
import time
from os import system

def delay(secs):
    time.sleep(secs)

def clean():
    """
    Clears the console
    """
    os = platform.system().lower()
    if 'windows' in os:
        system('cls')
    else:
        system('clear')

def ask_question(prompt, options):
    answer = ''
    opts = [x.upper() for x in options]
    while answer not in opts:
        try:
            answer = input(prompt).upper()
        except (EOFError, KeyboardInterrupt):
            exit()
    return answer
