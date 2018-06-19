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


def do_mdimport(filename, mdimporter_choice, arch_option):
    if arch_option is None:
        args_part0 = []
    else:
        args_part0 = ['arch', '-' + arch_option]
    args_part1 = ['mdimport', '-d4']
    if mdimporter_choice is None or mdimporter_choice == '(default)':
        args_part2 = []
    else:
        args_part2 = ['-g', mdimporter_choice]
    args_part3 = [filename]
    all_args = args_part0 + args_part1 + args_part2 + args_part3
    mdimport_output = subprocess.check_output(all_args,
                                              stderr=subprocess.STDOUT)
    # Assume output of mdimport can be decoded as UTF-8
    mdimport_output = mdimport_output.decode("utf-8")

    # There may be error messages in the output.  Ignore those,
    # looking for the one that says "Imported <filename> of type
    # <type> with plugIn <mdimporter>." and extract out the pieces.

    lines = mdimport_output.splitlines()
    found_attributes_start = False
    info = {}
    for line in lines:
        #print("dbg: %s" % (line))
        match = re.match(r"""(?x) ^
                             .* \s+ mdimport \[ .+ : .+ \]
                             \s+ Imported \s+ ' (?P<filename>.+) '
                             \s+ of \s+ type \s+ ' (?P<uti>.+) '
                             \s+ with \s+ plugIn \s+ (?P<mdimporter>.+)
                             \. \s* $""", line)
        if match:
            #print("dbg: found info line")
            info['filename'] = match.group('filename')
            info['uti'] = match.group('uti')
            info['mdimporter'] = match.group('mdimporter')
            continue

        match = re.match(r"""^.* mdimport.* Attributes: {\s*$""", line)
        if match:
            #print("dbg: found Attributes line")
            found_attributes_start = True
            break

    assert found_attributes_start
    assert 'filename' in info
    return info


def mdfind_search_results(test_search_term):
    output = subprocess.check_output(['mdfind', test_search_term])
    # Assume output of mdimport can be decoded as UTF-8
    output = output.decode("utf-8")
    hits = output.splitlines()
    return hits
