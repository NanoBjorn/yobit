# Python YoBit Binding
[![Travis](https://img.shields.io/travis/Mambix/yobit.svg)](https://travis-ci.org/Mambix/yobit)
[![Coverage Status](https://coveralls.io/repos/github/Mambix/yobit/badge.svg?branch=master)](https://coveralls.io/github/Mambix/yobit?branch=master)
[![PyPI](https://img.shields.io/pypi/v/yobit.svg)](https://pypi.python.org/pypi/yobit)  

Python binding for YoBit. Use at your own risk!

This has been forked from https://githun.com/NanoBjorn/yobit for the purpose of making it a PyPi package so it can be easily installed with python pip tool. For the purpose of publishing it to PyPi author agreed to flag it with MIT license.

# Installation

Clone the repository:  
`git clone https://github.com/Mambix/yobit.git`

In the cloned directory install with setup.py:  
`python setup.py install`

Or you can install with pip directly running:  
`pip install yobit`

# Usage
Get information about user balances and API permissions:
```Python
from YoBit import YoBit

yb = YoBit(api_key='YOUR_API_KEY', api_secret='YOUR_API_SECRET')
yb.get_info()
```

# Original author contributions

Tips to NanoBjorn can be send here BTC: 3NoXpUm2EeUWc1jJQhi5X7xKsneN9ReEpQ  
All the comments and descriptions are at [offical YoBit API page](https://yobit.net/en/api) and in the code.

# ToDO list
* Automated tests
* TravisCI
* Coveralls
* Automatic publish to PyPi?

# Issues
If you encounter any issues with the use of this python library please open a new issue in this repository and provide as much details as possible so we can quickly reproduce and resolve the issue.
