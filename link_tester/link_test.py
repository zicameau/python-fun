from bs4 import BeautifulSoup
import requests, sys
from termcolor import colored

def main():
    try:
        site = sys.argv[1]
    except:
        print colored('no site argument passed e.g. https://google.com', 'red')
        sys.exit(1)

    #Validate argument starts with http or https
    if site[:7] == 'http://':
        pass
    elif site[:8] == 'https://':
        pass
    else:
        print colored('invalid URL passed as arg.', 'red')
        exit(1)

    r  = requests.get(site)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    for link in soup.find_all('a'):
        usable_link=str(link.get('href'))

        if usable_link[:7] == 'http://':
            response=(str(requests.get(usable_link)).split()[1].replace('>',''))

            if response == '[200]':
                print colored(response, 'green'), usable_link

            else:
                print colored(response, 'red'), usable_link

        elif usable_link[:8] == 'https://':
            response=(str(requests.get(usable_link)).split()[1].replace('>',''))

            if response == '[200]':
                print colored(response, 'green'), usable_link
            else:
                print colored(response, 'red'), usable_link

        else:
            pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print colored('Interrupted, bye.', 'red')
