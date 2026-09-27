import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace img tags in insta-slide with video tags
def replace_img_with_video(match):
    img_tag = match.group(0)
    # Give them sequential names video1.mp4, video2.mp4 etc.
    # The user can just drop these files into assets/video/
    global counter
    counter += 1
    return f'<video src="assets/video/video{counter}.mp4" loop muted playsinline preload="auto" style="width:100%; height:100%; object-fit:cover;"></video>'

counter = 0
# We want to replace <img src="assets/img/..." alt="..."> inside the insta-img divs
html = re.sub(r'<img src="assets/img/[^"]+" alt="[^"]+">', replace_img_with_video, html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html to use video tags.")
