from __future__ import print_function
import os
import re
import subprocess
import sys


def one_file_detail(fname):
    output = subprocess.check_output(['ls', '-sAFldT', fname])
    output = output.decode("utf-8").strip()
    return output

def md5sum_of_normal_file(fname):
    output = subprocess.check_output(['openssl', 'md5', fname])
    output = output.decode("utf-8").strip()
    #print("md5sum dbg: '%s'" % (output))
    match = re.match(r"""^MD5\(.+\)=\s+([0-9a-fA-F]+)\s*$""", output)
    assert match
    return match.group(1)


def recursive_dir_snapshot(dir_name, f):
    lines_out = []
    w = list(os.walk(dir_name))
    for dir, subdirs, normal_files_in_dir in w:
        lines_out.append('                                 ' +
                         one_file_detail(dir))
        for fname in normal_files_in_dir:
            fullname = dir + '/' + fname
            tmp = (md5sum_of_normal_file(fullname) + ' ' +
                   one_file_detail(fullname))
            lines_out.append(tmp)
    for line in lines_out:
        #print("line='%s'" % (line))
        print(line, file=f)
