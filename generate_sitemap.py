# generate_sitemap.py

import requests
import xml.etree.ElementTree as ET
from datetime import datetime

RSS_FEED = "https://vegan-oriented.tistory.com/rss"
TODAY = datetime.today().strftime("%Y-%m-%d")

response = requests.get(RSS_FEED)
root = ET.fromstring(response.content)

items = root.findall(".//item")

entries = ""
for item in items:
    link = item.find("link").text
    entries += f"""  <url>
    <loc>{link}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>\n"""

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}</urlset>
"""

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)
