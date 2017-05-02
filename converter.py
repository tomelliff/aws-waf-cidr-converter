#!/usr/bin/env python
import netaddr


def converter(cidr_range):
    allowed_prefixes = [8, 16, 24, 32]
    ip = netaddr.IPNetwork(cidr_range)
    cidr_prefix = ip.prefixlen
    if cidr_prefix in allowed_prefixes:
        return [cidr_range]
    else:
        for prefix in allowed_prefixes:
            if cidr_prefix < prefix:
                subnets = []
                for subnet in ip.subnet(prefix):
                    subnets.append(str(subnet))
                return subnets
