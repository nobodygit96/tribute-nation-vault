"""
Generatore slide carosello Spotlight Tribute Nation.
Standard di produzione: vedi Produzione-Grafica-Social.md nella KB.

Uso:
    python make_slides.py --config band_config.json

Il config JSON descrive tutta la banda-specifica; questo script applica
gli standard fissi (font, colori, layout, dimensioni) decisi il 2026-08-16/17.

Schema config JSON:
{
  "band_slug": "fromzero",              // minuscolo, usato nei nomi file slide
  "logo_path": "C:/.../FromZeroLogo.png",
  "cover_photo_path": "C:/.../foto_live.jpg",  // null se non disponibile: la cover viene saltata
  "band_name": "Frøm Zerø",             // per il testo sotto il logo in cover
  "output_dir": "C:/.../output",
  "slides": [
    {"tag": "Chi sono", "title": "...", "body": "..."},
    ...
    {"tag": "Il consiglio", "closing": true, "quote": "...", "body": "...", "cta": "Seguili su Instagram"}
  ]
}
"""
import argparse
import json
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W = H = 1080
BG = (10, 10, 10)
RED = (204, 34, 0)
WHITE = (255, 255, 255)
GREY = (170, 170, 170)
DIVIDER = (50, 50, 50)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(SCRIPT_DIR, "fonts")
BEBAS = os.path.join(FONT_DIR, "BebasNeue-Regular.ttf")
DMSANS = os.path.join(FONT_DIR, "dmsans_variable.ttf")

# Logo TN per il footer: versionato nel repo (assets/), non sul NAS.
# Così lo script funziona identico su qualunque macchina senza Z:\ mappato.
LOGO_TN = os.path.join(SCRIPT_DIR, "assets", "LOGO_ORIZZONTALE_RED.png")

PAD = 90


