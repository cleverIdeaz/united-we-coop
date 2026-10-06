from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "index.html",
    ROOT / "styles.css",
    ROOT / "app.js",
    ROOT / "events" / "how-a-coop-runs.html",
    ROOT / "schools" / "creekside.html",
    ROOT / "local.sh",
    ROOT / "ship.sh",
]
missing = [p for p in required if not p.exists()]
if missing:
    for p in missing:
        print(f"MISSING: {p.relative_to(ROOT)}")
    sys.exit(1)

html_files = list(ROOT.rglob("*.html"))
errors = []
for page in html_files:
    text = page.read_text(encoding="utf-8")
    if "<title>" not in text:
        errors.append(f"{page.relative_to(ROOT)}: missing title")
    if 'name="description"' not in text:
        errors.append(f"{page.relative_to(ROOT)}: missing meta description")
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith(("#", "http://", "https://", "mailto:", "tel:")):
            continue
        target = href.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        candidate = ROOT / target.lstrip("/") if target.startswith("/") else page.parent / target
        if candidate.is_dir():
            candidate = candidate / "index.html"
        if not candidate.exists():
            errors.append(f"{page.relative_to(ROOT)}: broken local href {href}")

if errors:
    print("Static checks failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print(f"Static checks passed: {len(html_files)} HTML pages, required files present, local links resolve.")
