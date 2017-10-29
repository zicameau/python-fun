# python-fun
[![Build Status](https://travis-ci.org/circa10a/python-fun.svg?branch=master)](https://travis-ci.org/circa10a/python-fun)

Just for fun

### link_tester
Crawls webpage, gathers all links, then performs `get` requests on said links.

### Usage

```
python python-fun/link-tester/link_test.py https://www.github.com
```
![alt text](https://i.imgur.com/210IEMg.png)

### ssh_executor
Runs command/script on remote host via ssh.

```
python python-fun/ssh-executor/ssh.py --help

usage: ssh.py [-h] -a ADDRESS -c COMMAND -k KEY -u USER

SSH Command Executor

optional arguments:
  -h, --help            show this help message and exit
  -a ADDRESS, --address ADDRESS
                        Remote Host Address
  -c COMMAND, --command COMMAND
                        Command To Execute, Wrap in quotes('') for commands
                        with multiple fields.
  -k KEY, --key KEY     Path To Key
  -u USER, --user USER  Remote User
 ```
 **Example**
 ```
 python python-fun/ssh-executor/ssh.py -a 165.227.90.238 -u root -k ~/.ssh/id_rsa -c uptime
 23:12:53 up  1:01,  0 users,  load average: 0.13, 0.05, 0.01
```
![alt text](https://i.imgur.com/Q21fDyH.png)

### ssh_executor (GUI)
Used Gooey module to create interface around `ssh-executor`
Works on:
  - MacOS
  - Windows

### Usage

```bash
python python-fun/ssh-executor/gui/ssh.py
```

![alt text](https://i.imgur.com/CNUyz2X.jpg)
![alt text](https://i.imgur.com/GrAet3P.jpg)

### http_code_checker
Tiny modules to validate URL strings and response codes. 
Mainly to test OO python.
#### Accepts URL as argument and returns http response code

1. `import lib.http_code` - `http_code.py` is a file in the `lib` subdirectory.
2. `http_code.check(site)` - is how you reference the class and function then pass a parameter. (`site = 'https://www.github.com'`)
3. `import lib.validate` - `validate.py` is a file in the `lib` subdirectory.
4. `validate.url(site)` - is how you reference the class and function then pass a parameter. (`site = 'https://www.github.com'`)

### Usage

```
python python-fun/http_code_checker/main.py https://www.google.com
```
![alt text](https://i.imgur.com/IGV5Fgt.png)