def dm_sans(size, weight="Regular"):
    f = ImageFont.truetype(DMSANS, size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def bebas(size):
    return ImageFont.truetype(BEBAS, size)


def make_background():
    xs = np.arange(W)[np.newaxis, :]
    ys = np.arange(H)[:, np.newaxis]
    cx, cy = W / 2, H * 0.5
    dist = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
    max_dist = np.sqrt(cx ** 2 + cy ** 2)
    t = np.clip(1 - dist / (max_dist * 0.85), 0, 1) ** 1.6
    glow = np.array([70, 10, 6])
    bg = np.array(BG)
    arr = bg[np.newaxis, np.newaxis, :] + t[:, :, np.newaxis] * (glow - bg)[np.newaxis, np.newaxis, :]
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGB")


def wrap(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered_block(draw, lines, font, y, color, line_gap=1.15):
    bbox = draw.textbbox((0, 0), "Hg", font=font)
    line_h = (bbox[3] - bbox[1]) * line_gap
    for line in lines:
        b = draw.textbbox((0, 0), line, font=font)
        w = b[2] - b[0]
        draw.text(((W - w) / 2, y), line, font=font, fill=color)
        y += line_h
    return y


def paste_centered(img, overlay_path, target_w, top_y):
    overlay = Image.open(overlay_path).convert("RGBA")
    ratio = target_w / overlay.width
    overlay = overlay.resize((target_w, int(overlay.height * ratio)), Image.LANCZOS)
    x = (W - overlay.width) // 2
    img.paste(overlay, (x, top_y), overlay)
    return top_y + overlay.height


def footer(img, draw):
    tn_w = 190
    y_top = paste_centered(img, LOGO_TN, tn_w, H - 155)
    handle_font = dm_sans(26)
    handle = "@_tribute_nation_"
    b = draw.textbbox((0, 0), handle, font=handle_font)
    w = b[2] - b[0]
    draw.text(((W - w) / 2, y_top + 6), handle, font=handle_font, fill=(140, 140, 140))


HERO_LOGO_W = 780
HERO_LOGO_Y = -60
HERO_BAND_TOP = 560


def _hero_header(img, draw, logo_path, tag):
    """Logo banda gigante e sbiadito in alto, banda scura sotto separata da una riga rossa.
    Standard 'hero logo' deciso da Vale il 2026-08-30 dopo 4 round di iterazione sul
    problema 'slide vuote/testo piccolo' (vedi Produzione-Grafica-Social.md)."""
    logo = Image.open(logo_path).convert("RGBA")
    ratio = HERO_LOGO_W / logo.width
    logo = logo.resize((HERO_LOGO_W, int(logo.height * ratio)), Image.LANCZOS)
    alpha = logo.split()[3].point(lambda p: int(p * 0.5))
    logo.putalpha(alpha)
    img.paste(logo, ((W - HERO_LOGO_W) // 2, HERO_LOGO_Y), logo)

    draw.rectangle([(0, HERO_BAND_TOP), (W, H)], fill=(6, 6, 6))
    draw.line([(0, HERO_BAND_TOP), (W, HERO_BAND_TOP)], fill=RED, width=3)

    tag_font = dm_sans(30, "Medium")
    tag_up = tag.upper()
    tb = draw.textbbox((0, 0), tag_up, font=tag_font)
    tag_w = tb[2] - tb[0]
    ty = HERO_BAND_TOP + 45
    draw.text(((W - tag_w) / 2, ty), tag_up, font=tag_font, fill=RED)
    return ty


def content_slide(filename, logo_path, band_logo_w, tag, title, body):
    img = make_background()
    draw = ImageDraw.Draw(img)
    ty = _hero_header(img, draw, logo_path, tag)

    title_font = bebas(80 if len(title) < 26 else 66)
    title_lines = wrap(draw, title.upper(), title_font, W - 2 * PAD - 40)
    body_font = dm_sans(38)
    body_lines = wrap(draw, body, body_font, W - 2 * PAD - 80)

    y = ty + 58
    y = draw_centered_block(draw, title_lines, title_font, y, WHITE, line_gap=1.05)
    y += 18
    draw_centered_block(draw, body_lines, body_font, y, GREY, line_gap=1.3)

    footer(img, draw)
    img.save(filename)
    print("saved", filename)


def closing_slide(filename, logo_path, band_logo_w, tag, quote, body, cta):
    img = make_background()
    draw = ImageDraw.Draw(img)
    ty = _hero_header(img, draw, logo_path, tag)

    title_font = bebas(66 if len(quote) < 40 else 54)
    title_lines = wrap(draw, quote.upper(), title_font, W - 2 * PAD - 40)
    body_font = dm_sans(34)
    body_lines = wrap(draw, body, body_font, W - 2 * PAD - 80)
    cta_font = dm_sans(30)

    y = ty + 58
    y = draw_centered_block(draw, title_lines, title_font, y, WHITE, line_gap=1.05)
    y += 16
    y = draw_centered_block(draw, body_lines, body_font, y, GREY, line_gap=1.3)

    y += 14
    b = draw.textbbox((0, 0), cta, font=cta_font)
    w = b[2] - b[0]
    draw.text(((W - w) / 2, y), cta, font=cta_font, fill=(210, 210, 210))

    footer(img, draw)
    img.save(filename)
    print("saved", filename)


def cover_slide(filename, photo_path, logo_path, band_logo_w, band_name, center_pct=0.72, show_band_name=True):
    photo = Image.open(photo_path).convert("RGB")
    scale = max(W / photo.width, H / photo.height)
    photo = photo.resize((int(photo.width * scale), int(photo.height * scale)), Image.LANCZOS)
    x0 = (photo.width - W) // 2
    y0 = (photo.height - H) // 2
    photo = photo.crop((x0, y0, x0 + W, y0 + H))

    arr = np.array(photo).astype(np.float32)
    arr *= 0.6
    arr[:, :, 0] *= 1.5
    arr[:, :, 1] *= 0.55
    arr[:, :, 2] *= 0.5
    arr = np.clip(arr, 0, 255)

    xs = np.arange(W)[np.newaxis, :]
    ys = np.arange(H)[:, np.newaxis]
    cx, cy = W / 2, H / 2
    dist = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2) / (np.sqrt(2) * cx)
    vign = np.clip(1 - dist * 0.9, 0, 1)[:, :, np.newaxis]
    arr = np.clip(arr * vign, 0, 255).astype(np.uint8)

    img = Image.fromarray(arr, "RGB").convert("RGBA")
    draw = ImageDraw.Draw(img)

    logo = Image.open(logo_path).convert("RGBA")
    ratio = band_logo_w / logo.width
    logo = logo.resize((band_logo_w, int(logo.height * ratio)), Image.LANCZOS)

    if show_band_name:
        name_font = bebas(72)
        name_up = band_name.upper()
        nb = draw.textbbox((0, 0), name_up, font=name_font)
        name_h = nb[3] - nb[1]
        gap = 22
        total_h = logo.height + gap + name_h
    else:
        gap = 0
        name_h = 0
        total_h = logo.height

    top = int(H * center_pct - total_h / 2)

    x = (W - logo.width) // 2
    img.paste(logo, (x, top), logo)

    if show_band_name:
        name_y = top + logo.height + gap
        nw = nb[2] - nb[0]
        draw.text(((W - nw) / 2, name_y), name_up, font=name_font, fill=WHITE)

    img.convert("RGB").save(filename)
    print("saved", filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)

    os.makedirs(cfg["output_dir"], exist_ok=True)
    slug = cfg["band_slug"]
    logo_path = cfg["logo_path"]

    idx = 1
    if cfg.get("cover_photo_path"):
        cover_slide(
            os.path.join(cfg["output_dir"], f"{slug}_slide{idx}_cover.png"),
            cfg["cover_photo_path"], logo_path, cfg.get("cover_logo_w", 390), cfg["band_name"],
            center_pct=cfg.get("cover_vertical_center", 0.72),
            show_band_name=cfg.get("cover_show_band_name", True),
        )
        idx += 1
    else:
        print("ATTENZIONE: nessuna cover_photo_path, cover saltata (serve una foto live).")

    for s in cfg["slides"]:
        theme = s.get("theme") or s["tag"].lower().replace(" ", "")
        filename = os.path.join(cfg["output_dir"], f"{slug}_slide{idx}_{theme}.png")
        if s.get("closing"):
            closing_slide(filename, logo_path, 340, s["tag"], s["quote"], s["body"], s.get("cta", "Seguili su Instagram"))
        else:
            content_slide(filename, logo_path, 340, s["tag"], s["title"], s["body"])
        idx += 1


if __name__ == "__main__":
    main()
