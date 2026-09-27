import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
index_path = os.path.join(cwd, "index.html")
style_path = os.path.join(cwd, "style.css")
script_path = os.path.join(cwd, "script.js")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Instead of CSS hacks, we just close the container before the wrapper and reopen after
html = html.replace('<div class="instagram-feed-wrapper" data-aos="fade-up">', '</div> <!-- Close container -->\n            <div class="instagram-feed-wrapper" data-aos="fade-up">')
html = html.replace('<!-- Mute Toggle -->', '<!-- Mute Toggle -->') # just testing
# Wait, the end of the section is:
#             </div>
#         </div>
#     </section>
# If we closed the container early, we need to remove the closing div at the end.
html = re.sub(r'</div>\s*</section>', '</section>', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove the buggy CSS breakout
css = re.sub(r'\.instagram-feed-wrapper\s*\{[^}]*\}', '.instagram-feed-wrapper { width: 100%; position: relative; overflow: hidden; }', css)

with open(style_path, "w", encoding="utf-8") as f:
    f.write(css)

# Update Swiper to make sure it centers properly
with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# Ensure Swiper recalculates on resize
js = js.replace("loop: true,", "loop: true,\n            observer: true,\n            observeParents: true,")

with open(script_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Fixed HTML structure for full width.")
