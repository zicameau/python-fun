# python-fun
Just for fun

## Usage

### link_tester
Crawls webpage, gathers all links, then performs `get` requests on said links.

```
python main.py https://www.github.com
```

### http_code_checker
##### Accepts URL as argument and returns http response code
1. `./lib/__init__.py` - Tells the interpreter to look for files as modules.
2. `import lib.http_code` - `http_code.py` is a file in the `lib` subdirectory.
3. `http_code.check(site)` - is how to you reference the class, then the method, then pass a parameter. (`site = 'https://www.github.com'`)
4. `import lib.validate` - `validate.py` is a file in the `lib` subdirectory.
5. `validate.url(site)` - is how to you reference the class, then the method, then pass a parameter. (`site = 'https://www.github.com'`)

```
python main.py https://www.google.com
```
![alt text](https://i.imgur.com/IGV5Fgt.png)
