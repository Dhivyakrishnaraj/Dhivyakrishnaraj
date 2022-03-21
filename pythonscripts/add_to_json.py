Add to JSON

import json
with open('minidict.json','r+')as file:
    d= json.loads(file.read())
    d['employees'].append(dict(firstName='Albert',lastName ='Bert'))
    file.seek(0)
    json.dump(d,file,indent =4,sort_keys = True)
    file.truncate()