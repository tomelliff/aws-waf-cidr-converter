#!/usr/bin/env python
import netaddr


def _generator_to_list(subnets_generator):
    """Returns list of string representations
    of each yielded item from the generator.
    """
    subnets = []
    for subnet in subnets_generator:
        subnets.append(str(subnet))
    return subnets


def converter(cidr_range):
    allowed_prefixes = [8, 16, 24, 32]
    ip = netaddr.IPNetwork(cidr_range)
    cidr_prefix = ip.prefixlen
    if cidr_prefix in allowed_prefixes:
        return [cidr_range]
    else:
        for prefix in allowed_prefixes:
            if cidr_prefix < prefix:
                return _generator_to_list(ip.subnet(prefix))
