import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"
script_path = os.path.join(cwd, "script.js")

with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# Let's cleanly replace the duplicate mute-btn listeners and the old swiper code
# Actually we can just rewrite script.js if it's too messy. But let's just do a precise replace for the mute logic.

old_mute_logic = """
    // Instagram Static Grid Video Mute Toggles
    document.querySelectorAll('.mute-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const video = this.closest('.insta-grid-item').querySelector('video');
            const icon = this.querySelector('i');
            
            if(video.muted) {
                video.muted = false;
                icon.className = 'fas fa-volume-up';
            } else {
                video.muted = true;
                icon.className = 'fas fa-volume-mute';
            }
        });
    });
"""

# Remove all instances of the old logic
js = js.replace(old_mute_logic, "")

new_mute_logic = """
    // Reliable Video Mute Toggles for Static Grid
    document.querySelectorAll('.mute-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const video = this.closest('.insta-grid-item').querySelector('video');
            const icon = this.querySelector('i');
            
            if(video.muted) {
                // Mute all other videos first
                document.querySelectorAll('.insta-grid-item video').forEach(v => {
                    v.muted = true;
                });
                document.querySelectorAll('.mute-btn i').forEach(i => {
                    i.className = 'fas fa-volume-mute';
                });
                
                // Unmute this one and ensure it's playing
                video.muted = false;
                video.play().catch(err => console.log("Play interrupted:", err));
                icon.className = 'fas fa-volume-up';
            } else {
                video.muted = true;
                icon.className = 'fas fa-volume-mute';
            }
        });
    });
"""

# Append to DOMContentLoaded (just find the first one)
js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n" + new_mute_logic, 1)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Mute logic updated.")
