import sys
from termcolor import colored
def url(url):
    if url.startswith('http://') or url.startswith('https://'):
        pass
    else:
        print colored('invalid URL passed as arg. (Does not start with http/https)', 'red')
        sys.exit(1)
