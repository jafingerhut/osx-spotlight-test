#! /usr/bin/env python

from __future__ import print_function
import os, sys
import subprocess
import time

import mdimporters
import snapshot

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
            with open(fullname) as f:
                print(f.read())
