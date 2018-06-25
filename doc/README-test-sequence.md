Note: All test results were performed on a system with very light CPU
and memory load.  The average CPU load was under 10% for the entire
duration of the tests, as shown by Apple's Activity Monitor.

Spotlight indexing had been done on the system, but completed days
before these tests were run, as determined by the indexing progress
bar that shows up in Apple's Spotlight GUI window that appears when
you click on the Spotlight icon near the right of the top of screen
menu bar, and type any search term.


# Test results group 1

MacBook Pro running OSX 10.12.6
Microsoft Word for Mac Version 16.9 (180116)

All mdimporters are listed below, and as installed by Apple,
Microsoft, and/or the creator of the mdimporter, with no custom
modifications.

```
$ mdimport -L
2018-06-24 20:23:30.046 mdimport[2561:1144325] Paths: id(501) (
    "/Library/Spotlight/iBooksAuthor.mdimporter",
    "/Library/Spotlight/iWork.mdimporter",
    "/Library/Spotlight/Microsoft Office.mdimporter",
    "/System/Library/Spotlight/Application.mdimporter",
    "/System/Library/Spotlight/Archives.mdimporter",
    "/System/Library/Spotlight/Audio.mdimporter",
    "/System/Library/Spotlight/Automator.mdimporter",
    "/System/Library/Spotlight/Bookmarks.mdimporter",
    "/System/Library/Spotlight/Chat.mdimporter",
    "/System/Library/Spotlight/CoreMedia.mdimporter",
    "/System/Library/Spotlight/Font.mdimporter",
    "/System/Library/Spotlight/iCal.mdimporter",
    "/System/Library/Spotlight/Image.mdimporter",
    "/System/Library/Spotlight/iPhoto.mdimporter",
    "/System/Library/Spotlight/iPhoto8.mdimporter",
    "/System/Library/Spotlight/Mail.mdimporter",
    "/System/Library/Spotlight/MIDI.mdimporter",
    "/System/Library/Spotlight/Notes.mdimporter",
    "/System/Library/Spotlight/PDF.mdimporter",
    "/System/Library/Spotlight/PS.mdimporter",
    "/System/Library/Spotlight/QuartzComposer.mdimporter",
    "/System/Library/Spotlight/RichText.mdimporter",
    "/System/Library/Spotlight/SystemPrefs.mdimporter",
    "/System/Library/Spotlight/vCard.mdimporter",
    "/Applications/GarageBand.app/Contents/Library/Spotlight/GarageBandSpotlightImporter.mdimporter",
    "/Applications/GarageBand.app/Contents/Library/Spotlight/LogicX_MDImport.mdimporter",
    "/Applications/Microsoft Outlook.app/Contents/Library/Spotlight/Microsoft Outlook Spotlight Importer.mdimporter",
    "/Applications/Mindjet MindManager.app/Contents/Library/Spotlight/MindManager.mdimporter",
    "/Applications/OmniGraffle.app/Contents/Library/Spotlight/OmniGraffle.mdimporter",
    "/Applications/Thunderbird.app/Contents/Library/Spotlight/thunderbird.mdimporter",
    "/Applications/Xcode.app/Contents/Library/Spotlight/uuid.mdimporter",
    "/Applications/LibreOffice.app/Contents/Library/Spotlight/OOoSpotlightImporter.mdimporter",
    "/Applications/Xcode.app/Contents/Applications/Application Loader.app/Contents/Library/Spotlight/MZSpotlight.mdimporter"
)
```

urestr aph
ankewy nuglugh

I will use "term" as a shortened form of "search term".  You can use
any sequence of letters that you want, but I prefer to use made-up
sequences of letters that do not appear in other documents on the
system I am testing with, so I get either no results, or the one
document that I expect the term to occur in.

One such made-up word is "oleasterich".


Sequence #4

1. Start Word, when there is no file foo.docx in some folder
2. File -> New Document
3. Enter text "oleasterich"
4. File -> Save As.  Leave File format as the default "Word Document
   (.docx)".  Named the file "foo", which becomes "foo.docx" with the
   default file name extension added by Word.  Clicked Save button to
   save.
5. Left the Word document open.

From this point, I saw three different variations for what happened
next.

6a. Soon after saving the document, foo.docx was found by a Spotlight
    search, both in a Finder window kept open for that purpose, and
    via mdfind command in Terminal.  Continue with step 7a below.

6b. Within 60 seconds after saving the document, foo.docx was never
    found by a Spotlight search, neither in a Finder window, nor via
    mdfind command in Terminal.  Continue with step 7b below.

6c. foo.docx was displayed as a matching result in a Finder window,
    but only for a few seconds, then it disappeared, and it did not
    return within 60 seconds after saving the document.  It did not
    show up at that time via mdfind command, either.  Continue with
    step 7b below.

Continuing from step 6a above:

7a. In Terminal ran "mdimport -d1 foo.docx".  The mdimporter reported
    was: "/System/Library/Spotlight/RichText.mdimporter".  foo.docx
    still showed up in Spotlight results.
8a. Closed Word document.  Still in search results.
9a. Opened Word document.  Still in search results.
10a.  Quit Word.  Deleted file.

