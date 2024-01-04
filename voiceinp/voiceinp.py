import time
import subprocess

def voiceinp():
    print('listining')
    query = subprocess.getoutput("termux-speech-to-text")
    time.sleep(2)
    return query