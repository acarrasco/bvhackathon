import sys
import json

allreviews = sys.stdin
photos_and_feedback = ((review.get('Photos'),
                        review.get('TotalPositiveFeedbackCount'),
                        review.get('TotalNegativeFeedbackCount'))
                       for review in (json.loads(line) for line in allreviews) if review.get('Photos'))
for x in photos_and_feedback:
    print json.dumps(x)