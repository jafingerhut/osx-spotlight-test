#! /usr/bin/env python3

import json
import mdimporters
import sys

# Note: The words are stored separately as 'word_part1' and
# 'word_part2' so that searching for the entire word will not find the
# file 'test-file-info.json' as well as the documents where there word
# is contained.

with open('test-file-info.json', 'r') as f:
    maybe_unique_words = json.load(f)

for w in maybe_unique_words:
    full_word = w['word_part1'] + w['word_part2']
    #print("word %s filename %s" % (full_word, w['filename']))
    found_filenames = mdimporters.mdfind_search_results(full_word)
    matches_expected = [x for x in found_filenames if w['filename'] in x]
    w['matches_expected'] = matches_expected
    matches_other = [x for x in found_filenames if not (w['filename'] in x)]
    w['matches_other'] = matches_other

json.dump(maybe_unique_words, sys.stdout, sort_keys=True, indent=2)
