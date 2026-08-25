"""
Generatore PDF branded (articolo + caption) Spotlight Tribute Nation.
Schema dedotto dai PDF reali Wonderwall, vedi Produzione-Grafica-Social.md.

Uso:
    python make_pdfs.py --articolo Band_Articolo.md --out-articolo Band_Articolo.pdf
    python make_pdfs.py --caption Band_Caption.md --band "Nome Band" --out-caption Band_Caption.pdf
"""
import argparse
import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, HRFlowable,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

BG = colors.HexColor("#0A0A0A")
RED = colors.HexColor("#CC2200")
WHITE = colors.HexColor("#FFFFFF")
GREY = colors.HexColor("#C8C8C8")
FOOT_GREY = colors.HexColor("#8C8C8C")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(SCRIPT_DIR, "fonts")
pdfmetrics.registerFont(TTFont("Bebas", os.path.join(FONT_DIR, "BebasNeue-Regular.ttf")))
pdfmetrics.registerFont(TTFont("DMSans", os.path.join(FONT_DIR, "dmsans_variable.ttf")))

# Logo TN versionato nel repo (assets/), non sul NAS: funziona su qualunque macchina.
LOGO = os.path.join(SCRIPT_DIR, "assets", "LOGO_ORIZZONTALE_RED.png")
FOOTER_LEFT = "@_tribute_nation_  ·  www.tributenation.it"
MARGIN = 70

title_style = ParagraphStyle("title", fontName="Bebas", fontSize=28, leading=32, textColor=WHITE, spaceAfter=14, alignment=TA_LEFT)
h2_style = ParagraphStyle("h2", fontName="Bebas", fontSize=17, leading=20, textColor=WHITE, spaceBefore=6, spaceAfter=8)
body_style = ParagraphStyle("body", fontName="DMSans", fontSize=10.5, leading=16, textColor=GREY, spaceAfter=10)
quote_style = ParagraphStyle("quote", fontName="DMSans", fontSize=10.5, leading=15, textColor=WHITE)
caption_title_style = ParagraphStyle("ctitle", fontName="Bebas", fontSize=22, leading=26, textColor=WHITE, spaceAfter=10)
hashtag_style = ParagraphStyle("hashtags", fontName="DMSans", fontSize=10, leading=14, textColor=RED)


def make_doc(filename):
    doc = BaseDocTemplate(filename, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=110, bottomMargin=60)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")

    def on_page(canvas, doc_):
        canvas.saveState()
        canvas.setFillColor(BG)
        canvas.rect(0, 0, doc_.pagesize[0], doc_.pagesize[1], fill=1, stroke=0)
        canvas.drawImage(LOGO, MARGIN, doc_.pagesize[1] - 85, width=95, height=95 * (964 / 2000), mask="auto")
        canvas.setFont("DMSans", 9)
        canvas.setFillColor(FOOT_GREY)
        canvas.drawString(MARGIN, 32, FOOTER_LEFT)
        canvas.drawRightString(doc_.pagesize[0] - MARGIN, 32, str(doc_.page))
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id="page", frames=[frame], onPage=on_page)])
    return doc


def divider():
    return HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#333333"), spaceBefore=4, spaceAfter=14)


def quote_box(text):
    p = Paragraph(text, quote_style)
    t = Table([[p]], colWidths=[A4[0] - 2 * MARGIN])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1.2, RED),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def parse_article(md_text):
    blocks, title = [], None
    for raw in md_text.split("\n\n"):
        raw = raw.strip()
        if not raw:
            continue
        if raw.startswith("# "):
            title = raw[2:].strip()
        elif raw.startswith("## "):
            blocks.append(("h2", raw[3:].strip()))
        elif raw.startswith(">"):
            blocks.append(("quote", raw.lstrip(">").strip()))
        else:
            blocks.append(("p", raw.replace("\n", " ")))
    return title, blocks


def build_article_pdf(md_path, out_path):
    with open(md_path, encoding="utf-8") as f:
        title, blocks = parse_article(f.read())
    story = [Paragraph(title, title_style), divider()]
    for kind, text in blocks:
        if kind == "h2":
            story.append(divider())
            story.append(Paragraph(text, h2_style))
        elif kind == "quote":
            story.append(quote_box(text))
            story.append(Spacer(1, 10))
        else:
            story.append(Paragraph(text, body_style))
    make_doc(out_path).build(story)
    print("saved", out_path)


def strip_emoji(text):
    pattern = re.compile(
        "[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F9FF\U0001FA00-\U0001FAFF"
        "\U00002702-\U000027B0\U000024C2-\U0001F251]+",
        flags=re.UNICODE)
    return pattern.sub("", text).strip()


def build_caption_pdf(md_path, out_path, band_name):
    with open(md_path, encoding="utf-8") as f:
        raw_blocks = [b.strip() for b in f.read().split("\n\n") if b.strip()]
    story = [Paragraph(f"{band_name.upper()}: CAPTION SPOTLIGHT", caption_title_style), divider()]
    for block in raw_blocks:
        clean = strip_emoji(block)
        if not clean:
            continue
        if clean.startswith('"') and clean.endswith('"'):
            story.append(quote_box(clean))
            story.append(Spacer(1, 10))
        elif clean.startswith("#"):
            story.append(Paragraph(clean, hashtag_style))
        else:
            story.append(Paragraph(clean.replace("\n", "<br/>"), body_style))
    make_doc(out_path).build(story)
    print("saved", out_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--articolo")
    parser.add_argument("--out-articolo")
    parser.add_argument("--caption")
    parser.add_argument("--out-caption")
    parser.add_argument("--band", help="Nome banda, richiesto per --caption")
    args = parser.parse_args()

    if args.articolo:
        build_article_pdf(args.articolo, args.out_articolo)
    if args.caption:
        build_caption_pdf(args.caption, args.out_caption, args.band)


if __name__ == "__main__":
    main()
