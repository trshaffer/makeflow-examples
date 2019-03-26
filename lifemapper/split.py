#!/usr/bin/env python

import itertools
import argparse
import json
import csv
import sys
import os
import re

from pprint import pprint

from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: list(islice(it, size)), [])

POINTS_THRESHOLD = 3
CHUNK_SIZE = 50

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            'This script generates makeflows to process the input data')
    parser.add_argument('points_csv', type=str,
            help='A CSV file containing occurrence information. ' \
            + 'Like taxa should be in consecutive rows.')
    args = parser.parse_args()

    taxa_names = []

    with open(args.points_csv) as in_f:
        lines = csv.reader(in_f)
        taxa = itertools.groupby(lines, lambda x: x[13])
        for taxon, lines in taxa:
            name = re.sub('\s', '_', re.split('[^\w\s]', taxon)[0].strip())
            c = list(lines)
            if len(c) < POINTS_THRESHOLD:
                continue
            flat_fn = 'points_%s.csv' % name
            taxa_names.append(name)
            with open(flat_fn, 'w') as out_f:
                out = csv.writer(out_f)
                for l in c:
                    out.writerow([name] + l[14:16])

    json.dump(
        {
            "TAXA": taxa_names,
            "CHUNKS": list(chunk(taxa_names, CHUNK_SIZE)),
        }, sys.stdout, indent=2)
