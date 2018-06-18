#! /bin/bash

# Get the UTI (Uniform Type Identifier) of a file, as well as the 'UTI
# hierarchy'.

# https://en.wikipedia.org/wiki/Uniform_Type_Identifier

FNAME="$1"

mdls -name kMDItemContentType "${FNAME}"
mdls -name kMDItemContentTypeTree "${FNAME}"
