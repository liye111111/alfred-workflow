import time;
import datetime
import json
import sys




class Item:
    uid = ''
    arg = ''
    title = ''
    tz=''

    def __init__(self, uid,tz):
        self.uid = uid
        self.arg = uid
        self.tz = tz
        self.title = tz+':'+ str(uid)

format=['%Y-%m-%d %H:%M:%S','%Y-%m-%d','%Y%m%d']


#input='1212'
input=sys.argv[1]
output=''

now = int(time.time()*1000)
try:
    now=int(input)


except:
    pass
us_now=now-15*60*60*1000

items=[]

dt = datetime.datetime.fromtimestamp(now / 1000)

us_dt = datetime.datetime.fromtimestamp(us_now / 1000)


for frt in format:
    line = dt.strftime(frt)
    items.append(Item(line,'CN'))

for frt in format:
    line = us_dt.strftime(frt)
    items.append(Item(line,'US'))

items.append(Item(now,'TS'))

data = {"items": items}

out = json.dumps(data, default=lambda obj: obj.__dict__, sort_keys=True, indent=4, separators=(',', ': '))
print(out)
