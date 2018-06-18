# Introduction

I created this repository in order to test the Mac OS X Spotlight
feature's indexing and search capabilities.  My initial motivation was
because my wife, and apparently many other people, have found that
using OS X's Spotlight feature to search for words that are inside the
contents of Microsoft Office documents in some cases does not find
those documents.


# Tests you can try

I have created a separate repository containing files created with
Microsoft Office programs such as Word, Excel, and PowerPoint.  Those
documents include "non words", i.e. sequences of letters from the
English alphabet that are not in any dictionary, and unlikely to
already be in any document stored on someone's computer, to minimize
the size of the search results.  That repository is separate from this
one, to make it easy to remove those files from a system, then add
them back, under the control of programs included in this repository.

    https://github.com/jafingerhut/osx-spotlight-test-files


# Links

Since many other people have noticed similar problems on their
computers, several have asked about the issue, and others have
attempted to learn what is going worng, and proposed changes to their
systems that might improve the situation.

    https://discussions.apple.com/thread/7368240
    https://discussions.apple.com/thread/7937137

    https://superuser.com/questions/1214883/why-is-apple-spotlight-not-finding-contents-of-docx
    https://word.uservoice.com/forums/304942-word-for-mac/suggestions/10998114-apple-s-spotlight-can-t-find-word-docx-files
    https://forums.houdah.com/post/old-problem-with-spotlight-and-word-docx-files-8530096

    https://answers.microsoft.com/en-us/msoffice/forum/msoffice_word-mso_mac-mso_mac2011/is-it-true-that-mac-os-spotlight-does-not-index/6b4823b4-e8db-4578-91f0-3e77d52d7e3d

Apple Developer documentation on Spotlight importers:

    https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/MDImporters.html


# Generating search terms unlikely to be already on someone's computer

There are many ways to generate words that aren't in any dictionary,
and are unlikely to be already stored in any file on someone's
computer.  "Totro" is just one way.

    https://www.dwheeler.com/totro.html

I generated the ones below by setting Min Syllables to 8 and Max
Syllables to 10.
