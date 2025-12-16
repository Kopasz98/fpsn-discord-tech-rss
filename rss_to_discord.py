import feedparser
import requests
import json
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

RSS_FEEDS = [
    "https://techcrunch.com/feed/",
"https://www.theverge.com/rss/index.xml",
"https://www.wired.com/feed/rss",
"https://feeds.arstechnica.com/arstechnica/index",
"https://www.engadget.com/rss.xml",
"https://mashable.com/feeds/rss/tech",
"https://gizmodo.com/rss",
"https://www.digitaltrends.com/feed/",
"https://www.zdnet.com/news/rss.xml",
"https://venturebeat.com/feed/",
"https://rss.slashdot.org/Slashdot/slashdot",
"https://www.fastcompany.com/technology/rss",
"https://www.axios.com/technology/rss",
"https://www.technologyreview.com/feed/",
"https://spectrum.ieee.org/rss",
"https://www.tomsguide.com/feeds/all",
"https://www.cnet.com/rss/all/",
"https://www.pcmag.com/feeds/rss",
"https://www.howtogeek.com/feed/",
"https://www.extremetech.com/feed",

"https://news.ycombinator.com/rss",
"https://www.infoq.com/feed/",
"https://www.theregister.com/headlines.atom",
"https://stackoverflow.blog/feed/",
"https://dev.to/feed",
"https://www.smashingmagazine.com/feed/",
"https://css-tricks.com/feed/",
"https://dzone.com/feed",
"https://blog.cloudflare.com/rss/",
"https://developers.googleblog.com/feeds/posts/default",

"https://www.artificialintelligence-news.com/feed/",
"https://www.aitrends.com/feed/",
"https://syncedreview.com/feed/",
"https://openai.com/blog/rss/",
"https://deepmind.google/blog/rss.xml",
"https://towardsdatascience.com/feed",
"https://www.kdnuggets.com/feed",
"https://www.analyticsvidhya.com/feed/",
"https://machinelearningmastery.com/blog/feed/",

"https://krebsonsecurity.com/feed/",
"https://thehackernews.com/feeds/posts/default",
"https://www.bleepingcomputer.com/feed/",
"https://www.darkreading.com/rss.xml",
"https://threatpost.com/feed/",
"https://www.securityweek.com/rss",
"https://www.schneier.com/feed/atom/",

"https://www.hwsw.hu/xml/rss.xml",
"https://prohardver.hu/hirfolyam/rss.html",
"https://itcafe.hu/hirfolyam/rss.html",
"https://bitport.hu/rss",
"https://sg.hu/rss",
"https://pcworld.hu/rss",
"https://techkalauz.hu/rss",
"https://raketa.hu/rss",
"https://ipon.hu/magazin/rss",

"https://www.gsmarena.com/rss-news-reviews.php3",
"https://www.androidauthority.com/feed",
"https://9to5google.com/feed/",
"https://www.macrumors.com/macrumors.xml",
"https://www.anandtech.com/rss/"
  
]

POSTED_FILE = "posted.json"

if os.path.exists(POSTED_FILE):
    with open(POSTED_FILE, "r") as f:
        posted = set(json.load(f))
else:
    posted = set()

for feed_url in RSS_FEEDS:
    feed = feedparser.parse(feed_url)
    for entry in feed.entries[:5]:
        link = entry.get("link")
        if link and link not in posted:
            data = {
                "content": f"🎮 **{entry.title}**\n{link}"
            }
            requests.post(WEBHOOK_URL, json=data)
            posted.add(link)

with open(POSTED_FILE, "w") as f:
    json.dump(list(posted), f)
