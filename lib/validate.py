from termcolor import colored
def url(url):
#Validate argument starts with http or https
    if url[:7] == 'http://':
        pass
    elif url[:8] == 'https://':
        pass
    else:
        print colored('invalid URL passed as arg.', 'red')
        exit(1)
