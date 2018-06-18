#! /usr/bin/env python

from __future__ import print_function
import os, sys
import subprocess
import time

import mdimporters


#debug = False
debug = True

######################################################################
# Parsing optional command line arguments
######################################################################

import argparse

parser = argparse.ArgumentParser(description="""
Try importing a file into Spotlight with the default, and some or all
of the mdimporters installed on an OS X system, to see if there is any
difference in the mdfind search results afterwards.""")
parser.add_argument('-i', '--importers', dest='importers',
                    choices=['all', 'ms'],
                    help="""
                    If 'all' is specified (the default if this option
                    is not specified), then try all importers.  If
                    'ms' is specified, only try the RichText importer,
                    and ones with 'Microsoft' in their name.
                    """)
args = parser.parse_known_args()[0]

if args.importers is None:
    args.importers = 'all'


filename = 'osx-spotlight-test-files/MS-Word-for-Mac-version-16.9-Word-Document-docx.docx'
test_search_term = 'vorkon' + 'inkawu'

print("Filename: %s" % (filename))
print("Filename: %s" % (filename), file=sys.stderr)
print("test search term: %s" % (test_search_term))
print("test search term: %s" % (test_search_term), file=sys.stderr)
print("")

mdimporter_lst = mdimporters.get_mdimporters(args.importers)

if debug:
    n = 0
    for imp in mdimporter_lst:
        print('%3d %s' % (n, imp))
        n += 1

# Try doing 'mdimport -d4 -g <mdimporter_name> <filename>' for each
# mdimporter found, and also once without specifying an mdimporter, to
# see what Spotlight uses in that case.

for mdimporter in ['(default)'] + mdimporter_lst:
    args_part1 = ['mdimport', '-d4']
    if mdimporter == '(default)':
        args_part2 = []
    else:
        args_part2 = ['-g', mdimporter]
    args_part3 = [filename]
    all_args = args_part1 + args_part2 + args_part3
    mdimport_output = subprocess.check_output(all_args,
                                              stderr=subprocess.STDOUT)
    # Assume output of mdimport can be decoded as UTF-8
    mdimport_output = mdimport_output.decode("utf-8")

    # Try waiting 1 second after mdimport to see if it makes 'mdfind'
    # output more repeatable.
    time.sleep(1)

    # See whether 'mdfind <test_search_term>' output includes the file name
    found_filenames = mdimporters.mdfind_search_results(test_search_term)
    hits = [x for x in found_filenames if filename in x]

    print("")
    print("----------------------------------------------------------------------")
    print("mdimporter: %s" % (mdimporter))
    if len(hits) == 0:
        print("No files found from 'mdfind'")
    else:
        print("%d files found from 'mdfind':" % (len(hits)))
    for x in hits:
        print(x)
    print("mdimport output:")
    print(mdimport_output)
    print("mdimporter: %s -> %d hits" % (mdimporter, len(hits)),
          file=sys.stderr)
