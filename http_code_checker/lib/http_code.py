#!/usr/bin/env python
import requests, sys
from termcolor import colored
def check(url):
    try:
        r = requests.get(url, allow_redirects=False)
        return(r.status_code)

    except requests.exceptions.SSLError:
        print colored('SSL Error, try using http instead.' , 'red')
        sys.exit(1)

    except requests.ConnectionError:
        print colored('failed to connect', 'red')
        sys.exit(1)

    except:
        print colored('unknown error', 'red')
        sys.exit(1)
