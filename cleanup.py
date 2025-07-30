#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup

OLD_URL = "https://sites.google.com/view/f4swiki"
NEW_URL = "https://calloffreedom.github.io/f4swiki"

for root, _, files in os.walk("site"):  # assuming wget dumps files into ./site
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            print(f"🛠 Cleaning {path}")

            with open(path, "r", encoding="utf-8") as f:
                html = f.read()

            soup = BeautifulSoup(html, "html.parser")

            # ✅ 1. Remove any <script> that contains _at_config
            for script in soup.find_all("script"):
                if script.string and "_at_config" in script.string:
                    script.decompose()

            # ✅ 2. Rewrite URLs
            for tag in soup.find_all(href=True):
                tag["href"] = tag["href"].replace(OLD_URL, NEW_URL)
            for tag in soup.find_all(src=True):
                tag["src"] = tag["src"].replace(OLD_URL, NEW_URL)

            # ✅ 3. Rewrite text content (just in case Google hardcoded URLs in text)
            html_str = str(soup).replace(OLD_URL, NEW_URL)

            # ✅ 4. Write cleaned HTML back
            with open(path, "w", encoding="utf-8") as f:
                f.write(html_str)
