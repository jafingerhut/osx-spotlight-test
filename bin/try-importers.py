#! /usr/bin/env python3

import os, sys
import subprocess
import mdimporters


#debug = False
debug = True

######################################################################
# Parsing optional command line arguments
######################################################################

import argparse


filename = '/Users/jafinger/Downloads/new word.docx'
test_search_term = 'yarak'

#filename = '/Users/jafinger/Documents/gni-docs/huff_docs/doc/spec/huff_chipset_spec.doc'
#test_search_term = 'plesiochronous'

print("Filename: %s" % (filename))
print("test search term: %s" % (test_search_term))
print("")

mdimporter_lst = mdimporters.get_mdimporters()

if debug:
    n = 0
    for imp in mdimporter_lst:
        print('%3d %s' % (n, imp))
        n += 1

# Try doing 'mdimport -d4 -g <mdimporter_name> <filename>' for each
# mdimporter found.

for mdimporter in mdimporter_lst:
    mdimport_output = subprocess.check_output(['mdimport', '-d4',
                                               '-g', mdimporter,
                                               filename],
                                              stderr=subprocess.STDOUT)
    # Assume output of mdimport can be decoded as UTF-8
    mdimport_output = mdimport_output.decode("utf-8")
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
