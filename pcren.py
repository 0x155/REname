import os, re, sys, optparse

psParser = optparse.OptionParser(usage = "%prog [options] <match text> <replace text>", version = "REname 1.0\nThis program is released under the GNU GPL.")
psParser.add_option("-p", "--preview", action = "store_true", dest = "preview", help = "only preview changes")
psParser.set_defaults(preview = False)
(opOptions, arArguments) = psParser.parse_args()

if len(arArguments) != 2:
    psParser.print_help()
    sys.exit(1)

strSearch = arArguments[0]
strReplace = arArguments[1]
lstFiles = os.listdir(".")
intRenames = 0

for strFile in lstFiles:
    if os.path.isfile(strFile) == False: continue
    strNewFilename = re.sub(strSearch, strReplace, strFile)
    if strNewFilename != strFile:
        try:
            if opOptions.preview == False:
                os.rename(strFile, strNewFilename)
            print "Renamed '%s' to '%s'" % (strFile, strNewFilename)
            intRenames += 1
        except OSError:
            print "Error: Couldn't rename %s" % strFile

print "Done, renamed %s files." % intRenames