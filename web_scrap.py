from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

title_pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(title_pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)

name_pattern = "<h2>.*?</h2>"
name_match_results = re.search(name_pattern, html, re.IGNORECASE)
name = name_match_results.group()
name = re.sub("<.*?>", "", name)
print(name)

favorite_color_pattern = "<br><br.*?>.*?<h2.*?>" # "<br.*?>.*?</center.*?>"
favorite_color_match_results = re.search(favorite_color_pattern, html, re.IGNORECASE)
print(favorite_color_match_results)
favorite_color = favorite_color_match_results.group()
favorite_color = re.sub("<.*?>", "", favorite_color)
print(favorite_color)
