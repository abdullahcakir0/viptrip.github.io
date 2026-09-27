import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
script_path = os.path.join(cwd, "script.js")

with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# The garbage starts at the SECOND if(document.querySelector('.insta-swiper')) {
# Let's just find that block and replace it with closing the DOMContentLoaded
bad_code_pattern = r"    if\(document\.querySelector\('\.insta-swiper'\)\) \{\s+.*?\}\n\}\);"

# Actually it's safer to just split the file at the second 'if(document.querySelector('.insta-swiper'))' 
parts = js.split("if(document.querySelector('.insta-swiper')) {")
if len(parts) >= 3:
    # First part is up to the first 'if(document...', second part is our GOOD code, third part is the BAD code
    # We want to keep parts[0] + "if(document.querySelector('.insta-swiper')) {" + parts[1] + "});"
    # Wait, parts[1] already ends with '    }'
    # Let's just use string replacement for the exact garbage.
    pass

# A more reliable way: find the exact garbage string using regex from the end
fixed_js = re.sub(r'    if\(document\.querySelector\(\'\.insta-swiper\'\)\) \{\s*\}\s*\},.*?\}\n        \}\);\n    \}\n\}\);', '});', js, flags=re.DOTALL)
if fixed_js == js:
    # try again
    fixed_js = re.sub(r'    if\(document\.querySelector\(\'\.insta-swiper\'\)\) \{\s*\}\s*\},.*?\}\n        \}\);\n    \}', '', js, flags=re.DOTALL)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(fixed_js)
print("JS cleanup attempted.")
