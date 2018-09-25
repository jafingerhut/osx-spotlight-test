# Introduction

Possibly good news!  I have tested with a fresh install of macOS 10.14
"Mojave", and it appears that Apple may have fixed the Spotlight
importing problems that have been plaguing some people with indexing
the contents of Microsoft Word .docx files!

Here is a link to an Apple discussions form posting I wrote about it:
https://discussions.apple.com/message/33919531

If you are having issues with this, and are not able to upgrade to
Mojave yet for some reason, or you want a free program that can build
search indexes of document contents that works on Macs as well as
Linux and Windows machines, I have had some success using a free openhttp://docfetcher.sourceforge.net/en/index.html
source program called
[DocFetcher](http://docfetcher.sourceforge.net/en/index.html).

This document is for recording results of a particular test sequence
that demonstrates _incorrect_ search results from Spotlight for
Microsoft Word documents, on several Macs that I and others have tried
it on.

Please [vote
here](https://word.uservoice.com/forums/304942-word-for-mac/suggestions/10998114-apple-s-spotlight-can-t-find-word-docx-files)!
With enough votes, we can draw the attention of a Microsoft developer
to the problem -- hopefully someone that can determine the root cause
and have it fixed.  Click on the "Vote" button on the left side of the
window, and enter your email address.  I have done this and so far
have not received any spam from it, so you should be OK here.  This is
a Microsoft web site.

Note: All test results were performed on a system with very light CPU
and memory load.  The average CPU load was under 10% for the entire
duration of the tests, as shown by Apple's Activity Monitor.

Spotlight indexing had been done on the system, but completed before
these tests were run, as determined by the indexing progress bar that
shows up in Apple's Spotlight GUI window that appears when you click
on the Spotlight icon near the right of the top of screen menu bar,
and type any search term.


# Description of test sequence used

This test sequence is only relevant if you have a Mac with at least
Microsoft Word and PowerPoint installed on it.

## Setup

S1. Quit all or at least most applications on your system.

S2. Click on the Spotlight search icon on the right side of your menu
    bar near the top right of your screen.  It looks like a small hand
    held magnifying glass.  Enter a word that you expect to be found
    in some documents saved on your system, e.g. "time".  If you see
    "Indexing" with a progress bar next to it immediately beneath the
    search term you typed, then your system has not completed
    Spotlight indexing.  Wait until it is finished before running this
    test.  If your computer only recently started indexing on a disk
    with many files, completing could take hours.

S3. Start the Activity Monitor program to verify that your system is
    mostly idle.  In a Finder window, go to the Applications folder.
    Inside of it, find the folder named "Utilities" and open that.
    Inside of the "Utilities" folder, find the application called
    "Activity Monitor" and start it.  A new window will appear with
    "Activity Monitor" near the top.  There should be several buttons
    beneath that labeled "CPU", "Memory", "Energy", "Disk", and
    "Network".  Click the "CPU" button.  Near the bottom left of the
    window you should see the words "System:", "User:", and "Idle:".
    Percentage numbers next to those words should be updating every
    few seconds.  If the number next to "Idle:" is usually "85%" or
    higher, proceed.  If it is consistently less than that, see if
    there are any applications still running on your system that you
    forgot to quit.

S4. Pick a folder in which to save a new document.  I will use
    "Documents" for this example, but as with all folder names, file
    names, and search terms in this test sequence, customize it to
    whatever you want.  I would be surprised if these choices affect
    the results in any significant way.

S5. Pick a file name to save in that folder that does not already
    exist as a Microsoft Word or PowerPoint document there.  I will
    use `foop` for this example.  Choose a name with only letters in
    it, i.e. no spaces, digits, or other non-letter characters (this
    makes it straightforward to type it in one of the test sequence
    steps later).  Choose a file name that is _different_ than the
    search term you select in the next step.  We want to test whether
    Spotlight can find a file based on a word in the document's
    _content_, not based on the name of the file.

S6. In Finder, select the menu item "File -> New Finder Window".  In
    the new Finder window that appears, in the text box near the top
    right that says "Search" inside of it, enter a made-up word that
    you don't expect to exist in any documents on your computer
    already.  In my case, I used `oleasterich` as my search term, and
    when I type that search term, no documents show up in the search
    results.  Just keep adding more arbitrary letters to your search
    term until the search results show no documents.  I will call this
    window the "search results window" below.  If you can, position
    this window on your screen somewhere where you can always see at
    least the top few lines of the search results, if not the entire
    window.  You will be checking what documents appear in this search
    results window several times during the test.

S7. Start the Terminal application.  In the same Utilities folder
    where you found Activity Monitor in step S3, find the application
    called "Terminal" and start it.  A new window will appear with a
    command prompt.  When that window is the selected window, type `cd
    Documents`, then press the return key, or replace `Documents` with
    whatever folder you decided upon in step S4.  The instructions
    below have some steps where you will be asked to enter commands in
    the Terminal window.

S8. To ensure that Spotlight search is working on your system at all,
    start Microsoft PowerPoint.  Use the menu item "File -> New
    Presentation" to open a new presentation.  Type your selected
    search term, e.g. `oleasterich` somewhere in that new presentation
    document.  Use "File -> Save" to save the document, using the
    selected file name, e.g. `foop`.  Click the Save button.  Verify
    that within a few seconds, this file name appears in the search
    results window, and remains there for at least 10 seconds or so.
    If everything goes as expected here, quit PowerPoint, and delete
    the document you saved.  The document should then disappear from
    the search results window.

S9. Choose a place to save your test results, e.g. a TextEdit
    document, a new email message, etc.  Choose somewhere other than a
    Microsoft Word document, since the test sequence requires quitting
    Word before the test is done.
    
If the new document does _not_ appear in the search results window
soon, do not bother continuing with the rest of this test.
Perhaps you have Spotlight search disabled on your system.  See
[here](https://support.apple.com/kb/ph25486?locale=en_US) for
instructions by Apple on enabling Spotlight, although doing so on
a system will likely cause it to take a significant amount of
time, e.g. hours to finish indexing (go back to step S2 above).

## Test sequence

1. Start Microsoft Word
2. Select menu item "File -> New Document"
3. Type your selected search term, e.g. `oleasterich`
4. Select menu item "File -> Save".  Leave File format as the default
   "Word Document (.docx)".  Enter the selected file name,
   e.g. `foop`.  Click the Save button.
5. Leave the Word document open.
6. Examine the search results window.  The name of the document you
   just saved should ideally appear within a few seconds, and stay
   there, but this does not always happen with some Macs I have tried.

If the file you saved appears in the search results window and stays
there for a while, e.g. at least 15 seconds or so, continue with step
7 below.

If the file does not appear, try to be patient and wait a full 60
seconds to see if it does eventually appear.  If it does not appear in
those 60 seconds, continue with step 11 below.  Also continue with
step 11 if the document did appear in the search results for a little
while, but then disappeared again and did not reappear for the next 60
seconds.

Continuing from step 6 above, if the file did appear in the search
results window:

7. In the Terminal window, type the command `mdimport -d1 foop.docx`,
   replacing `foop` with the document name you selected.  You should
   see several lines of output that might look like one of the samples
   below:

```
2018-07-12 01:07:17.377 mdimport[66800:550623] Imported '/Users/jafinger/Documents/foop.docx' of type 'org.openxmlformats.wordprocessingml.document' with plugIn /System/Library/Spotlight/RichText.mdimporter.
```

```
2018-07-12 01:07:20.501 mdimport[66831:550736] Error loading /Library/Spotlight/Microsoft Office.mdimporter/Contents/MacOS/Microsoft Office:  dlopen(/Library/Spotlight/Microsoft Office.mdimporter/Contents/MacOS/Microsoft Office, 262): no suitable image found.  Did find:
	/Library/Spotlight/Microsoft Office.mdimporter/Contents/MacOS/Microsoft Office: mach-o, but wrong architecture
	/Library/Spotlight/Microsoft Office.mdimporter/Contents/MacOS/Microsoft Office: mach-o, but wrong architecture
2018-07-12 01:07:20.501 mdimport[66831:550736] Cannot find function pointer OfficeImporterPluginFactory for factory BFA4E323-1889-11D9-82C8-000A959816BE in CFBundle/CFPlugIn 0x7f8de5d024b0 </Library/Spotlight/Microsoft Office.mdimporter> (bundle, not loaded)
2018-07-12 01:07:20.501 mdimport[66831:550736] Imported '/Users/jafinger/Documents/foop.docx' of type 'org.openxmlformats.wordprocessingml.document' with plugIn /Library/Spotlight/Microsoft Office.mdimporter.
```

   Use your mouse to click near the beginning of that text, and drag
   to the end, highlighting it, much as you would select text in a
   Microsoft Word document.  Use the menu item "Edit -> Copy" (or the
   keyboard shortcut Command-C) to copy it, then paste it into your
   test results.

   Examine your search results window to see if the presence of the
   document changes from before you typed the `mdimport` command.  If
   so, make a note of that change in your test results like "In step
   7, file disappeared from search results" and continue.

8. Close the Word document.  I have never seen this action change
   whether the document appeared in the search results window.

9. Open the Word document you just saved.  Do not modify the contents
   of the document, or save it, or anything else other than opening
   it, so that the window apears showing its contents.

From here I saw two different results.  One I call "good results"
where the file was still in the search results after opening the
document in Word.  The other I call "bad results variant 2" where the
file _disappeared_ from the search results after opening the document
in Word.  In either case, continue with step 10 below.

10.  Quit Word.  Delete the document.


Continuing from step 6 above, if the file did _not_ appear in the
search results window:

11. Same as step 7 above.  I typically saw
    `/System/Library/Spotlight/RichText.mdimporter` in the output.
    `foop.docx` showed up in the search results window within seconds.

   If it does _not_ show up within a few seconds in your testing, make
   a note in your test results like "In step 11, file did not appear
   in search results" and continue.

12. Close the Word document.  I have never seen this action change
    whether the document appeared in the search results window.

13. Open the Word document you just saved.  Do not modify the contents
    of the document, or save it, or anything else other than opening
    it, so that the window apears showing its contents.

From here I saw two different results.  One I call "bad results
variant 3" where the file was still in the search results after
opening the document in Word.  The other I call "bad results" where
the file _disappeared_ from the search results after opening the
document in Word, within a couple of seconds.  In either case,
continue with step 14 below.

14. Quit Word.  Delete the document.


Whether you ended at step 10 or step 14, after deleting the document,
it should not appear in the search results window afterward.

If you want to send me results that I can collect and report to
Microsoft and/or Apple, they should look like the following example,
except customized for your particular system and the results that you
observed.  Send them to me via email at `andy.fingerhut@gmail.com`.
See below the sample output for how to find out the version numbers
for your system.

```
Operating system version: 10.12.6
Microsoft Word for Mac version: 16.14.1 (180613)
Test results: bad results variant 3
Output of mdimport command:
2018-07-12 02:20:08.033 mdimport[96475:686432] Imported '/Users/jafinger/Documents/foop.docx' of type 'org.openxmlformats.wordprocessingml.document' with plugIn /System/Library/Spotlight/RichText.mdimporter.
```

To find the operating system version, click on the apple icon near the
upper left of your screen.  In the menu that appears click "About This
Mac".  In the window that appears you should see `Version 10.<some
number>.<some number>`.

To find your Microsoft Word version, start Word, click on the "Word"
menu title near the top left of the screen, and in the menu that
appears click "About Microsoft Word".  The version number should be
one of the first items of text in the window that appears.

If you are interested, try starting over at step 1 and see if you get
the same or different results.  I have gotten different results on
consecutive tries on several systems, oddly enough.  If you repeated
the test multiple times and want to include all of the results you
observed, simply add a separate line for each test result you saw, in
the order you saw them.

You can stop reading here, unless you are interested in the gory
details of the test results that I recorded on several Macs of mine.


# Test results

Summary of operating system and Microsoft Word version combinations
for which test results have been recorded.

| Group # | OSX version | Microsoft Word version | RichText mdimporter Info.plist file | Notes |
| ------- | ----------- | ---------------------- | ----------------------------------- | ----- |
|  [[1]](#test-results-group-1)  | 10.12.6 | 16.9    | never modified since OS installed | some good, some bad results (no variant 2 or 3 bad results) |
|  [[2]](#test-results-group-2)  | 10.12.6 | 16.14.1 | never modified since OS installed | some good, some bad results (no variant 2 or 3 bad results) |
|  [[3]](#test-results-group-3)  | 10.12.6 | 16.14.1 | modified | all good results |
|  [[4]](#test-results-group-4)  | 10.12.6 | 16.14.1 | restored to original after earlier being modified | all bad results (no variant 2 or 3 bad results) |
|  [[5]](#test-results-group-5)  | 10.13.5 | 16.14.1 | never modified since OS installed | some good, some bad results (all 3 variants of bad results) |
|  [[6]](#test-results-group-6)  | 10.13.5 | 16.14.1 | modified | all good results |
|  [[7]](#test-results-group-7)  | 10.13.5 | 16.14.1 | restored to original after earlier being modified | all good results |
|  [[8]](#test-results-group-8)  | 10.11.6 | 16.14.1 | never modified since OS installed | all results bad, variant 3 |
|  [[9]](#test-results-group-9)  | 10.11.6 | 16.14.1 | modified | all good results, with the exception of 1 out of 15 tries being bad variant 3 |
| [[10]](#test-results-group-10) | 10.11.6 | 16.15   | modified | all good results |
| [[11]](#test-results-group-11) | 10.11.6 | 16.15   | restored to original after earlier being modified | all good results |
| [[12]](#test-results-group-12) | 10.9.5  | 14.7.7  | never modified since OS installed | all good results |
| [[13]](#test-results-group-13) | 10.13.6 | 16.15   | never modified since OS installed | all good results |
| [[15]](#test-results-group-15) | 10.14   | 16.17   | never modified since OS installed | all good results |


## Test results group 1

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


## Test results group 2

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


## Test results group 3

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

I didn't intentionally change anything else on the system, and I was
being quite careful about these things.  I am sure some files in
`/tmp` and system logs were changed, but no configurations, OSX
version, Microsoft Office version, or other similar things were
changed.

The directory
[`richtext-mdimporter-info-plist-files`](../richtext-mdimporter-info-plist-files)
contains copies of the original version of the OSX 10.12.6 RichText
Info.plist file that was on my system, as well as the modified one
that I used for this group of tests.

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


## Test results group 4

This is the same system as group 3 above, except that I disabled SIP,
restored the RichText Info.plist file to its original contents, then
re-enabled SIP:

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

I used `diff` to verify that my restored Info.plist file was identical
to the copy of the original file contents that I saved, before
modifying it.

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


## Test results group 5

+ OSX 10.13.5 running in a VMware Fusion VM on a MacBook Pro
+ Microsoft Word for Mac Version 16.14.1 (180613) installed via Office 365

Note that in this OSX install, there is _no_ software installed on
the system other than what comes with a fresh OSX install (of OSX
10.12, then use the App Store to upgrade to OSX 10.13, then update
to all updates available as of 2018-Jul-04), plus Microsoft Office
for Mac that I installed via Office 365 on 2018-Jul-04.

All mdimporters are listed below, and as installed by Apple,
Microsoft, and/or the creator of the mdimporter, with no custom
modifications.

```
$ mdimport -L
2018-07-04 13:55:13.158 mdimport[4848:35046] Paths: id(501) (
    "/Library/Spotlight/iWork.mdimporter",
    "/Library/Spotlight/Microsoft Office.mdimporter",
    "/Library/Spotlight/iBooksAuthor.mdimporter",
    "/System/Library/Spotlight/SystemPrefs.mdimporter",
    "/System/Library/Spotlight/Chat.mdimporter",
    "/System/Library/Spotlight/iPhoto.mdimporter",
    "/System/Library/Spotlight/PDF.mdimporter",
    "/System/Library/Spotlight/RichText.mdimporter",
    "/System/Library/Spotlight/Bookmarks.mdimporter",
    "/System/Library/Spotlight/PS.mdimporter",
    "/System/Library/Spotlight/MIDI.mdimporter",
    "/System/Library/Spotlight/Archives.mdimporter",
    "/System/Library/Spotlight/Audio.mdimporter",
    "/System/Library/Spotlight/iPhoto8.mdimporter",
    "/System/Library/Spotlight/Automator.mdimporter",
    "/System/Library/Spotlight/Application.mdimporter",
    "/System/Library/Spotlight/Font.mdimporter",
    "/System/Library/Spotlight/Mail.mdimporter",
    "/System/Library/Spotlight/QuartzComposer.mdimporter",
    "/System/Library/Spotlight/vCard.mdimporter",
    "/System/Library/Spotlight/Image.mdimporter",
    "/System/Library/Spotlight/iCal.mdimporter",
    "/System/Library/Spotlight/CoreMedia.mdimporter",
    "/Applications/Microsoft Outlook.app/Contents/Library/Spotlight/Microsoft Outlook Spotlight Importer.mdimporter"
)
```

In particular, both the RichText and Microsoft Office mdimporters
both contained the UTI type name
`org.openxmlformats.wordprocessingml.document`, as shown by the
following commands:

```
$ grep openxmlformats.wordprocessingml.document /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist 
				<string>org.openxmlformats.wordprocessingml.document</string>

$ grep openxmlformats.wordprocessingml.document /Library/Spotlight/Microsoft\ Office.mdimporter/Contents/Info.plist 
				<string>org.openxmlformats.wordprocessingml.document</string>
				<string>org.openxmlformats.wordprocessingml.document.macroenabled</string>
```

+ Try  1: bad results
+ Try  2: bad results variant 2
+ Try  3: bad results variant 3
+ Try  4: bad results variant 2
+ Try  5: bad results variant 3
+ Try  6: good results
+ Try  7: bad results
+ Try  8: good results
+ Try  9: bad results variant 2
+ Try 10: bad results


## Test results group 6

On same computer (a VM) as "Test results group 5":

+ OSX 10.13.5 running in a VMware Fusion VM on a MacBook Pro
+ Microsoft Word for Mac Version 16.14.1 (180613) installed via Office 365

I hand-edited my copy of this file:

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

to remove this line:

    <string>org.openxmlformats.wordprocessingml.document</string>

similarly to how I did so as described in "Test results group 3".

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


## Test results group 7

On same computer (a VM) as "Test results group 5" and "Test results
group 6":

+ OSX 10.13.5 running in a VMware Fusion VM on a MacBook Pro
+ Microsoft Word for Mac Version 16.14.1 (180613) installed via Office 365

I restored the contents of this file:

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

back to its original contents (byte for byte identical according
to `diff` output), after doing the experiments in "Test results
group 6".  I rebooted after restoring the file to its original
contents, and re-enabling SIP.

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

I have no guesses as to why the results are so consistently good
here.  The output of every `mdimport -d1 foo.docx` command was back
to showing RichText as the mdimporter used, as it was for "Test
results group 5".


## Test results group 8

+ OSX 10.11.6 running on an MacBook Pro, 15-inch Early 2008 model
+ Microsoft Word for Mac Version 16.14.1 (180613) installed via Office 365

All mdimporters are listed below, and as installed by Apple,
Microsoft, and/or the creator of the mdimporter, with no custom
modifications.

```
$ mdimport -L
2018-07-07 16:04:42.481 mdimport[10826:308648] Paths: id(501) (
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
    "/Applications/Xcode.app/Contents/Library/Spotlight/uuid.mdimporter",
    "/Applications/Xcode.app/Contents/Applications/Application Loader.app/Contents/Library/Spotlight/MZSpotlight.mdimporter",
    "/Applications/LibreOffice.app/Contents/Library/Spotlight/OOoSpotlightImporter.mdimporter",
    "/Applications/Microsoft Outlook.app/Contents/Library/Spotlight/Microsoft Outlook Spotlight Importer.mdimporter"
)
```

In particular, both the RichText and Microsoft Office mdimporters
both contained the UTI type name
`org.openxmlformats.wordprocessingml.document`, as shown by the
following commands:

```
$ grep openxmlformats.wordprocessingml.document /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist 
				<string>org.openxmlformats.wordprocessingml.document</string>

$ grep openxmlformats.wordprocessingml.document /Library/Spotlight/Microsoft\ Office.mdimporter/Contents/Info.plist 
				<string>org.openxmlformats.wordprocessingml.document</string>
				<string>org.openxmlformats.wordprocessingml.document.macroenabled</string>
```

Note: I believe that all of the earlier test result groups, I had
configured the bottom left of the Save window in Microsoft Word to
uncheck the box labeled "Hide extension".  In these first 10 tries
below, that check box was checked, so although I know that the file
had a '.docx' extension when saved in the file system, because I ran
terminal commands with that suffix and it was present in the file
name, the suffix did not show up in the save or open windows in
Microsoft Word.  I do not know whether that might make a difference in
the results, so the next group of tries after the first 10 I will
change that setting.

+ Try  1: bad results variant 3
+ Try  2: bad results variant 3
+ Try  3: bad results variant 3
+ Try  4: bad results variant 3
+ Try  5: bad results variant 3
+ Try  6: bad results variant 3
+ Try  7: bad results variant 3
+ Try  8: bad results variant 3
+ Try  9: bad results variant 3
+ Try 10: bad results variant 3

At this point, I turned off the checkbox in Microsoft Word's Save
window next to "Hide Extension".  The .docx suffix now showed up in
both the Save and Open windows.

+ Try  1: bad results variant 3
+ Try  2: bad results variant 3
+ Try  3: bad results variant 3
+ Try  4: bad results variant 3
+ Try  5: bad results variant 3


## Test results group 9

On same computer as "Test results group 8":

+ OSX 10.11.6 running on an MacBook Pro, 15-inch Early 2008 model
+ Microsoft Word for Mac Version 16.14.1 (180613) installed via Office 365

I hand-edited my copy of this file:

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

to remove this line:

    <string>org.openxmlformats.wordprocessingml.document</string>

similarly to how I did so as described in "Test results group 3".

The results reported below use the same test sequence as those above.

NOTE: Unlike the other cases above where I changed RichText's
Info.plist file in this same way, every time I ran `mdimport -d1
foo.docx` in _this_ group of tests, I still saw that the mdimporter
was reported as RichText, not the Microsoft Office importer.  I do not
know why this difference occurred.

I do not know if it makes any difference, but one difference besides
the version of OSX used was that in the following test sequences, I
left the system in a state where SIP was disabled.  I will try again
later with SIP enabled.

    /System/Library/Spotlight/RichText.mdimporter

+ Try  1: good results
+ Try  2: good results
+ Try  3: good results
+ Try  4: good results
+ Try  5: good results

I decided to be a bit lazy and only repeat the sequence 5 times
instead of 10 here.  All results were good, with no variations.


I tried again after re-enabling SIP, and got the following results.
RichText was still the mdimporter used by every mdimport command I
ran.

+ Try  1: good results
+ Try  2: good results
+ Try  3: bad results variant 3
+ Try  4: good results
+ Try  5: good results
+ Try  6: good results
+ Try  7: good results
+ Try  8: good results
+ Try  9: good results
+ Try 10: good results


## Test results group 10

On same computer as "Test results group 8", except Office 365 was
updated, then system shut down and booted again:

+ OSX 10.11.6 running on an MacBook Pro, 15-inch Early 2008 model
+ Microsoft Word for Mac Version 16.15 (180709) installed via Office 365

The RichText mdimporter Info.plist file was still in its modified
state as descried in "Test results group 9".

The `mdimport -d1 foo.docx` command reported the Microsoft Office
mdimporter this time:

    /Library/Spotlight/Microsoft Office.mdimporter

+ Try  1: good results
+ Try  2: good results
+ Try  3: good results
+ Try  4: good results
+ Try  5: good results


## Test results group 11

On same computer as "Test results group 8", with Office 365 updated as
described in "Test results group 10".

+ OSX 10.11.6 running on an MacBook Pro, 15-inch Early 2008 model
+ Microsoft Word for Mac Version 16.15 (180709) installed via Office 365

Also, I have disabled SIP, restored the following file to its original
contents, enabled SIP, and rebooted after enabling SIP.

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

+ Try  1: good results
+ Try  2: good results
+ Try  3: good results
+ Try  4: good results
+ Try  5: good results


## Test results group 12

+ OSX 10.9.5 running on a MacBook Air, 13-inch Mid 2012 model
+ Microsoft Word for Mac 2011 Version 14.7.7

The `mdimport -d1 foop.docx` command always reported RichText as the
mdimporter used.

+ Try  1: good results
+ Try  2: good results
+ Try  3: good results
+ Try  4: good results
+ Try  5: good results


## Test results group 13

+ OSX 10.13.6 running in a VMware Fusion VM on a MacBook Pro
+ Microsoft Word for Mac Version 16.15 (180709) installed via Office 365

Like "Test results group 5", this was a fresh install of OSX 10.13.6
on a VMware Fusion VM, then update to macOS High Sierra, then install
Microsoft Office via Office 365 as the first and only application
install.

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

I shut down this machine, rebooted, and installed the OSX version of
git from [this page](https://git-scm.com/download/mac), then did `git
clone https://github.com/jafingerhut/osx-spotlight-test` to get this
collection of files copied onto that virtual machine.  _Now the test
results look very different_.  I am baffled as to why.

+ Try  1: bad results
+ Try  2: bad results
+ Try  3: bad results
+ Try  4: bad results
+ Try  5: bad results

Now try deleting the copy of the `osx-spotlight-test` directory and
all files within it, then run the test sequence again.

+ Try  1: bad results
+ Try  2: bad results
+ Try  3: bad results
+ Try  4: bad results
+ Try  5: bad results

Is it because of the installation of git?  I doubt it, as I think I
have gotten bad results from machines where I did not install that
program.  But it would be relatively quick to do a test on a VM where
I had only installed Microsoft Office and git, but not yet done any
`git clone` commands, to see what happens.

Is it because this README-test-sequence.md file itself contains the
word "oleasterich"?  I doubt it, because I also tried creating a Word
document with a different made-up word, and it had the same "bad
results" as for a document containing only the word "oleasterich".

Maybe it is because the command `git clone
https://github.com/jafingerhut/osx-spotlight-test` creates some weird
files that mess up the Spotlight index somehow?  There are no
Microsoft Office format files in that repository when I ran this test,
so it cannot be files of that format causing the issue here.

I started over with a freshly installed OSX 10.13.6 VM, and a fresh
installation of MS Office 16.15, with no other applications.  A few
test results came back good.  Then I installed the OSX git
application, but did not clone any files.  Again, a few test results
came back good.

Next: In a Terminal window, used `vi README.md` command to create a
plain text file of that name with the only contents being the word
`oleasterich`.  It soon showed up in Spotlight search results.  After
creating that file and leaving it there, several test sequences gave
good results, with the Word files appearing as I created them, and
disappearing as I deleted them, and the text README.md file staying
there the entire time.

Next I did `git clone https://github.com/clojure/clojure`, which
should not contain any Microsoft-related files at all, but does have
several files with an `.md` suffix in their names (if that is even
relevant -- it may not be).  I verified that it contains no files with
`.doc` `.xls` nor `.ppt` in their names (and thus neither longer
suffixes like `.docx`).  I verified that Spotlight indexing was
complete after that, and that Spotlight could find the term `pprint`
that I knew occurred in many of the files in that repository, and they
were found.  At that time, 3 test sequences gave good results.

So installing the git application didn't cause problems.  Cloning just
any old git repository in the world doesn't' automatically cause
problems.  Using `vi` to create a `README.md` file with the search
term in it didn't cause problems.

Now I did `git clone
https://github.com/jafingerhut/osx-spotlight-test`.  I verified that
it contained no files with a `.doc` nor `.docx` suffix in their names,
nor `xls` nor `ppt`.  I did the test sequence 5 times and got good
results on all of them.

What is going on?  I do not yet have a reproducible way to trigger
going from the state "all test sequences give good results" to "some
or all test sequences give bad results".


## Test results group 14

+ OSX 10.13.4 running on a MacBook Air 13-inch Early 2014
+ Microsoft Word for Mac Version 15.27 (161010)

+ Try  1: good results
+ Try  2: good results
+ Try  3: good results
+ Try  4: good results


## Test results group 15

+ OSX 10.14 running in a VMware Fusion VM on a MacBook Pro
+ Microsoft Word for Mac Version 16.17 (180909) installed via Office 365

BIG NEWS!  The default contents of the RichText.mdimporter's
Info.plist file _no longer contains_ the line that makes that
mdimporter be a Spotlight importer for files with this type:

    org.openxmlformats.wordprocessingml.document

That is a modification I had tested and found good results with on OSX
10.11, 10.12, and 10.13, so maybe someone at Apple has changed this
with macOS 10.14 Mojave?  This is very good news!

There was a small difference I noted here during step 7 of the test
sequence.  There were no error messages like "Cannot find function
pointer".

```
2018-09-24 15:34:31.675 mdimport[4769:32087] Imported '/Users/andy/Documents/foop.docx' of type 'org.openxmlformats.wordprocessingml.document' with plugIn /System/Library/Spotlight/Office.mdimporter.
```

At least on Try 1, the file did not disappear from the search results
during step 7.

On try 1, step 9, the file foop.docx _briefly_ disappeared from the
search results, then reappeared in less than 1 second after
disappearing.

+ Try  1: good results
+ Try  2: good results
+ Try  3: good results
+ Try  4: good results
+ Try  5: good results


# Reporting of these results

I have tried officially reporting these results to both Apple and
Microsoft, but neglected to write down the details of where exactly on
their web sites I reported them.  I will add those details here if I
find them.

2018-Jul-07: I responded to a discussion on a Microsoft web site
[here](https://word.uservoice.com/forums/304942-word-for-mac/suggestions/10998114-apple-s-spotlight-can-t-find-word-docx-files),
linking to these test results, and I voted on the issue.  Please vote
on the issue yourself if you are interested having a Microsoft
developer examine the issue more carefully, and perhaps correct it.

I found that issue by going to the main page for Microsoft Word's
Suggestion box [here](https://word.uservoice.com), and searching for
the term "spotlight".
