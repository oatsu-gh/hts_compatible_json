#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) 2020 oatsu
"""
about module
"""
from os.path import basename, splitext

import hts2json


def main():
    path_lab = input('path_lab: ').strip('"')
    path_json = splitext(basename(path_lab))[0] + '.json'
    hts2json.hts2json(path_lab, path_json)


if __name__ == '__main__':
    main()
