#!/bin/python3

import os

web_pages = os.listdir()


pages = []
for _file in web_pages:
    if _file.endswith(".html") and not _file == "index.html":
        # print(f"page: {_file}")
        pages.append(_file)

print(f">> # of pages: {len(pages)}")

# write to file
js_syntax="var pages=["
comma=False
for page in pages:
    if comma:
        js_syntax+=","
    js_syntax+=f"'{page}'"
    comma=True
js_syntax+="]"

print(js_syntax)

pages_js=open("pages.js", "w")
pages_js.write(js_syntax)
pages_js.close()
