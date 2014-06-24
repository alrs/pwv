#!/usr/bin/env python
#vim: set ft=python

import requests

EC2_META = {}

EC2_META_ROOT = "http://169.254.169.254/2014-02-25"
EC2_META_MAC_URL = "/".join([EC2_META_ROOT, "meta-data", "mac"])
EC2_META_VPC_URL_TEMPLATE = "/".join([  EC2_META_ROOT,
                                        "meta-data",
                                        "network",
                                        "interfaces",
                                        "macs",
                                        "{}",  # INTERPOLATED POSITION
                                        "vpc-id"])


def _metaget_mac():
    req = requests.get(EC2_META_MAC_URL)
    return req.text


def _metaget_vpcid(mac):
    uri = EC2_META_VPC_URL_TEMPLATE.format(mac)
    req = requests.get(uri)
    return req.text


def pwv():
    return _metaget_vpcid(_metaget_mac())


def main():
    print pwv()


if __name__ == "__main__":
    main()
