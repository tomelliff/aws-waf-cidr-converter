#!/usr/bin/env python
from __future__ import print_function
import argparse
from builtins import str
import ipaddress


def _generator_to_list(subnets_generator):
    """Returns list of string representations
    of each yielded item from the generator.
    """
    subnets = []
    for subnet in subnets_generator:
        subnets.append(str(subnet))
    return subnets


def get_allowed_prefixes(ip_version):
    allowed_ip4_prefixes = [8, 16, 24, 32]
    allowed_ip6_prefixes = [16, 24, 32, 56, 64, 128]
    if ip_version == 4:
        return allowed_ip4_prefixes
    elif ip_version == 6:
        return allowed_ip6_prefixes
    else:
        raise ValueError('ip_version should be either 4 or 6')


def converter(cidr_range):
    ip = ipaddress.ip_network(cidr_range, strict=False)
    allowed_prefixes = get_allowed_prefixes(ip.version)
    cidr_prefix = ip.prefixlen
    if cidr_prefix in allowed_prefixes:
        return [cidr_range]
    else:
        for prefix in allowed_prefixes:
            if cidr_prefix < prefix:
                return _generator_to_list(ip.subnets(new_prefix=prefix))


def command_line_handler():
    parser = argparse.ArgumentParser(
        description='Converts CIDR ranges into AWS WAF IP Set allowed ranges')
    parser.add_argument('cidr_range',
                        help='eg. 192.168.0.0/23')
    args = parser.parse_args()
    cidr_ranges = converter(str(args.cidr_range))
    for cidr_range in cidr_ranges:
        print(str(cidr_range))


if __name__ == '__main__':
    command_line_handler()
