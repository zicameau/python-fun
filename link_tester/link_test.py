#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests, sys
from termcolor import colored

def check_protocol(site): #Validate argument starts with http or https
    return site.startswith('http://') or site.startswith('https://')

def print_response(response, link):
    color = 'green' if response == 200 else 'red'
    print colored('[' + str(response) + ']', color), link

def test_links(site):
    try:
        r  = requests.get(site)
    except requests.ConnectionError:
        print colored('Unable to Connect' , 'red')
        sys.exit(1)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a'):
        link=str(link.get('href'))
        if check_protocol(link):
            response=requests.get(link)
            print_response(response.status_code, link)

if __name__ == '__main__':
    try:
        site = str(sys.argv[1])
        if not check_protocol(site):
            print colored('invalid URL passed as arg. (Does not start with http/https)', 'red')
            sys.exit(1)
        try:
            test_links(site)
        except KeyboardInterrupt:
            print colored('Interrupted, bye.', 'red')
    except IndexError:
        print colored('no site argument passed e.g. https://google.com', 'red')
        sys.exit(1)
