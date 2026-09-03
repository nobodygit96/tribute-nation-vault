"""
Generatore formato verticale 1080x1920 (Storie/Reel IG-FB, copre anche il
placement WhatsApp Status che riusa lo stesso asset) per una statement-card
a slide singola. Stesso sistema visivo di make_statement_slides.py, canvas
diverso: qui serve margine di sicurezza in alto/basso per le UI di Storie
(profilo/testo in alto, barra risposta in basso).

Uso:
    python make_story_slide.py --config config.json

Schema config JSON: identico a una singola slide di make_statement_slides.py
(header, blocks), più "output_dir" e "filename" in root.
"""
import argparse
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_slides import wrap, bebas, dm_sans, paste_centered, RED, WHITE, GREY, BG, DIVIDER, LOGO_TN  # noqa: E402

W, H = 1080, 1920
PAD = 90
SAFE_TOP = 250
SAFE_BOTTOM = 250
COLORS = {"white": WHITE, "red": RED, "grey": GREY}


def make_background():
    xs = np.arange(W)[np.newaxis, :]
    ys = np.arange(H)[:, np.newaxis]
    cx, cy = W / 2, H * 0.4
    dist = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
    max_dist = np.sqrt(cx ** 2 + (H * 0.6) ** 2)
    t = np.clip(1 - dist / (max_dist * 0.85), 0, 1) ** 1.6
    glow = np.array([70, 10, 6])
    bg = np.array(BG)
    arr = bg[np.newaxis, np.newaxis, :] + t[:, :, np.newaxis] * (glow - bg)[np.newaxis, np.newaxis, :]
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGB")


def header_block(draw, header):
    header_font = dm_sans(34, "Medium")
    text = header.upper()
    b = draw.textbbox((0, 0), text, font=header_font)
    w = b[2] - b[0]
    y = SAFE_TOP
    draw.text(((W - w) / 2, y), text, font=header_font, fill=RED)
    divider_y = y + 50
    draw.line([(PAD, divider_y), (W - PAD, divider_y)], fill=DIVIDER, width=1)
    return divider_y


def measure_blocks(draw, blocks):
    total = 0
    rendered = []
    for i, blk in enumerate(blocks):
        font_fn = bebas if blk["font"] == "bebas" else dm_sans
        font = font_fn(blk["size"])
        max_w = W - 2 * PAD - (0 if blk["font"] == "bebas" else 60)
        lines = wrap(draw, blk["text"].upper() if blk["font"] == "bebas" else blk["text"], font, max_w)
        bbox = draw.textbbox((0, 0), "Hg", font=font)
        line_h = (bbox[3] - bbox[1]) * (1.15 if blk["font"] == "bebas" else 1.3)
        block_h = line_h * len(lines)
        rendered.append({"lines": lines, "font": font, "color": COLORS[blk["color"]], "line_h": line_h})
        total += block_h
        if i < len(blocks) - 1:
            total += 24
            if blk.get("divider_after"):
                total += 14 * 2
    return rendered, total


def story_slide(filename, header, blocks):
    img = make_background()
    draw = ImageDraw.Draw(img)

    header_bottom = header_block(draw, header)
    rendered, total_h = measure_blocks(draw, blocks)

    content_top = header_bottom + 80
    content_bottom = H - SAFE_BOTTOM - 140
    y = content_top + max(0, (content_bottom - content_top - total_h) / 2)

    for i, (blk, rend) in enumerate(zip(blocks, rendered)):
        for line in rend["lines"]:
            b = draw.textbbox((0, 0), line, font=rend["font"])
            w = b[2] - b[0]
            draw.text(((W - w) / 2, y), line, font=rend["font"], fill=rend["color"])
            y += rend["line_h"]
        if i < len(blocks) - 1:
            y += 24
            if blk.get("divider_after"):
                y += 14
                draw.line([(PAD, y), (W - PAD, y)], fill=DIVIDER, width=1)
                y += 14

    tn_w = 190
    y_top = paste_centered(img, LOGO_TN, tn_w, H - SAFE_BOTTOM - 90)
    handle_font = dm_sans(26)
    handle = "@_tribute_nation_"
    b = draw.textbbox((0, 0), handle, font=handle_font)
    w = b[2] - b[0]
    draw.text(((W - w) / 2, y_top + 6), handle, font=handle_font, fill=(140, 140, 140))

    img.save(filename)
    print("saved", filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)

    os.makedirs(cfg["output_dir"], exist_ok=True)
    filename = os.path.join(cfg["output_dir"], cfg["filename"])
    story_slide(filename, cfg["header"], cfg["blocks"])


if __name__ == "__main__":
    main()
