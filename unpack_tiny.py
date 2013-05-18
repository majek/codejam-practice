
import sys
import json
import urllib
import string
import os
import re

url = sys.argv[1]

f = urllib.urlopen(url)
data = f.read()

j = json.loads(data)

for name, p in zip(string.uppercase, j['problems']):
    code = p['body'].split('<code>\r\n')
    if len(code) != 3:
        print "[.] %s: Can't parse problem" % (name,)
        continue
    INP = '%s-tiny-0.in' % (name,)
    OUT = '%s-tiny-0.out' % (name,)
    if os.path.exists(INP) or os.path.exists(OUT):
        print "[.] %s: Won't overwrite files %r %r" % (name, INP, OUT)
        continue

    inp = code[1].split('</code>')[0].replace('<br/>\r\n', '\n').strip()
    out = code[2].split('</code>')[0].replace('<br/>\r\n', '\n').strip()

    # remove <b/> alike's
    inp = re.sub('<[^>]>', lambda a:'', inp)
    out = re.sub('<[^>]>', lambda a:'', out)

    with open(INP, 'wb') as fd:
        fd.write(inp + '\n')
    with open(OUT, 'wb') as fd:
        fd.write(out + '\n')
    print "[+] %s: Tiny downloaded" % (name,)
