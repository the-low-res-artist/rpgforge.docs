
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import datetime # to get the date
import time # measure duration

# goal : create the sitemap.xml file
# ---------------------------------
class Url:
    def __init__(self, loc):
        self.loc = loc
        self.lastmod = datetime.datetime.now().strftime("%Y-%m-%d")
        self.changefreq = "weeekly"
        self.priority = "0.5"
    
    def get_sitemap(self):
        return f"""
<url>
    <loc>{self.loc}</loc>
    <lastmod>{self.lastmod}</lastmod>
    <changefreq>{self.changefreq}</changefreq>
    <priority>{self.priority}</priority>
</url>"""

# ---------------------------------
class Urlset:
    def __init__(self):
        self.urls = []

    def get_sitemap(self):
        sitemap = "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"
        for url in self.urls:
            sitemap += url.get_sitemap()
        sitemap += "\n</urlset>"
        return sitemap

# ---------------------------------
class Xml:
    def __init__(self):
        self.urlset = Urlset()

    def crawl(self, website_root):
        # Walk through the directory structure
        for root, _, files in os.walk(website_root):
            for file in files:
                # Check if the file has a .html extension
                if file.endswith('.html'):
                    # Get the full path of the HTML file
                    path = os.path.join(root, file)
                    path = path.replace("./../book/", "https://rpgpowerforge.com/")
                    path = path.replace("\\", "/")
                    self.urlset.urls.append(Url(path))

    def get_sitemap(self):
        sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        sitemap += self.urlset.get_sitemap()
        return sitemap

# ---------------------------------
class Sitemap:
    def __init__(self):
        self.xml = Xml()
    
    def crawl(self, website_root):
        self.xml.crawl(website_root)

    def write(self, sitemap_filepath):
        with open(sitemap_filepath, 'w', encoding="utf8") as f:
            f.write(self.xml.get_sitemap())

# ---------------------------------


# generate the sitemap file
def generate_sitemap(website_root, sitemap_filepath):
    sitemap = Sitemap()
    sitemap.crawl(website_root)
    sitemap.write(sitemap_filepath)


# entry point
start = time.time()
generate_sitemap("./../book/", "./../book/sitemap.xml")
end = time.time()
print(f"[{str(round(end - start, 1))} sec] SITEMAP UPDATE : 1 updated")

# safe return
sys.exit(0)