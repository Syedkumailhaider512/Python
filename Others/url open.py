import urllib.request
import re

search_keyword="pasoori"
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
link = "https://www.youtube.com/watch?v=" + video_ids[0]
print(link)