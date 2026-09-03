"""
Verifica di completezza di un pacchetto Spotlight gia' prodotto.
Nato dopo aver trovato 2 pacchetti su 2 controllati (From Zero, Wild Berries)
segnati "pronti" in Materiali-NAS.md ma in realta' incompleti.

Uso:
    python check_package.py --dir "Z:/TRIBUTE NATION/Band della nation/<Banda>/Spotlight" --slug <banda>

Non genera nulla, non modifica nulla: solo un report di cosa manca o non
rispetta gli standard (Produzione-Grafica-Social.md, Tone-of-Voice.md).
"""
import argparse
import glob
import os
import re
import zipfile


def check_word_count(path, lo=1000, hi=1200):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    words = len(re.findall(r"\w+", text))
    ok = lo <= words <= hi
    return ok, f"{words} parole (target {lo}-{hi})"


def check_no_emdash(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    hits = [ln for ln in text.splitlines() if "—" in ln or "–" in ln]
    ok = len(hits) == 0
    detail = "nessun em-dash" if ok else f"{len(hits)} riga/e con em-dash"
    return ok, detail


def check_zip_contents(path, expected_min=6):
    try:
        with zipfile.ZipFile(path) as zf:
            names = zf.namelist()
        ok = len(names) >= expected_min
        return ok, f"{len(names)} file dentro (attesi almeno {expected_min})"
    except Exception as e:
        return False, f"zip illeggibile: {e}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True, help="Cartella Spotlight della banda")
    parser.add_argument("--slug", required=True, help="Nome banda usato nei file, es. WildBerries")
    parser.add_argument("--articolo-words-min", type=int, default=1000)
    parser.add_argument("--articolo-words-max", type=int, default=1200)
    args = parser.parse_args()

    d = args.dir
    s = args.slug
    results = []

    expected_files = {
        "Articolo.md": f"{s}_Articolo.md",
        "Articolo WordPress HTML": f"{s}_Articolo_WordPress.html",
        "Articolo PDF": f"{s}_Articolo.pdf",
        "Caption.md": f"{s}_Caption.md",
        "Caption PDF": f"{s}_Caption.pdf",
        "Logo": f"{s}_Logo.png",
        "Pacchetto zip": f"{s}_Pacchetto.zip",
    }

    for label, fname in expected_files.items():
        fpath = os.path.join(d, fname)
        exists = os.path.isfile(fpath)
        results.append((exists, f"{label}: {'trovato' if exists else 'MANCANTE'} ({fname})"))

    slides = glob.glob(os.path.join(d, f"{s.lower()}_slide*.png"))
    ok_slides = len(slides) >= 9
    results.append((ok_slides, f"Slide carosello: {len(slides)} trovate (attese almeno 9)"))

    articolo_path = os.path.join(d, expected_files["Articolo.md"])
    if os.path.isfile(articolo_path):
        ok, detail = check_word_count(articolo_path, args.articolo_words_min, args.articolo_words_max)
        results.append((ok, f"Conteggio parole articolo: {detail}"))
        ok, detail = check_no_emdash(articolo_path)
        results.append((ok, f"Em-dash articolo: {detail}"))

    caption_path = os.path.join(d, expected_files["Caption.md"])
    if os.path.isfile(caption_path):
        ok, detail = check_no_emdash(caption_path)
        results.append((ok, f"Em-dash caption: {detail}"))

    zip_path = os.path.join(d, expected_files["Pacchetto zip"])
    if os.path.isfile(zip_path):
        ok, detail = check_zip_contents(zip_path)
        results.append((ok, f"Contenuto zip: {detail}"))

    print(f"\n=== Verifica pacchetto: {s} ===\n")
    all_ok = True
    for ok, msg in results:
        mark = "OK " if ok else "XX "
        print(f"[{mark}] {msg}")
        if not ok:
            all_ok = False

    print()
    if all_ok:
        print("Pacchetto completo secondo i controlli automatici.")
        print("Restano da controllare a occhio: hero-logo layout sulle slide, testo non tagliato,")
        print("citazioni come blockquote veri supportati da prosa prima/dopo, cover con foto live reale.")
    else:
        print("Pacchetto INCOMPLETO. Non segnare come pronto finche' i punti sopra non sono risolti.")


if __name__ == "__main__":
    main()
