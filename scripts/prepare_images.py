#!/usr/bin/env python3
"""One-off script: organize & lightly optimize images harvested from the old
asco-groupe.com site into assets/img/<category>/ with clean names."""
import os, re, shutil
from PIL import Image

SRC = "/tmp/claude-1000/-home-eliel-T-l-chargements/1670ff1d-686e-4b4e-a1f8-4a9aa7efe3b6/scratchpad/asco-old-site/images"
DST = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")

MAP = {
    "assets__Men_Alu__": "menuiserie",
    "assets__Ouvert_Auto__": "automatisation",
    "assets__Coffre-fort__": "coffre-fort",
    "assets__Solu_Acess__": "solutions-acces",
    "assets__Uploads___resampled__": "hero",
    "themes__asco__images__": "divers",
}

def slugify(name):
    name = name.lower()
    name = re.sub(r"[^a-z0-9.]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name

def main():
    os.makedirs(DST, exist_ok=True)
    count = 0
    for fname in sorted(os.listdir(SRC)):
        if fname == "images__Arrow.png":
            continue
        prefix_cat = None
        rest = fname
        for prefix, cat in MAP.items():
            if fname.startswith(prefix):
                prefix_cat = cat
                rest = fname[len(prefix):]
                break
        if prefix_cat is None:
            continue
        outdir = os.path.join(DST, prefix_cat)
        os.makedirs(outdir, exist_ok=True)
        clean = slugify(rest)
        src_path = os.path.join(SRC, fname)
        dst_path = os.path.join(outdir, clean)

        try:
            im = Image.open(src_path)
            im.load()
            w, h = im.size
            # Downscale very large images (none expected >1600 but just in case)
            max_dim = 1600
            if max(w, h) > max_dim:
                ratio = max_dim / max(w, h)
                im = im.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)

            size_bytes = os.path.getsize(src_path)
            if im.mode in ("RGBA", "P") and clean.endswith((".jpg", ".jpeg")):
                im = im.convert("RGB")

            if size_bytes > 140_000 and clean.rsplit(".", 1)[-1] in ("png",) and im.mode in ("RGB",):
                # convert bulky flat PNG photos to JPEG for a big size win
                clean_jpg = clean.rsplit(".", 1)[0] + ".jpg"
                dst_path = os.path.join(outdir, clean_jpg)
                im.convert("RGB").save(dst_path, "JPEG", quality=82, optimize=True)
            elif clean.rsplit(".", 1)[-1] in ("jpg", "jpeg"):
                im.save(dst_path, "JPEG", quality=84, optimize=True)
            else:
                im.save(dst_path, optimize=True)
            count += 1
        except Exception as e:
            print("SKIP", fname, e)

    print(f"Organized {count} images into {DST}")

if __name__ == "__main__":
    main()
