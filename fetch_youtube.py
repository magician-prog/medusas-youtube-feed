import feedparser
import json

RSS_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UC7Gw87W_I2rl3n32hdcN4Pg"

feed = feedparser.parse(RSS_URL)

items = []

for entry in feed.entries[:10]:
    items.append({
        "title": entry.title,
        "url": entry.link,
        "published": entry.published
    })

with open("updates.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
