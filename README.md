<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/mktouch.svg?longCache=True)](https://pypi.org/project/mktouch/)
[![](https://img.shields.io/pypi/v/mktouch.svg?maxAge=3600)](https://pypi.org/project/mktouch/)
[![](https://img.shields.io/npm/v/mktouch.svg?maxAge=3600)](https://www.npmjs.com/package/mktouch)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mktouch.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mktouch.py/)

#### Installation
```bash
$ [sudo] npm i -g mktouch
```
```bash
$ [sudo] pip install mktouch
```

#### Functions
function|`__doc__`
-|-
`mktouch.mktouch(path)` |mkdir + touch

#### Examples
```python
>>> import mktouch
>>> mktouch.mktouch("folder/file")
>>> mktouch.mktouch(["folder/file1","folder/file2"])
```

```bash
$ mktouch /tmp/not-existing-dir/file
$ ls /tmp/not-existing-dir/file
/tmp/not-existing-dir/file
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>