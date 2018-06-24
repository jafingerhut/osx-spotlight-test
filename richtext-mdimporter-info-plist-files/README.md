File: original-Info.plist

This a copy of the file:

    /System/Library/Spotlight/RichText.mdimporter/Contents/Info.plist

that was installed on two Mac OSX 10.12.6 systems I own.  This file
has changed version numbers and a few other small things from a Mac
OSX 10.6.8 and OSX 10.11.6 system I also own, but they all have the
same contents within the key CFBundleDocumentTypes, including
org.openxmlformats.wordprocessingml.document.


File: modified-Info.plist

This is the same as original-Info.plist, but has the following line,
line 24 in original-Info.plist, deleted:

```
<string>org.openxmlformats.wordprocessingml.document</string>
```

I got the idea of trying to modify the file in this way from this
article: https://discussions.apple.com/thread/8373095

I have saved a copy of that web page in this file for future
reference, in case it changes.

```
newly created_modified .docx files are no… - Apple Community.html
newly created_modified .docx files are no… - Apple Community_files/
```
