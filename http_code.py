#!/usr/bin/env python
import requests
def check(url):
    try:
        r = requests.get(url)
        return(r.status_code)

    except requests.ConnectionError:
        print('failed to connect')

    except:
        print('unknown error')
