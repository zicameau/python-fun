#!/usr/bin/env python
import sys
from termcolor import colored
from random import randint
#local modules in ./lib
import lib.http_code as http_code
import lib.validate as validate



def main():
    colors = ['red','yellow','green','blue','magenta','cyan']
    # -1 to get accurate count of array elements (0,5)
    num_colors = int(len(colors)) - 1
    #pick random number within length of array
    rand_color = colors[randint(0, num_colors)]

    #Validate argument is passed to script
    try:
        site = sys.argv[1]
    except:
        print colored('no site argument passed e.g. https://google.com', 'red')
        sys.exit(1)

    #Validate argument starts with http or https from valid_url module
    validate.url(site)

    #Check response code from http module
    response = http_code.check(site)

    #print response code and color output depending if successful or not
    if response == 200:
        print colored(response, 'green'),
        # Print random color check mark for kicks
        print colored(u'\u2713', rand_color)
    else:
        print colored(response, 'red')

if __name__ == "__main__":
    main()
