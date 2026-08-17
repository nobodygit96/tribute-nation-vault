"""
Generatore slide "statement card" Tribute Nation: Spoiler Spotlight, B-Side,
Dalla Nation per la Nation. Diverso dal carosello Spotlight a 9 slide
(vedi make_slides.py): qui ogni slide e' un blocco di testo centrato,
niente logo band. Standard visivo condiviso: vedi Produzione-Grafica-Social.md.

Uso:
    python make_statement_slides.py --config config.json

Schema config JSON:
{
  "output_dir": "...",
  "progress_total": 5,          // opzionale: numero totale slide per la progress bar (carosello)
  "slides": [
    {
      "filename": "spoiler_desaparecidos.png",
      "header": "SPOILER SPOTLIGHT",
      "progress_index": 1,       // opzionale, 1-based, richiede progress_total
      "blocks": [
        {"text": "1986.", "font": "bebas", "size": 76, "color": "white", "divider_after": true},
        {"text": "17 RE.", "font": "bebas", "size": 76, "color": "red", "divider_after": true},
        {"text": "Domani lo Spotlight.", "font": "dmsans", "size": 30, "color": "grey"}
      ]
    }
  ]
}
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_slides import (  # noqa: E402
    make_background, wrap, footer, bebas, dm_sans,
    W, H, BG, RED, WHITE, GREY, DIVIDER, PAD,
)
from PIL import ImageDraw  # noqa: E402

COLORS = {"white": WHITE, "red": RED, "grey": GREY}

CONTENT_TOP = 340
CONTENT_BOTTOM = H - 200
BLOCK_GAP = 34
DIVIDER_GAP = 26


def header_block(draw, header):
    header_font = dm_sans(26, "Medium")
    text = header.upper()
    b = draw.textbbox((0, 0), text, font=header_font)
    w = b[2] - b[0]
    y = 254
    draw.text(((W - w) / 2, y), text, font=header_font, fill=RED)
    divider_y = y + 42
    draw.line([(PAD, divider_y), (W - PAD, divider_y)], fill=DIVIDER, width=1)
    return divider_y


def measure_blocks(draw, blocks):
    """Pre-misura l'altezza totale dello stack di blocchi (per centrarlo)."""
    total = 0
    rendered = []
    for i, blk in enumerate(blocks):
        font_fn = bebas if blk["font"] == "bebas" else dm_sans
        font = font_fn(blk["size"])
        max_w = W - 2 * PAD - (0 if blk["font"] == "bebas" else 60)
        lines = wrap(draw, blk["text"].upper() if blk["font"] == "bebas" else blk["text"], font, max_w)
        bbox = draw.textbbox((0, 0), "Hg", font=font)
        line_h = (bbox[3] - bbox[1]) * (1.05 if blk["font"] == "bebas" else 1.3)
        block_h = line_h * len(lines)
        rendered.append({"lines": lines, "font": font, "color": COLORS[blk["color"]], "line_h": line_h})
        total += block_h
        if i < len(blocks) - 1:
            total += BLOCK_GAP
            if blk.get("divider_after"):
                total += DIVIDER_GAP * 2
    return rendered, total


def statement_slide(filename, header, blocks, progress_total=None, progress_index=None):
    img = make_background()
    draw = ImageDraw.Draw(img)

    header_block(draw, header)
    rendered, total_h = measure_blocks(draw, blocks)

    y = CONTENT_TOP + max(0, (CONTENT_BOTTOM - CONTENT_TOP - total_h) / 2)
    for i, (blk, rend) in enumerate(zip(blocks, rendered)):
        for line in rend["lines"]:
            b = draw.textbbox((0, 0), line, font=rend["font"])
            w = b[2] - b[0]
            draw.text(((W - w) / 2, y), line, font=rend["font"], fill=rend["color"])
            y += rend["line_h"]
        if i < len(blocks) - 1:
            y += BLOCK_GAP
            if blk.get("divider_after"):
                y += DIVIDER_GAP
                draw.line([(PAD, y), (W - PAD, y)], fill=DIVIDER, width=1)
                y += DIVIDER_GAP

    footer(img, draw)

    if progress_total and progress_index:
        bar_y = H - 6
        draw.line([(PAD, bar_y), (W - PAD, bar_y)], fill=DIVIDER, width=3)
        seg_w = (W - 2 * PAD) / progress_total
        x0 = PAD + seg_w * (progress_index - 1)
        x1 = x0 + seg_w
        draw.line([(x0, bar_y), (x1, bar_y)], fill=RED, width=3)

    img.save(filename)
    print("saved", filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)

    os.makedirs(cfg["output_dir"], exist_ok=True)
    progress_total = cfg.get("progress_total")

    for s in cfg["slides"]:
        filename = os.path.join(cfg["output_dir"], s["filename"])
        statement_slide(
            filename, s["header"], s["blocks"],
            progress_total=progress_total, progress_index=s.get("progress_index"),
        )


if __name__ == "__main__":
    main()
