# REname renames files in a directory using [Regular Expressions](https://docs.python.org/2/library/re.html)


For example, if you have files **new1.txt to new100.txt** and run pcren new sample it will rename files to sample1.txt, sample2.txt, etc. You can use parentheses to capture text and tokens in the format “\1” to replace them. For example, in the above files, pcren new(\\d+).txt "new file \\\\\\\1.doc" will rename the files to New file 1.doc, New file 2.doc, etc.
