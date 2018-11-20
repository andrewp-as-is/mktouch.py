[![](https://img.shields.io/pypi/pyversions/mktouch.svg?longCache=True)](https://pypi.org/pypi/mktouch/)
[![](https://img.shields.io/pypi/v/mktouch.svg?maxAge=3600)](https://pypi.org/pypi/mktouch/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mktouch.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mktouch.py/)

#### Install
```bash
$ [sudo] pip install mktouch
```

#### Functions
function|description
-|-
`mktouch.mktouch(path)`|mkdir + touch

#### Examples
```python
>>> import mktouch
>>> mktouch.mktouch("folder/file")
>>> mktouch.mktouch(["folder/file1","folder/file2"])
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>