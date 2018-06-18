import re
import subprocess
import sys


def get_mdimporters(desired_importers):
    assert desired_importers in ['all', 'ms']
    output = subprocess.check_output(['mdimport', '-L'],
                                     stderr=subprocess.STDOUT)
    # Assume output of mdimport can be decoded as UTF-8
    output = output.decode("utf-8")
    
    lines = output.splitlines()
    # Remove first and last lines if they have expected contents
    if len(lines) < 2:
        print("Expected at least 2 lines of output from 'mdimport -L' command, but found %d lines instead:" % (len(lines)))
        print(output)
        sys.exit(1)

    match = re.match(r"""(?x)
                         ^.* mdimport
                          .* \s Paths:
                          .* \s \($""", lines[0])
    if not match:
        print("Expected first line of output from 'mdimport -L' command to contain 'mdimport' 'Paths:' and end with left paren, but found this instead:")
        print(lines[0])
        sys.exit(1)

    match = re.match(r"""^\s*\)\s*$""", lines[-1])
    if not match:
        print("Expected last line of output from 'mdimport -L' command to contain only a right paren, but found this instead:")
        print(lines[-1])
        sys.exit(1)


    # Remove first and last lines, and check the remaining ones
    lines = lines[1:-1]
    mdimporter_lst = []
    for line in lines:
        match = re.match(r"""^\s*"(.+)",?$""", line)
        if not match:
            print("Expected line of output from 'mdimport -L' command to contain only a file name enclosed in double quotes, optionally followed by a comma, but found this instead:")
            print(line)
            sys.exit(1)
        mdimporter_name = match.group(1)
        mdimporter_lst.append(mdimporter_name)

    if desired_importers == 'ms':
        mdimporter_lst = [x for x in mdimporter_lst
                          if ('RichText' in x or 'Microsoft' in x)]
    return mdimporter_lst


def mdfind_search_results(test_search_term):
    output = subprocess.check_output(['mdfind', test_search_term])
    # Assume output of mdimport can be decoded as UTF-8
    output = output.decode("utf-8")
    hits = output.splitlines()
    return hits
