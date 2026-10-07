#!/usr/bin/env python3
"""Generate the Open Graph / social share image (1200x630)."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "assets", "img")
OUT = os.path.join(IMG_DIR, "brand", "og-image.jpg")

W, H = 1200, 630

bg = Image.open(os.path.join(IMG_DIR, "hero", "men-alum3.jpg")).convert("RGB")
bw, bh = bg.size
scale = max(W / bw, H / bh)
bg = bg.resize((int(bw * scale), int(bh * scale)))
bw, bh = bg.size
bg = bg.crop(((bw - W) // 2, (bh - H) // 2, (bw - W) // 2 + W, (bh - H) // 2 + H))
bg = ImageEnhance.Brightness(bg).enhance(0.75)

overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for x in range(W):
    t = x / W
    r = int(10 + (255 - 10) * 0 + 10 * (1 - t))
    a = int(235 * (1 - t * 0.55))
    od.line([(x, 0), (x, H)], fill=(10, 16, 34, a))
od2 = ImageDraw.Draw(overlay)
od2.rectangle([0, 0, W, H], fill=None)
base = Image.alpha_composite(bg.convert("RGBA"), overlay)

logo = Image.open(os.path.join(IMG_DIR, "brand", "logo.png")).convert("RGBA")
lw, lh = logo.size
target_h = 90
logo = logo.resize((int(lw * target_h / lh), target_h))
base.paste(logo, (80, 80), logo)

draw = ImageDraw.Draw(base)
font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 54)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
font_tag = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)

orange = (255, 129, 47, 255)
white = (255, 255, 255, 255)

lines = ["Menuiserie Aluminium,", "Solutions d'Accès &", "Ouvertures Automatisées"]
y = 230
for i, line in enumerate(lines):
    color = orange if i == 0 else white
    draw.text((82, y), line, font=font_big, fill=color)
    y += 68

draw.text((84, y + 20), "ASCO Groupe · Cotonou, Bénin", font=font_small, fill=(220, 225, 235, 255))

base.convert("RGB").save(OUT, "JPEG", quality=88, optimize=True)
print("saved", OUT, base.size)
