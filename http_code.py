#!/usr/bin/env python
import requests
from termcolor import colored
def check(url):
    try:
        r = requests.get(url, allow_redirects=False)
        return(r.status_code)

    except requests.ConnectionError:
        print colored('failed to connect', 'red')

    except:
        print colored('unknown error', 'red')
