import sys
import json
import re

url_exp = re.compile(r'http://([^\.]*)\.ugc\.bazaarvoice\.com/([0-9]+)/([0-9]+)/photo\.jpg')
for line in sys.stdin:
    photos, positive, negative = json.loads(line)
    for photo in photos:
        command_pattern = 'curl "{url}" > {client}{dir1}{dir2}_{positive}_{negative}.jpg'
        url = photo.get('Sizes').get('normal').get('Url')
        client, dir1, dir2 = url_exp.match(url).groups()
        print command_pattern.format(url=url,
                                     client=client,
                                     dir1=dir1,
                                     dir2=dir2,
                                     positive=positive,
                                     negative=negative)