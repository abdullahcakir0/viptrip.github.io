import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
script_path = os.path.join(cwd, "script.js")
style_path = os.path.join(cwd, "style.css")

# 1. Update CSS to break out of container
with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

breakout_css = """
.instagram-feed-wrapper {
    width: 100vw !important;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    overflow: hidden;
}
"""
if "margin-left: -50vw" not in css:
    css += breakout_css

with open(style_path, "w", encoding="utf-8") as f:
    f.write(css)

# 2. Update JS to add loopedSlides
with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# Replace loop: true, with loop: true, loopedSlides: 6,
js = js.replace("loop: true,", "loop: true,\n            loopedSlides: 6,")

with open(script_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Applied full width CSS and loopedSlides fix.")
