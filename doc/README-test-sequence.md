Note: All test results were performed on a system with very light CPU
and memory load.  The average CPU load was under 10% for the entire
duration of the tests, as shown by Apple's Activity Monitor.

Spotlight indexing had been done on the system, but completed days
before these tests were run, as determined by the indexing progress
bar that shows up in Apple's Spotlight GUI window that appears when
you click on the Spotlight icon near the right of the top of screen
menu bar, and type any search term.


# Test results group 1

+ MacBook Pro running OSX 10.12.6
+ Microsoft Word for Mac Version 16.9 (180116)

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

I will use "term" as a shortened form of "search term".  You can use
any sequence of letters that you want, but I prefer to use made-up
sequences of letters that do not appear in other documents on the
system I am testing with, so I get either no results, or the one
document that I expect the term to occur in.

One such made-up word is "oleasterich".


Test sequence:

0. Pick a folder in which to save a new document, one that has no file
   named foo.docx in it already.  A folder newly created for testing
   purposes is good.  Also open a new window in Finder, and enter the
   search term in the text box near the upper right of the window.
   Leave this window open and visible during the tests so you can
   watch as its search results change (or not).
1. Start Word
2. Select menu item File -> New Document
3. Enter text "oleasterich"
4. Select menu item File -> Save As.  Leave File format as the default
   "Word Document (.docx)".  Named the file "foo", which becomes
   "foo.docx" with the default file name extension added by Word.
   Click Save button to save.
5. Left the Word document open.
6. Examine the search results for the search term, either via `mdfind`
   command in Terminal, via the Finder window created in step 0, or
   both.

From this point, I saw three different variations for what happened
next.

+ "good results" - Soon after saving the document, foo.docx was found
  by a Spotlight search, both in the Finder window kept open for that
  purpose, and via the `mdfind` command in Terminal.  Continue with
  step 7 below.
+ "bad results" - Within 60 seconds after saving the document,
  foo.docx was never found by a Spotlight search, neither in a Finder
  window, nor via `mdfind` command in Terminal.  Continue with step 11
  below.
+ "bad results, with brief but temporary good results" - foo.docx was
  displayed as a matching result in a Finder window, but only for a
  few seconds, then it disappeared, and it did not return within 60
  seconds after saving the document.  It did not show up at that time
  via `mdfind` command, either.  Continue with step 11 below.

Continuing from step 6 above:

7. In Terminal ran `mdimport -d1 foo.docx`.  The mdimporter reported
   was: `/System/Library/Spotlight/RichText.mdimporter`.  foo.docx
   still showed up in Spotlight results.
8. Closed Word document.  Still in search results.
9. Opened Word document.  Still in search results.
10.  Quit Word.  Deleted file.

Continuing from step 6 above:

11. In Terminal ran `mdimport -d1 foo.docx`.  The mdimporter reported
    was: `/System/Library/Spotlight/RichText.mdimporter`.  foo.docx
    showed up in Spotlight results within seconds.
12. Closed document window in Word.  Still in search results.
13. Opened foo.docx again in Word.  I merely opened the document so
    the window containing its text appeared.  I did not modify the
    content, save it, or anything other than open the document.
    foo.docx disappeared from search results within a couple of
    seconds.
14. Quit Word.  Deleted file.

+ Try  1: bad results
+ Try  2: good results
+ Try  3: bad results
+ Try  4: bad results
+ Try  5: bad results
+ Try  6: good results
+ Try  7: good results
+ Try  8: good results
+ Try  9: good results
+ Try 10: good results
+ Try 11: good results (shortened version where I stopped at step 6 after foo.docx showed up in search results, then jumped to step 10.)
+ Try 12: good results (same as try 11)
+ Try 13: good results (same as try 11)
+ Try 14: good results (same as try 11)
+ Try 15: good results (same as try 11)
+ Try 16: good results (same as try 11)
+ Try 17: bad results (file name was fo.docx by accident this time)
+ Try 18: good results (same as try 11)
+ Try 19: bad results
+ Try 20: bad results, with brief but temporary good results


# Test results group 2

On same computer, remained at same version of OSX, but updated to
latest version of Microsoft Office for Mac available at the time,
shown below:

+ MacBook Pro running OSX 10.12.6
+ Microsoft Word for Mac Version 16.14.1 (180613)


+ Try  1: bad results
+ Try  2: bad results, with brief but temporary good results
+ Try  3: bad results
+ Try  4: bad results
+ Try  5: good results
+ Try  6: bad results, with brief but temporary good results
+ Try  7: bad results, with brief but temporary good results
+ Try  8: good results
+ Try  9: good results
+ Try 10: good results


# Test results group 3

On same computer:

+ MacBook Pro running OSX 10.12.6
+ Microsoft Word for Mac Version 16.14.1 (180613)

I hand-edited my copy of this file:

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

to remove this line:

    <string>org.openxmlformats.wordprocessingml.document</string>

Because the file is in the /System directory, I had to first disable
SIP.  I re-enabled SIP after modifying the file.  I _did not modify
any other files in the system_.  I used instructions included on this
web page to disable, then later re-enable, SIP:

    https://discussions.apple.com/thread/8373095

The directory `richtext-mdimporter-info-plist-files` contains copies
of the original version of the OSX 10.12.6 RichText Info.plist file
that was on my system, as well as the modified one that I used for
this group of tests.

The results reported below use the same test sequence as those above,
with the one difference that every time I ran `mdimport -d1 foo.docx`
in a Terminal, the mdimporter that was reported as used was this one:

    /Library/Spotlight/Microsoft Office.mdimporter

I believe this change is because of how I changed the RichText
Info.plist file.

+ Try  1: good results
+ Try  2: good results
+ Try  3: good results
+ Try  4: good results
+ Try  5: good results
+ Try  6: good results
+ Try  7: good results
+ Try  8: good results
+ Try  9: good results
+ Try 10: good results


# Test results group 4

This is the same system as group 3 above, except that I disabled SIP,
restored the RichText Info.plist file to its original contents, then
re-enabled SIP:

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

I didn't intentionally change anything else on the system, and I was
being quite careful about these things.  I am sure some files in
`/tmp` and system logs were changed, but no configurations, OSX
version, Microsoft Office version, or other similar things were
changed.

The results reported below use the same test sequence as those above.
The mdimporter reported when I ran the command `mdimport -d1 foo.docx`
in a Terminal was back to its original:

    /System/Library/Spotlight/RichText.mdimporter

+ Try  1: bad results
+ Try  2: bad results
+ Try  3: bad results
+ Try  4: bad results
+ Try  5: bad results
+ Try  6: bad results
+ Try  7: bad results
+ Try  8: bad results
+ Try  9: bad results
+ Try 10: bad results
