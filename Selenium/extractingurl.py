import re
import linkGrabber

links = linkGrabber.links('http://google.com')
gb = links.find(limit=4)
print(gb)