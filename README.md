# Tornado ApiDoc

Tornado ApiDoc is a simple apidoc serving plugin for tornado inspired by flask-apidoc.

## Installation

```
$ pip install tornado-apidoc
```

## Usage

```python
import tornado.web
from tornado_apidoc import make_apidoc_route

application = tornado.web.Application([
    make_apidoc_route(folder_path='./static',
                      url_path='/docs')
])
```

## Example

```
$ git clone https://github.com/wenhan-wu/tornado-apidoc
$ cd tornado-apidoc
$ apidoc -i . -o ./static -f .py
$ python example.py
```

open [http://localhost:5000/docs](http://localhost:5000/docs) in your browser.