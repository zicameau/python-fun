#!/usr/bin/env python
import sys,http_code
try:
    site = sys.argv[1]
    response = http_code.check(site)
    print(response)
except:
    print('no site argument passed')
