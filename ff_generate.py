import sys
import fontforge

argvs = sys.argv
argc = len(argvs)
if (argc != 3):
  quit()
f = fontforge.open(argvs[1])

# 1. version
version = f.version + '.1'
f.version = version
f.sfnt_names = (
  tuple(
    filter(
      lambda x: not (x[0] == 'Japanese' and x[1] == 'Version'),
      f.sfnt_names))
  + (('Japanese', 'Version', 'Version ' + version),))

# 2. gsub table
for l in f.gsub_lookups:
  fe = ()
  for t in f.getLookupInfo(l)[2]:
    fe = fe + (
      (t[0],(
        ("latn",("dflt",)),
        ("kana",("JAN ", "dflt")),
        ("hani",("dflt",)))),)
  f.lookupSetFeatureList(l, fe)

# 3. vertical metrics
f.hasvmetrics = True

f.generate(argvs[2], '', ('short-post','opentype'))

