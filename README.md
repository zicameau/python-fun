# python-fun
Just for fun

## Usage

### link_tester
Crawls webpage, gathers all links, then performs `get` requests on said links.

```
python link_test.py https://www.github.com
```
![alt text](https://i.imgur.com/210IEMg.png)

### http_code_checker
Mainly to test OO python
##### Accepts URL as argument and returns http response code
Tiny modules to validue URL strings and response codes. (OOP)

1. `import lib.http_code` - `http_code.py` is a file in the `lib` subdirectory.
2. `http_code.check(site)` - is how you reference the class and function then pass a parameter. (`site = 'https://www.github.com'`)
3. `import lib.validate` - `validate.py` is a file in the `lib` subdirectory.
4. `validate.url(site)` - is how you reference the class and function then pass a parameter. (`site = 'https://www.github.com'`)

```
python main.py https://www.google.com
```
![alt text](https://i.imgur.com/IGV5Fgt.png)
