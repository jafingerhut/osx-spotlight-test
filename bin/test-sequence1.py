#! /usr/bin/env python

from __future__ import print_function
import argparse
import json
import os
import subprocess
import sys
import time

import mdimporters


pause_duration_sec = 10
apple_ms_mdimporter = '/Library/Spotlight/Microsoft Office.mdimporter'
dir_name = "osx-spotlight-test-files"
github_repo = "https://github.com/jafingerhut/" + dir_name


parser = argparse.ArgumentParser(description="""
Try a sequence of 'git clone', mdimport, and mdfind commands on a
selected file, to see how that sequence effects the search results.""")
parser.add_argument('-f', '--file', dest='file',
                    choices=['word-2016-mac-docx',
                             'word-2016-mac-doc'],
                    help="""Specify which file to use in the test.""")
parser.add_argument('-a', '--arch', dest='arch', type=str,
                    help="""Use 'arch <arch>' before mdimport command.
                    Required for my OS X 10.6.8 machine which is
                    64-bit Intel, but Microsoft mdimporter only has
                    32-bit Intel and PowerPC binaries, so you must use
                    options '--arch i386'.""")

args = parser.parse_known_args()[0]

# Note: The search term is written in this code as multiple shorter
# strings that are then concatenated together, so that searching for
# the term will not find the file containing this program.

if args.file is None:
    print("Must specify -f / --file option")
    sys.exit(1)

if args.file == 'word-2016-mac-docx':
    filename = "MS-Word-for-Mac-version-16.9-Word-Document-docx.docx"
    search_term = "vorkon" + "inkawu"
elif args.file == 'word-2016-mac-doc':
    filename = "MS-Word-for-Mac-version-16.9-Word-97-2004-Document-doc.doc"
    search_term = "lowhux" + "owaachii"

filename = os.path.join(dir_name, filename)


def delete_dir(dir_name):
    subprocess.check_output(['/bin/rm', '-fr', dir_name])


def pause(duration_seconds):
    print("Pausing %d seconds..." "" % (duration_seconds))
    time.sleep(duration_seconds)


def record_mdls_out(output_file_name, filename):
    out = subprocess.check_output(['mdls', filename], stderr=subprocess.STDOUT)
    with open(output_file_name, 'w') as f:
        print(out, file=f)


def do_search(search_term, filename, pause_duration_sec, msg,
              mdls_output_filename):
    pause(pause_duration_sec)
    record_mdls_out(mdls_output_filename, filename)
    found_filenames = mdimporters.mdfind_search_results(search_term)
    filtered_filenames = [x for x in found_filenames if filename in x]
    print("%d sec after %s, mdfind '%s' + '%s' found %d match(es)"
          "" % (pause_duration_sec, msg, search_term[0:6], search_term[6:],
                len(filtered_filenames)))
    return filtered_filenames


def print_mdimport_results(info):
    print("    filename       : %s" % (info['filename']))
    print("    type (UTI)     : %s" % (info['uti']))
    print("    mdimporter used: %s" % (info['mdimporter']))


def mdimport(msg, filename, mdimporter_choice):
    info = mdimporters.do_mdimport(filename, mdimporter_choice, args.arch)
    print(msg)
    print_mdimport_results(info)
    assert filename in info['filename']
    return info




output_dir_name = "test-sequence1-out"
delete_dir(output_dir_name)
os.mkdir(output_dir_name)


for pass_num in [1, 2, 3, 4, 5, 6]:
    if pass_num == 1:
        mdimporter_sequence = [None, apple_ms_mdimporter, None]
    elif pass_num == 2:
        mdimporter_sequence = [None, apple_ms_mdimporter, apple_ms_mdimporter,
                               None]
    elif pass_num == 3:
        mdimporter_sequence = [None, apple_ms_mdimporter, None,
                               apple_ms_mdimporter, None]
    elif pass_num == 4:
        mdimporter_sequence = [apple_ms_mdimporter, None,
                               apple_ms_mdimporter, None]
    elif pass_num == 5:
        mdimporter_sequence = [apple_ms_mdimporter, None,
                               apple_ms_mdimporter, None,
                               apple_ms_mdimporter, None]
    elif pass_num == 6:
        mdimporter_sequence = [None, None, None, None, None, None]

    print("")
    print("----------------------------------------")
    print("Start pass #%d" % (pass_num))

    delete_dir(dir_name)
    output = subprocess.check_output(['git', 'clone', github_repo])
    # Don't bother checking the output.  Hopefully if there is something
    # bad enough that the command above gives a non-0 exit status, it will
    # abort this program.

    # I do not know how to check whether all of a certain set of
    # recently created files are complete in their addition to the
    # Spotlight indexes.  I would be interested in knowing how to do
    # that, if it is reasonably straightforward.

    # So far I have occasionally seen different search success/fail
    # results 10 seconds after doing 'git clone' on my
    # osx-spotlight-test-files repository.  My guess is that this is
    # because sometimes it is done indexing those files, vs. sometimes
    # it is not yet done.  The other most likely explanation is that
    # the indexing process was done in both cases, but the results of
    # that indexing were different after different 'git clone'
    # operations, which is more disturbing.

    # For now, allow more time after the 'git clone' before starting
    # to run 'mdimport' commands that might change the index, to see
    # if the search results become more consistent across runs by
    # waiting longer.
    i = 0
    for tries in range(10):
        i += 1
        do_search(search_term, filename, pause_duration_sec,
                  ("'git clone' #%d" % (i)),
                  os.path.join(output_dir_name,
                               ("pass-%d-mdls-%d-after-git-clone.txt"
                                "" % (pass_num, i))))
    i = 0
    for m in mdimporter_sequence:
        i += 1
        mdimport("mdimport #%d complete:" % (i), filename, m)
        do_search(search_term, filename, pause_duration_sec,
                  "mdimport #%d" % (i),
                  os.path.join(output_dir_name,
                               ("pass-%d-mdls-after-mdimport-%d.txt"
                                "" % (pass_num, i))))
