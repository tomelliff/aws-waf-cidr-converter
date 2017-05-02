# AWS WAF CIDR converter

[![Build Status](https://travis-ci.org/tomelliff/aws-waf-cidr-converter.svg?branch=master)](https://travis-ci.org/tomelliff/aws-waf-cidr-converter) [![Coverage Status](https://coveralls.io/repos/github/tomelliff/aws-waf-cidr-converter/badge.svg?branch=master)](https://coveralls.io/github/tomelliff/aws-waf-cidr-converter?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5b28add6f9f84c728cbc01908f80dc81)](https://www.codacy.com/app/tomelliff/aws-waf-cidr-converter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tomelliff/aws-waf-cidr-converter&amp;utm_campaign=Badge_Grade)

Conversion between typical CIDR ranges and the [ranges allowed by AWS WAF](http://docs.aws.amazon.com/waf/latest/developerguide/web-acl-ip-conditions.html):

> AWS WAF supports /8, /16, /24, and /32 IPv4 address ranges and /16, /24, /32, /56, /64, and /128 IPv6 address ranges

## Usage

```sh
$ ./converter.py -h
usage: converter.py [-h] cidr_range

Converts CIDR ranges into AWS WAF IP Set allowed ranges

positional arguments:
  cidr_range  eg. 192.168.0.0/23

optional arguments:
  -h, --help  show this help message and exit

$ ./converter.py 192.168.0.0/23
192.168.0.0/24
192.168.1.0/24
```

### Requirements

Supports both Python 2.7 and 3.6 (others may run but no tests are ran against them).

For Python2 you will need to install some dependencies:
```sh
pip install -r requirements.txt
```

These are backported modules from Python3's Standard Library so Python3 has no such dependencies.

## Contributing

### Running the tests

To run all the tests for both Python2.7 and 3.6 just run:

```sh
tox
```

Obviously you will need [`tox`](https://pypi.python.org/pypi/tox) available but this will install all dependencies for each environment in a virtual environment.

There is a [pre-commit hook](https://github.com/tomelliff/aws-waf-cidr-converter/blob/master/pre-commit) available that will automatically run the tests for you. Simply copy it into your `.git/hooks` folder to install it:

```sh
cp pre-commit .git/hooks/
```
