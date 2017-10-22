#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests, sys
from termcolor import colored

def check_protocol(site): #Validate argument starts with http or https
    return bool(__import__('re').search('^http(|s):\/\/', site))

def check_response(response, link):
    if response == '[200]':
        print colored(response, 'green'), link
    else:
        print colored(response, 'red'), link

def test_links(site):
    try:
        r  = requests.get(site)
    except requests.ConnectionError:
        print colored('Unable to Connect' , 'red')
        sys.exit(1)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a'):
        link=str(link.get('href'))
        if check_protocol(link):
            response=(str(requests.get(link)).split()[1].replace('>',''))
            check_response(response, link)
        else:
            pass

if __name__ == "__main__":
    try:
        site = str(sys.argv[1])
        if not check_protocol(site):
            print colored('invalid URL passed as arg.', 'red')
            sys.exit(1)
        try:
            test_links(site)
        except KeyboardInterrupt:
            print colored('Interrupted, bye.', 'red')
    except IndexError:
        print colored('no site argument passed e.g. https://google.com', 'red')
        sys.exit(1)
