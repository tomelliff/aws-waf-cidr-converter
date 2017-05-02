# CIDR -> Classful range converter

[![Build Status](https://travis-ci.org/tomelliff/cidr-classful-converter.svg?branch=master)](https://travis-ci.org/tomelliff/cidr-classful-converter) [![Coverage Status](https://coveralls.io/repos/github/tomelliff/cidr-classful-converter/badge.svg?branch=master)](https://coveralls.io/github/tomelliff/cidr-classful-converter?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5d6cb0375a2544dd90bdb215f0fecf54)](https://www.codacy.com/app/tomelliff/cidr-classful-converter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tomelliff/cidr-classful-converter&amp;utm_campaign=Badge_Grade)

Convert between [CIDR ranges](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) and [Classful ranges](https://en.wikipedia.org/wiki/Classful_network).

Main aim is to allow conversion between typical CIDR ranges and the [ranges allowed by AWS WAF](http://docs.aws.amazon.com/waf/latest/developerguide/web-acl-ip-conditions.html):

> AWS WAF supports /8, /16, /24, and /32 IPv4 address ranges and /16, /24, /32, /56, /64, and /128 IPv6 address ranges
