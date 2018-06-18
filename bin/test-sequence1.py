#! /usr/bin/env python

from __future__ import print_function
import json
import subprocess
import sys
import time

import mdimporters


def print_mdimport_results(info):
    print("    filename       : %s" % (info['filename']))
    print("    type (UTI)     : %s" % (info['uti']))
    print("    mdimporter used: %s" % (info['mdimporter']))

    
# Note: The search term is stored separately as 'search_term_part1'
# and 'search_term_part2' so that searching for the term will not find
# the file containing this program.

search_term_part1 = "vorkon"
search_term_part2 = "inkawu"
search_term = search_term_part1 + search_term_part2

apple_ms_mdimporter = '/Library/Spotlight/Microsoft Office.mdimporter'

github_repo = "https://github.com/jafingerhut/osx-spotlight-test-files"
filename = "osx-spotlight-test-files/MS-Word-for-Mac-version-16.9-Word-Document-docx.docx"

output = subprocess.check_output(['git', 'clone', github_repo])

# Don't bother checking the output.  Hopefully if there is something
# bad enough that the command above gives a non-0 exit status, it will
# abort this program.

found_filenames = mdimporters.mdfind_search_results(search_term)
filtered_filenames = [x for x in found_filenames if filename in x]
assert len(filtered_filenames) == 0
print("Immediately after 'git clone', mdfind of term '%s' found no match"
      "" % (search_term))

info1 = mdimporters.do_mdimport(filename, None)
print("mdimport #1 complete:")
print_mdimport_results(info1)
assert filename in info1['filename']
time.sleep(5)

found_filenames = mdimporters.mdfind_search_results(search_term)
filtered_filenames = [x for x in found_filenames if filename in x]
assert len(filtered_filenames) == 1
print("After mdimport #1, mdfind of term '%s' found the file"
      "" % (search_term))

info2 = mdimporters.do_mdimport(filename, apple_ms_mdimporter)
print("mdimport #2 complete:")
print_mdimport_results(info2)
assert filename in info2['filename']
time.sleep(5)

found_filenames = mdimporters.mdfind_search_results(search_term)
filtered_filenames = [x for x in found_filenames if filename in x]
if len(filtered_filenames) == 0:
    print("After mdimport #2, mdfind of term '%s' _no longer_ found the file"
          "" % (search_term))
    print("This seems undesirable from the perspective of Apple's Microsoft file mdimporter not working as well as one would hope, but maybe expected for some reason.")
else:
    print("After mdimport #2, mdfind of term '%s' still found the file"
          "" % (search_term))
    print("This seems odd, but not necessarily undesirable.")
    assert len(filtered_filenames) == 1

info3 = mdimporters.do_mdimport(filename, None)
print("mdimport #3 complete:")
print_mdimport_results(info3)
assert filename in info3['filename']
time.sleep(5)

found_filenames = mdimporters.mdfind_search_results(search_term)
filtered_filenames = [x for x in found_filenames if filename in x]
assert len(filtered_filenames) == 1
if len(filtered_filenames) == 0:
    print("After mdimport #3, mdfind of term '%s' _no longer_ found the file"
          "" % (search_term))
    print("This seems like some kind of bug")
else:
    print("After mdimport #3, mdfind of term '%s' found the file"
          "" % (search_term))
    print("That looks correct")
    assert len(filtered_filenames) == 1
