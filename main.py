#!/usr/bin/env python
import sys,http_code,validate
from termcolor import colored

def main():
    #Validate argument is passed to script
    try:
        site = sys.argv[1]
    except:
        print colored('no site argument passed e.g. https://google.com', 'red')
        exit(1)
    #Validate argument starts with http or https from valid_url module
    validate.url(site)

    #Check response code from http module
    response = http_code.check(site)

    #print response code and color output depending if successful or not
    if (response == 200):
        print colored(response, 'green')
    else:
        print colored(response, 'red')

if __name__ == "__main__":
    main()
