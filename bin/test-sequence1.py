#! /usr/bin/env python

from __future__ import print_function
import json
import os
import subprocess
import sys
import time

import mdimporters


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
    print("%d sec after %s, mdfind '%s' found %d match(es)"
          "" % (pause_duration_sec, msg, search_term, len(filtered_filenames)))
    return filtered_filenames


def print_mdimport_results(info):
    print("    filename       : %s" % (info['filename']))
    print("    type (UTI)     : %s" % (info['uti']))
    print("    mdimporter used: %s" % (info['mdimporter']))


def mdimport(msg, filename, mdimporter_choice):
    info = mdimporters.do_mdimport(filename, mdimporter_choice)
    print(msg)
    print_mdimport_results(info)
    assert filename in info['filename']
    return info



pause_duration_sec = 10
apple_ms_mdimporter = '/Library/Spotlight/Microsoft Office.mdimporter'
dir_name = "osx-spotlight-test-files"
github_repo = "https://github.com/jafingerhut/" + dir_name

filename = dir_name + "/MS-Word-for-Mac-version-16.9-Word-Document-docx.docx"
# Note: The search term is stored separately as 'search_term_part1'
# and 'search_term_part2' so that searching for the term will not find
# the file containing this program.
search_term_part1 = "vorkon"
search_term_part2 = "inkawu"
search_term = search_term_part1 + search_term_part2

output_dir_name = "test-sequence1-out"
delete_dir(output_dir_name)
os.mkdir(output_dir_name)


for pass_num in [1, 2, 3, 4, 5]:
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

    print("")
    print("----------------------------------------")
    print("Start pass #%d" % (pass_num))

    delete_dir(dir_name)
    output = subprocess.check_output(['git', 'clone', github_repo])
    # Don't bother checking the output.  Hopefully if there is something
    # bad enough that the command above gives a non-0 exit status, it will
    # abort this program.
    do_search(search_term, filename, pause_duration_sec, "'git clone'",
              output_dir_name +
              ("/pass-%d-mdls-after-git-clone.txt" % (pass_num)))

    i = 0
    for m in mdimporter_sequence:
        i += 1
        mdimport("mdimport #%d complete:" % (i), filename, m)
        do_search(search_term, filename, pause_duration_sec,
                  "mdimport #%d" % (i),
                  output_dir_name +
                  ("/pass-%d-mdls-after-mdimport-%d.txt"
                   "" % (pass_num, i)))
