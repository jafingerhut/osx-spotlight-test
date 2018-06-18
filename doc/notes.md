# Research notes

Question: How does Spotlight determine which mdimporter to run on a
file?

Partial answer from this page:

https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/Concepts/HowDoesItWork.html#//apple_ref/doc/uid/TP40001847-CJBEJBHH

"Using Launch Services, Spotlight determines the uniform type identifier of the file and attempts to find an appropriate importer plug-in. If an importer exists and is authorized, it is loaded and passed the path to the file."


Question: Is there a way to determine which mdimporter Spotlight ran
for a new file?

TBD: If I have evidence that it is not always the same one that the
'mdimport' command chooses, e.g. because the content search results
change before vs. after running 'mdimport' manually on a file, then
record the details here.


I have tried using an `mdls` command like this one on several files
that Spotlight has indexed:

```bash
$ mdls -name kMDItemTextContent osx-spotlight-test-files/MS-Word-for-Mac-version-16.9-Word-2003-XML-Document-xml.xml 
kMDItemTextContent = (null)
```

So far I have always seen the value `(null)`, even for files that I
can use `mdfind` to successfully find words in the text content of the
file, and for which `kMDItemTextContent` contains what looks like the
correct text content for the file when I manually run `mdimport -d4`
on the file.

My guess is that showing `(null)` instead of the extracted text
content of the file is by design, probably for performance, storage
space, or security reasons.  Search for `kMDItemTextContent` on the
page below, and you will see this note: "Applications can create
queries using this attribute, but are not able to read the value of
this attribute directly."

    https://developer.apple.com/library/archive/documentation/CoreServices/Reference/MetadataAttributesRef/Reference/CommonAttrs.html#//apple_ref/doc/uid/TP40001694-SW1


Although many of the developer.apple.com pages on Spotlight have a
note near the top saying that they are no longer maintained, this page
looks like it has some useful debugging info on Spotlight mdimporters:

    https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/Concepts/Troubleshooting.html#//apple_ref/doc/uid/TP40001690-CJBEJBHH


Possibly relevant factors:

The particular version of the mdimporters installed, whether from
Apple, or Microsoft.

Perhaps new ones are installed with some updates of Microsoft Office?

Perhaps the precise time stamp of one or more of the mdimporter
executable files?  So perhaps running 'touch' on some file, with admin
privileges, might change which importer is run on a file?

Whether a file has a '.doc' or '.docx' suffix?

Some other attributes associated with the documents by OS X?

How exactly does mdimport decide which mdimporter to run on a file?

When is mdimport run again on a document?

When it is opened in Microsoft Word, even if you do not save it?  How
could one determine this by experiment?  Is running of mdimport
recorded in any system log?

When it is saved in Microsoft Word?


# Details

My wife has a Mac laptop, and has sometimes noticed that when opening
a new window in Finder, clicking in the "Search" text box near the top
right of the Finder window, and entering a word, will often cause a
list of documents to appear in the file list, where she knows that
some documents she has stored on her computer's internal hard drive do
not appear in the list of results.  Very frustrating.

Is there a way to make searching for files on a Mac work better than
this?

In particular, she has many documents created using Microsoft Word,
and some of them go back to the late 1990s or so, originally created
with Microsoft Office 1997 on a Windows machine.  Those files have a
file name suffix `.doc`.  Some more recent files created using a Mac
version of Microsoft office probably also have a `.doc` suffix, and
she also has Microsoft Office for Mac 2011 installed on her laptop (we
haven't yet had a strong motivation for updating that to the 2016
version).

Andy's laptop:

MacBook Pro (Retina, 15-inch, Mid 2015) running macOS Sierra version
10.12.6, with all of the latest updates as of June 14, 2018 _except_
Security Update 2018-003 10.12.6, which I just haven't gotten around
to backing up my system before installing that update yet.

Tonya's laptop:

MacBook Air (circa 2011) running TBD.
