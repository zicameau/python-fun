#!/usr/bin/env python
import sys
from termcolor import colored
from random import randint
#local modules in ./lib
import lib.http_code as http_code
import lib.validate as validate

def http(site):
    colors = ['red','yellow','green','blue','magenta','cyan']
    # -1 to get accurate count of array elements (0,5)
    num_colors = int(len(colors)) - 1
    #pick random number within length of array
    rand_color = colors[randint(0, num_colors)]
    #Validate argument starts with http or https from validate module
    validate.url(site)
    #Get response code from http_code module
    response = http_code.check(site)
    #print response code and color output depending if successful or not
    if response == 200:
        print colored(response, 'green'),
        # Print random color check mark for kicks
        print colored(u'\u2713', rand_color)
    else:
        print colored(response, 'red')

if __name__ == "__main__":
    try:
        site = sys.argv[1]
    except IndexError:
        print colored('no site argument passed e.g. https://google.com', 'red')
        sys.exit(1)
    try:
        http(site)
    except KeyboardInterrupt:
        print colored('Interrupted, bye.', 'red')
