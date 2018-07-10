#! /usr/bin/env python

from __future__ import print_function
import os, sys
import subprocess
import time

import mdimporters
import snapshot

def file_type_from_file_cmd(filename):
    cmd_lst = ['file', '--brief', filename]
    output = subprocess.check_output(cmd_lst)
    output = output.decode("utf-8")
    return output.strip(), cmd_lst


def binary_plist_converted_to_xml(filename):
    # With these command line options, plutil should leave the
    # original file unchanged, and print to its stdout the contents of
    # the plist file converted to XML format.
    cmd_lst = ['plutil', '-convert', 'xml1', '-o', '-', filename]
    output = subprocess.check_output(cmd_lst)
    output = output.decode("utf-8")
    return output


mdimporter_lst = sorted(mdimporters.get_mdimporters('all'))

for m in mdimporter_lst:
    #print("type(sys.stdout)='%s'" % (type(sys.stdout)))
    print("")
    print("------------------------------------------------------------")
    print(m)
    print("")
    snapshot.recursive_dir_snapshot(m, sys.stdout)
    w = list(os.walk(m + '/Contents'))
    dir, subdirs, normal_fnames = w[0]
    #print("dbg normal_fnames='%s'" % (normal_fnames))
    for x in normal_fnames:
        if x[-6:] == '.plist':
            fullname = os.path.join(dir, x)
            print("")
            print(fullname)
            print("")
            file_type, cmd_lst = file_type_from_file_cmd(fullname)
            print("$ %s" % (' '.join(cmd_lst)))
            print(file_type)
            print("")
            if file_type == "Apple binary property list":
                text = binary_plist_converted_to_xml(fullname)
                print(text)
            else:
                with open(fullname) as f:
                    print(f.read())