Continuing from step 6b or 6c above:

7b. In Terminal ran "mdimport -d1 foo.docx".  The mdimporter reported
    was: "/System/Library/Spotlight/RichText.mdimporter".  foo.docx
    showed up in Spotlight results within seconds.
8b. Closed document window in Word.  Still in search results.
9b. Opened foo.docx again in Word.  I merely opened the document so
    the window containing its text appeared.  I did not modify the
    content, save it, or anything other than open the document.
    foo.docx disappeared from search results within a couple of
    seconds.
10b.  Quit Word.  Deleted file.

Try  1: Sequence #4 took path b.
Try  2: Sequence #4 took path a.
Try  3: Sequence #4 took path b.
Try  4: Sequence #4 took path b.
Try  5: Sequence #4 took path b.
Try  6: Sequence #4 took path a.
Try  7: Sequence #4 took path a.
Try  8: Sequence #4 took path a.
Try  9: Sequence #4 took path a.
Try 10: Sequence #4 took path a.

Try 11: Sequence #4 took path a (shortened version where I stopped at step 6a after foo.docx showed up in search results, then jumped to 10a.)
Try 12: Sequence #4 took path a (same as try 11)
Try 13: Sequence #4 took path a (same as try 11)
Try 14: Sequence #4 took path a (same as try 11)
Try 15: Sequence #4 took path a (same as try 11)
Try 16: Sequence #4 took path a (same as try 11)
Try 17: Sequence #4 took path b (file name was fo.docx by accident this time)
Try 18: Sequence #4 took path a (same as try 11)
Try 19: Sequence #4 took path b
Try 20: Sequence #4 took path b, except foo.docx showed up in search results for a few seconds after saving the document, before it disappeared and stayed that way for 60 seconds after saving.


# Test results group 2

On same computer, remained at this version of OSX:

MacBook Pro running OSX 10.12.6

but updated to latest version of Microsoft Office for Mac available at
the time, which was this:

Microsoft Word for Mac Version 16.14.1 (180613)

Try  1: Sequence #4 took path b
Try  2: Sequence #4 took path b, except foo.docx showed up in search results for a few seconds after saving the document, before it disappeared and stayed that way for 60 seconds after saving.
Try  3: Sequence #4 took path b
Try  4: Sequence #4 took path b
Try  5: Sequence #4 took path a
Try  6: Sequence #4 took path b, except foo.docx showed up in search results for a few seconds after saving the document, before it disappeared and stayed that way for 60 seconds after saving.
Try  7: Sequence #4 took path b, except foo.docx showed up in search results for a few seconds after saving the document, before it disappeared and stayed that way for 60 seconds after saving.
Try  8: Sequence #4 took path a
Try  9: Sequence #4 took path a
Try 10: Sequence #4 took path a


# Test results group 3

On same computer:

MacBook Pro running OSX 10.12.6
Microsoft Word for Mac Version 16.14.1 (180613)

I hand-edited my copy of this file:

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

to remove this line:

    <string>org.openxmlformats.wordprocessingml.document</string>

Because the file is in the /System directory, I had to follow these
instructions to disable SIP.  I re-enabled SIP after modifying the
file.  I _did not modify any other files in the system_.  I used
instructions included on this web page to disable, then later
re-enable, SIP:

    https://discussions.apple.com/thread/8373095

The directory `richtext-mdimporter-info-plist-files` contains copies
of the original version of the OSX 10.12.6 RichText Info.plist file
that was on my system, as well as the modified one that I used for
this group of tests.

The results reported below use the same test sequence as those above,
with the one difference that every time I ran 'mdimport -d1 foo.docx'
in a Terminal, the mdimporter that was reported as used was this one:

    /Library/Spotlight/Microsoft Office.mdimporter

I believe this change is because of how I changed the RichText
Info.plist file.

Try  1: Sequence #4 took path a
Try  2: Sequence #4 took path a
Try  3: Sequence #4 took path a
Try  4: Sequence #4 took path a
Try  5: Sequence #4 took path a
Try  6: Sequence #4 took path a
Try  7: Sequence #4 took path a
Try  8: Sequence #4 took path a
Try  9: Sequence #4 took path a
Try 10: Sequence #4 took path a


# Test results group 4

This is the same system as group 3 above, except that I disabled SIP,
restored this file to its original contents, then re-enabled SIP:

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

I didn't intentionally change anything else on the system.  I am sure
some files in /tmp and system logs were changed, but no
configurations, OSX version, Microsoft Office version, or other
similar things were changed.

The results reported below use the same test sequence as those above.
The mdimporter reported when I ran the command 'mdimport -d1 foo.docx'
in a Terminal was back to its original:

    /System/Library/Spotlight/RichText.mdimporter

Try  1: Sequence #4 took path b
Try  2: Sequence #4 took path b
Try  3: Sequence #4 took path b
Try  4: Sequence #4 took path b
Try  5: Sequence #4 took path b
Try  6: Sequence #4 took path b
Try  7: Sequence #4 took path b
Try  8: Sequence #4 took path b
Try  9: Sequence #4 took path b
Try 10: Sequence #4 took path b
